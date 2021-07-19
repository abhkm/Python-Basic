# Python code to reverse a string
# using loop

given_string = input("Enter the string you want to be reversed : ")

def reverse(s):
    str = ""
    for i in s:
        print(type(str), type(i))
	   # str = i + str
    return str


print ("The original string is : ",end="")
print (given_string)

print ("The reversed string(using loops) is : ",end="")
print (reverse(given_string))
