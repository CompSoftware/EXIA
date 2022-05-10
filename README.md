## **EXIA**
___

EXIA is the data analysis software package for quantumn mechanics (QM) and molecular dynamics (MD) calculations.
This is the portable version. EXIA can be downloaded and placed in anywhere.

* [MD Features](#Features)

### MD Features
___

* EXIA utilizes features from [PYTRAJ](https://github.com/Amber-MD/pytraj/blob/master/README.md) to extract the data from MD calcualtions by [AMBER](http://ambermd.org) including RMSD, bond lengths, angles, PDB extraction, water cluster, and hydrogen bond analysises.
* EXIA has its own feature to extract energy data from MD.

### Getting Started
___

EXIA can be imported by sys module. It needs output and input directories.

* Examples

```
import os, sys
sys.path.insert(0, os.path.abspath("../../../../EXIA/EXIA/md"))
import pdb_analysis
```

```
system='RE'

traj_name='prod_all.nc'
top_name='RE_solv.prmtop'

for i in range(1,2):
    model=''.join(['model_',str(i)])
    traj_dir = os.path.join('..','..','raw_data','md',system,'result','trajectory',model)
    top_dir   =  os.path.join('..','..','raw_data','md',system,'top_coord',model)
    export_data_dir = os.path.join('..','results','md_analysis_part_1',system,model)
    print('processing on',model)
    pdb_analysis.get_data(i,traj_name,top_name,traj_dir,top_dir,export_data_dir)
```
Each _system_ has many different substrate orientations which is called as _model_. _system_ and _model_ are used as the indexs to save the extraced data.

### License
___
[GPL v3](https://github.com/PYMMAMA/EXIA/blob/master/licenses/EXIA_license.txt).