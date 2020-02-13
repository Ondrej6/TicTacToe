import pygame, random, time
pygame.init()

# inicializacia a nastavneie zakladnych údajov
## sirka a vyska okna
window_width=660
window_height=660

## nastavenie farby
green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)

## nastavenie parametrov pre jednotlive tvary
circle0=108,108
circle1=328,108
circle2=548,108
circle3=108,328
circle4=328,328
circle5=548,328
circle6=108,548
circle7=328,548
circle8=548,548

cross0=54,54,162,162,162,54,54,162 
cross1=274,54,382,162,382,54,274,162
cross2=494,54,602,162,602,54,494,162
cross3=54,274,162,382,162,274,54,382
cross4=274,274,382,382,382,274,274,382
cross5=494,274,602,382,602,274,494,382
cross6=54,494,162,602,162,494,54,602
cross7=274,494,382,602,382,494,274,602
cross8=494,494,602,602,602,494,494,602

## nastavenie fontov
bigfont = pygame.font.SysFont("comicsansms", 72)
smallfont = pygame.font.SysFont("comicsansms", 36)

## nastavenie parametrov okna
window=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('TicTacToe')

def check_win(screen,who): # kontrola vyhry
    if ((screen[0]== who and screen[0]== screen[1] and screen[0] == screen[2])
    or (screen[3]== who and screen[3]== screen[4] and screen[3] == screen[5])
    or (screen[6]== who and screen[6]== screen[7] and screen[6] == screen[8]) 
    or (screen[0]== who and screen[0]== screen[3] and screen[0] == screen[6]) 
    or (screen[1]== who and screen[1]== screen[4] and screen[1] == screen[7]) 
    or (screen[2]== who and screen[2]== screen[5] and screen[2] == screen[8]) 
    or (screen[0]== who and screen[0] == screen[4] and screen[0] == screen[8]) 
    or (screen[2]== who and screen[2]== screen[4] and screen[2] == screen[6])):
        return True
    else:
        return False

def best_choice(screen,human): # vyberie najlepsiu poziciu pre pocitac
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

def win_condition(screen,human, player): # najde vyherny tah
    next=screen.copy()
    for position in range(len(next)):
        if next[position]== 0:
            next[position] = player
        if win(next, 3, player,human):
            return position
        else:
            next=screen.copy()
    return -1

def win(screen, who, player1 = None, player2 = None): # urci vitaza
    if who == 0:
        if player1 == 2:
            if player1 == player2:
                if check_win(screen,1):
                    display_message('Computer 1 won!',bigfont,screen)
                    return True

            elif player1 != player2: 
                if check_win(screen,2):
                    display_message('Computer 2 won!',bigfont,screen)
                    return True
            else:
                return False
        if player1 == 1:
            if player1 == player2:
                if check_win(screen,2):
                    display_message('Computer 2 won!',bigfont,screen)
                    return True

            elif player1 != player2: 
                if check_win(screen,1):
                    display_message('Computer 1 won!',bigfont,screen)
                    return True
            else:
                return False        

    if who == 1:
        if player1 == 2:
            if player1 == player2:
                if check_win(screen,1):
                    display_message('You lost!',bigfont,screen)
                    return True

            elif player1 != player2: 
                if check_win(screen,2):
                    display_message('You won!',bigfont,screen)
                    return True
            else:
                return False
        if player1 == 1:
            if player1 == player2:
                if check_win(screen,2):
                    display_message('You lost!',bigfont,screen)
                    return True

            elif player1 != player2: 
                if check_win(screen,1):
                    display_message('You won!',bigfont,screen)
                    return True
            else:
                return False

    if who == 2:
        if check_win(screen,1):
            display_message(f'Player 1 won!',bigfont,screen)
            return True

        elif  check_win(screen,2):
            display_message(f'Player 2 won!',bigfont,screen)
            return True
        else:
            return False

    if who == 3:
        if check_win(screen,1):
            return True
        elif check_win(screen,2):
            return True
        else:
            return False

