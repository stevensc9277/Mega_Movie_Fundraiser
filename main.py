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
def num_check(question):
  error = "PLease enter an integer that is more than 0"
  while True:
    try:
      response = int(input(question))
      # repeat question if input is too low
      if  response <= 0:
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

  

# initialise loop so that it runs at least once
name = ""
count = 0
max_tickets = 5
while name != "xxx" and count <= max_tickets:
  # get details
  print("You have {} seats left".format(max_tickets - count))
  # ask for name
  name = name_check("Name: ")
  
# End the loop if exit code is entered
  if name == "xxx":
    break
  count += 1

  print()
if count == max_tickets:
  print("You have sold all available tickets")
else:
  print("You have {} tickets left".format(max_tickets - count + 1))


  age = num_check("How old are you? ")
  # Check that age is valid...
  if age < 12:
    print("Sorry, you are too young for this movie")
    continue
  elif age > 130:
    print("That is very old - it looks like a mistake")
    continue

# Ask user what snack they want and how many portions
# Ask for the payment method (cash/credit)
# Credit payment incurs a 5% surcharge which is not included in the movie company's profits (goes to credit company)
# Calculate the cost of tickets and snacks (including the credit card surcharge if necessary)
# Work out how many of each snack has been ordered
# Work out the total profit (see the spreadsheet for profit details). Note that the profit on the snacks is 20% of the sales price (excluding the surcharge).
# Print out the total cost for each ticket / snack purchase