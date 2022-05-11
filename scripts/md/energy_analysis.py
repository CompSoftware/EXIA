import os, glob
import pandas as pd

def get_data(model_number,energy_dir,loop_num,frame_per_loop,export_data_dir):
    
    analysis_method     ='energy'
    model               = ''.join(['model_',str(model_number)])
    saved_energy_dir      = os.path.join(export_data_dir,analysis_method)  
    energy_txt_name           = ''.join([model, '.txt'])
    energy_txt_output         = os.path.join(saved_energy_dir, energy_txt_name)

    isExist = os.path.exists(saved_energy_dir)
    if not isExist:
        os.makedirs(saved_energy_dir)
        print("The new directory is created! : ", saved_energy_dir)

    list=[]
    new_loop_num=loop_num+1

    for i in range(1,new_loop_num):
        item = ''.join(['prod',str(i),'.out'])
        list.append(item)    

    with open( energy_txt_output, 'wt') as result:
        for file in list:
            for line in open(os.path.join(energy_dir,file),'r'):
                result.write(line)

    energy_1   = ''.join(['energy_',model,'_1.txt'])   
    energy_1_output   = os.path.join(saved_energy_dir, energy_1)         
    with open(energy_txt_output, 'rt') as infile, open(energy_1_output, 'a') as outfile:
        for line in infile:
            if 'Etot   =' in line: outfile.write(line)

    os.remove(energy_txt_output)

    Raw_output = open( energy_1_output, 'rt')
    Raw_output_mod = Raw_output.read()
    Raw_output_mod = Raw_output_mod.replace('=', '')
    Raw_output_mod = Raw_output_mod.replace('Etot', '')
    Raw_output_mod = Raw_output_mod.replace('EKtot', '')
    Raw_output_mod = Raw_output_mod.replace('EPtot', '')
    Raw_output_mod = Raw_output_mod.replace('   ', ',')
    Raw_output_mod = Raw_output_mod.replace('  ', ',')
    Raw_output_mod = Raw_output_mod.replace(' ', ',')
    Raw_output_mod = Raw_output_mod.replace(',,,', ',')
    Raw_output_mod = Raw_output_mod.replace(',,', ',')
    Raw_output.close()
    Raw_output = open( energy_txt_output, 'wt')
    Raw_output.write(Raw_output_mod)
    Raw_output.close()
    os.remove(energy_1_output)

    energy = pd.read_csv(energy_txt_output, sep=",", header=None, on_bad_lines='skip')
    os.remove(energy_txt_output)
    energy.columns = ["dummy", "Etot", "EKtot", "EPtot"]
    energy = energy[["Etot", "EKtot", "EPtot"]]

    labels=[]
    for i in range(1,loop_num):
        item = frame_per_loop*i
        labels.append(item)    

    energy = energy.drop(labels, axis=0)
    energy_name   = ''.join([model,'.csv'])
    energy_save   = os.path.join(saved_energy_dir, energy_name)
    energy.to_csv(energy_save, header = True, index = False)

def get_data_single(energy_dir,loop_num,export_data_dir):
    
    analysis_method     ='energy'
    saved_energy_dir      = os.path.join(export_data_dir,analysis_method)  

    isExist = os.path.exists(saved_energy_dir)
    if not isExist:
        os.makedirs(saved_energy_dir)
        print("The new directory is created! : ", saved_energy_dir)

    list=[]
    new_loop_num=loop_num+1

    for i in range(1,new_loop_num):
        item = ''.join(['prod',str(i),'.out'])
        list.append(item)   


    for i in list:
        energy_txt_output         = os.path.join(energy_dir, i)

        energy_1_output   = os.path.join(saved_energy_dir, i)         
        with open(energy_txt_output, 'rt') as infile, open(energy_1_output, 'a') as outfile:
            for line in infile:
                if 'Etot   =' in line: outfile.write(line)

        Raw_output = open( energy_1_output, 'rt')
        Raw_output_mod = Raw_output.read()
        Raw_output_mod = Raw_output_mod.replace('=', '')
        Raw_output_mod = Raw_output_mod.replace('Etot', '')
        Raw_output_mod = Raw_output_mod.replace('EKtot', '')
        Raw_output_mod = Raw_output_mod.replace('EPtot', '')
        Raw_output_mod = Raw_output_mod.replace('   ', ',')
        Raw_output_mod = Raw_output_mod.replace('  ', ',')
        Raw_output_mod = Raw_output_mod.replace(' ', ',')
        Raw_output_mod = Raw_output_mod.replace(',,,', ',')
        Raw_output_mod = Raw_output_mod.replace(',,', ',')
        Raw_output.close()
        Raw_output = open( energy_1_output, 'wt')
        Raw_output.write(Raw_output_mod)
        Raw_output.close()
        
    for fi in glob.glob(os.path.join(saved_energy_dir,"*.out")):
        os.rename(fi, fi[:-3] + "txt")   
    
    list=[]
    new_loop_num=loop_num+1

    for i in range(1,new_loop_num):
        item = ''.join(['prod',str(i),'.txt'])
        list.append(item)  

    for i in list:
        energy_1_output   = os.path.join(saved_energy_dir, i)  

        energy = pd.read_csv(energy_1_output, sep=",", header=None, on_bad_lines='skip')
        os.remove(energy_1_output)
        energy.columns = ["dummy", "Etot", "EKtot", "EPtot"]
        energy = energy[["Etot", "EKtot", "EPtot"]]

        energy_name   = ''.join([os.path.splitext(i)[0],'.csv'])
        energy_save   = os.path.join(saved_energy_dir, energy_name)
        energy.to_csv(energy_save, header = True, index = False)