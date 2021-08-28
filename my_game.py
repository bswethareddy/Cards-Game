import itertools, random
con = "Y"
while con=="Y":
    deck = list(itertools.product(['S', 'H', 'D', 'C'],['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']))
    random.shuffle(deck)
    print(deck)

    # Define a 2D list with all entries as 0

    player = [0 for j in range(13)]
    bot1 = [0 for j in range(13)]
    bot2 = [0 for j in range(13)]
    bot3 = [0 for j in range(13)]

    # To distrubute all the cards among 4 players
    def distribute():
        for i in range(13):
            player[i] = deck[i][0] + deck[i][1]
            deck.remove(deck[i])
        for i in range(13):
            bot1[i] = deck[i][0] + deck[i][1]
            deck.remove(deck[i])
        for i in range(13):
            bot2[i] = deck[i][0] + deck[i][1]
            deck.remove(deck[i])
        for i in range(13):
            bot3[i] = deck[i][0] + deck[i][1]
        
        print("Player got -> ", player)
        print("Bot 1 got -> ",bot1)
        print("Bot 2 got -> ",bot2)
        print("Bot 3 got -> ",bot3)

    # To count calls of bots
    def calls(p1): 
        count = 0
        for i in range(len(p1)):
            if p1[i][1] == 'A' or p1[i][1] == 'K' or p1[i][1] == 'Q' or p1[i][1] == 'J':
                count+=1
        return count

    # Start the game
    def solve():
        print()
    distribute()
    bot1_call = calls(bot1)
    bot2_call = calls(bot2)
    bot3_call = calls(bot3)
    player_call  = input(f"Call of Players: Bot1-> {str(bot1_call)} Bot2-> {str(bot2_call)} Bot3-> {str(bot3_call)} Player-> ")
    solve()




    con = input("Continue(Y/N): ")