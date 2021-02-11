# Number checker used to check user's age
def num_check(question, low, high, error):
  while True:
    try:
      response = int(input(question))
      if response < low:
        print("Please enter an integer that is more than (or equal to) {}".format(low))
        print()
      elif response > high:
        print("Please enter an integer that is less than (or equal to) {}".format(high))
        print()
      else:
        print()
        return response
    except ValueError:
      print(error)
      print()

for i in range(0, 3):
  age_verify = num_check("How old are you? ", 12, 130, "Please enter a valid age between 12 and 130")
