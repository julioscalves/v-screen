# v-screen
Virtual screening using Vina.

# usage
- Place both scripts in the receptor folder alongside with vina.exe
- Prepare the receptor's and the ligands' pdbqt file (add hydrogens and charges)
- Prepare the config.txt file for vina.exe
- Run

# description
- screen.py will loop through the ligands, executing vina.exe for each of them. The docked output will be moved for the receptor's folder.
- log.py will parse the log file generated by vina and will write a csv file with the ligands' id, pos, affinity (kcal/mol) and rmsd. Thus, selecting the ligands with highest affinity will be easier.