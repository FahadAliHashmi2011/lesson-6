a = 10
b = 12
c = 0
if a and b and c :
    print("all the numbers have a boolean value as true")
else:
    print("at least one number has a boolean value of false")


a = 10
b =-10
c = 0
if a > 0 or b > 0:
    print("either number is greater than 0")
else: 
    print(" no number is greater than 0")

if a > 0 or b > 0:
    print("either number is greater than 0")
else: 
    print(" no number is greater than 0")



#not equal operator
a = 10 
b = 12
c = 12
print(a != b)
print(b != c)
a = "python"
b = "coding"
if a != b:
    print(a,'and',b, "are different") 

    a=5
    b=5

if(a == 1) != (b==5):
    print( "hello")


a=int (input("enter a number"))
if a%2 !=0 : 
    print( a,"is not an even number")


# bmi checker  
height = float(input("please enter your height in cm"))
weight = float(input("please enter your weight in kg"))

bmi = weight / (height/100)**2
print("ur BMI is",bmi)

if bmi<=18.4:
    print("u are underweight")
elif bmi<=24.9:
    print("u are healthy")
elif bmi<=29.9:
    print("u are overweight")

elif bmi<=34.9:
    print("u are severley overweight")
elif bmi<=39.9:
    print("u are obese")
else:
    print(" u are sevrely obese")
































