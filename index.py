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