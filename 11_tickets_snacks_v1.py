import pandas

# initialise snack lists...

all_names = ['Rangi', 'Manaia', 'Talia', 'Arihi', 'Fetu']
all_tickets = [7.5, 10.5, 10.5, 10.5, 6.5]

popcorn = []
mms = []
pita_chips = [] 
water = [] 
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]
 # Data frame dictionary
movie_data_dict = {
  'Name': all_names,
  'Tickets': all_tickets,
  'Popcorn': popcorn,
  'Water': water,
  'Pita Chips': pita_chips,
  'M&Ms': mms,
  'Orange Juice': orange_juice
}

# cost of each snack
price_dict = {
  'Popcorn': 2.5, 
  'Water': 2, 
  'Pita Chips': 4.5,
  'M&Ms': 3,
  'Orange Juice': 3.25
}
test_data = [
  [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
  [[]],
  [[1, 'Water']],
  [[1, 'Popcorn'], [1, 'Orange Juice']],
  [[1, 'M&Ms'], [1, 'Pita Chips'], [3, 'Orange Juice']]
]

count = 0
for client_order in test_data:

  # Assume no snacks have been bought...
  for item in snack_lists:
    item.append(0)

  #print (snack_lists)

  # get order (hard coded for easy testing)
  snack_order = test_data[count]
  count += 1
  
  for item in snack_order:
    if len(item) > 0:
      to_find = (item[1])
      amount = (item[0])
      add_list = movie_data_dict[to_find]
      add_list[-1] = amount

print()
print("Popcorn: ", snack_lists[0])
print("M&Ms: ", snack_lists[1])
print("Pita Chips: ", snack_lists[2])
print("Water: ", snack_lists[3])
print("Orange Juice: ", snack_lists[4])
print()

movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')
print(movie_frame)
