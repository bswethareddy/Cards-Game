# import modules
import itertools, random
def input_user():
    n=list(input("Enter the input in the form of H,A OR S,K from the set given to you: ").split(','))
    return n


# make a deck of cards
deck = list(itertools.product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
                            ['S', 'H', 'D', 'C']))
print(len(deck))
# shuffle the cards
random.shuffle(deck)
# Define a 2D list with all entries as 0

player = [[0 for i in range(2)] for j in range(13)]
bot1 = [[0 for i in range(2)] for j in range(13)]
bot2 = [[0 for i in range(2)] for j in range(13)]
bot3 = [[0 for i in range(2)] for j in range(13)]

def sort_fxn(li):
    l=[]
    for i in range(len(li)):
        if li[i][0]=='A':
            l.append(li[i])
    for i in range(len(li)):
        if li[i][0]=='K':
            l.append(li[i])
    for i in range(len(li)):
        if li[i][0]=='Q':
            l.append(li[i])
    for i in range(len(li)):
        if li[i][0]=='J':
            l.append(li[i])
    for i in range(len(li)):
        if li[i][0]=='10':
            l.append(li[i])
    for i in range(len(li)):
        if li[i][0]=='9':
            l.append(li[i])
    for i in range(len(li)):
        if li[i][0]=='8':
            l.append(li[i])
    for i in range(len(li)):
        if li[i][0]=='7':
            l.append(li[i])
    for i in range(len(li)):
        if li[i][0]=='6':
            l.append(li[i])
    for i in range(len(li)):
        if li[i][0]=='5':
            l.append(li[i])
    for i in range(len(li)):
        if li[i][0]=='4':
            l.append(li[i])
    for i in range(len(li)):
        if li[i][0]=='3':
            l.append(li[i])
    for i in range(len(li)):
        if li[i][0]=='2':
            l.append(li[i])
    return l

# draw cards, a total of 52 cards divided among 4 players 
print("\nPlayer  got: ")
for i in range(13):
    player[i][0] = deck[i][0]
    player[i][1] = deck[i][1]
    deck.remove(deck[i])
player=sort_fxn(player)
print(player)

print("\nBot 1 got: ") 
for j in range(13):
    bot1[j][0] = deck[j][0]
    bot1[j][1] = deck[j][1]
    deck.remove(deck[j])
bot1=sort_fxn(bot1)
print(bot1)
    
print("\nbot2 got: ")
for k in range(13):
    bot2[k][0] = deck[k][0]
    bot2[k][1] = deck[k][1]
    deck.remove(deck[k])
bot2=sort_fxn(bot2)
print(bot2)

print("\nBot3 got: ")
for l in range(13):
    bot3[l][0] = deck[l][0]
    bot3[l][1] = deck[l][1]
bot3=sort_fxn(bot3)
print(bot3)



def calls(p1): 
    count = 0
    for i in range(len(p1)):
        if p1[i][0] == 'A' or p1[i][0] == 'K' or p1[i][0] == 'Q' or p1[i][0] == 'J':
            count+=1
    return count


bot1_call = calls(bot1)
bot2_call = calls(bot2)
bot3_call = calls(bot3)
player_call = calls(player)
print("Call of Players: Bot1->"+str(bot1_call)+ " Bot2->"+str(bot2_call)+ " Bot3->"+str(bot3_call)+ " Player->"+str(player_call))
print("Order of arrangement: Bot1, Bot2, Player, Bot3, Bot1, ...... ")

start = input("Who is gonna start the game ( bot1 / bot2 / bot3 / player )? ")

