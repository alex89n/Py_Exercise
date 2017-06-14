# def funk(c):
    # if c < -(273.15):
        # print("That temperature doesn't make sense!")
    # else:
        # f = c*1.8 + 32
        # return f

        
# temperatures = [10, -20, -289, 100]

# for temp in temperatures:
    # print(funk(temp))
    
    
file = open("example.txt", 'r')
content = file.read()
file.seek(0)
content = file.readlines()
print(content)
content = [i.rstrip("\n") for i in content]
print(content)
file.close()
print(content)