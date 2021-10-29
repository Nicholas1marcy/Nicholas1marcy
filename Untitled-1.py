import random
agedcheese=[]
cheeses = ["chedder","gouda","parmasean","american","mozzerella"]
age = ["no year","1 year","2 year","3 year","4 year"]
for x in cheeses:
    for y in age:
     agedcheese.append(x+" "+y)
     
randomcheese=random.choice(agedcheese)

print (randomcheese)
    