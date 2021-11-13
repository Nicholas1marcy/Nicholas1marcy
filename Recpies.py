import queue 
cookbook={}
recipe={}
createRecipe{cookbook}
running = True
while running==True:
       print ("Input what you need")
       print ("N to add")
       print ("L for list")
       print ("R to read")
       print ("Q to quit")
       userinput=input () 
       if userinput ==  "Q" : running = False
       if userinput ==  "N" : cookbook = createRecipe()
       if userinput ==  "L" : print (recipe["name"])
       if userinput ==  "R" : print (cookbook)
       if userinput ==  "N" : cookbook = alreadyin()

def createRecipe(cookbook):
  print("Adding new recipe")
  name = input("give recipename: ")
  recipe={}
  recipe["name"] = name
  userinput = input("give recipe ingredients: ")
  recipe["ingredients"]= userinput
  userinput = input("give recipe instructions: ")
  recipe["instructions"]= userinput
  cookbook[name] = recipe

def alreadyin():
  if "name" in cookbook:
    cookbook["name"] += 1
  else:
    cookbook["name"] = 1
    print("Error, this is already in the cookbook")





      







