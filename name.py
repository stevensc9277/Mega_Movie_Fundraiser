def name_check(question):
  while True:
    response = input(question)
    if response.isdigit():
      print("Please enter a name")
      print()
    elif response != "":
      return response
    else:
      print("Please enter a valid name")
      print()

user = name_check("Enter name here: ")
  