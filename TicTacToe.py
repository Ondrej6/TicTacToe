import pygame, random, time, sys
pygame.init()
window_width=660
window_height=660
window=pygame.display.set_mode((window_width,window_height))
bigfont = pygame.font.SysFont("comicsansms", 72)
smallfont = pygame.font.SysFont("comicsansms", 36)
pygame.display.set_caption('TicTacToe')
green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)

def win_pc_AI(screen, easy, player):
    if easy == 2:
        if easy == player:
            if (screen[0]== 1 and screen[0]== screen[1] and screen[0] == screen[2]) or (screen[3]== 1 and screen[3]== screen[4] and screen[3] == screen[5]) or (screen[6]== 1 and screen[6]== screen[7] and screen[6] == screen[8]) or (screen[0]== 1 and screen[0]== screen[3] and screen[0] == screen[6]) or (screen[1]== 1 and screen[1]== screen[4] and screen[1] == screen[7]) or (screen[2]== 1 and screen[2]== screen[5] and screen[2] == screen[8]) or (screen[0]== 1 and screen[0] == screen[4] and screen[0] == screen[8]) or (screen[2]== 1 and screen[2]== screen[4] and screen[2] == screen[6]):
                display_message('Computer 1 won!',bigfont,screen)
                return True

        elif easy != player: 
            if (screen[0]== 2 and screen[0]== screen[1] and screen[0] == screen[2]) or (screen[3]== 2 and screen[3]== screen[4] and screen[3] == screen[5]) or (screen[6]== 2 and screen[6]== screen[7] and screen[6] == screen[8]) or (screen[0]== 2 and screen[0]== screen[3] and screen[0] == screen[6]) or (screen[1]== 2 and screen[1]== screen[4] and screen[1] == screen[7]) or (screen[2]== 2 and screen[2]== screen[5] and screen[2] == screen[8]) or (screen[0]== 2 and screen[0] == screen[4] and screen[0] == screen[8]) or (screen[2]== 2 and screen[2]== screen[4] and screen[2] == screen[6]):
                display_message('Computer 2 won!',bigfont,screen)
                return True
        else:
            return False
    if easy == 1:
        if easy == player:
            if (screen[0]== 2 and screen[0]== screen[1] and screen[0] == screen[2]) or (screen[3]== 2 and screen[3]== screen[4] and screen[3] == screen[5]) or (screen[6]== 2 and screen[6]== screen[7] and screen[6] == screen[8]) or (screen[0]== 2 and screen[0]== screen[3] and screen[0] == screen[6]) or (screen[1]== 2 and screen[1]== screen[4] and screen[1] == screen[7]) or (screen[2]== 2 and screen[2]== screen[5] and screen[2] == screen[8]) or (screen[0]== 2 and screen[0] == screen[4] and screen[0] == screen[8]) or (screen[2]== 2 and screen[2]== screen[4] and screen[2] == screen[6]):
                display_message('Computer 2 won!',bigfont,screen)
                return True

        elif easy != player: 
            if (screen[0]== 1 and screen[0]== screen[1] and screen[0] == screen[2]) or (screen[3]== 1 and screen[3]== screen[4] and screen[3] == screen[5]) or (screen[6]== 1 and screen[6]== screen[7] and screen[6] == screen[8]) or (screen[0]== 1 and screen[0]== screen[3] and screen[0] == screen[6]) or (screen[1]== 1 and screen[1]== screen[4] and screen[1] == screen[7]) or (screen[2]== 1 and screen[2]== screen[5] and screen[2] == screen[8]) or (screen[0]== 1 and screen[0] == screen[4] and screen[0] == screen[8]) or (screen[2]== 1 and screen[2]== screen[4] and screen[2] == screen[6]):
                display_message('Computer 1 won!',bigfont,screen)
                return True
        else:
            return False
def best_choice(screen,human):
    if (1 in screen and 2 not in screen) or (2 in screen and 1 not in screen):
        if screen[4] == 0:
            return 4
    if (screen[0] == human and screen[8] == human) or (screen[2] == human and screen[6]==human):
        best=[1,3,5,7]
        while best:
            position = random.choice(best)
            if screen[position] == 0:
                return position
            else:
                del best[best.index(position)]
    
    best=[0,2,6,8]
    while best:
        position = random.choice(best)
        if screen[position] == 0:
            return position
        else:
            del best[best.index(position)]
    if screen[4] == 0:
        return 4
    best=[1,3,5,7]
    while best:
        position = random.choice(best)
        if screen[position] == 0:
            return position
        else:
            del best[best.index(position)]

def win_condition(screen,human, player):
    next=screen.copy()
    for position in range(len(next)):
        if next[position]== 0:
            next[position] = player
        if win_pc_hard(next,player,human):
            return position
        else:
            next=screen.copy()
    return -1
def no_lose(screen, human, player):
    next = screen.copy()
    for position in range(len(next)):
        if next[position]== 0:
            next[position]= human
        if win_pc_hard(next,human,player):
            return position
        else:
            next=screen.copy()
    return -1
