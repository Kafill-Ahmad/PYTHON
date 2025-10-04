#while loop..
i=1
while(i<6):
    print(i)
    i+=1

#do while loop..
i=1
while True:
    print(i)
    i+=1
    if not (i<6):
        break
#Boolean data type..
if True:
    print("Valid")
else:
    print("Invalid")
if False:
    print("Valid")
else:
    print("Invalid")



#Exceptions..
try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    result=a+b
    print("Sum:",result)
except ValueError:
    # print("Indentation Error")
    print("Invalid input! Please enter numbers only.")



try:
    num=int(input("Enter a number: "))
    result=10/num
    print("Result:",result)
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Does not divided by zero.")















#Complex data type...
a=2+3j
print(type(a))
print(a)
