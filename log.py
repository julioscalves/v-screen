import glob
import pandas as pd

logs = glob.glob("*.log")

dataset = {"id": [],
           "pos": [],
           "affinity (kcal/mol)": [],
           "rmsd l.b.": [],
           "rmsd u.b.": []}

for log in logs:
    with open(log) as dock:
        for line in dock.readlines():
            if line.startswith("  ") and line.split()[0] != "|":
                dataset["id"].append(log[:-4])
                dataset["pos"].append(line.split()[0])
                dataset["affinity (kcal/mol)"].append(line.split()[1])
                dataset["rmsd l.b."].append(line.split()[2])
                dataset["rmsd u.b."].append(line.split()[3])

dataframe = pd.DataFrame(data=dataset)
dataframe.to_csv("docks.csv")
