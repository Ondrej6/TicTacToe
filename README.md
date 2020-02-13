# TicTacToe
TicTacToe alebo piškvorky je klasická hra pre dvoch hráčov. V tejto variante si uživateľ môže vybrať, či chce hrať proti druhému užívateľovi alebo proti počítaču. Taktiež je možnosť simulovať hru počítaču proti samému sebe.
Úroveň počítaču sa dá zvoliť z dvoch možností - optimálny súper, slabý súper

## Cieľ
Cieľom tohto zápočtového programu je vytvorenie funkčnej hry TicTacToe

## Požiadavky
- Pygame - grafické zobrazenie a beh samotnej hry
- Random - náhodné určovanie ťahov a poradia hráčov
- Time - využitie funkcie sleep

## Ovládanie 
Pomocou myšky

## Použitie
Pre hru spustite [Main.py](Main.py)
Otvorí sa okno programu s hlavným menu

<img src="img/menu.png" width="660" height="660" />

Po kliknutí na play dostanete na výber na výber z troch možností:
- AI vs AI: hra dvoch počítačov
- Human vs AI: hra užívateľa proti počítaču
- Human vs Human: hra dvoch užívateľov

Hru je možné kedykoľvek ukončiť kliknutím na krížik v pravom hornom rohu okna.

### AIvsAI
Nasimuluje hru dvoch rôznych obtiažností.
Počítač s ľahkou obtiažnosťou vyberá svoje ťahy náhodne. Tento ťah určuje funkcia turn. Táto funkcia vráti pozíciu na hracej ploche, na ktorú uskutoční svoj ťah

```
def turn(screen):
    while True:
        position = random.randint(0,8)
        if screen[position] == 0:
            return position
```
Počítač s náročnou obtiažnosťou sa snaží nájsť najvhodnejší ťah.
Na tento ťah využíva počítač dve funkcie win_condition a best_choice.

Win_condition kontroluje či existuje vyherný ťah či už pre daný počítač alebo pre súpera. Ak takýto ťah neexistuje tak funkcia vráti hodnotu -1, inak vráti pozíciu na hracej ploche

```
def win_condition(screen,human, player):
    next=screen.copy()
    for position in range(len(next)):
        if next[position]== 0:
            next[position] = player
        if win(next, 3, player,human):
            return position
        else:
            next=screen.copy()
    return -1
```

Best_choice sa spúšťa len v prípade ak funkcia win_condition vráti hodnotu -1. Táto funkcia vyberá vhodný ťah z voľných políčok. 
Prvé dve podmienky určujú, aký ťah má počítač zahrať pri špecifických situáciach. Zvyšok funkcie vyberá náhodné políčko na základe priradenia hodnôt jednotlivým políčkam. Pozície 0,2,6,8 majú najvyššiu hodnotu následne pozícia 4 a  najhoršie ťahy sú 1,3,5,7.

