# Python-String-Formatting
To make sure a string will display as expected, we can format the result with the format() method.

# String format()
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholdrs (curly bracket {}) in the text , and run the values through the format() method:

Example 

Add a placeholder wheere you want to display the price:

    price = 49
    txt = "The price is {} dollars"
    print(txt.format(price))

YOu can add parameters inside the curly brackets to specify how to conver to the value:

Example

Format the price to be displayed as a number with two decimals:

    price = 49
    txt = "The prce is {:.2f} dollars"
    print(txt.format(price))

Check out all formatting types in our String format() Reference.    

# Multiple Values
If you want to use more values, just add more values to the format() method:

    print(txt.format(price, itemno, count))

And add more placeholder:    

Example

    quantity = 3     #if not working then change value to quentity
    itemno = 567
    price = 49
    myorder = "I want {} pieces of item number {} for {:.2f} dollars."
    print(myorder.format(quantity, itemno, price))

# Index Numbers
You can use index numbers (a number inside the curly brackets {0}) to be
sure the values are placed in the correct placeholder:

Example

    quantity = 3
    itemno = 567
    price = 49
    myorder = "I want {0} pieces of item numbe {1} for {2:.2f} dollars."
    print(myorder.format(quantity, itemno, price))

    
