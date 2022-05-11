import os
import numpy as np
import pandas as pd
import pytraj as pt

from topology_analysis import amber

def get_data(model_number,traj_name,top_name,traj_dir,top_dir,export_data_dir):
    
    analysis_method     ='hydrogen_bond'
    model               = ''.join(['model_',str(model_number)])
    traj_file           = os.path.join(traj_dir,traj_name)
    top_file            = os.path.join(top_dir,top_name)
    loaded_top          = amber(traj_file,top_file)

    saved_hb_dir        = os.path.join(export_data_dir,analysis_method)   
    hb_txt_name             = ''.join([model,'.csv'])
    hb_txt_output           = os.path.join(saved_hb_dir, hb_txt_name)

    isExist = os.path.exists(saved_hb_dir)
    if not isExist:
        os.makedirs(saved_hb_dir)
        print("The new directory is created! : ", saved_hb_dir)

    hb            = pt.hbond(loaded_top)
    distance_mask = hb.get_amber_mask()[0]  
    hb_list = pd.DataFrame(distance_mask, columns = ['h_bond_list'])
    hb_list['h_bond_list']   = hb_list['h_bond_list'].str.replace(':',',')
    hb_list['h_bond_list']   = hb_list['h_bond_list'].str.replace('@',',')
    hb_list['h_bond_list']   = hb_list['h_bond_list'].str.replace(' ','')
    hb_list.to_csv(hb_txt_output, sep ='\t', index=False, header=False)

    hb_list                  = pd.read_csv(hb_txt_output, header=None)
    hb_list.columns          = ['N','RES_DONOR', 'ATOM_DONOR', 'RES_ACCEPTOR','ATOM_ACCEPTOR']
    hb_list                  = hb_list[['RES_DONOR', 'ATOM_DONOR', 'RES_ACCEPTOR','ATOM_ACCEPTOR']]
    hb_list                  = hb_list.sort_values(by="RES_DONOR", ascending=True)
    hb_list['MODEL'] = str(model)
    hb_list_name                     = ''.join(['hb_list_', model, '.csv'])
    
    hb_list_output       = os.path.join(saved_hb_dir, hb_list_name)
    hb_list.to_csv(hb_list_output, index=False)
    os.remove(hb_txt_output)

    hb_count           = hb_list['RES_DONOR'].value_counts()
    hb_count           = hb_count.sort_index(ascending=True)
    hb_count_name         = ''.join(['hb_count_', model, '.csv'])

    hb_count_output = os.path.join(saved_hb_dir, hb_count_name)

    hb_count.to_csv(hb_count_output, index=True)
    hb_count           = pd.read_csv(hb_count_output)
    hb_count           = hb_count.rename(columns={"RES_DONOR":"COUNT"})
    hb_count           = hb_count.rename(columns={"Unnamed: 0":"RESIDUE"})
    hb_count.to_csv(hb_count_output, index=False)