def win_pc_hard(screen, human, player):
    if human == 2:
        if human == player:
            if (screen[0]== 1 and screen[0]== screen[1] and screen[0] == screen[2]) or (screen[3]== 1 and screen[3]== screen[4] and screen[3] == screen[5]) or (screen[6]== 1 and screen[6]== screen[7] and screen[6] == screen[8]) or (screen[0]== 1 and screen[0]== screen[3] and screen[0] == screen[6]) or (screen[1]== 1 and screen[1]== screen[4] and screen[1] == screen[7]) or (screen[2]== 1 and screen[2]== screen[5] and screen[2] == screen[8]) or (screen[0]== 1 and screen[0] == screen[4] and screen[0] == screen[8]) or (screen[2]== 1 and screen[2]== screen[4] and screen[2] == screen[6]):
                #display_message('You won!',bigfont,screen)
                return True

        elif human != player: 
            if (screen[0]== 2 and screen[0]== screen[1] and screen[0] == screen[2]) or (screen[3]== 2 and screen[3]== screen[4] and screen[3] == screen[5]) or (screen[6]== 2 and screen[6]== screen[7] and screen[6] == screen[8]) or (screen[0]== 2 and screen[0]== screen[3] and screen[0] == screen[6]) or (screen[1]== 2 and screen[1]== screen[4] and screen[1] == screen[7]) or (screen[2]== 2 and screen[2]== screen[5] and screen[2] == screen[8]) or (screen[0]== 2 and screen[0] == screen[4] and screen[0] == screen[8]) or (screen[2]== 2 and screen[2]== screen[4] and screen[2] == screen[6]):
                #display_message('You lost!',bigfont,screen)
                return True
        else:
            return False
    if human == 1:
        if human == player:
            if (screen[0]== 2 and screen[0]== screen[1] and screen[0] == screen[2]) or (screen[3]== 2 and screen[3]== screen[4] and screen[3] == screen[5]) or (screen[6]== 2 and screen[6]== screen[7] and screen[6] == screen[8]) or (screen[0]== 2 and screen[0]== screen[3] and screen[0] == screen[6]) or (screen[1]== 2 and screen[1]== screen[4] and screen[1] == screen[7]) or (screen[2]== 2 and screen[2]== screen[5] and screen[2] == screen[8]) or (screen[0]== 2 and screen[0] == screen[4] and screen[0] == screen[8]) or (screen[2]== 2 and screen[2]== screen[4] and screen[2] == screen[6]):
                #display_message('You lost!',bigfont,screen)
                return True

        elif human != player: 
            if (screen[0]== 1 and screen[0]== screen[1] and screen[0] == screen[2]) or (screen[3]== 1 and screen[3]== screen[4] and screen[3] == screen[5]) or (screen[6]== 1 and screen[6]== screen[7] and screen[6] == screen[8]) or (screen[0]== 1 and screen[0]== screen[3] and screen[0] == screen[6]) or (screen[1]== 1 and screen[1]== screen[4] and screen[1] == screen[7]) or (screen[2]== 1 and screen[2]== screen[5] and screen[2] == screen[8]) or (screen[0]== 1 and screen[0] == screen[4] and screen[0] == screen[8]) or (screen[2]== 1 and screen[2]== screen[4] and screen[2] == screen[6]):
                #display_message('You won!',bigfont,screen)
                return True
        else:
            return False
def win_pc(screen, human, player):
    if human == 2:
        if human == player:
            if (screen[0]== 1 and screen[0]== screen[1] and screen[0] == screen[2]) or (screen[3]== 1 and screen[3]== screen[4] and screen[3] == screen[5]) or (screen[6]== 1 and screen[6]== screen[7] and screen[6] == screen[8]) or (screen[0]== 1 and screen[0]== screen[3] and screen[0] == screen[6]) or (screen[1]== 1 and screen[1]== screen[4] and screen[1] == screen[7]) or (screen[2]== 1 and screen[2]== screen[5] and screen[2] == screen[8]) or (screen[0]== 1 and screen[0] == screen[4] and screen[0] == screen[8]) or (screen[2]== 1 and screen[2]== screen[4] and screen[2] == screen[6]):
                display_message('You lost!',bigfont,screen)
                return True

        elif human != player: 
            if (screen[0]== 2 and screen[0]== screen[1] and screen[0] == screen[2]) or (screen[3]== 2 and screen[3]== screen[4] and screen[3] == screen[5]) or (screen[6]== 2 and screen[6]== screen[7] and screen[6] == screen[8]) or (screen[0]== 2 and screen[0]== screen[3] and screen[0] == screen[6]) or (screen[1]== 2 and screen[1]== screen[4] and screen[1] == screen[7]) or (screen[2]== 2 and screen[2]== screen[5] and screen[2] == screen[8]) or (screen[0]== 2 and screen[0] == screen[4] and screen[0] == screen[8]) or (screen[2]== 2 and screen[2]== screen[4] and screen[2] == screen[6]):
                display_message('You won!',bigfont,screen)
                return True
        else:
            return False
    if human == 1:
        if human == player:
            if (screen[0]== 2 and screen[0]== screen[1] and screen[0] == screen[2]) or (screen[3]== 2 and screen[3]== screen[4] and screen[3] == screen[5]) or (screen[6]== 2 and screen[6]== screen[7] and screen[6] == screen[8]) or (screen[0]== 2 and screen[0]== screen[3] and screen[0] == screen[6]) or (screen[1]== 2 and screen[1]== screen[4] and screen[1] == screen[7]) or (screen[2]== 2 and screen[2]== screen[5] and screen[2] == screen[8]) or (screen[0]== 2 and screen[0] == screen[4] and screen[0] == screen[8]) or (screen[2]== 2 and screen[2]== screen[4] and screen[2] == screen[6]):
                display_message('You lost!',bigfont,screen)
                return True

        elif human != player: 
            if (screen[0]== 1 and screen[0]== screen[1] and screen[0] == screen[2]) or (screen[3]== 1 and screen[3]== screen[4] and screen[3] == screen[5]) or (screen[6]== 1 and screen[6]== screen[7] and screen[6] == screen[8]) or (screen[0]== 1 and screen[0]== screen[3] and screen[0] == screen[6]) or (screen[1]== 1 and screen[1]== screen[4] and screen[1] == screen[7]) or (screen[2]== 1 and screen[2]== screen[5] and screen[2] == screen[8]) or (screen[0]== 1 and screen[0] == screen[4] and screen[0] == screen[8]) or (screen[2]== 1 and screen[2]== screen[4] and screen[2] == screen[6]):
                display_message('You won!',bigfont,screen)
                return True
        else:
            return False
