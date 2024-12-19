import os
model_file_path = "food_101//model.keras"
file_path = "food_101//label.labels.txt"
# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_paths = os.path.join(current_dir, file_path)
# Open the file
with open(file_paths, 'r') as file:
    class_names = [line.strip() for line in file]
