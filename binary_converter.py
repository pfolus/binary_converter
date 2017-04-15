a = input('Provide a number and its type (e.g.: "1011 2"):')
a = a.split(" ")
number = a[0]
numbertype = a[1]
decimal = '10'
binary = '2' 

if numbertype == decimal:  #decimal to binary conversion using divide by 2 method
    binary = ''
    number = int(number)
    print(binary)
    while number > 0:
        a = number % 2
        number //= 2
        binary += str(a)  # here we get reversed binary code as a string 

    binary = list(binary)   #turning "binary" string into list in order to reverse it
    binary.reverse()
    if binary[0] == '0':  
        binary.pop(0)
    binary = "".join(binary)
    print(binary, str(2))

elif numbertype == binary:  #binary to decimal conversion using sum of weighter digits
    dec = 0
    n = len(number) - 1
    number = list(number)
    error = 0                          
    for item in number:  #checking if entered binary number is correct
        if item != '0' and item != '1':
            error = 1
    if error == 1:
        print("incorrect binary number format")
    else:
        for char in number:   
            if char == '1':
                dec += 2**n
            n -= 1
        print(dec, str(10))
else:
    print("Wrong type inputed")




