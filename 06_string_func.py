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
    return "invalid choice"

# valid snacks holds list of all snacks
# Each item in valid snacks is a list with valid options for each snack < full name, letter code (a - e), and possibly abbreviations, etc

valid_snacks = [
  ["popcorn", "p", "corn", "a"],
  ["M&M's", "m&m's", "mms", "m", "b"],
  ["pita chips", "chips", "pc", "pita", "c"],
  ["water", "w", "d"]
]

yes_no = [
  ["yes", "y"],
  ["no", "n"]
]

check_snack = "invalid choice"
while check_snack == "invalid choice":
  want_snack = input("Do you want to order snacks? ").lower()
  check_snack = string_check(want_snack, yes_no)

# loop three times to make testing quicker
for item in range(0, 6):
  # ask user for desired snack and put it in lowercase
  desired_snack = input("Snack: ").lower()

  # check if snack is valid
  snack_choice = string_check(desired_snack, valid_snacks)
  print("Snack Choice: ", snack_choice)