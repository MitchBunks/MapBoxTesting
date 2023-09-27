import json

def format_coordinates(file_path):
    # Initialize an empty list to store the coordinates
    coordinates = []

    # Open the file and read each line
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into x and y coordinates
            x, y = map(float, line.strip().split(','))

            # Append the coordinate pair as a list to the coordinates list
            coordinates.append([x, y])

    # Convert each Python list to a JavaScript array and print it
    for coord in coordinates:
        js_array = json.dumps(coord)
        print(js_array + ',')  # Add a comma after each coordinate pair

# Call the function with the path to your text file
format_coordinates('coordinates.txt')
