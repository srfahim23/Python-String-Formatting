#Python-String-Formatting

#String format()
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

#Format theprice to be displayed as a number with two decimals:
price = 46
txt = "The price is {:.2f} dollars"
print(txt.format(price))

#Multiple Values
#If you want to use more values, just add more values to the format() method:
#print(txt.format(price, itemno, count))

#And add more placeholders:
quentity = 3
itemno = 567
price = 49
myorder = "I want {} prices of item number {} for {:.2f} dollars."
print(myorder.format(quentity, itemno, price))

#Index Numbers
#You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
quentity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quentity, itemno, price))

# Also, if youw ant to refer to the same value more than once, user the index number:
age = 36
name = "Fahim"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named Indexes 
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))