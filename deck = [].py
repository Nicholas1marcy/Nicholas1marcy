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

deck1=random.choice(deck) 


player1 = deck1
player2 = deck1

deckcut = len(deck)
decksize = deckcut//2
hand1 = deck1 [:decksize]
hand2 = deck1 [decksize:]





  
print (hand1)
print  (hand2)





  

    