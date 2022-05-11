import os
import numpy as np
import pytraj as pt

from topology_analysis import amber

def get_data(system,model_number,traj_name,top_name,traj_dir,top_dir,solvent_type,center_residue,tag,first_shell_radius,second_shell_radius,export_data_dir):
    
    analysis_method     ='water_shell'
    model               = ''.join(['model_',str(model_number)])
    traj_file           = os.path.join(traj_dir,traj_name)
    top_file            = os.path.join(top_dir,top_name)
    loaded_top          = amber(traj_file,top_file)

    saved_wat_dir      = os.path.join(export_data_dir,analysis_method)   
    wat_name           = ''.join([model,'_',tag, '.csv'])
    wat_output         = os.path.join(saved_wat_dir, wat_name)

    isExist = os.path.exists(saved_wat_dir)
    if not isExist:
        os.makedirs(saved_wat_dir)
        print("The new directory is created! : ", saved_wat_dir)

    wat      = pt.watershell(loaded_top, solute_mask=center_residue,solvent_mask=solvent_type,lower=first_shell_radius,upper=second_shell_radius,dtype='dataframe')
    wat.index = np.arange(1, len(wat) + 1)
    wat = wat.rename({'WS_00000[lower]': 'First shell at 5 Å', 'WS_00000[upper]': 'Second shell at 8 Å'}, axis=1) 
    wat['TIME'] = wat.index / 10
    wat['MAIN_SYSTEM'] = str(system)
    wat['MODEL'] = str(model)
    wat   = wat[['TIME','First shell at 5 Å','Second shell at 8 Å','MAIN_SYSTEM','MODEL']]

    wat.to_csv(wat_output, index=False)