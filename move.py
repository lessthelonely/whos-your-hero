import os
import shutil

# Set the paths to the source and destination directories
source_directory = './tropes'
destination_directory = './tropes/owl_rejected'

# Ensure the destination directory exists; create it if it doesn't
os.makedirs(destination_directory, exist_ok=True)

# Get a list of all files in the source directory with the ".owl" extension
owl_files = [file for file in os.listdir(source_directory) if file.endswith('.owl')]

# Move each ".owl" file to the destination directory
for file in owl_files:
    source_path = os.path.join(source_directory, file)
    destination_path = os.path.join(destination_directory, file)
    shutil.move(source_path, destination_path)

print("Files moved successfully.")
