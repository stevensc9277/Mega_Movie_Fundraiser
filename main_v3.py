import re
import pandas

# Function goes here


# This function checks to make sure that user inputs a valid string
def name_check(question):
    while True:
        response = input(question)
        if response != "":
            return response
        else:
            print("Sorry - this can't be blank, please enter your name")
            print()


def string_check(choice, options):
    for var_list in options:

        # if the snack is in one of the lists, return the full name
        if choice in var_list:

            # Get full snack and put it in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if snack is not ok - ask question again.
    if is_valid == "yes":
        return chosen

    else:
        print("Please enter a valid option")
        print()
        return "invalid choice"


# Gets list of snacks
def get_snack():
    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # Each item in valid snacks is a list with valid options for each snack < full name, letter code (a - e), and possibly abbreviations, etc

    valid_snacks = [["popcorn", "p", "corn", "a"],
                    ["M&Ms", "m&m's", "mms", "m", "b"],
                    ["pita chips", "chips", "pc", "pita", "c"],
                    ["water", "w", "d"],
                    ["orange juice", "juice", "oj", "orange", "e"]]
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":
        snack_row = []

        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        # if item has a number, separate it into two (number / snack)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        # remove white space around snack
        desired_snack = desired_snack.strip()

        # check if snack is valid
        
        snack_choice = string_check(desired_snack, valid_snacks)

        # check snack amount is valid (less than 5)
        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "invalid choice"

        # add snack and amount to list...
        snack_row.append(amount)
        snack_row.append(snack_choice)

        # check that snack is not the exit code before adding it
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)


# Checks number of tickets left and warns user if maximum is being approached
def check_tickets(tickets_sold, ticket_limit):
    # tells user how many seats are left
    if tickets_sold < ticket_limit - 1:
        print("You have {} seats left".format(ticket_limit - tickets_sold))

    # warns user that only one seat is left:
    else:
        print("*** There is ONE seat left!! ***")

    return ""


# This function checks to make sure that user inputs an integer between 12 and 130
def num_check(question):
    error = "PLease enter an integer that is more than 0"
    while True:
        try:
            response = int(input(question))
            # repeat question if input is too low
            if response <= 0:
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


# list for valid yes / no responses
yes_no = [["yes", "y"], ["no", "n"]]

# list for valid pay method
pay_method = [["cash", "ca"], ["credit", "cr"]]

# initialise loop so that it runs at least once
name = ""
ticket_count = 0
ticket_sales = 0
max_tickets = 5

# initialise lists (to make data frame in due course)
all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# store surcharge surcharge_multiplier
surcharge_multi_list = []

# Data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Tickets': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_multi_list
}

# cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
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

    # End of tickets / snacks / payment loop

    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snacks? ").lower()
        check_snack = string_check(want_snack, yes_no)

    # if they say yes, ask what snacks they want (and add to our snack list)
    if check_snack == "Yes":

        snack_order = get_snack()
        print(snack_order)

    else:
        snack_order = []

    # Assume no snacks have been bought...
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

        # Get payment method (ie: work out if surcharge is needed)

        # Ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash / credit)? ").lower()
        # how_pay = "Please choose a payment method (cash / credit)? "
        check_pay = string_check(how_pay, pay_method)

    if check_pay == "Credit":
        surcharge_multiplier = 0.05

    else:
        surcharge_multiplier = 0

    surcharge_multi_list.append(surcharge_multiplier
    )
    # print details...
    # Create dataframe and set index to name column
    movie_frame = pandas.DataFrame(movie_data_dict)
    movie_frame = movie_frame.set_index('Name')

    # Create column called 'Sub Total'
    # Fill it with price for snacks and ticket
movie_frame["Sub Total"] = \
  movie_frame['Tickets']  +\
  movie_frame['Popcorn']*price_dict['Popcorn'] +\
  movie_frame['Water']*price_dict['Water'] +\
  movie_frame['Pita Chips']*price_dict['Pita Chips'] +\
  movie_frame['M&Ms']*price_dict['M&Ms'] +\
  movie_frame['Orange Juice']*price_dict['Orange Juice']

movie_frame["Surcharge"] = \
  movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
  movie_frame['Surcharge']
# Shorten column names
movie_frame = movie_frame.rename(columns={
    'Orange Juice': 'OJ',
    'Pita Chips': 'Chips',
    'Surcharge_Multiplier': 'SM'
})

# Set up columns to be printed
pandas.set_option('display.max_columns', None)

# Display numbers to 2dp
pandas.set_option('precision', 2)

print_all = input("Print all columns? (y) for yes: ")
if print_all == "y":
  print(movie_frame)

else:
  print(movie_frame[['Ticket', 'Subtotal', 'Surcharge', 'Total']])

print()

# Calculate ticket profit...
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))
# Tell user if they have unsold tickets...
if ticket_count == max_tickets:
    print("You have sold all available tickets!")
else:
    print("You have sold {} tickets. \nThere are {} places still available".
          format(ticket_count, max_tickets - ticket_count))