def draw_pc(screen,human,player):
    if 0 not in screen and not win_pc(screen,human,player):
        display_message(f'Draw!',bigfont,screen)
        return True
    else:
        return False
def win(screen):
    if (screen[0]== 1 and screen[0]== screen[1] and screen[0] == screen[2]) or (screen[3]== 1 and screen[3]== screen[4] and screen[3] == screen[5]) or (screen[6]== 1 and screen[6]== screen[7] and screen[6] == screen[8]) or (screen[0]== 1 and screen[0]== screen[3] and screen[0] == screen[6]) or (screen[1]== 1 and screen[1]== screen[4] and screen[1] == screen[7]) or (screen[2]== 1 and screen[2]== screen[5] and screen[2] == screen[8]) or (screen[0]== 1 and screen[0] == screen[4] and screen[0] == screen[8]) or (screen[2]== 1 and screen[2]== screen[4] and screen[2] == screen[6]):
        display_message(f'Player 1 won!',bigfont,screen)
        return True

    elif (screen[0]== 2 and screen[0]== screen[1] and screen[0] == screen[2]) or (screen[3]== 2 and screen[3]== screen[4] and screen[3] == screen[5]) or (screen[6]== 2 and screen[6]== screen[7] and screen[6] == screen[8]) or (screen[0]== 2 and screen[0]== screen[3] and screen[0] == screen[6]) or (screen[1]== 2 and screen[1]== screen[4] and screen[1] == screen[7]) or (screen[2]== 2 and screen[2]== screen[5] and screen[2] == screen[8]) or (screen[0]== 2 and screen[0] == screen[4] and screen[0] == screen[8]) or (screen[2]== 2 and screen[2]== screen[4] and screen[2] == screen[6]):
        display_message(f'Player 2 won!',bigfont,screen)
        return True
    else:
        return False
def draw(screen):
    if 0 not in screen and not win(screen):
        display_message(f'Draw!',bigfont,screen)
        return True
    else:
        return False
def turn(screen):
    while True:
        position = random.randint(0,8)
        if screen[position] == 0:
            return position