```
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
```
### HumanVsAI
Po kliknutí na Human vs AI sa zobrazia dve obtiažnosti. Tieto náročnosti som vysvetlil v časti [AI vs AI](#AIvsAI)

<img src="img/difficult.png" width="660" height="660" />

Následne sa zobrazí okno s možnosťou výberu či chce hráč hrať za krúžok alebo krížik.

<img src="img/cross.png" width="660" height="660" />

Užívateľ určuje svoj ťah pomocou myšky:

```
if pygame.mouse.get_pressed() == (1,0,0):
    x,y = pygame.mouse.get_pos()
```

### HumanVsHuman
Po kliknutí sa spustí hra pre dvoch užívateľov. Player 1 je krúžok a Player 2 je krížik.

## Zvyšné funkcie
### ```win(screen, who, player1 = None, player2 = None)```
Táto funkcia skontroluje či niekto vyhral a vypíše víťaza. Celá funkcia funguje na vyhodnocovaní podmienok. 

```
def win(screen, who, player1 = None, player2 = None): # urci vitaza
    if who == 0:
        if player1 == 2:
            if player1 == player2:
                if ((screen[0]== 1 and screen[0]== screen[1] and screen[0] == screen[2])
                  or (screen[3]== 1 and screen[3]== screen[4] and screen[3] == screen[5])
                  or (screen[6]== 1 and screen[6]== screen[7] and screen[6] == screen[8]) 
                  or (screen[0]== 1 and screen[0]== screen[3] and screen[0] == screen[6]) 
                  or (screen[1]== 1 and screen[1]== screen[4] and screen[1] == screen[7]) 
                  or (screen[2]== 1 and screen[2]== screen[5] and screen[2] == screen[8]) 
                  or (screen[0]== 1 and screen[0] == screen[4] and screen[0] == screen[8]) 
                  or (screen[2]== 1 and screen[2]== screen[4] and screen[2] == screen[6])):
                    display_message('Computer 1 won!',bigfont,screen)
                    return True

            elif player1 != player2: 
                if ((screen[0]== 2 and screen[0]== screen[1] and screen[0] == screen[2]) 
                    or (screen[3]== 2 and screen[3]== screen[4] and screen[3] == screen[5]) 
                    or (screen[6]== 2 and screen[6]== screen[7] and screen[6] == screen[8]) 
                    or (screen[0]== 2 and screen[0]== screen[3] and screen[0] == screen[6]) 
                    or (screen[1]== 2 and screen[1]== screen[4] and screen[1] == screen[7]) 
                    or (screen[2]== 2 and screen[2]== screen[5] and screen[2] == screen[8]) 
                    or (screen[0]== 2 and screen[0] == screen[4] and screen[0] == screen[8])
                    or (screen[2]== 2 and screen[2]== screen[4] and screen[2] == screen[6])):
                    display_message('Computer 2 won!',bigfont,screen)
                    return True
            else:
                return False
        if player1 == 1:
            if player1 == player2:
                if ((screen[0]== 2 and screen[0]== screen[1] and screen[0] == screen[2]) 
                    or (screen[3]== 2 and screen[3]== screen[4] and screen[3] == screen[5]) 
                    or (screen[6]== 2 and screen[6]== screen[7] and screen[6] == screen[8]) 
                    or (screen[0]== 2 and screen[0]== screen[3] and screen[0] == screen[6]) 
                    or (screen[1]== 2 and screen[1]== screen[4] and screen[1] == screen[7]) 
                    or (screen[2]== 2 and screen[2]== screen[5] and screen[2] == screen[8]) 
                    or (screen[0]== 2 and screen[0] == screen[4] and screen[0] == screen[8])
                    or (screen[2]== 2 and screen[2]== screen[4] and screen[2] == screen[6])):
                    display_message('Computer 2 won!',bigfont,screen)
                    return True

            elif player1 != player2: 
                if ((screen[0]== 1 and screen[0]== screen[1] and screen[0] == screen[2])
                  or (screen[3]== 1 and screen[3]== screen[4] and screen[3] == screen[5])
                  or (screen[6]== 1 and screen[6]== screen[7] and screen[6] == screen[8]) 
                  or (screen[0]== 1 and screen[0]== screen[3] and screen[0] == screen[6]) 
                  or (screen[1]== 1 and screen[1]== screen[4] and screen[1] == screen[7]) 
                  or (screen[2]== 1 and screen[2]== screen[5] and screen[2] == screen[8]) 
                  or (screen[0]== 1 and screen[0] == screen[4] and screen[0] == screen[8]) 
                  or (screen[2]== 1 and screen[2]== screen[4] and screen[2] == screen[6])):
                    display_message('Computer 1 won!',bigfont,screen)
                    return True
            else:
                return False        

    if who == 1:
        if player1 == 2:
            if player1 == player2:
                if ((screen[0]== 1 and screen[0]== screen[1] and screen[0] == screen[2])
                  or (screen[3]== 1 and screen[3]== screen[4] and screen[3] == screen[5])
                  or (screen[6]== 1 and screen[6]== screen[7] and screen[6] == screen[8]) 
                  or (screen[0]== 1 and screen[0]== screen[3] and screen[0] == screen[6]) 
                  or (screen[1]== 1 and screen[1]== screen[4] and screen[1] == screen[7]) 
                  or (screen[2]== 1 and screen[2]== screen[5] and screen[2] == screen[8]) 
                  or (screen[0]== 1 and screen[0] == screen[4] and screen[0] == screen[8]) 
                  or (screen[2]== 1 and screen[2]== screen[4] and screen[2] == screen[6])):
                    display_message('You lost!',bigfont,screen)
                    return True

            elif player1 != player2: 
                if ((screen[0]== 2 and screen[0]== screen[1] and screen[0] == screen[2]) 
                    or (screen[3]== 2 and screen[3]== screen[4] and screen[3] == screen[5]) 
                    or (screen[6]== 2 and screen[6]== screen[7] and screen[6] == screen[8]) 
                    or (screen[0]== 2 and screen[0]== screen[3] and screen[0] == screen[6]) 
                    or (screen[1]== 2 and screen[1]== screen[4] and screen[1] == screen[7]) 
                    or (screen[2]== 2 and screen[2]== screen[5] and screen[2] == screen[8]) 
                    or (screen[0]== 2 and screen[0] == screen[4] and screen[0] == screen[8])
                    or (screen[2]== 2 and screen[2]== screen[4] and screen[2] == screen[6])):
                    display_message('You won!',bigfont,screen)
                    return True
            else:
                return False
        if player1 == 1:
            if player1 == player2:
                if ((screen[0]== 2 and screen[0]== screen[1] and screen[0] == screen[2]) 
                    or (screen[3]== 2 and screen[3]== screen[4] and screen[3] == screen[5]) 
                    or (screen[6]== 2 and screen[6]== screen[7] and screen[6] == screen[8]) 
                    or (screen[0]== 2 and screen[0]== screen[3] and screen[0] == screen[6]) 
                    or (screen[1]== 2 and screen[1]== screen[4] and screen[1] == screen[7]) 
                    or (screen[2]== 2 and screen[2]== screen[5] and screen[2] == screen[8]) 
                    or (screen[0]== 2 and screen[0] == screen[4] and screen[0] == screen[8])
                    or (screen[2]== 2 and screen[2]== screen[4] and screen[2] == screen[6])):
                    display_message('You lost!',bigfont,screen)
                    return True

            elif player1 != player2: 
                if ((screen[0]== 1 and screen[0]== screen[1] and screen[0] == screen[2])
                  or (screen[3]== 1 and screen[3]== screen[4] and screen[3] == screen[5])
                  or (screen[6]== 1 and screen[6]== screen[7] and screen[6] == screen[8]) 
                  or (screen[0]== 1 and screen[0]== screen[3] and screen[0] == screen[6]) 
                  or (screen[1]== 1 and screen[1]== screen[4] and screen[1] == screen[7]) 
                  or (screen[2]== 1 and screen[2]== screen[5] and screen[2] == screen[8]) 
                  or (screen[0]== 1 and screen[0] == screen[4] and screen[0] == screen[8]) 
                  or (screen[2]== 1 and screen[2]== screen[4] and screen[2] == screen[6])):
                    display_message('You won!',bigfont,screen)
                    return True
            else:
                return False

    if who == 2:
        if ((screen[0]== 1 and screen[0]== screen[1] and screen[0] == screen[2])
          or (screen[3]== 1 and screen[3]== screen[4] and screen[3] == screen[5])
          or (screen[6]== 1 and screen[6]== screen[7] and screen[6] == screen[8]) 
          or (screen[0]== 1 and screen[0]== screen[3] and screen[0] == screen[6]) 
          or (screen[1]== 1 and screen[1]== screen[4] and screen[1] == screen[7]) 
          or (screen[2]== 1 and screen[2]== screen[5] and screen[2] == screen[8]) 
          or (screen[0]== 1 and screen[0] == screen[4] and screen[0] == screen[8]) 
          or (screen[2]== 1 and screen[2]== screen[4] and screen[2] == screen[6])):
            display_message(f'Player 1 won!',bigfont,screen)
            return True

        elif ((screen[0]== 2 and screen[0]== screen[1] and screen[0] == screen[2]) 
            or (screen[3]== 2 and screen[3]== screen[4] and screen[3] == screen[5]) 
            or (screen[6]== 2 and screen[6]== screen[7] and screen[6] == screen[8]) 
            or (screen[0]== 2 and screen[0]== screen[3] and screen[0] == screen[6]) 
            or (screen[1]== 2 and screen[1]== screen[4] and screen[1] == screen[7]) 
            or (screen[2]== 2 and screen[2]== screen[5] and screen[2] == screen[8]) 
            or (screen[0]== 2 and screen[0] == screen[4] and screen[0] == screen[8])
            or (screen[2]== 2 and screen[2]== screen[4] and screen[2] == screen[6])):
            display_message(f'Player 2 won!',bigfont,screen)
            return True
        else:
            return False

    if who == 3:
        if ((screen[0]== 1 and screen[0]== screen[1] and screen[0] == screen[2])
          or (screen[3]== 1 and screen[3]== screen[4] and screen[3] == screen[5])
          or (screen[6]== 1 and screen[6]== screen[7] and screen[6] == screen[8]) 
          or (screen[0]== 1 and screen[0]== screen[3] and screen[0] == screen[6]) 
          or (screen[1]== 1 and screen[1]== screen[4] and screen[1] == screen[7]) 
          or (screen[2]== 1 and screen[2]== screen[5] and screen[2] == screen[8]) 
          or (screen[0]== 1 and screen[0] == screen[4] and screen[0] == screen[8]) 
          or (screen[2]== 1 and screen[2]== screen[4] and screen[2] == screen[6])):
            return True
        elif ((screen[0]== 2 and screen[0]== screen[1] and screen[0] == screen[2]) 
            or (screen[3]== 2 and screen[3]== screen[4] and screen[3] == screen[5]) 
            or (screen[6]== 2 and screen[6]== screen[7] and screen[6] == screen[8]) 
            or (screen[0]== 2 and screen[0]== screen[3] and screen[0] == screen[6]) 
            or (screen[1]== 2 and screen[1]== screen[4] and screen[1] == screen[7]) 
            or (screen[2]== 2 and screen[2]== screen[5] and screen[2] == screen[8]) 
            or (screen[0]== 2 and screen[0] == screen[4] and screen[0] == screen[8])
            or (screen[2]== 2 and screen[2]== screen[4] and screen[2] == screen[6])):
            return True
        else:
            return False
```

Parametre:
- screen: zoberie hraciu dosku
- who: hodnota, ktorá určuje aká z troch hier prebieha (0 predstavuje [AI vs AI](#AIvsAI), 1 predstavuje [Human vs AI](#HumanVsAI), 2 predstavuje [Human vs Human](#HumanVsHuman))
-player1 a player2: určuje kto je na ťahu a tým určí víťaza

### draw(screen)
Parameter screen predstavuje zoznam hodnôt, ktorého jednotlivé hodnoty predstavujú jednotlivé pozície na hracej doske. 1 predstavuje krúžok a 2 predstavuje krížik. Ak screen neobsahuje 0 a funkcia win vráti False uskutoční sa táto funkcia
```
def draw(screen):
    if 0 not in screen and not win(screen,3):
        display_message(f'Draw!',bigfont,screen)
        return True
    else:
        return False
```
### def menu()
Vykreslí úvodné menu
```
def menu():   # nakresli menu
    desk()
    button('TicTacToe',bigfont,200,80)
    button('Play',smallfont, window_width//2, window_height//2)
    pygame.display.update()
```

### def text_objects(text, font), def button(text,font, width, height)
Tieto funkcie fungujú na uľahčenie vykresľovania tlačítok

```
def text_objects(text, font): 
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def button(text,font, width, height): # vytvori blok na tlacitko
    TextSurf, TextRect = text_objects(text,font)
    TextRect.center = ((width),(height))
    window.blit(TextSurf, TextRect)
    pygame.display.update()
    return font.size(text)
```
### display_message(text,font,screen)
Funkcia ktorá slúži na výpis textu.
Parametre:
- text: text, ktorý bude vypísaný
- font: typ fontu, ktorý bude použitý
- screen: zoberie list s hodnotami, ktoré už boli zahrané
```
def display_message(text,font,screen): # vypise spravu
    TextSurf, TextRect = text_objects(text,font)
    TextRect.center = ((window_width/2),(window_height/2))
    window.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)    
    draw_screen(screen)
```
