import math

import math

def  quadRoots(a,b,c):


    if b**2-4*a*c < 0:
        return "No real roots"

    root1= ( -b + math.sqrt(b**2 - 4*a*c )) /(2*a)

    root2= ( -b - math.sqrt(b**2 - 4*a*c )) /(2*a)

    if b**2-4*a*c > 0:

        if root1>root2:
            return root1
        else:
            return root2



def perfectSquare(n):

   square = 1

   while square < n:
      if square*square==n:
          return True
      square = square + 1
          
   return False

def isPrime(number):
   if number > 1 :
      for x in range(2,number):
        if number % x == 0:
          return False
      return True
   else:
     return False



def addPrimes(x):
    num = 1
    sum = 0
    while(num<= x):

        if(isPrime(num) == True):
           sum+= num
        num = num + 1
    return sum   
    
            
          

    
