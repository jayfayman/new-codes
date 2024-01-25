import math

length_ab = int(input("Enter the length of AB: "))
length_bc = int(input("Enter the length of BC: "))
length_ac = math.sqrt(((length_ab ** 2) + (length_bc ** 2)))
length_mc = length_ac/2
angle_in_radians = math.asin(length_mc/length_bc)
angle_in_degrees = int(angle_in_radians * (180/math.pi))
print (f"{angle_in_degrees}°")