import getpass

choice = None
try:
    choice = int(input("Enter a num:"))
except ValueError:
    print("Enter in number format")    
print (choice)