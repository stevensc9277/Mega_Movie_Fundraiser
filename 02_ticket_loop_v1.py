# start of loop

# initialise loop so that it runs at least once
name = ""
count = 1
max_tickets = 5
while name != "xxx" and count <= max_tickets:
  # get details
  name = input("Name: ")
  count += 1
print("You have sold all available tickets")