#######################################################################################################################################################
#
# Name: Atul
# SID: 750011108
# Exam Date: 27 March 2025
# Module: BEMM458
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-Atulexeter.git
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments


import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import random
customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments.

# Initialize an empty list to store (start, end) positions
my_list = []

# answer
# My student ID is 750011108 in that 1st digit is 7 and last digit is 8 and reslove and overall are the key comments in the list
# first i create a empty list in that then use the find() function where the word start and end

allocated_keys = [7, 8]

# i created a empty list as mention above (start_index, end_index)

# loop over the allocated keys
for key in allocated_keys:
    word = key_comments[key]
    start = customer_feedback.find(word)
    end = start + len(word) - 1  # calculate the ned index
    my_list.append((start, end))  # append the tuple to my_list

    print('my list')


##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
# Insert last two digits of ID number here:

# Write your code for Operating Profit Margin

# Write your code for Revenue per Customer

# Write your code for Customer Churn Rate

# Write your code for Average Order Value

# Call your designed functions here

# anser


# Operating Profit Margin
def operating_profit_margin(revenue, operating_profit):
    """
    Calculates Operating Profit Margin as a percentage.
    Formula: (Operating Profit / Revenue) * 100
    """


# Revenue per Customer
def revenue_per_customer(total_revenue, number_of_customers):
    """
    Calculates Revenue per Customer.
    Formula: Total Revenue / Number of Customers
    """


# Customer Churn Rate
def customer_churn_rate(customers_lost, total_customers):
    """
    Calculates Customer Churn Rate as a percentage.
    Formula: (Customers Lost / Total Customers) * 100
    """


# Average Order Value
def average_order_value(total_revenue, total_orders):
    """
    Calculates Average Order Value.
    Formula: Total Revenue / Total Orders
    """


# Inputs from my SID is  (First two digits: 75, Last two digits: 08)  as my SID is 750011108
first_two_digits = 75  # Example: Revenue, Customers Lost
last_two_digits = 8    # Example: Operating Profit, Number of Customers

# Call the functions with example inputs
# Example Revenue = £75,000; Operating Profit = £800
opm = operating_profit_margin(first_two_digits * 1000, last_two_digits * 100)
# Example Revenue = £75,000; Customers = 80
rpc = revenue_per_customer(first_two_digits * 1000, last_two_digits * 10)
# Example Customers Lost = 8; Total Customers = 75
ccr = customer_churn_rate(last_two_digits, first_two_digits)
# Example Revenue = £75,000; Orders = 750
aov = average_order_value(first_two_digits * 1000, first_two_digits * 10)

# Print the metrics
print(f"Operating Profit Margin: {opm:.2f}%")
print(f"Revenue per Customer: {rpc:.2f}")
print(f"Customer Churn Rate: {ccr:.2f}")
print(f"Average Order Value: {aov:.2f}")

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here

# answer
# first of all we have to import numpy, matplotlib, LinearRegression in the terminal as he help of pip install numpy, matplotlib, LinearRegression

# data
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
                  ).reshape(-1, 1)  # Independent variable
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# build a linear model
model = LinearRegression()
model.fit(prices, demand)

# Revenue maximazation
# Revenue  = price * demand
# Demand = slope * Price + intercept
# Revenue = Price * (slope * Price + intercept)
# Revenue = slope * Price^2 + intercept * Price
# Equation will be: Revenue = a * Price^2 + b * Price
# Vertex formula for equcation ax^2 + bx + c is -b/(2a)

# when we plot the  Regressionn line and data
plt.scatter(prices, demand, color='blue', label='Data')
plt.plot(prices, model.predict(prices), color='red', label='Regression Line')
plt.xlabel('Price')
plt.ylabel('Demand (Units)')
plt.title('Price vs Demand')
plt.legend()
plt.show()


##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart


# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0, 100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green',
         markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue')
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel = "Index"
plt.ylabel = "Random Number"
plt.legend('---')
plt.grid(True)
plt.show()


# anser
# In that we have to import matplotlib

# 100 random numbers between 1 and your student ID
# Student ID as maximum value
max_value = 750011108
random_numbers = [random.randint(1, max_value) for i in range(100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='o',
         markerfacecolor='green',
         markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')

plt.title("Line Chart of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.legend()
plt.grid(True)
plt.show()
