# list
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli', '']
accepted = 'mnopqrstuvwxyz'
fellowship2 = []
def filter_names(*arg):
  
    for name in fellowship:
        if any(name.startswith(x) for x in accepted):
            fellowship2.append(name)
    return fellowship2



result = filter_names(fellowship, accepted)
print(result)
