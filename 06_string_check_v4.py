def confirm():
  response = input("Do oyu want to order snacks? ").lower()
  if response not in yes_no:
    return "Please enter a valid response"
  else:
    return response



yes_no = [
  ["yes", "y"],
  ["no", "n"]
]
