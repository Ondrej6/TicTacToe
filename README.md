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

## AI vs AI
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
## Human vs AI
Po kliknutí na Human vs AI sa zobrazia dve obtiažnosti. Tieto náročnosti som vysvetlil v časti [AI vs AI](# AI vs AI)

