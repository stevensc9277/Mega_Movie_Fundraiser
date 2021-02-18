# functions go here
def name_check(question):
  while True:
    response = input(question)
    if response.isnumeric() != False: 
      return response
    else:
      print("Sorry - this can't be blank and we also do not accept numbers with your name. \nPlease enter your name")
      print()

user = name_check("Name: ")
  