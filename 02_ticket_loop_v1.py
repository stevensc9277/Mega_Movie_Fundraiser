# start of loop

# initialise loop so that it runs at least once
name = ""
count = 0
max_tickets = 5
while name != "xxx" and count <= max_tickets:
  # get details
  print("You have {} seats left".format(max_tickets - count))
  name = input("Name: ")
  count += 1
 
  print()
if count == max_tickets:
  print("You have sold all available tickets")
else:
  print("You have {} tickets left".format(max_tickets - count + 1))