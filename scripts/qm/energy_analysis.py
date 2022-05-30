import os

def frequency(system,tag,input_dir,output_dir):

    analysis_method         = 'frequency_energy'
    input_file_list         = [_ for _ in os.listdir(input_dir) if _.endswith('.out')]
        
    output_new_dir          = os.path.join(output_dir,system,tag,analysis_method)
    isExist = os.path.exists(output_new_dir)
    if not isExist:
        os.makedirs(output_new_dir)
        print("The new directory is created! : ", output_new_dir)    
    
    for file in os.listdir(output_new_dir):
        os.remove(os.path.join(output_new_dir,file))

    for single_file in input_file_list:
        target_file = os.path.join(input_dir,single_file)

        isExist = os.path.exists(output_new_dir)
        if not isExist:
            os.makedirs(output_new_dir)
            print("The new directory is created! : ", output_new_dir)

        file_name,extension=single_file.split('.')
        system_label,state_label,mul_label,charge_label=file_name.split('_')
        output_file = open(os.path.join(output_new_dir,''.join([file_name,'.csv'])),'w+')

        masking_label       =   {   system_label:',',
                                    state_label:',',
                                    mul_label:',',
                                    charge_label:',',
                                }

        for single_label, split_sym in masking_label.items():
            output_file.write(','),output_file.write(single_label)

        masking_search      =   {   'Zero-point correction=',
                                    'Thermal correction to Energy=',
                                    'Thermal correction to Enthalpy=',
                                    'Thermal correction to Gibbs Free Energy=',
                                    'Sum of electronic and zero-point Energies=',
                                    'Sum of electronic and thermal Energies=',
                                    'Sum of electronic and thermal Enthalpies=',
                                    'Sum of electronic and thermal Free Energies='
                                }

        for line in open(target_file,'r'):
            for single_mask in masking_search:
                if single_mask in line: output_file.write(','),output_file.write(line)

        masking_replace     =   {   ' Zero-point correction=                           ':'',
                                    ' (Hartree/Particle)':'',
                                    ' Thermal correction to Energy=                    ':'',
                                    ' Thermal correction to Enthalpy=                  ':'',
                                    ' Thermal correction to Gibbs Free Energy=         ':'',
                                    ' Sum of electronic and zero-point Energies=          ':'',
                                    ' Sum of electronic and thermal Energies=             ':'',
                                    ' Sum of electronic and thermal Enthalpies=           ':'',
                                    ' Sum of electronic and thermal Free Energies=        ':'',
                                    '_':',',
                                    '\n':'',
                                    ' ':'',
                                    ''.join([',',system_label]):''.join(['\n',system_label])
                                    }   
        header_table='SYSTEM,STATE,MULTIPLICITY,CHARGE,ZPE,Etot,Hcorr,Gcorr,E0+ZPE,E0+Etot,E0+Hcorr,E0+Gcorr'
        i = 1
        for existing_data, replacing_data in masking_replace.items():
            output_file = open(os.path.join(output_new_dir,''.join([file_name,'.csv'])),'r')
            replaceing_output = output_file.read()
            replaceing_output = replaceing_output.replace(existing_data,replacing_data)
            read_output = open(os.path.join(output_new_dir,''.join([file_name,'.csv'])),'wt')
            if i == 1:
                read_output.write(header_table)
            read_output.write(replaceing_output)
            read_output.close()
            i +=1
        print(''.join([file_name,'.csv']),'done!')

def single_point(system,tag,input_dir,output_dir):
    analysis_method         = 'single_point_energy'
    input_file_list         = [_ for _ in os.listdir(input_dir) if _.endswith('.out')]
        
    output_new_dir          = os.path.join(output_dir,system,tag,analysis_method)
    isExist = os.path.exists(output_new_dir)
    if not isExist:
        os.makedirs(output_new_dir)
        print("The new directory is created! : ", output_new_dir)    

    for file in os.listdir(output_new_dir):
        os.remove(os.path.join(output_new_dir,file))

    for single_file in input_file_list:
        target_file = os.path.join(input_dir,single_file)

        isExist = os.path.exists(output_new_dir)
        if not isExist:
            os.makedirs(output_new_dir)
            print("The new directory is created! : ", output_new_dir)

        file_name,extension=single_file.split('.')
        system_label,state_label,mul_label,charge_label=file_name.split('_')
        output_file = open(os.path.join(output_new_dir,''.join([file_name,'.csv'])),'w+')

        masking_label       =   {   system_label:',',
                                    state_label:',',
                                    mul_label:',',
                                    charge_label:',',
                                }

        for single_label, split_sym in masking_label.items():
            output_file.write(','),output_file.write(single_label)

        masking_search      =   {   'SCF Done:  E(UB3LYP) ='
                                }

        for line in open(target_file,'r'):
            for single_mask in masking_search:
                if single_mask in line: output_file.write(','),output_file.write(line.split('a',1)[0])

        masking_replace         =   {   ' SCF Done:  E(UB3LYP) =  ':'',
                                    'A.U.':'',
                                    '_':',',
                                    '\n':'',
                                    ' ':'',
                                    ''.join([',',system_label]):''.join(['\n',system_label])
                                    } 
        header_table=''.join(['SYSTEM,STATE,MULTIPLICITY,CHARGE,','E0-',tag])
        print(header_table)
        i = 1
        for existing_data, replacing_data in masking_replace.items():
            output_file = open(os.path.join(output_new_dir,''.join([file_name,'.csv'])),'r')
            replaceing_output = output_file.read()
            replaceing_output = replaceing_output.replace(existing_data,replacing_data)
            read_output = open(os.path.join(output_new_dir,''.join([file_name,'.csv'])),'wt')
            if i == 1:
                read_output.write(header_table)
            read_output.write(replaceing_output)
            read_output.close()
            i +=1
        print(''.join([file_name,'.csv']),'done!')