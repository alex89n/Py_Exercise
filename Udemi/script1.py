def funk(c):
    if c < -(273.15):
        print("That temperature doesn't make sense!")
    else:
        f = c*1.8 + 32
        return f

        
temperatures = [10, -20, -289, 100]

for temp in temperatures:
    print(funk(temp))