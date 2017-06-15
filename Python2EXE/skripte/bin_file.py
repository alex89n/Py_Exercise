template = "c:\\Shared\\Printer\\Barcode_template"
f = open (template, 'rb')
x = open ("log", 'wb')
try:
    temp = f.read(255)
    while temp:
        x.write(temp)
        temp = f.read(255)
finally:
    x.close()
    f.close()    
    



