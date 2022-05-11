import pytraj as pt
import os

def amber(traj_file,top_file):

    loaded_top  = pt.load(traj_file, top=top_file)

    return loaded_top

# system can be re (reactant), ts1 (transition state 1) or im1 (intermediate 1)
# model number can be int starting from 1
# traj_name is the name of trajectory file (for amber it can be .nc and .ncrst files)
# top_name is the name of topology file (for amber it can be .prmtop)
# traj_dir is the tracjectory directory
# top_dir is the topology directory