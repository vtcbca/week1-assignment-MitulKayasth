2)Write a python script to enter any number and print the sum of its digit.
def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = 12345
print(getSum(n))




