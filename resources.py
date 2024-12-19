import os
# Paths relative to the script directory
current_dir = os.path.dirname(os.path.abspath(__file__))
model_file_path = os.path.join(current_dir, "food_101", "model.keras")
file_path = os.path.join(current_dir, "food_101", "label.labels.txt")
# Load class names
try:
    with open(file_path, 'r') as file:
        class_names = [line.strip() for line in file]
except FileNotFoundError:
    raise FileNotFoundError(f"File not found: {file_path}. Ensure it is included in the deployment.")
