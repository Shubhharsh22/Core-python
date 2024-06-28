count=0
number=input("ENTER THE NUMBER FOR CHECKING IF ITS PRIME")
for number in range(1,100):
    if number == 1:
        print("1 is not a prime number")
    else:
        for number in range(2,100):
            if number % 2 == 0:
                count=count+1
if count>1:
    print(number,"is not a prime number")
else:
    print(number,"is a prime number")





