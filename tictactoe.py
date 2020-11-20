import re
from os import get_terminal_size,name,system
theBoard = {'top-l':' ','top-m':' ','top-r':' ',
            'mid-l':' ','mid-m':' ','mid-r':' ',
            'low-l':' ','low-m':' ','low-r':' '}
turn0 = 'X'
def instruct():#Instructions
    title = "TIC-TAC-TOE"
    print_text(title,"+","!¡")
    #Enclose your string within \033[1m and \033[0m for bold text
    print("\033[1m" + "Instructions:" + "\033[0m",end = ' ')
    print('''Enter the position you want to mark in <row>-<column> pair
              Enter -1 to exit current game
Example: 1. For top row left column type: top-l
         2. For middle row right column type: mid-r

          ''')



def setBoard():#For resetting the board
    global theBoard
    global turn0
    theBoard = dict.fromkeys(theBoard.keys(),' ')
    turn0 = 'X'

def clear():#Clear screen
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def printBoard(board):#Printing the board
    print('    l|m|r')
    print('top ' + board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('    —+—+—')
    print('mid ' + board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('    —+—+—')
    print('low ' + board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])



def check(turn):#Checking for win condition
    while True:
        winlist = [ rf"[{turn}]{{3}}[\sXO]{{6}}", rf"[\sXO]{{3}}[{turn}]{{3}}[\sXO]{{3}}", rf"[\sXO]{{6}}[{turn}]{{3}}", rf"([{turn}][\sXO]{{2}}){{3}}", rf"([\sXO][{turn}][\sXO]){{3}}", rf"([\sXO]{{2}}[{turn}]){{3}}", rf"[{turn}][\sXO]{{3}}[{turn}][\sXO]{{3}}[{turn}]", rf"[\sXO]{{2}}[{turn}][\sXO][{turn}][\sXO][{turn}][\sXO]{{2}}" ]#All possible win conditions
        teststr = ''.join(theBoard.values())
        temp = '(?:% s)' % '|'.join(winlist)
        return bool(re.search(temp,teststr))


def game():#Actual gameplay
    global turn0
    global theBoard
    i = 1
    printBoard(theBoard)
    while i < 10:
        move = input('Turn for ' + "\033[1m" + turn0 + "\033[0m" + '. Move on which space? ').lower()
        if move == "-1":
            return
        if move not in theBoard.keys():#To prevent KeyError and creation of new pairs in the dictionary
            print_text('Stay within limits',"!")
            continue
        if theBoard[move] != ' ':#To avoid overwriting
            print_text("It's already filled","!")
            continue
        theBoard[move] = turn0#Marking in the board
        printBoard(theBoard)
        if check(turn0):
            print_text(turn0+' WINS',"$","✓")
            break
        turn0= 'O' if turn0 == 'X' else 'X'#Toggle
        i += 1
    if i == 10:#When the game leads to draw
        print_text("It's a DRAW","†","‽")

#Execution begins here
while True:
    clear()
    setBoard()
    col = get_terminal_size().columns


    def decor(func):
        def wraper(wmsg,wfill = " ",wwrap ="=",wn = col):
            if bool(len(wfill) not in range(1,3)):
                
                raise TypeError("The fill character could have either one or two characters only. You have "+ str(len(wfill) + " characters."))
            print(wwrap[0]*wn , end = "\n")
            func(wmsg,wfill,wwrap,wn)
            print(wwrap[-1]*wn , end = "\n")
            print()
        return wraper
    @decor
    def print_text(msg,fill,wrap,n):
        print(msg.center(n,fill) , end = "\n")


    instruct()
    game()
    if not input("Play again?(Y/N) ").lower() == 'y':#Making sure that the user explicitly states he wants another game
        break
