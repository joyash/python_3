pi = 3.141592656
formatPI = "value of PI: {:.3f}" .format(pi)
print(formatPI)

radius = float(input("Enter the radius"))
areaCircle = pi * radius ** 2

print(f"Area of a circle {areaCircle:.4f}")