def menu():   
    desk()
    button('TicTacToe',bigfont,200,80)
    button('Play',smallfont, window_width//2, window_height//2)
    pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def button(text,font, width, height):
    TextSurf, TextRect = text_objects(text,font)
    TextRect.center = ((width),(height))
    window.blit(TextSurf, TextRect)
    pygame.display.update()
    return font.size(text)

def display_message(text,font,screen):
    TextSurf, TextRect = text_objects(text,font)
    TextRect.center = ((window_width/2),(window_height/2))
    window.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    
    draw_screen(screen)
def display_player(display,player,screen, against):
    if display == True:
        if not against: 
            display_message(f'Player {player}',bigfont,screen)
            display = False
        else:
            display_message('Your turn!',bigfont,screen)
            display = False
    
def circle(x,y,color):
    pygame.draw.circle(window,color,(x,y),54,10)
    pygame.display.update()

def cross(sx1,sy1,ex1,ey1,sx2,sy2,ex2,ey2,color):
    pygame.draw.line(window,color,(sx1,sy1),(ex1,ey1),8)
    pygame.draw.line(window,color,(sx2,sy2),(ex2,ey2),8)
    pygame.display.update()

def desk():
    window.fill(black)
    pygame.draw.line(window,(0,0,255),(220,0),(220,660),8)
    pygame.draw.line(window,(0,0,255),(440,0),(440,660),8)
    pygame.draw.line(window,(0,0,255),(0,220),(660,220),8)
    pygame.draw.line(window,(0,0,255),(0,440),(660,440),8)
    pygame.display.update()

def draw_screen(screen):
    window.fill(black)
    desk()
    if screen[0] == 1:
        circle(108,108,red)
    if screen[0] == 2:
        cross(54,54,162,162,162,54,54,162,green)
    if screen[1] == 1:
        circle(328,108,red)
    if screen[1] == 2:
        cross(274,54,382,162,382,54,274,162,green)
    if screen[2] == 1:
        circle(548,108,red)
    if screen[2] == 2:
        cross(494,54,602,162,602,54,494,162,green)
    if screen[3] == 1:
        circle(108,328,red)
    if screen[3] == 2:
        cross(54,274,162,382,162,274,54,382,green)
    if screen[4] == 1:
        circle(328,328,red)
    if screen[4] == 2:
        cross(274,274,382,382,382,274,274,382,green)
    if screen[5] == 1:
        circle(548,328,red)
    if screen[5] == 2:
        cross(494,274,602,382,602,274,494,382,green)
    if screen[6] == 1:
        circle(108,548,red)
    if screen[6] == 2:
        cross(54,494,162,602,162,494,54,602,green)
    if screen[7] == 1:
        circle(328,548,red)
    if screen[7] == 2:
        cross(274,494,382,602,382,494,274,602,green)
    if screen[8] == 1:
        circle(548,548,red)
    if screen[8] == 2:
        cross(494,494,602,602,602,494,494,602,green)

def who_goes_first():
    player= random.randint(1,2)
    return player

def game_loop(run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO, gameeasy):
    while run:
        player=who_goes_first()
        gamehard = False
        screen=[0,0,0,0,0,0,0,0,0]
        display = True
        if title == True:
            menu()
        while title:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    title = False 
                    run = False
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y= pygame.mouse.get_pos()
                    if x>= (window_width//2)-60 and x <= (window_width//2) + 60 and y >= (window_height//2) - 20 and y <= (window_height//2) + 20:                        
                        settings= True
                        title = False
        if settings == True:
            window.fill(black)
            desk()
            button('TicTacToe',bigfont,200,80)
            AIvAIw, AIvAIh = button('AI vs AI',smallfont, window_width//4,window_height//4)            
            HumanvAIw, HumanvAIh = button('Human vs AI',smallfont, 2*window_width//4,2*window_height//4)            
            HumanvHumanw, HumanvHumanh = button('Human vs Human',smallfont, 3*window_width//4,3*window_height//4)            

        while settings == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settings= False
                    run = False
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if x >= (window_width//4)-(AIvAIw//2) and x <= (window_width//4)+(AIvAIw//2) and y >= (window_height//4) - (AIvAIh//2)  and y<= (window_height//4)+(AIvAIh//2):
                        gameAIvAI = True
                        settings = False
                    if x >= (2*window_width//4)-(HumanvAIw//2) and x <= (2*window_width//4)+(HumanvAIw//2) and y >= (2*window_height//4) - (HumanvAIh//2)  and y<= (2*window_height//4)+(HumanvAIh//2):
                        difficulty = True
                        settings = False
                    if x >= (3*window_width//4)-(HumanvHumanw//2) and x <= (3*window_width//4)+(HumanvHumanw//2) and y >= (3*window_height//4) - (HumanvHumanh//2)  and y<= (3*window_height//4)+(HumanvHumanh//2):
                        gameHumanvHuman = True
                        settings = False
        if gameAIvAI == True:
            window.fill(black)
            desk()
            if player == 1:
                display_message('Circle go first!', smallfont, screen)
            else:
                display_message('Cross go first!', smallfont,screen)
            easy=random.randint(1,2)

        while gameAIvAI:
            position =-1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameAIvAI = False
                    run = False
            if easy == player:
                position = turn(screen)
                if position == 0:
                    if player == 1:
                        circle(108,108,red)
                        player=2
                        if screen[0] == 0:
                            screen[0] = 1
                    else:
                        cross(54,54,162,162,162,54,54,162,green)
                        player=1
                        if screen[0] == 0:
                            screen[0] = 2

                if position == 1:
                    if player == 1:            
                        if screen[1] == 0:
                            circle(328,108,red)
                            player=2
                            screen[1] = 1
                    else:
                        if screen[1] == 0:
                            cross(274,54,382,162,382,54,274,162,green)
                            player=1
                            screen[1] = 2
                if position == 2:
                    if player == 1:
                        if screen[2] == 0:
                            circle(548,108,red)
                            player=2
                            screen[2] = 1
                    else:                            
                        if screen[2] == 0:
                            cross(494,54,602,162,602,54,494,162,green)
                            player=1
                            screen[2] = 2
                if position == 3:
                    if player == 1:                            
                        if screen[3] == 0:
                            circle(108,328,red)
                            player=2
                            screen[3] = 1
                    else:                            
                        if screen[3] == 0:
                            cross(54,274,162,382,162,274,54,382,green)
                            player=1
                            screen[3] = 2
                if position == 4:
                    if player == 1:                            
                        if screen[4] == 0:
                            circle(328,328,red)
                            player=2
                            screen[4] = 1
                    else:                            
                        if screen[4] == 0:
                            cross(274,274,382,382,382,274,274,382,green)
                            player=1
                            screen[4] = 2
                if position == 5:
                    if player==1:                            
                        if screen[5] == 0:
                            circle(548,328,red)
                            player=2
                            screen[5] = 1
                    else:                            
                        if screen[5] == 0:
                            cross(494,274,602,382,602,274,494,382,green)
                            player=1
                            screen[5] = 2
                if position == 6:
                    if player == 1:                            
                        if screen[6] == 0:
                            circle(108,548,red)
                            player=2
                            screen[6] = 1
                    else:                            
                        if screen[6] == 0:
                            cross(54,494,162,602,162,494,54,602,green)
                            player=1
                            screen[6] = 2
                if position == 7:
                    if player == 1:                            
                        if screen[7] == 0:
                            circle(328,548,red)
                            player=2
                            screen[7] = 1
                    else:                            
                        if screen[7] == 0:
                            cross(274,494,382,602,382,494,274,602,green)
                            player=1
                            screen[7] = 2
                if position == 8:
                    if player == 1:                            
                        if screen[8] == 0:
                            circle(548,548,red)
                            player=2
                            screen[8] = 1
                    else:                            
                        if screen[8] == 0:
                            cross(494,494,602,602,602,494,494,602,green)
                            player=1
                            screen[8] = 2
                if not win_pc_AI(screen, easy, player):
                        if draw_pc(screen,easy,player):                            
                            run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO, gameeasy= True ,True, False, False, False, False, False, False, False                            
                            continue                    
                elif win_pc_AI(screen, easy, player):                      
                        run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO,gameeasy = True ,True, False, False, False, False, False, False, False                  
                        continue
                time.sleep(1)
            else:
                position=win_condition(screen,easy,player)
                if position == -1:
                    position = no_lose(screen,easy, player)
                if position == -1:
                    position = best_choice(screen,easy)
                if position == 0:
                    if player == 1:
                        circle(108,108,red)
                        player=2                                
                        screen[0] = 1
                    else:
                        cross(54,54,162,162,162,54,54,162,green)
                        player=1                                
                        screen[0] = 2
                if position == 1:
                    if player == 1:                           
                        circle(328,108,red)
                        player=2
                        screen[1] = 1
                    else:
                        cross(274,54,382,162,382,54,274,162,green)
                        player=1
                        screen[1] = 2
                if position == 2:
                    if player == 1:
                        circle(548,108,red)
                        player=2
                        screen[2] = 1
                    else:
                        cross(494,54,602,162,602,54,494,162,green)
                        player=1
                        screen[2] = 2
                if position == 3:
                    if player == 1:
                        circle(108,328,red)
                        player=2
                        screen[3] = 1
                    else:
                        cross(54,274,162,382,162,274,54,382,green)
                        player=1
                        screen[3] = 2
                if position == 4:
                    if player == 1:
                        circle(328,328,red)
                        player=2
                        screen[4] = 1
                    else:
                        cross(274,274,382,382,382,274,274,382,green)
                        player=1
                        screen[4] = 2
                if position == 5:
                    if player==1:
                        circle(548,328,red)
                        player=2
                        screen[5] = 1
                    else:
                        cross(494,274,602,382,602,274,494,382,green)
                        player=1
                        screen[5] = 2
                if position == 6:
                    if player == 1:
                        circle(108,548,red)
                        player=2
                        screen[6] = 1
                    else:
                        cross(54,494,162,602,162,494,54,602,green)
                        player=1
                        screen[6] = 2
                if position == 7:
                    if player == 1:
                        circle(328,548,red)
                        player=2
                        screen[7] = 1
                    else:
                        cross(274,494,382,602,382,494,274,602,green)
                        player=1
                        screen[7] = 2
                if position == 8:
                    if player == 1:
                        circle(548,548,red)
                        player=2
                        screen[8] = 1
                    else:
                        cross(494,494,602,602,602,494,494,602,green)
                        player=1
                        screen[8] = 2
                time.sleep(1)
                if not win_pc_AI(screen, easy, player):
                        if draw_pc(screen,easy,player): 
                            run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO, gameeasy= True ,True, False, False, False, False, False, False, False
                            gamehard= False
                            continue                    
                elif win_pc_AI(screen, easy, player):                     
                    run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO,gameeasy = True ,True, False, False, False, False, False, False, False
                    gamehard = False
                    continue




        if difficulty == True:
            window.fill(black)
            desk()
            button('TicTacToe',bigfont,200,80)
            easyw, easyh = button('Easy',smallfont, window_width//4,window_height//2)
            hardw, hardh = button('Hard',smallfont, 3*window_width//4,window_height//2)
            difficult = button('Difficult',smallfont, window_width//2, window_height//3)

        while difficulty == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    difficulty = False
                    run = False
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if x >= (window_width//4)-(easyw//2) and x <= (window_width//4)+(easyw//2) and y >= (window_height//2) - (easyh//2)  and y<= (window_height//2)+(easyh//2):
                        gameeasy = True
                        gamehard = False
                        XO = True
                        difficulty = False
                    if x >= (3*window_width//4)-(hardw//2) and x <= (3*window_width//4)+(hardw//2) and y >= (window_height//2) - (hardh//2)  and y<= (window_height//2)+(hardh//2):
                        gamehard = True
                        gameeasy= False
                        XO = True
                        difficulty = False
        if XO == True:
            window.fill(black)
            desk()
            button('TicTacToe',bigfont,200,80)
            crossw, crossh = button('Cross',smallfont, window_width//4,window_height//2)
            circlew, circleh = button('Circle',smallfont, 3*window_width//4,window_height//2)
            difficult = button('Choose one',smallfont, window_width//2, window_height//3)

        while XO == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    XO = False
                    run = False
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if x >= (window_width//4)-(crossw//2) and x <= (window_width//4)+(crossw//2) and y >= (window_height//2) - (crossh//2)  and y<= (window_height//2)+(crossh//2):
                        human = 2
                        XO= False                        
                    if x >= (3*window_width//4)-(circlew//2) and x <= (3*window_width//4)+(circlew//2) and y >= (window_height//2) - (circleh//2)  and y<= (window_height//2)+(circleh//2):
                        human = 1
                        XO= False
                        
                        
                        
        if gameeasy == True:
            window.fill(black)
            desk()
            if human == player:
                display_message('You go first!', smallfont, screen)
            else:
                display_message('You go second!', smallfont,screen)

        while gameeasy == True:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameeasy = False
                    run = False
                if human == player:                    
                    if pygame.mouse.get_pressed() == (1,0,0):
                        x,y = pygame.mouse.get_pos()                        
                        if x <= 216 and y <= 216:
                            if player == 1:
                                if screen[0] == 0:
                                    circle(108,108,red)
                                    player=2                                
                                    screen[0] = 1
                            else:
                                if screen[0] == 0:
                                    cross(54,54,162,162,162,54,54,162,green)
                                    player=1                                
                                    screen[0] = 2
                        if x >= 224 and x <= 436 and y <= 216:
                            if player == 1:            
                                if screen[1] == 0:
                                    circle(328,108,red)
                                    player=2
                                    screen[1] = 1
                            else:
                                if screen[1] == 0:
                                    cross(274,54,382,162,382,54,274,162,green)
                                    player=1
                                    screen[1] = 2
                        if x >= 444 and x <= 660 and y <= 216:
                            if player == 1:
                                if screen[2] == 0:
                                    circle(548,108,red)
                                    player=2
                                    screen[2] = 1
                            else:                            
                                if screen[2] == 0:
                                    cross(494,54,602,162,602,54,494,162,green)
                                    player=1
                                    screen[2] = 2
                        if x <= 216 and y >= 216 and y <= 436:
                            if player == 1:                            
                                if screen[3] == 0:
                                    circle(108,328,red)
                                    player=2
                                    screen[3] = 1
                            else:                            
                                if screen[3] == 0:
                                    cross(54,274,162,382,162,274,54,382,green)
                                    player=1
                                    screen[3] = 2
                        if x >= 224 and x <= 436 and y >= 216 and y <= 436:
                            if player == 1:                            
                                if screen[4] == 0:
                                    circle(328,328,red)
                                    player=2
                                    screen[4] = 1
                            else:                            
                                if screen[4] == 0:
                                    cross(274,274,382,382,382,274,274,382,green)
                                    player=1
                                    screen[4] = 2
                        if x >= 444 and x <= 660 and y >= 216 and y <= 436:
                            if player==1:                            
                                if screen[5] == 0:
                                    circle(548,328,red)
                                    player=2
                                    screen[5] = 1
                            else:                            
                                if screen[5] == 0:
                                    cross(494,274,602,382,602,274,494,382,green)
                                    player=1
                                    screen[5] = 2
                        if x <= 216 and y >= 436:
                            if player == 1:                            
                                if screen[6] == 0:
                                    circle(108,548,red)
                                    player=2
                                    screen[6] = 1
                            else:                            
                                if screen[6] == 0:
                                    cross(54,494,162,602,162,494,54,602,green)
                                    player=1
                                    screen[6] = 2
                        if x >= 224 and x <= 436 and y >= 436:
                            if player == 1:                            
                                if screen[7] == 0:
                                    circle(328,548,red)
                                    player=2
                                    screen[7] = 1
                            else:                            
                                if screen[7] == 0:
                                    cross(274,494,382,602,382,494,274,602,green)
                                    player=1
                                    screen[7] = 2
                        if x >= 444 and x <= 660 and y >= 436:
                            if player == 1:                            
                                if screen[8] == 0:
                                    circle(548,548,red)
                                    player=2
                                    screen[8] = 1
                            else:                            
                                if screen[8] == 0:
                                    cross(494,494,602,602,602,494,494,602,green)
                                    player=1
                                    screen[8] = 2
                        if not win_pc(screen, human, player):
                            if draw_pc(screen,human,player):                            
                                run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO, gameeasy= True ,True, False, False, False, False, False, False, False                            
                                continue                    
                        elif win_pc(screen, human, player):                      
                            run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO,gameeasy = True ,True, False, False, False, False, False, False, False                  
                            continue
                else:
                    position = turn(screen)
                    if position == 0:
                        if player == 1:
                            circle(108,108,red)
                            player=2
                            if screen[0] == 0:
                                screen[0] = 1
                        else:
                            cross(54,54,162,162,162,54,54,162,green)
                            player=1
                            if screen[0] == 0:
                                screen[0] = 2

                    if position == 1:
                        if player == 1:            
                            if screen[1] == 0:
                                circle(328,108,red)
                                player=2
                                screen[1] = 1
                        else:
                            if screen[1] == 0:
                                cross(274,54,382,162,382,54,274,162,green)
                                player=1
                                screen[1] = 2
                    if position == 2:
                        if player == 1:
                            if screen[2] == 0:
                                circle(548,108,red)
                                player=2
                                screen[2] = 1
                        else:                            
                            if screen[2] == 0:
                                cross(494,54,602,162,602,54,494,162,green)
                                player=1
                                screen[2] = 2
                    if position == 3:
                        if player == 1:                            
                            if screen[3] == 0:
                                circle(108,328,red)
                                player=2
                                screen[3] = 1
                        else:                            
                            if screen[3] == 0:
                                cross(54,274,162,382,162,274,54,382,green)
                                player=1
                                screen[3] = 2
                    if position == 4:
                        if player == 1:                            
                            if screen[4] == 0:
                                circle(328,328,red)
                                player=2
                                screen[4] = 1
                        else:                            
                            if screen[4] == 0:
                                cross(274,274,382,382,382,274,274,382,green)
                                player=1
                                screen[4] = 2
                    if position == 5:
                        if player==1:                            
                            if screen[5] == 0:
                                circle(548,328,red)
                                player=2
                                screen[5] = 1
                        else:                            
                            if screen[5] == 0:
                                cross(494,274,602,382,602,274,494,382,green)
                                player=1
                                screen[5] = 2
                    if position == 6:
                        if player == 1:                            
                            if screen[6] == 0:
                                circle(108,548,red)
                                player=2
                                screen[6] = 1
                        else:                            
                            if screen[6] == 0:
                                cross(54,494,162,602,162,494,54,602,green)
                                player=1
                                screen[6] = 2
                    if position == 7:
                        if player == 1:                            
                            if screen[7] == 0:
                                circle(328,548,red)
                                player=2
                                screen[7] = 1
                        else:                            
                            if screen[7] == 0:
                                cross(274,494,382,602,382,494,274,602,green)
                                player=1
                                screen[7] = 2
                    if position == 8:
                        if player == 1:                            
                            if screen[8] == 0:
                                circle(548,548,red)
                                player=2
                                screen[8] = 1
                        else:                            
                            if screen[8] == 0:
                                cross(494,494,602,602,602,494,494,602,green)
                                player=1
                                screen[8] = 2
                    
                
                
                    if not win_pc(screen, human, player):
                        if not draw_pc(screen,human,player):
                            display = True
                            against = True
                            display_player(display,player,screen,against)
                        else:  
                            run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO, gameeasy= True ,True, False, False, False, False, False, False, False                            
                            continue                    
                    elif win_pc(screen, human, player):                      
                        run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO,gameeasy = True ,True, False, False, False, False, False, False, False                  
                        continue
                


        if gamehard == True:
            window.fill(black)
            desk()
            if human == player:
                display_message('You go first!', smallfont, screen)
            else:
                display_message('You go second!', smallfont,screen)

        while gamehard == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamehard = False
                    run = False
                if human == player:                    
                    if pygame.mouse.get_pressed() == (1,0,0):
                        x,y = pygame.mouse.get_pos()
                        if x <= 216 and y <= 216:
                            if player == 1:
                                if screen[0] == 0:
                                    circle(108,108,red)
                                    player=2                                
                                    screen[0] = 1
                            else:
                                if screen[0] == 0:
                                    cross(54,54,162,162,162,54,54,162,green)
                                    player=1                                
                                    screen[0] = 2
                        if x >= 224 and x <= 436 and y <= 216:
                            if player == 1:            
                                if screen[1] == 0:
                                    circle(328,108,red)
                                    player=2
                                    screen[1] = 1
                            else:
                                if screen[1] == 0:
                                    cross(274,54,382,162,382,54,274,162,green)
                                    player=1
                                    screen[1] = 2
                        if x >= 444 and x <= 660 and y <= 216:
                            if player == 1:
                                if screen[2] == 0:
                                    circle(548,108,red)
                                    player=2
                                    screen[2] = 1
                            else:                            
                                if screen[2] == 0:
                                    cross(494,54,602,162,602,54,494,162,green)
                                    player=1
                                    screen[2] = 2
                        if x <= 216 and y >= 216 and y <= 436:
                            if player == 1:                            
                                if screen[3] == 0:
                                    circle(108,328,red)
                                    player=2
                                    screen[3] = 1
                            else:                            
                                if screen[3] == 0:
                                    cross(54,274,162,382,162,274,54,382,green)
                                    player=1
                                    screen[3] = 2
                        if x >= 224 and x <= 436 and y >= 216 and y <= 436:
                            if player == 1:                            
                                if screen[4] == 0:
                                    circle(328,328,red)
                                    player=2
                                    screen[4] = 1
                            else:                            
                                if screen[4] == 0:
                                    cross(274,274,382,382,382,274,274,382,green)
                                    player=1
                                    screen[4] = 2
                        if x >= 444 and x <= 660 and y >= 216 and y <= 436:
                            if player==1:                            
                                if screen[5] == 0:
                                    circle(548,328,red)
                                    player=2
                                    screen[5] = 1
                            else:                            
                                if screen[5] == 0:
                                    cross(494,274,602,382,602,274,494,382,green)
                                    player=1
                                    screen[5] = 2
                        if x <= 216 and y >= 436:
                            if player == 1:                            
                                if screen[6] == 0:
                                    circle(108,548,red)
                                    player=2
                                    screen[6] = 1
                            else:                            
                                if screen[6] == 0:
                                    cross(54,494,162,602,162,494,54,602,green)
                                    player=1
                                    screen[6] = 2
                        if x >= 224 and x <= 436 and y >= 436:
                            if player == 1:                            
                                if screen[7] == 0:
                                    circle(328,548,red)
                                    player=2
                                    screen[7] = 1
                            else:                            
                                if screen[7] == 0:
                                    cross(274,494,382,602,382,494,274,602,green)
                                    player=1
                                    screen[7] = 2
                        if x >= 444 and x <= 660 and y >= 436:
                            if player == 1:                            
                                if screen[8] == 0:
                                    circle(548,548,red)
                                    player=2
                                    screen[8] = 1
                            else:                            
                                if screen[8] == 0:
                                    cross(494,494,602,602,602,494,494,602,green)
                                    player=1
                                    screen[8] = 2
                        if not win_pc(screen, human, player):
                            if draw_pc(screen,human,player):                            
                                run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO, gameeasy= True ,True, False, False, False, False, False, False, False
                                gamehard= False
                                continue                    
                        elif win_pc(screen, human, player):                      
                            run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO,gameeasy = True ,True, False, False, False, False, False, False, False
                            gamehard= False
                            continue
                else:
                    position=win_condition(screen,human, player)
                    if position == -1:
                        position = no_lose(screen,human,player)
                    if position == -1:
                        position = best_choice(screen,human)
                    if position == 0:
                        if player == 1:
                            circle(108,108,red)
                            player=2                                
                            screen[0] = 1
                        else:
                            cross(54,54,162,162,162,54,54,162,green)
                            player=1                                
                            screen[0] = 2
                    if position == 1:
                        if player == 1:                           
                            circle(328,108,red)
                            player=2
                            screen[1] = 1
                        else:
                            cross(274,54,382,162,382,54,274,162,green)
                            player=1
                            screen[1] = 2
                    if position == 2:
                        if player == 1:
                            circle(548,108,red)
                            player=2
                            screen[2] = 1
                        else:
                            cross(494,54,602,162,602,54,494,162,green)
                            player=1
                            screen[2] = 2
                    if position == 3:
                        if player == 1:
                            circle(108,328,red)
                            player=2
                            screen[3] = 1
                        else:
                            cross(54,274,162,382,162,274,54,382,green)
                            player=1
                            screen[3] = 2
                    if position == 4:
                        if player == 1:
                            circle(328,328,red)
                            player=2
                            screen[4] = 1
                        else:
                            cross(274,274,382,382,382,274,274,382,green)
                            player=1
                            screen[4] = 2
                    if position == 5:
                        if player==1:
                            circle(548,328,red)
                            player=2
                            screen[5] = 1
                        else:
                            cross(494,274,602,382,602,274,494,382,green)
                            player=1
                            screen[5] = 2
                    if position == 6:
                        if player == 1:
                            circle(108,548,red)
                            player=2
                            screen[6] = 1
                        else:
                            cross(54,494,162,602,162,494,54,602,green)
                            player=1
                            screen[6] = 2
                    if position == 7:
                        if player == 1:
                            circle(328,548,red)
                            player=2
                            screen[7] = 1
                        else:
                            cross(274,494,382,602,382,494,274,602,green)
                            player=1
                            screen[7] = 2
                    if position == 8:
                        if player == 1:
                            circle(548,548,red)
                            player=2
                            screen[8] = 1
                        else:
                            cross(494,494,602,602,602,494,494,602,green)
                            player=1
                            screen[8] = 2
                    if not win_pc(screen, human, player):
                            if not draw_pc(screen,human,player):
                                display = True
                                against = True
                                display_player(display,player,screen,against)
                            else:  
                                run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO, gameeasy= True ,True, False, False, False, False, False, False, False
                                gamehard= False
                                continue                    
                    elif win_pc(screen, human, player):                     
                        run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO,gameeasy = True ,True, False, False, False, False, False, False, False
                        gamehard = False
                        continue




        if gameHumanvHuman == True:
            desk()
            against=False
            display_player(display,player,screen,against)
        while gameHumanvHuman:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameHumanvHuman = False
                    run = False
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if x <= 216 and y <= 216:
                        if player == 1:
                            if screen[0] == 0:
                                circle(108,108,red)
                                player=2                            
                                screen[0] = 1
                        else:
                            if screen[0] == 0:
                                cross(54,54,162,162,162,54,54,162,green)
                                player=1                            
                                screen[0] = 2
                    if x >= 224 and x <= 436 and y <= 216:
                        if player == 1:            
                            if screen[1] == 0:
                                circle(328,108,red)
                                player=2
                                screen[1] = 1
                        else:
                            if screen[1] == 0:
                                cross(274,54,382,162,382,54,274,162,green)
                                player=1
                                screen[1] = 2
                    if x >= 444 and x <= 660 and y <= 216:
                        if player == 1:
                            if screen[2] == 0:
                                circle(548,108,red)
                                player=2
                                screen[2] = 1
                        else:                            
                            if screen[2] == 0:
                                cross(494,54,602,162,602,54,494,162,green)
                                player=1
                                screen[2] = 2
                    if x <= 216 and y >= 216 and y <= 436:
                        if player == 1:                            
                            if screen[3] == 0:
                                circle(108,328,red)
                                player=2
                                screen[3] = 1
                        else:                            
                            if screen[3] == 0:
                                cross(54,274,162,382,162,274,54,382,green)
                                player=1
                                screen[3] = 2
                    if x >= 224 and x <= 436 and y >= 216 and y <= 436:
                        if player == 1:                            
                            if screen[4] == 0:
                                circle(328,328,red)
                                player=2
                                screen[4] = 1
                        else:                            
                            if screen[4] == 0:
                                cross(274,274,382,382,382,274,274,382,green)
                                player=1
                                screen[4] = 2
                    if x >= 444 and x <= 660 and y >= 216 and y <= 436:
                        if player==1:                            
                            if screen[5] == 0:
                                circle(548,328,red)
                                player=2
                                screen[5] = 1
                        else:                            
                            if screen[5] == 0:
                                cross(494,274,602,382,602,274,494,382,green)
                                player=1
                                screen[5] = 2
                    if x <= 216 and y >= 436:
                        if player == 1:                            
                            if screen[6] == 0:
                                circle(108,548,red)
                                player=2
                                screen[6] = 1
                        else:                            
                            if screen[6] == 0:
                                cross(54,494,162,602,162,494,54,602,green)
                                player=1
                                screen[6] = 2
                    if x >= 224 and x <= 436 and y >= 436:
                        if player == 1:                            
                            if screen[7] == 0:
                                circle(328,548,red)
                                player=2
                                screen[7] = 1
                        else:                            
                            if screen[7] == 0:
                                cross(274,494,382,602,382,494,274,602,green)
                                player=1
                                screen[7] = 2
                    if x >= 444 and x <= 660 and y >= 436:
                        if player == 1:                            
                            if screen[8] == 0:
                                circle(548,548,red)
                                player=2
                                screen[8] = 1
                        else:                            
                            if screen[8] == 0:
                                cross(494,494,602,602,602,494,494,602,green)
                                player=1
                                screen[8] = 2                            
                    display == True
                    against = False
                    if not win(screen):
                        if not draw(screen):
                            time.sleep(0.5)
                            display_player(display,player,screen,against)
                        else:
                            run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO, gameeasy = True ,True, False, False, False, False, False, False,False
                            continue
                    elif win(screen):                      
                        run, title, settings, gameAIvAI,gameHumanvAI,gameHumanvHuman, difficulty, XO,gameeasy = True ,True, False, False, False, False, False, False,False
                        continue






game_loop(True,True,False,False,False,False,False, False, False)
pygame.quit()
