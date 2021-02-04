# Number checker used to check user's age
def num_check(question, low, high):
  error = "Please enter a valid number"
  while True:
    try:
      response = int(input("Enter a number. "))
      if response < low:
        print(error)
        print()
      elif response > high:
        print(error)
        print
      else:
        print()
        return response
    except ValueError:
      print(error)
      print()

tickets_av = 150
for i in range(0, tickets_av):
  age_verify = num_check("How old are you? ", 12, 70)
  tickets_av -= 1