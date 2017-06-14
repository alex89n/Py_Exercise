def convert(c):
    f = c * 1.8 +32
    return f

temp = float(input("Enter temp in C: "))

if temp < -273.15:
    print("Imposible")
else:
    print("Temp of {}C is equal to {}F".format(temp,convert(temp)))
