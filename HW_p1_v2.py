x = int(input("Input a whole number:_"))

if x%5==0 and x%3==0:
    print("Fizz Buzz")
elif x%5==0:
    print ("Fizz")
elif x%3==0:
    print ("Buzz")
else:
    print(x)
