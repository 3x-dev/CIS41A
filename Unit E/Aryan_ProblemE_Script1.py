'''
Aryan Singhal
CIS 41A   Winter 2024
Unit E, Problem E
'''

def find_garden(plant_name, plant_type, plant_height):
    suitable_gardens = []

    if plant_type.lower() == "vegetable":
        suitable_gardens.append("Vegetable Garden")

    if plant_type.lower() == "flower" and plant_height <= 3:
        suitable_gardens.append("Low Garden")

    if plant_type.lower() == "flower" and plant_height <= 6:
        suitable_gardens.append("High Garden")

    if suitable_gardens:
        print(f"A {plant_name} can be planted in the {' or the '.join(suitable_gardens)}.")
    else:
        print(f"A {plant_name} cannot be planted in any of the gardens.")

plant_name = input("Please enter the plant name: ")
plant_type = input("Please enter the plant type: ")
plant_height = int(input("Please enter the plant height: "))

find_garden(plant_name, plant_type, plant_height)


# Test:
# Name: Lily, Type: Flower, Height 3
# Name: Bonsai, Type: Tree, Height 2
# Name: Carrots, Type: Vegetable, Height 1
# Name: Corn, Type: Vegetable, Height 8
# Name: Rose, Type: Flower, Height 5
# Name: Sunflower, Type: Flower, Height 8



'''
Execution results:
Please enter the plant name: Lily
Please enter the plant type: Flower
Please enter the plant height: 3
A Lily can be planted in the Low Garden or the High Garden.

Please enter the plant name: Bonsai
Please enter the plant type: Tree
Please enter the plant height: 2
A Bonsai cannot be planted in any of the gardens.

Please enter the plant name: Carrots  
Please enter the plant type: Vegetable
Please enter the plant height: 1
A Carrots can be planted in the Vegetable Garden.

Please enter the plant name: Corn
Please enter the plant type: Vegetable
Please enter the plant height: 8
A Corn can be planted in the Vegetable Garden.

Please enter the plant name: Rose
Please enter the plant type: Flower
Please enter the plant height: 5
A Rose can be planted in the High Garden.

Please enter the plant name: Sunflower
Please enter the plant type: Flower
Please enter the plant height: 8
A Sunflower cannot be planted in any of the gardens.
'''