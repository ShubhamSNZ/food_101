model_file_path = "food_101//model.keras"
file_path = "food_101//label.labels.txt"
# Read the class names into a list
with open(file_path, 'r') as file:
    class_names = [line.strip() for line in file]


if __name__ == '__main__':
    # Print the class names to verify
    print(class_names)