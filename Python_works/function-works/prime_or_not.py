
"""
def is_prime(num):
     
     if num <= 1:
          
        return False
     
     for i in range(2,num):
          
        if num % i == 0:
               
            return False
          
     return True

print(is_prime(17)) #True

print(is_prime(20)) #False

"""

def is_prime(num):
    
   flag = True

   for i in range(2,num):
        
      if num % i ==0:
            
         flag = False

         break
        
   return flag


def prime_upto_limit(limit):

   for number in range(1,limit+1):

      result = is_prime(number)

      if result == True:

         print(number)

prime_upto_limit(50)