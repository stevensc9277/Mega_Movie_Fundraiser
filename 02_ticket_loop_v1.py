# start of loop

# initialise loop so that it runs at least once
name = ""
count = 1
max_tickets = 5
tickets_left = 5
while name != "xxx" and count <= max_tickets:
  # get details
  print("You have {} seats left".format(tickets_left))
  name = input("Name: ")
  count += 1
  tickets_left -= 1

  print()
print("You have sold all available tickets")