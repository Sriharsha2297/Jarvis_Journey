def Temparature(Temp):
    if Temp > 30:
        return print("Temp is Raising, check for overheating")
    elif Temp < 0:
        return print("Temp is Falling, check for freezing")
    else:        return print("Temp is Normal")

def Selection(int):
    if int == 1: 
        return print("You will get 10% discount")
    elif int == 2: 
        return print("You will get 20% discount")
    elif int == 3:
        return print("You will get 30% discount")
    else:        return print("Invalid Selection")


#Temparature Check
Temp = float(input("Enter the Temparature in Celsius: "))
Temparature(Temp)


#Discount Selection 
print("Select the discount option:")
Select = input ("enter your choice from 1, 2, or 3: ")
Selection(int(Select))