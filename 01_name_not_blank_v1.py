# functions go here
def name_check(question):
  while True:
    response = input(question)
    if response.isnumeric != False: 
      return response
    else:
      print("Sorry - this can't be blank, please enter your name")
      print()

user = name_check("Name: ")
  