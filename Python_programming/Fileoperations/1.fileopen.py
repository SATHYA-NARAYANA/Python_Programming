# File operation opening a file and eading its contents
#f = open("F:\PythonProgramming\product.txt","r")
#f = open(r"F:/PythonProgramming/product.txt","r")

# use r if dont need to change path in reverse

# by default read mode is considered so we no need to specify 
f = open("F:\PythonProgramming\product.txt")
print(f.read())

f.close()

print("\n Products Data Display Succesfully")
