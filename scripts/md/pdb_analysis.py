import os, glob
import pytraj as pt

from topology_analysis import amber
from rename_file import get_pdb

def get_data(model_number,traj_name,top_name,traj_dir,top_dir,export_data_dir):
    
    analysis_method     ='multiple_pdb'
    model               = ''.join(['model_',str(model_number)])
    traj_file           = os.path.join(traj_dir,traj_name)
    top_file            = os.path.join(top_dir,top_name)
    loaded_top          = amber(traj_file,top_file)

    saved_pdb_dir       = os.path.join(export_data_dir,analysis_method)   
    pdb_name            = ''.join([model,'_'])
    pdb_output          = os.path.join(saved_pdb_dir, pdb_name)

    isExist = os.path.exists(saved_pdb_dir)
    if not isExist:
        os.makedirs(saved_pdb_dir)
        print("The new directory is created! : ", saved_pdb_dir)

    pt.save(pdb_output, loaded_top, format='PDB', overwrite=True, options='multi')
    get_pdb(saved_pdb_dir)

def get_data_single(model_number,traj_name,top_name,traj_dir,top_dir,time,export_data_dir):
    
    analysis_method     =''
    model               = ''.join(['model_',str(model_number)])
    traj_file           = os.path.join(traj_dir,traj_name)
    top_file            = os.path.join(top_dir,top_name)
    loaded_top          = amber(traj_file,top_file)

    saved_pdb_dir       = os.path.join(export_data_dir,analysis_method)   
    pdb_name            = ''.join([model,'_',str(time)])
    pdb_output          = os.path.join(saved_pdb_dir, pdb_name)

    time_range = range(time,time+1)

    isExist = os.path.exists(saved_pdb_dir)
    if not isExist:
        os.makedirs(saved_pdb_dir)
        print("The new directory is created! : ", saved_pdb_dir)

    pt.save(pdb_output, loaded_top, format='PDB',overwrite=True,frame_indices=time_range, options='multi')
    get_pdb(saved_pdb_dir)
