def filter_names(list_of_names, letter_list):
  filtered_list = []
  for name in list_of_names:
        if any(name.startswith(x) for x in letter_list):
            filtered_list.append(name)
  return filtered_list

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli', '']
accepted = 'mnopqrstuvwxyz'

result = filter_names(fellowship, accepted)
print(result)
