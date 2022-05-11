import os

def get_pdb(pdb_dir):
    files = os.listdir(pdb_dir)

    for f in files:
        if '_.' in f:
            newname_1 = f.split('.')[0]
            newname_2 = int(f.split('.')[1])
            newname = newname_1 + '{:04}'.format(newname_2) + '.pdb'
            os.rename(os.path.join(pdb_dir,f), os.path.join(pdb_dir,newname))