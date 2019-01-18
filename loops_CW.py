def main():

    # exercise1()
    # exercise2()
    # exercise3()
    exercise4()



# ### Exercise 1:
# Print -20 to and including 50.
# Use any loop you want.

def exercise1():
    x = -20
    while x <= 50:
        print(x)
        x += 1

# ### Exercise 2:
# Create a loop that prints even numbers from 0 to and including 20.
def exercise2():
    y = 0
    while y <= 20:
        print(y)
        y += 2

# ### Exercise 3:
# Prompt the user for 3 numbers.
# Then print the 3 numbers along with their average after the 3rd number is entered.
# Refer to example below replacing ```NUMBER1```, ```NUMBER2```, ```NUMBER3```, and
# ```THEAVERAGE``` with the actual values.
#
# Ex.Output
# ```
# The average of NUMBER1, NUMBER2, and NUMBER3 is THEAVERAGE
# ```

def exercise3():
    userInput1 = int(input("Enter a number"))
    userInput2 = int(input("Enter another number"))
    userInput3 = int(input("Enter one last number"))
    average = (userInput1 + userInput2 + userInput3) / 3

    print("The average of " + str(userInput1) + ", " + str(userInput2) + ", " + str(userInput3) + " is " + str(average))

# ### Exercise 4:
# Password Checker - Ask the user to enter a password.
# Ask them to confirm the password.
# If it's not equal, keep asking until it's correct or they enter 'Q' to quit.

def exercise4():



    while True:
        passWord = input("Enter password")
        confirm = input("Confirm password")
        if(confirm == passWord):
            print("CONFIRMED!")
            break
        print("Passwords Do Not Match!")



if __name__ == '__main__':
    main()
