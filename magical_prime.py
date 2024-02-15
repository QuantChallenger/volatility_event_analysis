# Write a function that will return the index of the first magical prime from an list.
# A magical prime is something we consider that the addition of two inputs from the array equals a magical prime present in the array.
# For instance, [1, 2, 15, 17, 38, 42], 2 + 15 = 17, so 17 would be our magical prime.
# In this case the function should return 3 because 17 is at the 3rd position.
# In the case you can't find a magical prime, return -1.

# [1, 2, 4, 9, 16, 20, 23], 4 + 16 = 20, index is 5
# [2, 4, 5] , index -1, no magical prime can be found

"""
loop chiffre index 1
loop sur la liste ou je fais la sum du premier de la chiffre avec le deuxieme
if sum = chiffre de la liste then magical prime
next
elif loop sur la liste ou je fais la sum du deuxieme de la chiffre avec le troisieme
else
-1

#trouver edge cases (peut)

pas d'ordre inverse, pas de self addition, dernier chiffre inutile, 
pas d'ordre reverse, le chiffre le plus élévé n'est jamais pris en compte dans la somme, 1er
count le nombre de chiffres dans la liste, minimum '



""" 

#funct that finds magical prime

def find_magical_prime_index(list_magical_prime):
    
    
    
    return -1

list =[1, 2, 4, 9, 16, 20, 23]

list.del(0)


# Tests cases
result = find_magical_prime_index([1, 2, 4, 9, 16, 20, 23])
#  5
print(result)

# [1, 2, 4, 9, 16, 20, 23], 4 + 16 = 20, index is 5
# [2, 4, 5] , index -1, no magical prime can be found

result = find_magical_prime_index([2, 4, 5])
#  -1
print(result)

result = find_magical_prime_index([1, 2, 15, 17, 38, 42])
# 3
print(result)