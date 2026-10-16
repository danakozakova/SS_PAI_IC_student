x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x >= y:
    max = x
else:
    max = y
if max < z:
    max = z
print(max)
