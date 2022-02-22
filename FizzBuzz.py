count = 1

while count<=100: #maximum amount that will be printed
    if count%3 == 0: #residue when devided by 3
        if count%5 == 0: #residue when also devided by 5
            print("Fizz Buzz")
        else:
            print("Fizz")
    elif count%5 == 0: #residue when devided by 5
        print("Buzz")
    else:
        print(count) #if not devided by 3 or 5 print the number
    count += 1 #increase the count
    continue #return to start of loop