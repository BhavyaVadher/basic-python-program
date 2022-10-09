num1= float(input("enter the value of num1 :"))
num2= float(input("enter the value of num2 :"))
num3= float(input("enter the value of num3 :"))
num4= float(input("enter the value of num4 :"))

if(num1>num4):
    f1= num1
else:
    f1= num4
    
if(num2>num3):
    f2= num2
else:
    f2= num3   

if(f1>f2):
    print(f1, "is the gretest number")
else:
    print(f2, "is the gretest number")