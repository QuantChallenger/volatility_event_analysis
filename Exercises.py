# list
def filter_names(fellowship, accepted):
  filtered_list = []
  for name in fellowship:
        if any(name.startswith(x) for x in accepted):
            filtered_list.append(name)
  return filtered_list

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli', '']
accepted = 'mnopqrstuvwxyz'

result = filter_names(fellowship, accepted)
print(result)
