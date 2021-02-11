# functions go here
def name_check(question, error_message):
  while True:
    response = input(question)
    if response != "":
      return response
    else:
      print(error_message)
      print()

user = name_check("Name: ", "Sorry - this can't be blank, please enter your name")
  