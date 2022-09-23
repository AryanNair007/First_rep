import random
import turtle



print("Welcome to the game section created by Aryan nair")
print()
print('''In this section you can play
1. Rock paper scissor 
2. Odd even or cricket (playable) (partial complete)
3. Ping Pong (graphic orientated)
4. Coming soon''')
def game_select_back():

    select_game=input('which game do you want to play:').lower()

    #game 1 rock paper scissor (complete)==========================================================================================
    if select_game=='1' or select_game=='rock' or select_game=='paper' or select_game=='scissor' or select_game=='rock paper scissor':
        print()
        print('''Rules of this game:
	    1.You have to choose from Rock Paper or Scissor
	    2.Compuer will also choose one of them
	    3.If your choice is better than computer you win or loose if not else you and computer choose the same its a tie
	    4.To go back in game selection type 2 else if you want quit type quit or exit''')
        print()
        def rock_paper_scissor():
	        win_count=lose_count=tie_count=0
	        dummy=count=1
	        while dummy<20:
	            print(f"------------------------------{count}--------------------------")
	            dummy+=1
	            count+=1
	            lis=['Paper','Scissor','Rock']
	            computer=random.choice(lis) 							
	            person=input('Type your choice=').lower()     
	            print("Computer's choice=",computer)
	       		
	       		#conditions of rock paper scissor     
	            if person=='rock':
	                if computer=='Rock':
	                    print('RESULT= Tie')
	                    tie_count+=1
	                elif computer=='Paper':
	                    print('RESULT= You Lose')
	                    lose_count+=1
	                elif computer=='Scissor':
	                    print('RESULT= You Win')
	                    win_count+=1
	            
	            elif person=='paper':
	                if computer=='Rock':
	                    print('RESULT= You Win')
	                    win_count+=1
	                elif computer=='Paper':
	                    print('RESULT= Tie')
	                    tie_count+=1
	                elif computer=='Scissor':
	                    print('RESULT= You Lose')
	                    lose_count+=1

	            elif person=='scissor':
	                if computer=='Rock':
	                    print('RESULT= You Lose')
	                    lose_count+=1
	                elif computer=='Paper':
	                    print('RESULT= You Win')
	                    win_count+=1
	                elif computer=='Scissor':
	                    print('RESULT= Tie')
	                    tie_count+=1
	            
	            else:
	                print('Please choose from Rock,Paper or Scissor')

	        print(f"RESULT:- Won={win_count} ,Lost={lose_count},Tied={tie_count}")        
        rock_paper_scissor()
	        
	
        
        print()        
        print('''To go back in game selection type 2 or to continue type 1 or yes else you want quit press any key''')   
        restart=input("Do you want to restart:").lower()                  #restart input
        if restart=='2':
            print()
            game_select_back()

        elif restart=='1' or 'yes':
            print()
            print()
            print()
        else:
            exit()
    #game 2 odd even (under development)====================================================================================================

    elif select_game=='2' or select_game=='odd' or select_game=='even' or select_game=='odd even' or select_game=='cricket':
        print('============================================')
        print()
        print('''Rules of game:
        1. You have to choose from 1,2,3,4,5 or 6
        2. Computer will choose a number
        3. If your choice is same as of computer you are out
        4. Other wise your choice will be add to your score
        5. Greater your score better more intresting it becomes''')
        print()
        print()
        print("there are 2 types games 1.main game 2.quick games")
        print()
        game_select_sub=input("what game do you want to play:")
        print()

        #part 1 ----------------------------------------------------------------------------------

        if game_select_sub=='1':
            def input_unit():
                count=dummy=1
                player_score=computer_score=0
                while dummy==1:                                                   #dummy to loop it till infinity	
                    players_input=int(input("Choose your number:"))               #players input                     
                    list_of_runs=[1,2,3,4,5,6]
                    computer_choice=random.choice(list_of_runs)
                    print("Computer's choice:",computer_choice)

                    if players_input != computer_choice:                          #conditions on players input   
                        player_score+=players_input
                        print('Your score:',player_score)
                        print()
                        print('-------------',count,'--------------')
                        count=count+1
                        print()
                    elif players_input>6 or players_input<1:
                        print("please choose a number from 1,2,3,4,5 or 6")
                        print()
                        input_unit()

                    else:
                        print("You lost the game ")
                        print("Your high score is",player_score)
                        print()
                        print()

                        dummy=2
                        break

                while dummy==2:                                                   #computers turn to bat
                    computer_choice=random.choice(list_of_runs)
                    players_input=int(input("Choose your number(You are balling):"))
                    print("Computer's choice:",computer_choice)
                    count=1

                    if players_input != computer_choice:                          #conditions on computers choice
                        computer_score+=computer_choice
                        print("Computer's score:",computer_score)
                        print()
                        print('-------------',count,'--------------')
                        count=count+1
                    elif players_input>6 or players_input<1:
                        print()
                        print('Choose a number between 1 to 6')
                        continue

                    elif computer_score> player_score:
                        break
                    else:
                        print()
                        print("Computer is OUT")
                        print()
                        print("Computer's high score is",computer_score)
                        break

                print("Computer's batting score",computer_score,'      ',"Your batting score",player_score)   
                if computer_score>player_score:                                   #consition on print statement
                    print('You Lost The Game')
                elif player_score> computer_score:
                    print('You Won The Game')

                print('''To go back in game selection type 2 or to continue type 1 or yes else you want quit press any key''')   
                restart=input("Do you want to restart:").lower()                  #restart input
                if restart=='2':
                    print()
                    game_select_back()

                elif restart=='1' or 'yes':
                    print()
                    print()
                    input_unit()
                    print()
                else:
                    exit()


            input_unit()

        #part 2 -----------------------------------------------------------------------------
            
        elif game_select_sub=='2':
            list_of_runs=[1,2,3,4,5,6]
            player_score=computer_score=select=0
            
            print("This is quick match menu.Here you can play many ways of odd even or criket")
            print('1.Fastest 50 first                                                                   = 1')
            print('2.Fastest runs first (here you can decide the runs)                  = 2')
            print('3.Fastest to take 5 wickets                                                    = 3')
            print('4.Fastest to take wickets first(here you can decide wickets)   = 4')
            print()
            select=int(input("Which game would you like to play:"))
            print()
            #quick match 1 ?????????????????????????????????????????????????????
                  
            if select ==1:
                while player_score<50 or computer_score>50:
                    players_input=int(input("Choose your number:"))
                    computer_choice=random.choice(list_of_runs)
                    print("Computer's choice:",computer_choice)
                    if computer_choice != players_input:
                        player_score+=players_input
                        print("Your score:",player_score)
                    else :
                        print("You are OUT")
                        
                        
                        print("sorry you lost the game")
                        break
                    players_input=int(input("Choose your number:"))
                    computer_choice=random.choice(list_of_runs)
                    print("Computer's choice:",computer_choice)
                    if computer_choice != players_input:
                        computer_score +=computer_choice
                        print("Computer's score:",computer_score)
                    else :
                        print("Computer is  OUT")
                        print("Won the game")
                        break
                if player_score>50:
                    print("You WON the quick match")
                elif computer_score>50:
                    print("You lost the match")

                print('''To go back in game selection type 2 or to continue type 1 or yes else you want quit press any key''')
                restart=input("Do you want to restart:").lower()                  #restart input
                if restart=='2':
                    print()
                    game_select_back()

                elif restart=='1' or 'yes':
                    print()
                    print()
                    #()
                    print()
                else:
                    exit()


            #()      

            #quick match 2 ?????????????????????????????????????????????????????
            
            elif select==2:
                count=1
                max_score=int(input("what will be the max score to win the game"))
                print()
                while player_score<max_score or computer_score>max_score:
                    players_input=int(input("Choose your number:"))
                    computer_choice=random.choice(list_of_runs)
                    print("Computer's choice:",computer_choice)
                    print()
                    if computer_choice != players_input:
                        player_score+=players_input
                        print("Your score:",player_score)
                    else :
                        print("You are OUT")
                        print("sorry you lost the game")
                        break
                    players_input=int(input("Choose your number:"))
                    computer_choice=random.choice(list_of_runs)
                    print("Computer's choice:",computer_choice)
                    if computer_choice != players_input:
                        computer_score +=computer_choice
                        print("Computer's score:",computer_score)
                        print('-----------------------',count,'-----------------------------')
                        count+=1
                    else :
                        print("Computer is  OUT")
                        print("Won the game")
                        break
                if player_score>max_score:
                    print("You WON the quick match")
                elif computer_score>max_score:
                    print("You lost the match")

                print('''To go back in game selection type 2 or to continue type 1 or yes else you want quit press any key''')   
                restart=input("Do you want to restart:").lower()				  #restart input      	
                if restart=='2':
                    print()
                    game_select_back()

                elif restart=='1' or 'yes':
                    print()
                    print()
                else:
                    exit()

    #game 3 ping pong(complete) =================================================================================================                
    elif select_game=='3' or select_game=='ping pong':
        wn= turtle.Screen()
        wn.title('Ping Pong')
        wn.bgcolor('black')
        wn.setup(width=800, height=600)
        wn.tracer(0)

        # Score
        score_a=0
        score_b=0

        # paddle A
        paddle_a = turtle.Turtle()
        paddle_a.speed(0)
        paddle_a.shape('square')
        paddle_a.color('white')
        paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        paddle_a.penup()
        paddle_a.goto(-350, 0)

        # paddle B
        paddle_b = turtle.Turtle()
        paddle_b.speed(0)
        paddle_b.shape('square')
        paddle_b.color('white')
        paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        paddle_b.penup()
        paddle_b.goto(350, 0)

        # Ball
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape('square')
        ball.color('white')
        ball.penup()
        ball.goto(0, 0)
        ball.dx=0.17
        ball.dy=0.17

        # Pen
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color('white')
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))

        # Function
        def paddle_a_up():
            y= paddle_a.ycor()
            y+= 20
            paddle_a.sety(y)

        def paddle_a_down():
            y= paddle_a.ycor()
            y-= 20
            paddle_a.sety(y)

        def paddle_b_up():
            y= paddle_b.ycor()
            y+= 20
            paddle_b.sety(y)

        def paddle_b_down():
            y= paddle_b.ycor()
            y-= 20
            paddle_b.sety(y)

        # Keyword binding
        wn.listen()
        wn.onkeypress(paddle_a_up, "w")
        wn.onkeypress(paddle_a_down, "s")
        wn.onkeypress(paddle_b_up, "Up")
        wn.onkeypress(paddle_b_down, "Down")


        # Main game loop
        while True:
            wn.update()
            
            # Move the ball
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # Border cheaking
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1

            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1

            if ball.xcor() > 390:
                ball.goto(0,0)
                ball.dx *= -1
                score_a+= 1
                pen.clear()
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

            if ball.xcor() < -390:
                ball.goto(0,0)
                ball.dx *= -1
                score_b+= 1
                pen.clear()
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

            # Paddle and ball collisions
            if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor() -50 ):
                ball.setx(340)
                ball.dx *= -1

            if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +50 and ball.ycor() > paddle_a.ycor() -50 ):
                ball.setx(-340)
                ball.dx *= -1   


    #game 4 (coming soon) =================================================================================================                        
    elif select_game=='4' or select_game=='coming soon':
        print("It is coming soon")

game_select_back()
#dummy=input("PRESS ANY KEY TO EXIT")