def win_fxn(l):
    
    if(l[0]==player):
       
        x=input_user()
        l[0].remove(x)
        print(l[0])
        a=x[1]
        #l[0]will be remaining option for player
        #x1 be variable for Bot1
        #x2 for bot2
        #x3 for bot3
        
        for i in range(len(bot3)):
            if bot3[i][1]==a:
                x3=bot3[i]
                break
            else:
                x3=bot3[-1]
        bot3.remove(x3)

        for i in range(len(bot1)):
            if bot1[i][1]==a:
                x1=bot1[i]
                break
            else:
                x1=bot1[-1]
        bot1.remove(x1)

        for i in range(len(bot2)):
            if bot2[i][1]==a:
                x2=bot2[i]
                break
            else:
                x2=bot2[-1]
        bot2.remove(x2)
 

        print("x2 ",x2)
        print("x3 ",x3)
        print("x1 ",x1)

    elif(l[1]==player):
        
        x2=bot2[0]
        bot2.remove(x2)
        a=x2[1]
        x=input_user()
        l[1].remove(x)
        print(l[1])

        for i in range(len(bot3)):
            if bot3[i][1]==a:
                x3=bot3[i]
                break
            else:
                x3=bot3[-1]
        bot3.remove(x3)

        for i in range(len(bot1)):
            if bot1[i][1]==a:
                x1=bot1[i]
                break
            else:
                x1=bot1[-1]
        bot1.remove(x1)

        print("x2 ",x2)
        print("x3 ",x3)
        print("x1 ",x1)


    elif(l[2]==player):
        
        x1=bot1[0]
        bot1.remove(x1)
        a=x1[1]
        
        x=input_user()
        
        l[2].remove(x)
        print(l[2])
        
        for i in range(len(bot3)):
            if bot3[i][1]==a:
                x3=bot3[i]
                break
            else:
                x3=bot3[-1]
        bot3.remove(x3)

        for i in range(len(bot2)):
            if bot2[i][1]==a:
                x2=bot2[i]
                break
            else:
                x2=bot2[-1]
        bot2.remove(x2)


        print("x2 ",x2)
        print("x3 ",x3)
        print("x1 ",x1)
        


    elif(l[3]==player):
        
        x3=bot3[0]
        
        bot3.remove(x3)

        x=input_user()
    
        l[3].remove(x)
        print(l[3])
        
        a=x3[1]
        
        for i in range(len(bot2)):
            if bot2[i][1]==a:
                x2=bot2[i]
                break
            else :
                x2=bot2[-1]
        bot2.remove(x2)


        for i in range(len(bot1)):
            if bot1[i][1]==a:
                x1=bot1[i]
                break
            else :
                x1=bot1[-1]
        bot1.remove(x1)


        print("x2 ",x2)
        print("x3 ",x3)
        print("x1 ",x1)

    final=[x1,x2,x3,x]

    f=sort_fxn(final)
    if f[0]==x1:
        print("Bot1 wins")
        return ("Bot1")
    elif f[0]==x2:
        print("Bot2 wins")
        return("Bot2")
        
    elif f[0]==x3:
        print("Bot3 wins")
        return("Bot3")
        
    else:
        print("Player wins")
        return('Player')
        


     
bot1_win=0
bot2_win=0
bot3_win=0
p_win=0
if start == 'bot1':
    order = [bot1, bot2,player, bot3]
    for i in range(0,13):
        x=win_fxn(order)
        if x=='Bot1':
            bot1_win+=1
        elif x=='Bot2':
            bot2_win+=1
        elif x=='Bot3':
            bot3_win+=1
        else:
            p_win+=1
    win_list=[bot1_win,bot2_win,bot3_win,p_win]
    win_list.sort()
    if win_list[-1]==bot1_win:
        print("Bot1 won")
    elif win_list[-1]==bot2_win:
        print("Bot2 won")
    elif win_list[-1]==bot3_win:
        print("Bot3 won")
    elif win_list[-1]==p_win:
        print("Player won")



        
        
elif start == 'player':
    order = [player, bot3, bot1, bot2]
    for i in range(0,13):
        x=win_fxn(order)
        if x=='Bot1':
            bot1_win+=1
        elif x=='Bot2':
            bot2_win+=1
        elif x=='Bot3':
            bot3_win+=1
        else:
            p_win+=1
    win_list=[bot1_win,bot2_win,bot3_win,p_win]
    win_list.sort()
    if win_list[-1]==bot1_win:
        print("Bot1 won")
    elif win_list[-1]==bot2_win:
        print("Bot2 won")
    elif win_list[-1]==bot3_win:
        print("Bot3 won")
    elif win_list[-1]==p_win:
        print("Player won")
        
elif start == 'bot3':
    order = [bot3, bot1, bot2, player]
    for i in range(0,13):
        x=win_fxn(order)
        if x=='Bot1':
            bot1_win+=1
        elif x=='Bot2':
            bot2_win+=1
        elif x=='Bot3':
            bot3_win+=1
        else:
            p_win+=1
    win_list=[bot1_win,bot2_win,bot3_win,p_win]
    win_list.sort()
    if win_list[-1]==bot1_win:
        print("Bot1 won")
    elif win_list[-1]==bot2_win:
        print("Bot2 won")
    elif win_list[-1]==bot3_win:
        print("Bot3 won")
    elif win_list[-1]==p_win:
        print("Player won")

elif start=='bot2':
    order=[bot2,player,bot3,bot1]
    for i in range(0,13):
        x=win_fxn(order)
        if x=='Bot1':
            bot1_win+=1
        elif x=='Bot2':
            bot2_win+=1
        elif x=='Bot3':
            bot3_win+=1
        else:
            p_win+=1
    win_list=[bot1_win,bot2_win,bot3_win,p_win]
    win_list.sort()
    if win_list[-1]==bot1_win:
        print("Bot1 won")
    elif win_list[-1]==bot2_win:
        print("Bot2 won")
    elif win_list[-1]==bot3_win:
        print("Bot3 won")
    elif win_list[-1]==p_win:
        print("Player won")