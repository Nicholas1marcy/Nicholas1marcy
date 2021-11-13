import random, time
   
def main():
   
    totalCards = 52
    player1 = 0
    player2 = 0
    score1 = 0
    score2 = 0
    deck=[]
 
   
    number = ["ace","king","queen","jack","2","3","4","5","6","7","8","9","10"]
    suit = ["of spades","of hearts","of clubs","of diamonds"]
   
    for numbers in number:
        for suitType in suit:
            deck.append(numbers + ' ' + suitType)
         
    
   
    while (totalCards > 0):
           
       
        print("dealing cards") 
        print()
        carddeal = dealCard(deck, player1, player2)
        deck = carddeal[0]
        player1= carddeal[1]
        player2 = carddeal[2]
        print()
        time.sleep(5)
        scoreup = score(player1, player2, score1, score2)
        score1 = scoreup[0]
        score2 = scoreup[1]
              
        totalCards -= 2
           
        print(totalCards, "cards remain in the deck.")
   
        print("one's score: ", score1)
        print("two's score: ", score2)
   
    print("war has ended!")
    if score1 >score2:
        winner = 'eels wins'
    elif score1 < score2:
        winner = 'escalators wins'
    else:
        winner = 'your shoes are looking cool'
    print(f"The final score is: {score1} to {score2}, {winner}")
   
def dealCard(deck, player1, player2):
    
    player1card = ""
    player2card = ""
       
    player1 = random.choice(deck)
   
    print("Player one: ",player1, player1card)
    deck.remove(player1)
 
    time.sleep(5)
    player2 = random.choice(deck)
       
    print("Player two: ",player2, player2card)
    deck.remove(player2)
   
    return deck, player1, player2
   
def score(player1, player2, score1, score2):
    two = 0
    one = 0
    player1= player1.split()
    player2 = player2.split()
    try:
        int(player1[0])
        pOne = int(player2) + 3
    except:
        if player1[0] == "ace":
            one = 1
        elif player1[0] == "king":
            one = 2
        elif player1[0] == "queen":
            one = 3
        elif player1[0] == "jack":
            one =4
          
    try:
        int(player2[0])
        one = int(player1) + 3
    except:
        if player2[0] == "ace":
            two = 1
        elif player2[0] == "king":
            two = 2
        elif player2[0] == "queen":
            two = 3
        elif player2[0] == "jack":
            two = 4
   
    
    if one > two:
        score1 += 1
        print("escalators")
    elif one < two:
        score2 += 1
        print("Eels")
    elif one == two:
        print("tie your shoes")
    return score1, score2
   
main()