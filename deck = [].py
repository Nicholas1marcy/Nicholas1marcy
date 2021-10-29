import random

  
totalcards = 52
playerone=0
player2=0
score1=0
score2=0


deck = []

suit = ["club","spade","diamond","heart"]
numbers = ["ace","two" ,"3","4","5" ,"6" ,"7","8","9","10","jack","queen","king"]

for Suit in suit:
  for Number in numbers:
   deck.append(Suit+" "+Number) 
    
player1=[]
player2=[]

deck1=random.choice(deck) 

while(totalcards>0):
  print("dealing cards")
  print()
   


  

    