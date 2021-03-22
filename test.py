# functions go here
import re
import pandas
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

  
# Checks number of tickets left and warns user if maximum is being approached
def check_tickets(tickets_sold, ticket_limit):
  # tells user how many seats are left
  if tickets_sold < ticket_limit - 1:
    print("You have {} seats left".format(ticket_limit - tickets_sold))
  
  # warns user that only one seat is left:
  else:
    print("*** There is ONE seat left!! ***")
  
  return ""

# Gets ticket price based on age
def get_ticket_price():
  # Get age (between 12 and 130)
  age = num_check("Age: ")

  # Check that age is valid
  if age < 12:
    print("Sorry you are too young for this movie")
    return "invalid ticket price"

  elif age > 130:
    print("That is very old - it looks like a mistake")
    return "invalid ticket price"

  if age < 16:
    ticket_price = 7.5
    return ticket_price

  elif age < 65:
    ticket_price = 10.5
    return ticket_price

  else:
    ticket_price = 6.5
    return ticket_price


number_regex = "^[1-9]"

# list for valid yes / no response
yes_no = [
  ["yes", "y"],
  ["no", "n"]
]

# list of valid responses for pay method
pay_method = [
  ["cash", "ca"],
  ["credit", "cr"]
]
# initialise loop so that it runs at least once
name = ""
ticket_count = 0
ticket_sales = 0
max_tickets = 5

# Initialise lists (to make data-frame in due course)
all_names = []
all_tickets = []

# Data frame dictionary
movie_data_dict = {
  'Name': all_names,
  'Ticket': all_tickets
}
while name != "xxx" and ticket_count < max_tickets:
  # check numbers of ticket limit has not been exceeded
  check_tickets(ticket_count, max_tickets)

  # Get details for each ticket_count
  
  # get name (Can't be blank)
  name = name_check("Name: ")
  
# End the loop if exit code is entered
  if name == "xxx":
    break
  
  # get ticket price based on age
  ticket_price = get_ticket_price()

  # if age is invalid, restart loop (and get name again)
  if ticket_price == "invalid ticket price":
    continue

  
  ticket_count += 1
  ticket_sales += ticket_price

  # add name and ticket price to lists
  all_names.append(name)
  all_tickets.append(ticket_price)

  # Get snacks

  # Get payment method (ie: work out if surcharge)

# End of tickets / snacks / payment loop

# print details...
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

# Calculate ticket profit..max_tickets
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))
# Tell user if they have unsold tickets...
if ticket_count == max_tickets:
  print("You have sold all available tickets!")
else:
  print("You have sold {} tickets. \nThere are {} places still available".format(ticket_count, max_tickets - ticket_count))

 