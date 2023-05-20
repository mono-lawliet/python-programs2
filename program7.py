x = int(input("Enter first number? "))
y = int(input("Enter second number? "))
usr_input = input ("Enter what to do? ")
print("First Number:", x)
print("Second Number:", y)
sum1 = x + y
sum2 = x-y
sum3 = x*y
sum4 = x/y
if usr_input =="add":
   print("Your answer is = "+str(sum1))
elif usr_input =="subtract":
   print("Your answer is = "+str(sum2))
elif usr_input =="multiply":
   print("Your answer is = "+str(sum3))
elif usr_input =="divide":
   print("Your answer is = "+str(sum4))
else:
   print("try again")
