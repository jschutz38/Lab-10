#authors names are Julia Schutz, Julia Bub, and Christina Shadid
red = {"flour": 2.5, "Sugar": 1.5, "Baking Soda": 1, "Salt": 1, "Cocoa Powder": 1, "Oil": 1.5, "Milk": 1, "Eggs": 2, "Vanilla": 1}

lemon = {"flour": 1.5, "Baking Powder": 1.5, "Zest": 1, "Salt": .5, "Butter": .5, "Sugar": 1, "Eggs": 2, "Vanilla": 1, "Lemon Juice": 2, "Milk": .5}

def check_recipes(recipe1, recipe2):
    similiar = []
    for ingredient in recipe1:
        if ingredient in recipe2:
            similiar.append(ingredient)
    return similiar
print(check_recipes(red,  lemon))    