def draw(screen): # vypise 'remiza' pri hre medzi dvoma hracmi
    if 0 not in screen and not win(screen,3):
        display_message(f'Draw!',bigfont,screen)
        return True
    else:
        return False

def turn(screen): # nahodny tah pocitaca
    while True:
        position = random.randint(0,8)
        if screen[position] == 0:
            return position

def menu():   # nakresli menu
    desk()
    button('TicTacToe',bigfont,200,80)
    button('Play',smallfont, window_width//2, window_height//2)
    pygame.display.update()

def text_objects(text, font): 
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def button(text,font, width, height): # vytvori blok na tlacitko
    TextSurf, TextRect = text_objects(text,font)
    TextRect.center = (width, height)
    window.blit(TextSurf, TextRect)
    pygame.display.update()
    return font.size(text)

def display_message(text,font,screen): # vypise spravu
    TextSurf, TextRect = text_objects(text,font)
    TextRect.center = ((window_width/2),(window_height/2))
    window.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)    
    draw_screen(screen)

def display_player(display,player,screen, against): # vypise kto je na tahu
    if display:
        if not against: 
            display_message(f'Player {player}',bigfont,screen)
        else:
            display_message('Your turn!',bigfont,screen)

def circle(x,y,color): # nakresli kruh
    pygame.draw.circle(window,color,(x,y),54,10)
    pygame.display.update()

def cross(sx1,sy1,ex1,ey1,sx2,sy2,ex2,ey2,color): # nakresli krizik
    pygame.draw.line(window,color,(sx1,sy1),(ex1,ey1),8)
    pygame.draw.line(window,color,(sx2,sy2),(ex2,ey2),8)
    pygame.display.update()

def desk(): # nakresli hraciu dosku
    window.fill(black)
    pygame.draw.line(window,(0,0,255),(220,0),(220,660),8)
    pygame.draw.line(window,(0,0,255),(440,0),(440,660),8)
    pygame.draw.line(window,(0,0,255),(0,220),(660,220),8)
    pygame.draw.line(window,(0,0,255),(0,440),(660,440),8)
    pygame.display.update()

def draw_screen(screen): # nakresli dosku aj s uz zahranymi tahmi
    window.fill(black)
    desk()
    if screen[0] == 1:
        circle(circle0[0],circle0[1],red)
    if screen[0] == 2:
        cross(cross0[0],cross0[1],cross0[2],cross0[3],cross0[4],cross0[5],cross0[6],cross0[7],green)
    if screen[1] == 1:
        circle(circle1[0],circle1[1],red)
    if screen[1] == 2:
        cross(cross1[0],cross1[1],cross1[2],cross1[3],cross1[4],cross1[5],cross1[6],cross1[7],green)
    if screen[2] == 1:
        circle(circle2[0],circle2[1],red)
    if screen[2] == 2:
        cross(cross2[0],cross2[1],cross2[2],cross2[3],cross2[4],cross2[5],cross2[6],cross2[7],green)
    if screen[3] == 1:
        circle(circle3[0],circle3[1],red)
    if screen[3] == 2:
        cross(cross3[0],cross3[1],cross3[2],cross3[3],cross3[4],cross3[5],cross3[6],cross3[7],green)
    if screen[4] == 1:
        circle(circle4[0],circle4[1],red)
    if screen[4] == 2:
        cross(cross4[0],cross4[1],cross4[2],cross4[3],cross4[4],cross4[5],cross4[6],cross4[7],green)
    if screen[5] == 1:
        circle(circle5[0],circle5[1],red)
    if screen[5] == 2:
        cross(cross5[0],cross5[1],cross5[2],cross5[3],cross5[4],cross5[5],cross5[6],cross5[7],green)
    if screen[6] == 1:
        circle(circle6[0],circle6[1],red)
    if screen[6] == 2:
        cross(cross6[0],cross6[1],cross6[2],cross6[3],cross6[4],cross6[5],cross6[6],cross6[7],green)
    if screen[7] == 1:
        circle(circle7[0],circle7[1],red)
    if screen[7] == 2:
        cross(cross7[0],cross7[1],cross7[2],cross7[3],cross7[4],cross7[5],cross7[6],cross7[7],green)
    if screen[8] == 1:
        circle(circle8[0],circle8[1],red)
    if screen[8] == 2:
        cross(cross8[0],cross8[1],cross8[2],cross8[3],cross8[4],cross8[5],cross8[6],cross8[7],green)

