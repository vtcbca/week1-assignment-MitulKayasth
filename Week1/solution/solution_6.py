#Write a python script to enter any string and print only part of string. Take input of start character and end character from user.
inputString = "Geeksforgeeks"
 
count = 0
 
# Loop through the string
for i in inputString:
      count = count + 1
newString = inputString[ 0:2 ] + inputString [count - 2: count ]
 
# Printing the new String
print("Input string = " + inputString)
print("New String = "+ newString)
