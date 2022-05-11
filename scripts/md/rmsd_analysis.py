import os
import numpy as np
import pytraj as pt

from topology_analysis import amber

def get_data(system,model_number,masking,reference_frame,tag,traj_name,top_name,traj_dir,top_dir,export_data_dir):
    
    analysis_method     ='rmsd'
    model               = ''.join(['model_',str(model_number)])
    traj_file           = os.path.join(traj_dir,traj_name)
    top_file            = os.path.join(top_dir,top_name)
    loaded_top          = amber(traj_file,top_file)

    saved_rmsd_dir      = os.path.join(export_data_dir,analysis_method)   
    rmsd_name           = ''.join([model,'_', tag, '.csv'])
    rmsd_output         = os.path.join(saved_rmsd_dir, rmsd_name)

    isExist = os.path.exists(saved_rmsd_dir)
    if not isExist:
        os.makedirs(saved_rmsd_dir)
        print("The new directory is created! : ", saved_rmsd_dir)

    rmsd                = pt.rmsd(loaded_top, ref=reference_frame, mask=masking,dtype='dataframe')
    rmsd.index          = np.arange(1, len(rmsd) + 1)
    rmsd['RMSD']        = rmsd['RMSD_00001']
    rmsd['TIME']        = rmsd.index / 10
    rmsd['MODE']        = str(tag)
    rmsd['MAIN_SYSTEM'] = str(system)
    rmsd['MODEL']       = str(model)
    rmsd                = rmsd.drop(rmsd.columns[[0]], axis=1)
    rmsd                = rmsd[['MAIN_SYSTEM','MODEL','MODE','TIME', 'RMSD']]

    rmsd.to_csv(rmsd_output, index=False)

# masking can be the residue name, residue number, a group of residues or even a group of atoms
# tag is the name for the specific masking