def one_turn(screen, player,x,y): # tah hraca
    if player == 1:
        if x <= window_width//3 and y <= window_height//3:
            if screen[0] == 0:
                    circle(circle0[0],circle0[1],red)
                    player=2                                
                    screen[0] = 1
        if window_width//3 <= x <= (2 * window_width)//3 and y <= window_height//3:
            if screen[1] == 0:
                circle(circle1[0],circle1[1],red)
                player=2
                screen[1] = 1
        if (2*window_width)//3 <= x <= window_width and y <= window_height//3:
            if screen[2] == 0:
                circle(circle2[0],circle2[1],red)
                player=2
                screen[2] = 1
        if x <= window_width//3 and window_height // 3 <= y <= (2 * window_height) // 3:
            if screen[3] == 0:
                circle(circle3[0],circle3[1],red)
                player=2
                screen[3] = 1
        if window_width // 3 <= x <= (2 * window_width) // 3 and window_height // 3 <= y <= (2 * window_height) // 3:
            if screen[4] == 0:
                circle(circle4[0],circle4[1],red)
                player=2
                screen[4] = 1
        if (2 * window_width) // 3 <= x <= window_width and window_height // 3 <= y <= (2 * window_height) // 3:
            if screen[5] == 0:
                circle(circle5[0],circle5[1],red)
                player=2
                screen[5] = 1
        if x <= window_width//3 and y >= (2*window_height)//3:
            if screen[6] == 0:
                circle(circle6[0],circle6[1],red)
                player=2
                screen[6] = 1
        if (2*window_width)//3 >= x >= window_height//3 and y >= (2 * window_height)//3:
            if screen[7] == 0:
                circle(circle7[0],circle7[1],red)
                player=2
                screen[7] = 1
        if (2*window_width)//3 <= x <= window_width and y >= (2 * window_height)//3:
            if screen[8] == 0:
                circle(circle8[0],circle8[1],red)
                player=2
                screen[8] = 1
    else:
        if x <= window_width//3 and y <= window_height//3:
            if screen[0] == 0:
                cross(cross0[0],cross0[1],cross0[2],cross0[3],cross0[4],cross0[5],cross0[6],cross0[7],green)
                player=1                                
                screen[0] = 2
        if window_width//3 <= x <= (2 * window_width)//3 and y <= window_height//3:
            if screen[1] == 0:
                cross(cross1[0],cross1[1],cross1[2],cross1[3],cross1[4],cross1[5],cross1[6],cross1[7],green)
                player=1
                screen[1] = 2
        if (2*window_width)//3 <= x <= window_width and y <= window_height//3:
            if screen[2] == 0:
                cross(cross2[0],cross2[1],cross2[2],cross2[3],cross2[4],cross2[5],cross2[6],cross2[7],green)
                player=1
                screen[2] = 2
        if x <= window_width//3 and window_height // 3 <= y <= (2 * window_height) // 3:
            if screen[3] == 0:
                cross(cross3[0],cross3[1],cross3[2],cross3[3],cross3[4],cross3[5],cross3[6],cross3[7],green)
                player=1
                screen[3] = 2
        if window_width // 3 <= x <= (2 * window_width) // 3 and window_height // 3 <= y <= (2 * window_height) // 3:
            if screen[4] == 0:
                cross(cross4[0],cross4[1],cross4[2],cross4[3],cross4[4],cross4[5],cross4[6],cross4[7],green)
                player=1
                screen[4] = 2
        if (2 * window_width) // 3 <= x <= window_width and window_height // 3 <= y <= (2 * window_height) // 3:
            if screen[5] == 0:
                cross(cross5[0],cross5[1],cross5[2],cross5[3],cross5[4],cross5[5],cross5[6],cross5[7],green)
                player=1
                screen[5] = 2
        if x <= window_width//3 and y >= (2*window_height)//3:
            if screen[6] == 0:
                cross(cross6[0],cross6[1],cross6[2],cross6[3],cross6[4],cross6[5],cross6[6],cross6[7],green)
                player=1
                screen[6] = 2
        if (2*window_width)//3 >= x >= window_height//3 and y >= (2 * window_height)//3:
            if screen[7] == 0:
                cross(cross7[0],cross7[1],cross7[2],cross7[3],cross7[4],cross7[5],cross7[6],cross7[7],green)
                player=1
                screen[7] = 2
        if (2*window_width)//3 <= x <= window_width and y >= (2 * window_height)//3:
            if screen[8] == 0:
                cross(cross8[0],cross8[1],cross8[2],cross8[3],cross8[4],cross8[5],cross8[6],cross8[7],green)
                player=1
                screen[8] = 2
    return screen, player

