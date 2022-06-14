import os

def get_pdb(pdb_dir):
    files = os.listdir(pdb_dir)

    for f in files:
        if '_.' in f:
            newname_1 = f.split('.')[0]
            newname_2 = int(f.split('.')[1])
            newname = newname_1 + '{:04}'.format(newname_2) + '.pdb'
            os.rename(os.path.join(pdb_dir,f), os.path.join(pdb_dir,newname))

    for f in files:
        if '.1' in f:
            newname_1 = f.split('.')[0]
            newname_2 = int(f.split('.')[1])
            newname_3 = f.split('_')[0]
            newname_4 = f.split('_')[1]
            newname_5 = f.split('_')[2]
            newname_6 = newname_5.split('.')[0]
            newname = ''.join([newname_3,'_',newname_4,'_']) + '{:04}'.format(int(newname_6)) + '.pdb'
            os.rename(os.path.join(pdb_dir,f), os.path.join(pdb_dir,newname))