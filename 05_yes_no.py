def yes_no(question):
  error = "Please answer yes / no"

  while True:

    # ask question and put response in lowercase
    response = input(question).lower
    if response == "yes" or response == "y":
      return "yes"

    elif response == "no" or response == "no":
      return "no"

    else:
      print(error) 

for item in range(0, 6):
  want_snack = yes_no("Do you want snacks? ")
  print("Answer OK, you said:", want_snack)