cubes = [value ** 3 for value in range(1, 11)]

for cube in cubes:
    print(f"The cube of number {round(cube ** (1/3))} is: {cube}")