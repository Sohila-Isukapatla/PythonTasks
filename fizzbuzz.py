# Print numbers from 1 to 100.
# For multiples of 3,print "Fizz",
# for multiples of 5 print "Buzz",
#for multiples of both print "FizzBuzz".


for x in range(1,101):
    if x%3 ==0 and x%5 ==0 :
        print("FizzBuzz")
    elif x%3 ==0 :
        print("Fizz")
    elif x%5 ==0:
        print("Buzz")
    else :
        print(x)