def one_turn_pc(screen, player, position): # tah pocitacu
    if player == 1:
        if position == 0:
            if screen[0] == 0:
                circle(circle0[0],circle0[1],red)
                player=2                        
                screen[0] = 1
        elif position == 1:
            if screen[1] == 0:
                circle(circle1[0],circle1[1],red)
                player=2
                screen[1] = 1
        elif position == 2:
            if screen[2] == 0:
                circle(circle2[0],circle2[1],red)
                player=2
                screen[2] = 1
        elif position == 3:
            if screen[3] == 0:
                circle(circle3[0],circle3[1],red)
                player=2
                screen[3] = 1
        elif position == 4:
            if screen[4] == 0:
                circle(circle4[0],circle4[1],red)
                player=2
                screen[4] = 1
        elif position == 5:
            if screen[5] == 0:
                circle(circle5[0],circle5[1],red)
                player=2
                screen[5] = 1
        elif position == 6:
            if screen[6] == 0:
                circle(circle6[0],circle6[1],red)
                player=2
                screen[6] = 1
        elif position == 7:
            if screen[7] == 0:
                circle(circle7[0],circle8[1],red)
                player=2
                screen[7] = 1
        elif position == 8:
            if screen[8] == 0:
                circle(circle8[0],circle8[1],red)
                player=2
                screen[8] = 1
    else:
            if position == 0:
                if screen[0] == 0:
                    cross(cross0[0],cross0[1],cross0[2],cross0[3],cross0[4],cross0[5],cross0[6],cross0[7],green)
                    player=1                      
                    screen[0] = 2
            elif position == 1:
                if screen[1] == 0:
                    cross(cross1[0],cross1[1],cross1[2],cross1[3],cross1[4],cross1[5],cross1[6],cross1[7],green)
                    player=1
                    screen[1] = 2
            elif position == 2:
                if screen[2] == 0:
                    cross(cross2[0],cross2[1],cross2[2],cross2[3],cross2[4],cross2[5],cross2[6],cross2[7],green)
                    player=1
                    screen[2] = 2
            elif position == 3:
                if screen[3] == 0:
                    cross(cross3[0],cross3[1],cross3[2],cross3[3],cross3[4],cross3[5],cross3[6],cross3[7],green)
                    player=1
                    screen[3] = 2
            elif position == 4:
                if screen[4] == 0:
                    cross(cross4[0],cross4[1],cross4[2],cross4[3],cross4[4],cross4[5],cross4[6],cross4[7],green)
                    player=1
                    screen[4] = 2
            elif position == 5:
                if screen[5] == 0:
                    cross(cross5[0],cross5[1],cross5[2],cross5[3],cross5[4],cross5[5],cross5[6],cross5[7],green)
                    player=1
                    screen[5] = 2
            elif position == 6:
                if screen[6] == 0:
                    cross(cross6[0],cross6[1],cross6[2],cross6[3],cross6[4],cross6[5],cross6[6],cross6[7],green)
                    player=1
                    screen[6] = 2
            elif position == 7:
                if screen[7] == 0:
                    cross(cross7[0],cross7[1],cross7[2],cross7[3],cross7[4],cross7[5],cross7[6],cross7[7],green)
                    player=1
                    screen[7] = 2
            elif position == 8:
                if screen[8] == 0:
                    cross(cross8[0],cross8[1],cross8[2],cross8[3],cross8[4],cross8[5],cross8[6],cross8[7],green)
                    player=1
                    screen[8] = 2
    return screen, player
        

