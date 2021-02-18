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
ticket_count = 0
profit = 0
ticket_sales = 0
max_tickets = 5
while name != "xxx" and ticket_count < max_tickets:
  # tells user how many seats are left
  if ticket_count < max_tickets - 1:
    print("You have {} seats left".format(max_tickets - ticket_count))
  
  else:
    print("*** There is ONE seat left!! ***")
  # get details 
  name = name_check("Name: ")
  
# End the loop if exit code is entered
  if name == "xxx":
    break
  
  # Check that age is valid...
  age = num_check("How old are you? ")
  if age < 12:
    print("Sorry, you are too young for this movie")
    continue
  elif age > 130:
    print("That is very old - it looks like a mistake")
    continue


  if age < 16:
    ticket_price = 7.5

  elif  age < 65:
    ticket_price = 10.5

  else:
    ticket_price = 6.5
  print()

  
  ticket_count += 1
  ticket_sales += ticket_price

ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))
# Tell user if they have unsold tickets...
if ticket_count == max_tickets:
  print("You have sold all available tickets!")
else:
  print("You have sold {} tickets. \nThere are {} places still available".format(ticket_count, max_tickets - ticket_count))

 