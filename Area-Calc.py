import math

print("Which shape do you want to calculate the area for?")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
print("4. Pentagon (Regular)")
print("5. Hexagon (Regular)")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    r = float(input("Enter the radius: "))
    area = math.pi * r * r
    print("The area of the circle is:", area)

elif choice == 2:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length * width
    print("The area of the rectangle is:", area)

elif choice == 3:
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)

elif choice == 4:
    side = float(input("Enter the side length of the regular pentagon: "))
    area = (5 * side ** 2) / (4 * math.tan(math.pi / 5))
    print("The area of the regular pentagon is:", area)

elif choice == 5:
    side = float(input("Enter the side length of the regular hexagon: "))
    area = (3 * math.sqrt(3) * side ** 2) / 2
    print("The area of the regular hexagon is:", area)

else:
    print("Invalid choice. Please run the program again.")