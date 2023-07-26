# program to check input function behaviour
n = int(input("Enter the size of list : ")) 
lst = list(map(str,input("Enter the integer elements of list :").strip().split()))[:n]   #skip "strip().split()" function
print("The list is: ",lst)  # function to change input into list 