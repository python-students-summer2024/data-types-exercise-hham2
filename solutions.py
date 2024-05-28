"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """
    sales = input("What is the company's annual total sales figure? ")
    profitpt1 = int(sales)*23
    totalprofit = float(profitpt1 / 100)
    formattedprofit = "Profit: " + "$" + "{0:,.2f}".format(totalprofit)
    print(formattedprofit)




def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    n1 = int(input("enter one integer: "))
    n2 = int(input("enter another integer: "))
    n3 = float(n1 / n2)
    truncatedn3 = ("{0:.0f}".format(n3))
    remainder = n1 % n2
    if int(truncatedn3) != 1: 
      print(str(n2) + " goes into " + str(n1) + " a total of " + str(truncatedn3) + " times with a remainder of " + str(remainder))
    if int(truncatedn3) == 1: 
      print(str(n2) + " goes into " + str(n1) + " a total of " + str(truncatedn3) + " time with a remainder of " + str(remainder))


def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
    """
    miles_driven = input("how many miles have been driven? ")
    gas_used = input("how many gallons of gas have been used? ")
    mpg = float(miles_driven) / float(gas_used)
    print("Miles driven: " + str(miles_driven) + "\n" + "Gas used (gallons): " + str(gas_used) + "\n" + "Miles per gallon: " + str(mpg))




def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
    price1 = float(input("Enter price #1: "))
    price2 = float(input("Enter price #2: "))
    price3 = float(input("Enter price #3: "))
    formattedprice1 = "{0:.2f}".format(price1)
    formattedprice2 = "{0:.2f}".format(price2)
    formattedprice3 = "{0:.2f}".format(price3)
    ralignedprice1 = format(formattedprice1, ">10s")
    ralignedprice2 = format(formattedprice2, ">10s")
    ralignedprice3 = format(formattedprice3, ">10s")
    print("Here are your prices!" + "\n")
    print("Price #1: $ " + str(ralignedprice1) + "\n" + "Price #2: $ " + str(ralignedprice2) + "\n" + "Price #3: $ " + str(ralignedprice3))
