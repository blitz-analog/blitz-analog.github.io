import os
import subprocess
dir_path = "photos/Destinations/"
os.chdir(dir_path)
top_to_bottom = [
    "Faroe Islands",
    "Thailand",
    "Japan",
    "Iceland",
    "China",
    "San Francisco",
    "Hong Kong",
    "Costa Rica",
    "Switzerland",
    "Portugal",
    "Singapore",
    "New York",
    "Utah",
    "Tuscany",
    "Sardinia",
    "London",
    "Durham",
    "Boston",
    "Miami",
]

current_year = 2022

for ind, folder in enumerate(top_to_bottom):
    year = current_year-ind
    #if " " in folder:
    #   folder = folder.replace(" ", "\ ")
    print(f"{year}01180130 {folder}")
    subprocess.run(["touch", "-a", "-m", "-t", f"{year}01180130", f"{folder}"])
