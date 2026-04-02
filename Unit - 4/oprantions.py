file = open("1.txt","w")

file.write("Swastika is dagebaj \n")

file.close()

print("Data return Successfully")

file = open("1.txt","r")

content = file .read()

print(content)

file.close()


