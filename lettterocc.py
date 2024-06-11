# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 21:37:08 2024

@author: reyna
"""

"""
je te donne une string "Bonjour, comment allez vous mon AMIE???"
et un chiffre: 3

retourne moi une liste de type class LetterOccurence, où tu trouves 3 ou + la lettre même lettre qui se répète
La case ne devrait pas être prise en compte pour la recherche, les symboles ne comptent pas

Donc ici, je m'attends à recevoir 

o 5 
n 3
m 4
e 3

retourner une liste d'instance de classe'

"""

"""
Edge Cases

Toute lettre moins de 3 n'est pas compté
Les espaces ne peuvent être comptés


"""
"""
Pseudo code

string list :("Bonjour,...")
def letter_occurence(letter):
dict= {}
boucle 1: pour letter dans string list:
        keys = dict.keys()

    boucle 2 : pour letter dans string list:
        dict[letter] += 1
         if dict[letter]<3
         pop.keys[letter]
         
         return letter_occurence.count
    
"""

def letter_occurence(letter):
    string_list = "Bonjour, comment allez vous mon AMIE???" 
    dictio = {}
    for letter in string_list:
        
        dictio[letter] += 1
        
       
    
    return letter_occurence(letter)
    print("no")
        
        
        
        
        
        
        
        
        


result= letter_occurence(["e"])
# 3
print(result)


result= letter_occurence(["m"])
# 4
print(result)

result= letter_occurence(["n"])
# 3
print(result)

result= letter_occurence(["o"])
# 5
print(result)




