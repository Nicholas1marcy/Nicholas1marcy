import random
deck = []
totalcards= 52


suit = ["club","spade","diamond","heart"]
numbers = ["ace","two" ,"3","4","5" ,"6" ,"7","8","9","10","jack","queen","king"]

for Suit in suit:
  for Number in numbers:
   deck.append(Suit+" "+Number) 
    
player1=[]
player2=[]

card=random(deck) 

deckcut=len(deck)
decksize=deckcut//2
player1=card[:decksize]
print (player1)



  

    