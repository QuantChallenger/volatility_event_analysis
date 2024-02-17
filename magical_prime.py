# Write a function that will return the index of the first magical prime from a list.
# A magical prime is something we consider that the addition of two inputs from the array equals a
# magical prime present in the array.
# For instance, [1, 2, 15, 17, 38, 42], 2 + 15 = 17, so 17 would be our magical prime.
# In this case the function should return 3 because 17 is at the 3rd position.
# In the case you can't find a magical prime, return -1.

# [1, 2, 4, 9, 16, 20, 23], 4 + 16 = 20, index is 5
# [2, 4, 5] , index -1, no magical prime can be found

"""

# trouver edge cases 

pas d'ordre inverse, pas de self addition, dernier chiffre inutile,
pas d'ordre reverse,
le chiffre le plus élévé n'est jamais pris en compte dans la somme,
1er count le nombre de chiffres dans la liste,
minimum 3 chiffres dans la liste


#Pseudo code


def func


For loop internal
list_test
reduce(apply add() => add the 2 firts items dans une liste
si sum = any(element in list)
print index
elif
for


x=list_test[0]
y=2

sum =1+2
    si sum = any(element in list), return index.sum


x=1
y=4
sum=1+4
 si sum = any(element in list), return index.sum

 ...
 x=2
 y=4
 sum=2+4

test_list = [1, 2, 4, 9, 16, 20, 23]

"""


# funct that finds magical prime


def find_magical_prime_index(list_magical_prime):
    index = 0

    for x in list_magical_prime:

        index = index+1

        copy_list_magical_prime = list_magical_prime[index:len(list_magical_prime)-1]

        for y in copy_list_magical_prime:

            #print(f'test list {x} {y}')

            magical_sum = x + y

            if magical_sum in list_magical_prime:
                 
                 return list_magical_prime.index(magical_sum)


    return -1






# Tests cases
result = find_magical_prime_index([1, 2, 4, 9, 16, 20, 23])
#  5
print(result)


result = find_magical_prime_index([2, 4, 5])
#  -1
print(result)

result = find_magical_prime_index([1, 2, 15, 17, 38, 42])
# 3
print(result)

