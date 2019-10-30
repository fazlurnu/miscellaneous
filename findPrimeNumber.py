#python 3.5.2

a = 1000; #input

primeNumberList = [2, 3]

#start with loop, from the value to 1
#if the mod of the value and that test number is zero, it's not prime number

isPrimeNumber = True

for i in range(a): #
    if(i>3):
        for primeNumber in primeNumberList:
            if(i%primeNumber==0):
                isPrimeNumber = False
                break
            else: isPrimeNumber = True

        if(isPrimeNumber):
            primeNumberList.append(i)
    
print(primeNumberList)