def who_goes_first(): # nahodne urci kto zacina
    player= random.randint(1,2)
    return player

def game_loop(run): # cyklus samotnej hry
    while run:
        title= True
        gameAIvAI = False
        gameHumanvHuman = False
        difficulty = False
        XO = False
        gameeasy = False        
        gamehard = False
        display = True

        player=who_goes_first()
        screen=[0,0,0,0,0,0,0,0,0]

        # uvodne menu
        if title:
            menu()
        while title:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    title = False 
                    run = False
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y= pygame.mouse.get_pos()
                    if (window_width // 2) - 60 <= x <= (window_width // 2) + 60 and (window_height // 2) - 20 <= y <= (
                            window_height // 2) + 20:
                        settings= True
                        title = False

        # vyber moznosti hry
        if settings:
            window.fill(black)
            desk()
            button('TicTacToe',bigfont,200,80)
            AIvAIw, AIvAIh = button('AI vs AI',smallfont, window_width//4,window_height//4)            
            HumanvAIw, HumanvAIh = button('Human vs AI',smallfont, 2*window_width//4,2*window_height//4)            
            HumanvHumanw, HumanvHumanh = button('Human vs Human',smallfont, 3*window_width//4,3*window_height//4)            

        while settings:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settings= False
                    run = False
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (window_width // 4) - (AIvAIw // 2) <= x <= (window_width // 4) + (AIvAIw // 2) and (
                            window_height // 4) - (AIvAIh // 2) <= y <= (window_height // 4) + (AIvAIh // 2):
                        gameAIvAI = True
                        settings = False
                    if (2 * window_width // 4) - (HumanvAIw // 2) <= x <= (2 * window_width // 4) + (
                            HumanvAIw // 2) and (2 * window_height // 4) - (HumanvAIh // 2) <= y <= (
                            2 * window_height // 4) + (HumanvAIh // 2):
                        difficulty = True
                        settings = False
                    if (3 * window_width // 4) - (HumanvHumanw // 2) <= x <= (3 * window_width // 4) + (
                            HumanvHumanw // 2) and (3 * window_height // 4) - (HumanvHumanh // 2) <= y <= (
                            3 * window_height // 4) + (HumanvHumanh // 2):
                        gameHumanvHuman = True
                        settings = False

        # hra dvoch pocitacov
        if gameAIvAI:
            window.fill(black)
            desk()
            if player == 1:
                display_message('Circle go first!', smallfont, screen)
            else:
                display_message('Cross go first!', smallfont,screen)
            easy=random.randint(1,2)

        while gameAIvAI:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameAIvAI = False
                    run = False
            if easy == player:
                position = turn(screen)
                if player == 1:
                    screen, player = one_turn_pc(screen, player, position)
                else:
                    screen, player = one_turn_pc(screen, player, position)
                if not win(screen, 0, easy, player):
                        if draw(screen):                            
                            run, title, settings, gameAIvAI,gameHumanvHuman, difficulty, XO,gameeasy, gamehard = True ,True, False, False, False, False, False,False, False                            
                            continue                    
                elif win(screen, 0, easy, player):                      
                        run, title, settings, gameAIvAI,gameHumanvHuman, difficulty, XO,gameeasy, gamehard = True ,True, False, False, False, False, False,False, False                  
                        continue
                time.sleep(1)
            else:
                position=win_condition(screen,easy, player)
                if position == -1:
                    position = win_condition(screen,player, easy)
                if position == -1:
                    position = best_choice(screen,easy)
                if player == 1:
                    screen, player = one_turn_pc(screen, player, position)
                else:
                    screen, player = one_turn_pc(screen, player, position)       
                time.sleep(1)
                if not win(screen, 0, easy, player):
                        if draw(screen): 
                            run, title, settings, gameAIvAI,gameHumanvHuman, difficulty, XO,gameeasy, gamehard = True ,True, False, False,False, False, False,False, False
                            continue                    
                elif win(screen, 0, easy, player):                     
                    run, title, settings, gameAIvAI,gameHumanvHuman, difficulty, XO,gameeasy, gamehard = True ,True, False, False, False, False, False,False, False
                    continue

        # nastavenie obtiaznosti
        if difficulty:
            window.fill(black)
            desk()
            button('TicTacToe',bigfont,200,80)
            easyw, easyh = button('Easy',smallfont, window_width//4,window_height//2)
            hardw, hardh = button('Hard',smallfont, 3*window_width//4,window_height//2)

        while difficulty:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    difficulty = False
                    run = False
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (window_width // 4) - (easyw // 2) <= x <= (window_width // 4) + (easyw // 2) and (
                            window_height // 2) - (easyh // 2) <= y <= (window_height // 2) + (easyh // 2):
                        gameeasy = True
                        gamehard = False
                        XO = True
                        difficulty = False
                    if (3 * window_width // 4) - (hardw // 2) <= x <= (3 * window_width // 4) + (hardw // 2) and (
                            window_height // 2) - (hardh // 2) <= y <= (window_height // 2) + (hardh // 2):
                        gamehard = True
                        gameeasy= False
                        XO = True
                        difficulty = False

        # vyber za ktory tvar bude hrac hrat
        if XO:
            window.fill(black)
            desk()
            button('TicTacToe',bigfont,200,80)
            crossw, crossh = button('Cross',smallfont, window_width//4,window_height//2)
            circlew, circleh = button('Circle',smallfont, 3*window_width//4,window_height//2)

        while XO:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    XO = False
                    run = False
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (window_width // 4) - (crossw // 2) <= x <= (window_width // 4) + (crossw // 2) and (
                            window_height // 2) - (crossh // 2) <= y <= (window_height // 2) + (crossh // 2):
                        human = 2
                        XO= False                        
                    if (3 * window_width // 4) - (circlew // 2) <= x <= (3 * window_width // 4) + (circlew // 2) and (
                            window_height // 2) - (circleh // 2) <= y <= (window_height // 2) + (circleh // 2):
                        human = 1
                        XO= False
                        
                        
        # lahka hra proti pocitacu              
        if gameeasy:
            window.fill(black)
            desk()
            if human == player:
                display_message('You go first!', smallfont, screen)
            else:
                display_message('You go second!', smallfont,screen)

        while gameeasy:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameeasy = False
                    run = False
                if human == player:                    
                    if pygame.mouse.get_pressed() == (1,0,0):
                        x,y = pygame.mouse.get_pos()
                        
                        if player == 1:
                            screen, player = one_turn(screen, player,x,y)
                        else:
                            screen, player = one_turn(screen, player,x,y)
                        if not win(screen, 1, human, player):
                            if draw(screen):                            
                                run, title, settings, gameAIvAI,gameHumanvHuman, difficulty, XO,gameeasy, gamehard = True ,True, False, False, False, False, False,False, False                            
                                continue                    
                        elif win(screen, 1, human, player):                      
                            run, title, settings, gameAIvAI,gameHumanvHuman, difficulty, XO,gameeasy, gamehard = True ,True, False, False, False, False, False,False, False                  
                            continue
                else:
                    position = turn(screen)
                    if player == 1:
                        screen, player = one_turn_pc(screen, player, position)
                    else:
                        screen, player = one_turn_pc(screen, player, position)         
                                
                    if not win(screen, 1, human, player):
                        if not draw(screen):
                            display = True
                            against = True
                            display_player(display,player,screen,against)
                        else:  
                            run, title, settings, gameAIvAI,gameHumanvHuman, difficulty, XO,gameeasy, gamehard = True ,True, False, False, False, False, False,False, False                            
                            continue                    
                    elif win(screen, 1, human, player):                      
                        run, title, settings, gameAIvAI,gameHumanvHuman, difficulty, XO,gameeasy, gamehard = True ,True, False, False, False, False, False,False, False                  
                        continue

        # hra proti narocnej obtiaznosti
        if gamehard:
            window.fill(black)
            desk()
            if human == player:
                display_message('You go first!', smallfont, screen)
            else:
                display_message('You go second!', smallfont,screen)

        while gamehard:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamehard = False
                    run = False
                if human == player:                    
                    if pygame.mouse.get_pressed() == (1,0,0):
                        x,y = pygame.mouse.get_pos()
                        
                        if player == 1:
                            screen, player = one_turn(screen, player,x,y)
                        else:
                            screen, player = one_turn(screen, player,x,y)
                        if not win(screen, 1, human, player):
                            if draw(screen):                            
                                run, title, settings, gameAIvAI,gameHumanvHuman, difficulty, XO,gameeasy, gamehard = True ,True, False, False, False, False, False,False, False
                                continue                    
                        elif win(screen, 1, human, player):                      
                            run, title, settings, gameAIvAI,gameHumanvHuman, difficulty, XO,gameeasy, gamehard = True ,True, False, False, False, False, False,False, False
                            continue
                else:
                    position=win_condition(screen,human, player)
                    if position == -1:
                        position = win_condition(screen,player, human)
                    if position == -1:
                        position = best_choice(screen,human)
                    if player == 1:
                        screen, player = one_turn_pc(screen, player, position)
                    else:
                        screen, player = one_turn_pc(screen, player, position)
                    if not win(screen, 1, human, player):
                            if not draw(screen):
                                display = True
                                against = True
                                display_player(display,player,screen,against)
                            else:  
                                run, title, settings, gameAIvAI,gameHumanvHuman, difficulty, XO,gameeasy, gamehard = True ,True, False, False, False, False, False,False, False
                                continue                    
                    elif win(screen, 1, human, player):                     
                        run, title, settings, gameAIvAI,gameHumanvHuman, difficulty, XO,gameeasy, gamehard = True ,True, False, False, False, False, False,False, False
                        continue

        # hra dvoch ludi
        if gameHumanvHuman:
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

                    if player == 1:
                        screen, player = one_turn(screen, player,x,y)
                    else:
                        screen, player = one_turn(screen, player,x,y)                       
                    display = True
                    against = False
                    if not win(screen, 2):
                        if not draw(screen):
                            time.sleep(0.5)
                            display_player(display,player,screen,against)
                        else:
                            run, title, settings, gameAIvAI,gameHumanvHuman, difficulty, XO,gameeasy, gamehard = True ,True, False, False, False, False, False,False, False
                            continue
                    elif win(screen,2):                      
                        run, title, settings, gameAIvAI,gameHumanvHuman, difficulty, XO,gameeasy, gamehard = True ,True, False, False, False, False, False,False, False
                        continue

# spustenie aplikacie
game_loop(True)
pygame.quit()
