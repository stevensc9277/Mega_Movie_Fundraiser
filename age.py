# Number checker used to check user's age
def num_check(question, low, high):
  error = "Please enter a valid number"
  while True:
    try:
      response = int(input(question))
      if response < low:
        print(error)
        print()
      elif response > high:
        print(error)
        print()
      else:
        print()
        return response
    except ValueError:
      print(error)
      print()

for i in range(0, 3):
  age_verify = num_check("How old are you? ", 12, 70)
