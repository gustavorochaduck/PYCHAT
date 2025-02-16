import time
import sys
import os

def acssi_client_art():
    print('''
        _____                   /|
        |   \      ____        / |
  __    |    \    /\   |      /  ;
 /\  \  |     \  /  \  |     /  ;
/,'\  \ |      \/  : \ |    /   ;
~  ;   \|      /   :  \|   /   ;
   |    \     /   :'  |   /    ;
   |     \   /    :   |  /    ;
   |      \ /    :'   | /     ;
   |       /     :    |/     ;
   |      /     :'    |      ;
    \    /      :     |     ;
     \  /      :'     |     ;
      \       :'      |    ;
       \______:_______|___;
                ''')

def cleanTerminal():
    os.system('cls' if os.name == "nt" else "clear")

def typingAnimationClearProgram(text):
    count = 0
    while count < 3:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(0.5)
        #cleanTerminal()
        count += 1 
    print('-=-'*20, '\n')
def pc_ascii():
    print('''
                                .,,uod8B8bou,,.
                    ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
                ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
                !...:!TVBBBRPFT||||||||||!!^^""'   ||||
                !.......:!?|||||!!^^""'            ||||
                !.........||||                     ||||
                !.........||||  ##                 ||||
                !.........||||                     ||||
                !.........||||                     ||||
                !.........||||                     ||||
                !.........||||                     ||||
                `.........||||                    ,||||
                .;.......||||               _.-!!|||||
        .,uodWBBBBb.....||||       _.-!!|||||||||!:'
        !YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
        !..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
        !....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
        !......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
        !........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
        `..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
        `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
            `........::::::::::::::::;iof688888888888888888888b.     `
            `......:::::::::;iof688888888888888888888888888888b.
                `....:::;iof688888888888888888888888888888888899fT!
                `..::!8888888888888888888888888888888899fT|!^"'
                    `' !!988888888888888888888888899fT|!^"'
                        `!!8888888888888888899fT|!^"'
                        `!988888888899fT|!^"'
                            `!9899fT|!^"'
                    ''')

    