def cubicSeries(n):

      if n <= 0:
          return 0
              
      else:
            i=1

            while i <= n:
                 
                    return n**3 + cubicSeries(n-1)

                    i = i - 1

   

def cubicSeries_r(n):

       if n<=0:  #base case stops the recursion 
           return 0   #if else statement stops infinite recursion

       else:
        return n**3 + cubicSeries_r(n-1)  # recursive case 



def power(n):
    if n <= 0:
           return 0

    else:
           return n**n
           


def sumSeries(n):

       if n <= 0:
              return 0
       else:
             return power(n) + sumSeries(n-1)
               
       
       
       
       


   
