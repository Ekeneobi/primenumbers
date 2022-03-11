################################################
#### Name: Ekene Obi ###########################
#### Student Id: 31-03-030-20-2 ################
#### Email: ekene.obi.2020@student.ism.de ######
################################################
################################################

#### Question(1.1) ####
## (a.) ##

# Define variable and ask user to input a +ve integer 
IntP = int(input('Kindly type in a positive integer here:'))

#  Define codition to check if the inputed interger is positive  
if  IntP > 1 :  #define condition for +ve integers
    
    print(IntP, "is a positive integer") #print if codition is true 
      
else: 
    
    print(IntP,"is not a positive integer") #print if condition is false

## (b.)

# Define variable and ask user to input a +ve integer 
IntP = int(input('Kindly type in a number here:'))
#  Define codition to check if the inputed interger is positive  
if  IntP > 1:    #define condition for +ve integers
    #Define range for prime number search and conditions for prime number
    for i in range(2,IntP//2):     #define range of factors
        if (IntP % i) == 0:        #conditon for prime numbers                    
           print(IntP, "is not a primenumber")  #print if condition is true
           break
    else:
           print(IntP,"is a primenumber")       #print if condition is false
        
else:     
    print(IntP,"is not a +ve integer, please input a +ve integer")  
                                                                         
## (c.)    

IntP = int(input('Kindly type in a number here:'))
#  Define codition to check if the inputed interger is positive  
if  IntP > 1:    
    #Define range for prime number search and condition for prime number
    for i in range(2,IntP//2):
        if (IntP % i) == 0:    
            print(IntP, "is not a primenumber")
            print("because",i,"X",IntP//i, "is",IntP)  #print factors         
            break  
    if (IntP % i) != 0:  
            print (IntP,"is a prime number")
    
IntPn = IntP + 1 #increase variable 
if True:
    for i in range (2,IntPn//2):
        if (IntPn % i) == 0:
          IntPn += 1  #increase variable till condition is met
              
    else:              
         print(IntPn,"is the next primenumber") #print next prime number
IntPp = IntP - 1  #reduce variable 
if True:
        for j in range (2,IntPp//2):
           if (IntPp % j) == 0:
              IntPp -= 1 #reduce till condition is met
              
        else:              
              print(IntPp,"is the previous primenumber") #print previous Prime number
              
        
else:    
     print(IntP,"is not a +ve integer, please input a +ve integer")
     
     
#### Question(1.2) ####################################
#######################################################
#######################################################
def checkInput(number):
    # check whether the input is valid
    # an input is valid if it is a positive integer value greater than one
    if number <= 1:
        return False
    # in case of an invalid input ask to re-enter another input until it 
    # is valid
    return True

def isPrime(number):
    
    # check whether the provided number is prime
    # you may use the algorithm presented in the lecture slides or another
    # (maybe more efficient) algorithm
    testPrime = True
    for i in range (2,number//2):
        if (number % i) == 0:
            return False
    
    return testPrime # should be boolean
    
    
def divisor(number):
    
    # return a divisor greater than 1 of the number
    # if it is a prime number, divisor should be number
    if  number > 1:    
    #Define range for prime number search
      for i in range(2,number//2):
        if (number % i) == 0: 
            print("divisors of",number,"are",i,"and",number//i)          
            break 
        divisor = i
    else:
        divisor = None
        return divisor
    

def nextPrime(startNumber):
    
    # get the next prime number
    # Hint: You may refer to other functions (within function call) e.g. isPrime()
    startNumber = startNumber + 1
    if True:
       for j in range (2,startNumber//2):
            if (startNumber % j) == 0:
                startNumber += 1
                
       else:
                print("the next prime number is", startNumber )
                nextPrime = startNumber
                return nextPrime
     

def prevPrime(startNumber):
    # get the next prime number
    # Hint: You may refer to other functions (within function call) e.g. isPrime()
    
    startNumber = startNumber - 1
    if True:
        for j in range (2,startNumber//2):
            if (startNumber % j) == 0:
                startNumber -= 1
                
        else:
               print("the previous prime number is", startNumber)
               prevPrime = startNumber
               return prevPrime

def main():
    
    #Use all the defined functions above
    number = int(input('Kindly type in a number here:'))
    #1st: Input a number and check whether the input is valid
    if checkInput(number) == True:
        print(number, "is a +ve integer" )
   
    
    #2nd: Check whether it is prime
        if isPrime(number) == True:
           print(number, "is a prime number" )
        else:
           print(number,"is not a prime number")
    #3rd: If it is not prime explain why. 
           divisor(number)
           startNumber = number
    # 4th: Print the previous and the next prime number 
           nextPrime(startNumber)
           prevPrime(startNumber)
           
    else:
        print(number,"is not a +ve integer")
    
    
    
    

# Run and test the main program               
main()


     


