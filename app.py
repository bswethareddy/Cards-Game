# import modules
import itertools, random
con = "Y"
while con=="Y":
    def input_user():
        n=(input("Enter the input in the form of H,A OR S,K from the set given to you: "))
        n=list(n)
        ar=[]
        if len(n)==2:
            ar.append(n[1])
            ar.append(n[0])
        else :
            ar.append(str(n[1]+n[2]))
            ar.append(n[0])
        return ar

    def str_fxn(l):
        rl=[ele[::-1] for ele in l]
        ls=[''.join(ele) for ele in rl] 
        res=[i for i in ls]
        return res

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
    p=str_fxn(player)
    print(*p)

    print("\nBot 1 got: ") 
    for j in range(13):
        bot1[j][0] = deck[j][0]
        bot1[j][1] = deck[j][1]
        deck.remove(deck[j])
    bot1=sort_fxn(bot1)
    b1=str_fxn(bot1)
    print(*b1)
        
    print("\nbot2 got: ")
    for k in range(13):
        bot2[k][0] = deck[k][0]
        bot2[k][1] = deck[k][1]
        deck.remove(deck[k])
    bot2=sort_fxn(bot2)
    b2=str_fxn(bot2)
    print(*b2)

    print("\nBot3 got: ")
    for l in range(13):
        bot3[l][0] = deck[l][0]
        bot3[l][1] = deck[l][1]
    bot3=sort_fxn(bot3)
    b3=str_fxn(bot3)
    print(*b3)



    def calls(p1): 
        count = 0
        for i in range(len(p1)):
            if p1[i][0] == 'A' or p1[i][0] == 'K' or p1[i][0] == 'Q' or p1[i][0] == 'J':
                count+=1
        return count


    bot1_call = calls(bot1)
    bot2_call = calls(bot2)
    bot3_call = calls(bot3)
    player_call  = input(f"Call of Players: Bot1-> {str(bot1_call)} Bot2-> {str(bot2_call)} Bot3-> {str(bot3_call)} Player-> ")
    print("Order of arrangement: Bot1, Bot2, Player, Bot3, Bot1, ...... ")

    start = input("Who is gonna start the game ( bot1 / bot2 / bot3 / player )? ")

    def win_fxn(l):
        
        if(l[0]==player):
            x=input_user()
            l[0].remove(x)
            m=str_fxn(l[0])
            print(*m)
            a =x[1]
            #l[0]will be remaining option for player
            #x1 be variable for Bot1
            #x2 for bot2
            #x3 for bot3
            check_list=[]
            check_list.append(x)

            l_x3=[]
            l_x3.append(x)
            for i in range(len(bot3)):
                if bot3[i][1]==a:
                    l_x3.append(bot3[i])
            l_x3=sort_fxn(l_x3)
            print(l_x3)
            for i in range(len(bot3)):
                if len(l_x3)>1:
                    for j in range(len(l_x3)):
                        if l_x3[j]==x:
                            if j!=0:
                                x3=l_x3[0]
                                break
                            else:
                                x3=l_x3[-1]
                                break
                    check_list.append(x3)  
                    break              
                else:
                    x3=bot3[-1]
            bot3.remove(x3)
            print("x3 ",x3)

            l_x1=[]
            l_x1.append(x)
            for i in range(len(bot1)):
                if bot1[i][1]==a:
                    l_x1.append(bot1[i])
            l_x1=sort_fxn(l_x1)
            print(l_x1)
            for i in range(len(bot1)):
                if len(l_x1)>1:
                    for j in range(len(l_x1)):
                        if l_x1[j]==x:
                            if j!=0:
                                x1=l_x1[0]
                                break
                            else:
                                x1=l_x1[-1]
                                break
                    check_list.append(x1)  
                    break              
                else:
                    x1=bot1[-1]
            bot1.remove(x1)
            print("x1 ",x1)

            l_x2=[]
            l_x2.append(x)
            for i in range(len(bot2)):
                if bot2[i][1]==a:
                    l_x2.append(bot2[i])
            l_x2=sort_fxn(l_x2)
            print(l_x2)
            for i in range(len(bot2)):
                if len(l_x2)>1:
                    for j in range(len(l_x2)):
                        if l_x2[j]==x:
                            if j!=0:
                                x2=l_x2[0]
                                break
                            else:
                                x2=l_x2[-1]
                                break
                    check_list.append(x2)  
                    break              
                else:
                    x2=bot2[-1]
            bot2.remove(x2)
            print("x2 ",x2)

        elif(l[1]==player):
            
            x2=bot2[0]
            bot2.remove(x2)
            print("x2 ",x2)
            a = x2[1]
            check_list=[]
            check_list.append(x2)

            x=input_user()
            l[1].remove(x)
            m=str_fxn(l[1])
            print(*m)
            if x[1]==a:
                check_list.append(x)
                
            l_x3=[]
            l_x3.append(x2)
            for i in range(len(bot3)):
                if bot3[i][1]==a:
                    l_x3.append(bot3[i])
            l_x3=sort_fxn(l_x3)
            print(l_x3)           
            for i in range(len(bot3)):
                if len(l_x3)>1:
                    for j in range(len(l_x3)):
                        if l_x3[j]==x2:
                            if j!=0:
                                x3=l_x3[0]
                                break
                            else:
                                x3=l_x3[-1]
                                break
                    check_list.append(x3)  
                    break              
                else:
                    x3=bot3[-1]
            bot3.remove(x3)
            print("x3 ",x3)

            l_x1=[]
            l_x1.append(x2)
            for i in range(len(bot1)):
                if bot1[i][1]==a:
                    l_x1.append(bot1[i])
            l_x1=sort_fxn(l_x1)
            print(l_x1)
            for i in range(len(bot1)):
                if len(l_x1)>1:
                    for j in range(len(l_x1)):
                        if l_x1[j]==x2:
                            if j!=0:
                                x1=l_x1[0]
                                break
                            else:
                                x1=l_x1[-1]
                                break
                    check_list.append(x1)  
                    break              
                else:
                    x1=bot1[-1]
            bot1.remove(x1)
            print("x1 ",x1)


        elif(l[2]==player):
            
            x1=bot1[0]
            bot1.remove(x1)
            print("x1 ",x1)
            a=x1[1]
            check_list=[]
            check_list.append(x1)

            l_x2=[]
            l_x2.append(x1)
            for i in range(len(bot2)):
                if bot2[i][1]==a:
                    l_x2.append(bot2[i])
            l_x2=sort_fxn(l_x2)
            print(l_x2)
            for i in range(len(bot2)):
                if len(l_x2)>1:
                    for j in range(len(l_x2)):
                        if l_x2[j]==x1:
                            if j!=0:
                                x2=l_x2[0]
                                break
                            else:
                                x2=l_x2[-1]
                                break
                    check_list.append(x2)  
                    break              
                else:
                    x2=bot2[-1]
            bot2.remove(x2)
            print("x2 ",x2)
            
            x=input_user()
            l[2].remove(x)
            m=str_fxn(l[2])
            print(*m)
            if x[1]==a:
                check_list.append(x)

            l_x3=[]
            l_x3.append(x1)
            for i in range(len(bot3)):
                if bot3[i][1]==a:
                    l_x3.append(bot3[i])
            l_x3=sort_fxn(l_x3)
            print(l_x3)           
            for i in range(len(bot3)):
                if len(l_x3)>1:
                    for j in range(len(l_x3)):
                        if l_x3[j]==x1:
                            if j!=0:
                                x3=l_x3[0]
                                break
                            else:
                                x3=l_x3[-1]
                                break
                    check_list.append(x3)  
                    break              
                else:
                    x3=bot3[-1]
            bot3.remove(x3)
            print("x3 ",x3)
            

        elif(l[3]==player):
            
            x3=bot3[0]
            bot3.remove(x3)
            print("x3 ",x3)
            a=x3[1]
            check_list=[]
            check_list.append(x3)

            l_x2=[]
            l_x2.append(x3)
            for i in range(len(bot2)):
                if bot2[i][1]==a:
                    l_x2.append(bot2[i])
            l_x2=sort_fxn(l_x2)
            print(l_x2)
            for i in range(len(bot2)):
                if len(l_x2)>1:
                    for j in range(len(l_x2)):
                        if l_x2[j]==x3:
                            if j!=0:
                                x2=l_x2[0]
                                break
                            else:
                                x2=l_x2[-1]
                                break
                    check_list.append(x2)  
                    break              
                else:
                    x2=bot2[-1]
            bot2.remove(x2)
            print("x2 ",x2)

            l_x1=[]
            l_x1.append(x3)
            for i in range(len(bot1)):
                if bot1[i][1]==a:
                    l_x1.append(bot1[i])
            l_x1=sort_fxn(l_x1)
            print(l_x1)
            for i in range(len(bot1)):
                if len(l_x1)>1:
                    for j in range(len(l_x1)):
                        if l_x1[j]==x3:
                            if j!=0:
                                x1=l_x1[0]
                                break
                            else:
                                x1=l_x1[-1]
                                break
                    check_list.append(x1)  
                    break              
                else:
                    x1=bot1[-1]
            bot1.remove(x1)
            print("x1 ",x1)

            x=input_user()
            l[3].remove(x)
            m=str_fxn(l[3])
            print(*m)
            if x[1]==a:
                check_list.append(x)

        print("CHECK_LIST",check_list)

        f=sort_fxn(check_list)
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
    bot1_score = 0
    bot2_score = 0
    bot3_score = 0
    p_score = 0 

    if start == 'bot1':
        order = [bot1, bot2,player, bot3]
        for i in range(0,13):
            print("TURN - ",i+1)
            x=win_fxn(order)
            if x=='Bot1':
                bot1_win+=1
                order=[bot1,bot2,player,bot3]
            elif x=='Bot2':
                bot2_win+=1
                order=[bot2,player,bot3,bot1]
            elif x=='Bot3':
                bot3_win+=1
                order=[bot3, bot1, bot2, player]
            else:
                p_win+=1
                order=[player, bot3, bot1, bot2]
        

        if(bot1_call>bot1_win):
            bot1_score += -10*(bot1_call)
        else:
            bot1_score += 10*(bot1_call) + (bot1_win-bot1_call)
        if(bot2_call>bot2_win):
            bot2_score += -10*(bot2_call)
        else:
            bot2_score += 10*(bot2_call) + (bot2_win-bot2_call)
        if(bot3_call>bot3_win):
            bot3_score += -10*(bot3_call)
        else:
            bot3_score += 10*(bot3_call) + (bot3_win-bot3_call)
        if(player_call>p_win):
            p_score += -10*(player_call)
        else:
            p_score += 10*(player_call) + (p_win-player_call)

        win_list=[bot1_score,bot2_score,bot3_score,p_score]
        win_list.sort()
        final_list = list(set(win_list))
        if final_list != win_list:
            print("The game is tied")

        elif win_list[-1]==bot1_score:
            print("Bot1 won")
            
        elif win_list[-1]==bot2_score:
            print("Bot2 won")
            
        elif win_list[-1]==bot3_score:
            print("Bot3 won")
            
        elif win_list[-1]==p_score:
            print("Player won")
            
        
    elif start == 'player':
        order = [player, bot3, bot1, bot2]
        for i in range(0,13):
            print("TURN - ",i+1)
            x=win_fxn(order)
            if x=='Bot1':
                bot1_win+=1
                order=[bot1,bot2,player,bot3]
            elif x=='Bot2':
                bot2_win+=1
                order=[bot2,player,bot3,bot1]
            elif x=='Bot3':
                bot3_win+=1
                order=[bot3, bot1, bot2, player]
            else:
                p_win+=1
                order=[player, bot3, bot1, bot2]
        if(bot1_call>bot1_win):
            bot1_score += -10*(bot1_call)
        else:
            bot1_score += 10*(bot1_call) + (bot1_win-bot1_call)
        if(bot2_call>bot2_win):
            bot2_score += -10*(bot2_call)
        else:
            bot2_score += 10*(bot2_call) + (bot2_win-bot2_call)
        if(bot3_call>bot3_win):
            bot3_score += -10*(bot3_call)
        else:
            bot3_score += 10*(bot3_call) + (bot3_win-bot3_call)
        if(player_call>p_win):
            p_score += -10*(player_call)
        else:
            p_score += 10*(player_call) + (p_win-player_call)

        win_list=[bot1_score,bot2_score,bot3_score,p_score]
        win_list.sort()
        final_list = list(set(win_list))
        if final_list != win_list:
            print("The game is tied")

        elif win_list[-1]==bot1_score:
            print("Bot1 won")
        
        elif win_list[-1]==bot2_score:
            print("Bot2 won")
            
        elif win_list[-1]==bot3_score:
            print("Bot3 won")
            
        elif win_list[-1]==p_score:
            print("Player won")
            
            
    elif start == 'bot3':
        order = [bot3, bot1, bot2, player]
        for i in range(0,13):
            print("TURN - ",i+1)
            x=win_fxn(order)
            if x=='Bot1':
                bot1_win+=1
                order=[bot1,bot2,player,bot3]
            elif x=='Bot2':
                bot2_win+=1
                order=[bot2,player,bot3,bot1]
            elif x=='Bot3':
                bot3_win+=1
                order=[bot3, bot1, bot2, player]
            else:
                p_win+=1
                order=[player, bot3, bot1, bot2]
        if(bot1_call>bot1_win):
            bot1_score += -10*(bot1_call)
        else:
            bot1_score += 10*(bot1_call) + (bot1_win-bot1_call)
        if(bot2_call>bot2_win):
            bot2_score += -10*(bot2_call)
        else:
            bot2_score += 10*(bot2_call) + (bot2_win-bot2_call)
        if(bot3_call>bot3_win):
            bot3_score += -10*(bot3_call)
        else:
            bot3_score += 10*(bot3_call) + (bot3_win-bot3_call)
        if(player_call>p_win):
            p_score += -10*(player_call)
        else:
            p_score += 10*(player_call) + (p_win-player_call)

        win_list=[bot1_score,bot2_score,bot3_score,p_score]
        win_list.sort()
        final_list = list(set(win_list))
        if final_list != win_list:
            print("The game is tied")
        elif win_list[-1]==bot1_score:
            print("Bot1 won")
            
        elif win_list[-1]==bot2_score:
            print("Bot2 won")
            
        elif win_list[-1]==bot3_score:
            print("Bot3 won")
            
        elif win_list[-1]==p_score:
            print("Player won")
            

    elif start=='bot2':
        order=[bot2,player,bot3,bot1]
        for i in range(0,13):
            print("TURN - ",i+1)
            x=win_fxn(order)
            if x=='Bot1':
                bot1_win+=1
                order=[bot1,bot2,player,bot3]
            elif x=='Bot2':
                bot2_win+=1
                order=[bot2,player,bot3,bot1]
            elif x=='Bot3':
                bot3_win+=1
                order=[bot3, bot1, bot2, player]
            else:
                p_win+=1
                order=[player, bot3, bot1, bot2]
        if(bot1_call>bot1_win):
            bot1_score += -10*(bot1_call)
        else:
            bot1_score += 10*(bot1_call) + (bot1_win-bot1_call)
        if(bot2_call>bot2_win):
            bot2_score += -10*(bot2_call)
        else:
            bot2_score += 10*(bot2_call) + (bot2_win-bot2_call)
        if(bot3_call>bot3_win):
            bot3_score += -10*(bot3_call)
        else:
            bot3_score += 10*(bot3_call) + (bot3_win-bot3_call)
        if(player_call>p_win):
            p_score += -10*(player_call)
        else:
            p_score += 10*(player_call) + (p_win-player_call)

        win_list=[bot1_score,bot2_score,bot3_score,p_score]
        win_list.sort()
        final_list = list(set(win_list))
        if final_list != win_list:
            print("The game is tied")

        elif win_list[-1]==bot1_score:
            print("Bot1 won")
            
        elif win_list[-1]==bot2_score:
            print("Bot2 won")
            
        elif win_list[-1]==bot3_score:
            print("Bot3 won")
            
        elif win_list[-1]==p_score:
            print("Player won")
    
    con = input("Continue(Y/N): ")