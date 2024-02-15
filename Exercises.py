# list
def filter_names(fellowship, accepted):
  filtered_list = []
    for name in fellowship:
        if any(name.startswith(x) for x in accepted):
            fellowship2.append(name)
    return fellowship2

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli', '']
accepted = 'mnopqrstuvwxyz'

result = filter_names(fellowship, accepted)
print(result)
