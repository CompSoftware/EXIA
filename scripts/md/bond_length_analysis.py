import os
import numpy as np
import pandas as pd
import pytraj as pt

from topology_analysis import amber

def get_data(system,model_number,masking,tag,traj_name,top_name,traj_dir,top_dir,export_data_dir):
    
    analysis_method     ='bond_length'
    model               = ''.join(['model_',str(model_number)])
    traj_file           = os.path.join(traj_dir,traj_name)
    top_file            = os.path.join(top_dir,top_name)
    loaded_top          = amber(traj_file,top_file)

    saved_bd_dir        = os.path.join(export_data_dir,analysis_method)   
    bd_name             = ''.join([model,'_', tag, '.csv'])
    bd_output           = os.path.join(saved_bd_dir, bd_name)

    isExist = os.path.exists(saved_bd_dir)
    if not isExist:
        os.makedirs(saved_bd_dir)
        print("The new directory is created! : ", saved_bd_dir)

    bd                  = pt.distance(loaded_top, masking)
    bd                  = pd.DataFrame(bd)
    bd.index = np.arange(1, len(bd) + 1)
    bd['BOND_LENGTH']   = bd[0]
    bd['TIME']          = bd.index / 10
    bd['MODE']          = str(tag)
    bd['MAIN_SYSTEM']   = str(system)
    bd['MODEL']         = str(model)
    bd                  = bd.drop(bd.columns[[0]], axis=1)
    bd                  = bd[['MAIN_SYSTEM','MODEL','MODE','TIME', 'BOND_LENGTH']]

    bd.to_csv(bd_output, index=False)


def get_data_single(system,model_number,masking,tag,traj_name,top_name,traj_dir,top_dir,time,export_data_dir):
    
    analysis_method     ='bond_length'
    model               = ''.join(['model_',str(model_number)])
    traj_file           = os.path.join(traj_dir,traj_name)
    top_file            = os.path.join(top_dir,top_name)
    loaded_top          = amber(traj_file,top_file)

    saved_bd_dir        = os.path.join(export_data_dir,analysis_method)   
    bd_name             = ''.join([model,'_', tag, '.csv'])
    bd_output           = os.path.join(saved_bd_dir, bd_name)

    isExist = os.path.exists(saved_bd_dir)
    if not isExist:
        os.makedirs(saved_bd_dir)
        print("The new directory is created! : ", saved_bd_dir)

    bd                  = pt.distance(loaded_top, masking,frame_indices=time)
    bd                  = pd.DataFrame(bd)
    bd.index = np.arange(1, len(bd) + 1)
    bd['BOND_LENGTH']   = bd[0]
    bd['TIME']          = bd.index / 10
    bd['MODE']          = str(tag)
    bd['MAIN_SYSTEM']   = str(system)
    bd['MODEL']         = str(model)
    bd                  = bd.drop(bd.columns[[0]], axis=1)
    bd                  = bd[['MAIN_SYSTEM','MODEL','MODE','TIME', 'BOND_LENGTH']]

    bd.to_csv(bd_output, index=False)