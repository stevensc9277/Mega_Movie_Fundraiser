# string checking function takes in question and list of valid responses
def string_checker(question, to_check):
  error = "Sorry that is not a valid response"

  while True:

    # ask question and put response in lowercase
    response = input(question).lower()
    if response in to_check:
      return response

    else:
      for item in to_check:
        # checks if response is the first letter of an item in the list
        if response == item[0]:
          # return the entire response rather than just the first letter
          return item
      print(error) 

for item in range(0, 6):
  want_snack = string_checker("Do you want snacks? ", ["yes", "no"])
  print("Answer OK, you said:", want_snack)
  print()