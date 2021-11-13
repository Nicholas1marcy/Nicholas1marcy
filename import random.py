import random
import time
def main ():

  
  totalcards = 52
playerone=0
playertwo=0
score1=0
score2=0


deck = []

suit = ["club","spade","diamond","heart"]
numbers = ["ace","two" ,"3","4","5" ,"6" ,"7","8","9","10","jack","queen","king"]

for Suit in suit:
  for Number in numbers:
   deck.append(Suit+" "+Number) 
    




while(totalcards>0):
 print("dealing cards")
 print()
 Output = dealcards(deck, playerone, playertwo)
 deck = Output[0] 
 player1 = Output[1]
 player2 = Output[2]
 print()
 time.sleep(5)
 scoreup = score(player1, player2, score1, score2)
 score1 = scoreup[0]
 score2 = scoreup[1]
 totalcards -= 2

 print("The game of war has ended!")
    if one > two:
        winner = 'Player One Wins'
    elif one < two:
        winner = 'Player Two Wins'
    else:
        winner = 'It was a tie'
    print(f"The final score is: {one} to {two}, {winner}")

def dealcards(deck, playerone, playertwo):

    player1= ""
    player2 = ""

   player1=random.choice(deck)
   print(print("Player one: ",playerone, player1)
    deck.remove(playerone))
    time.sleep(2)
    playertwo = random.choice(deck)
    print("player two:",playertwo,player2)
    deck.remove(player2)
    return deck,playerone,playertwo

 

def score(playerone, player2, score1, score2)
  one=0
  two=0
 playerone = playerone.split()
 playertwo = playertwo.split()

 try:
  int(playerone[0])
  one=int(playerone)+1
  except:
      if playerone[0] == "ace":
        one=1
        elif playerone[0] == "jack":
        one=2
        elif playerone[0] == "queen":
        one=3
        elif playerone[0] == "king":
        one=4

        try:
  int(playertwo[0])
  one=int(playertwo)+1
  except:
      if playertwo[0] == "ace":
        two=1
        elif playertwo[0] == "jack":
        two=2
        elif playertwo[0] == "queen":
        two=3
        elif playertwo[0] == "king":
        two=4


    if one < two:
        print("Player 2 wins")
        pTwoScore += 1

    elif one > two :
        print("Player 1 wins")
        pOneScore += 1

    elif pOne == pTwo:
        print("tie")

    return pOneScore, pTwoScore


main()