import os
import pandas as pd
import numpy as np

def optmized_structure(system,tag,input_dir,output_dir):

    analysis_method         = 'optimized_charge'
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
        output_file = open(os.path.join(output_new_dir,''.join([file_name,'.csv'])),'w+')
        print(file_name)
        start_word=' Mulliken charges and spin densities:'
        end_word=' Mulliken charges and spin densities with hydrogens summed into heavy atoms:'
        for i,line in enumerate(open(target_file,'r')):
            if start_word in line: 
                start_line_num=i

            if end_word in line: 
                end_line_num=i

        for j,line in enumerate(open(target_file,'r')):
            if j > start_line_num and j < end_line_num-1:
                output_file.write(line)

        masking_replace     =   {   ' ':',',
                                    ',,,,,':',',
                                    ',,,,':',',
                                    ',,,':',',
                                    ',,':','} 
        for existing_data, replacing_data in masking_replace.items():
            output_file = open(os.path.join(output_new_dir,''.join([file_name,'.csv'])),'r')
            replaceing_output = output_file.read()
            replaceing_output = replaceing_output.replace(existing_data,replacing_data)
            read_output = open(os.path.join(output_new_dir,''.join([file_name,'.csv'])),'wt')
            read_output.write(replaceing_output)
            read_output.close()
        
        df = pd.read_csv(os.path.join(output_new_dir,''.join([file_name,'.csv'])))
        df=df.reset_index(drop=True) 
        df.index = df.index + 1
        df.columns=['ELEMENT','CHARGE','MULTIPLICITY']
        df.to_csv(os.path.join(output_new_dir,''.join([file_name,'.csv'])),index=False)