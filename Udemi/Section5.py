# file = open("example.txt", 'r')
# content = file.read()
# file.seek(0)
# content = file.readlines()
# print(content)
# content = [i.rstrip("\n") for i in content]
# print(content)
# file.close()
# print(content)

# cont = ["Pera","djoka","mika"]
# file = open("example2.txt", 'w')
# cont = [file.write(i + "\n") for i in cont]
# file.close()

# with open("example.txt" , "a+") as file:
    # file.seek(0)
    # cont = file.read()
    # file.write("\nLINE")

# print(cont) 
  

def funk(c):
    # if c < -(273.15):
        # pass
        # print("That temperature doesn't make sense!")
    # else:
    if c > -(273.15):
        f = c*1.8 + 32        
        with open("Exercise 5.txt", 'a') as file:
            file.write(str(f) + "\n")
        return f

        
temperatures = [10, -20, -289, 100]

for temp in temperatures:
    funk(temp)
        
# temperatures=[10,-20,-289,100]
        
# def writer(temperatures):
    # with open("Exercise 5.txt", 'w') as file:
        # for c in temperatures:
            # if c>-273.15:
                # f=c*9/5+32
                # file.write(str(f)+"\n")
 
# writer(temperatures)