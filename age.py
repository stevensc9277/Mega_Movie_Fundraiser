# Number checker used to check user's age
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

# Ask user for their age
age_verify = num_check("How old are you? ", 12, 130)
