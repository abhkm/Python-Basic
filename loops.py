smallest = None
largest = None

while True :
    num = input("Enter  number : ")
    
    if num == "done" : 
         break
    try : 
        temp = int(num)
        if  largest is None and smallest is None : 
            largest = temp
            smallest = temp
        elif temp > largest :
            largest = temp
        elif temp < smallest :
            smallest = temp 
    except : 
        print("Invalid Input")
    
    print (num)

print("Maximum : ", largest)
print("Minimum : ", smallest)