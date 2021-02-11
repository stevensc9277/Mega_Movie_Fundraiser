# functions go here
# This function checks to make sure that user inputs a valid string
def name_check(question):
  while True:
    response = input(question)
    if response != "":
      return response
    else:
      print("Sorry - this can't be blank, please enter your name")
      print()


# This function checks to make sure that user inputs an integer between 12 and 130
def num_check(question, low, high):
  error = "Please enter an integer between {} and {}".format(low, high)
  while True:
    try:
      response = int(input(question))
      # repeat question if input is too low or too high
      if  response < low:
        print(error)
        print()
      elif response > high:
        print(error)
        print()
      # Program continues for valid input
      else:
        print()
        return response
    # For unexpected strings
    except ValueError:
      print(error)
      print()

  
# Get user details (name and age)
user = name_check("Name: ")
age_verify = num_check("How old are you? ", 12, 130)
# Ask user what snack they want and how many portions
# Ask for the payment method (cash/credit)
# Credit payment incurs a 5% surcharge which is not included in the movie company's profits (goes to credit company)
# Calculate the cost of tickets and snacks (including the credit card surcharge if necessary)
# Work out how many of each snack has been ordered
# Work out the total profit (see the spreadsheet for profit details). Note that the profit on the snacks is 20% of the sales price (excluding the surcharge).
# Print out the total cost for each ticket / snack purchase