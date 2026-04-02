file = open("1.txt","w")

file.write("Python is very easy laguege \n")

file.close()

print("Data return Successfully")

file = open("1.txt","r")

content = file .read()

print(content)

file.close()


