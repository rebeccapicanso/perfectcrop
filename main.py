# main.py magic

import subprocess

print("Welcome!")

def run():
    shots_yes_no = input("Do you need to divide your video into individual shots? (yes/no)")
    if shots_yes_no == "yes":
        print("Great, a json file will be created with the shots, and the shots will be saved as individual newly rendered videos.")

        subprocess.run(['python', 'shots.py'])
        subprocess.run(['python', 'splice_shots.py'])

    grids = input("Do you want to use the grid? (yes/no)\n"+
    "Please note that the grid will standardize all shots. Some loss of quality may occur.\n"+
    "You need more than 24 shots to use the grid as intended. If you have less, files will be duplicated.\n")

    if grids == "yes":
        print("Great, the grid will standardize all shots. Some loss of quality may occur.")
        
        subprocess.run(['python', 'video_standardize.py'])
        subprocess.run(['python', 'nightmare_grid.py'])

run()
print("Thank you for using Perfect Crop. Check your files for the newly rendered videos.")
print("Please continue to respect the artistic & open-source nature of this project.")
print("Created by Rebecca Picanso for Court Laureate, a short computational film screened at LARPA gallery, 2023 (NY,NY)\n\n")

