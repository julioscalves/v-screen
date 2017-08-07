import os
import glob
import shutil
import tqdm # Provides a nice progress bar

receptor_dir = os.getcwd()
ligand_dir = "C:\Autodock-MGL-1.5.6\ligands\cin\\" # <<< Remember to change this
os.chdir(ligand_dir)
ligands = glob.glob("*.pdbqt")
os.chdir(receptor_dir)

with open("config.txt") as config_file:
    for line in config_file.readlines():
        if line.startswith("receptor"):
            receptor = line[10:]
            break

for ligand in tqdm.tqdm(ligands):
    print("\n  Docking: {0} >>> {1}".format(ligand, receptor))
    os.system("vina.exe --config config.txt --ligand " + ligand_dir + ligand + " --log " + ligand[:-6] + ".log > vina.txt")
    shutil.move(ligand_dir + ligand[:-6] + "_out.pdbqt", receptor_dir + "\\" + ligand[:-6] + "_out.pdbqt")
