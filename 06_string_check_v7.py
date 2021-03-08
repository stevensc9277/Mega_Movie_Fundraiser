import re
# Function goes here

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

  valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "juice", "oj", "orange", "e"]
  ]
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
    desired_snack = desired_snack.strip

    # check if snack is valid
    snack_choice = string_check(desired_snack, valid_snacks)

yes_no = [
  ["yes", "y"],
  ["no", "n"]
]

check_snack = "invalid choice"
while check_snack == "invalid choice":
  want_snack = input("Do you want to order snacks? ").lower()
  check_snack = string_check(want_snack, yes_no)

# if they say yes, ask what snacks they want (and add to our snack list)
if check_snack == "Yes":
  
  get_order = get_snack()

else:
  get_order = []

    

# show snack orders
print()
if len(get_order) ==  0:
  print("Snacks ordered: None")

else:
  print("Snacks ordered: ")
  
  ''' for item in snack_order:
  print(item)'''

  print(get_order)
# loop three times to make testing quicker
