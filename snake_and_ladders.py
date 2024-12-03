from random import randint, choice
import colorama
from colorama import Fore, Style
from time import sleep
import emoji

colorama.init(autoreset=True)

print("")
allPlayersInfo = []

allLadders = [{"start": 7,"end": 26},{"start": 9,"end": 55},{"start": 21,"end": 97},{"start": 36,"end": 64},{"start": 41,"end": 94},{"start": 44,"end": 65},{"start": 50,"end": 92},{"start": 61,"end": 98},{"start": 66,"end": 86},{"start": 67,"end": 88}]
allSnakes = [{"start": 99,"end": 10}, {"start": 95,"end": 65}, {"start": 91,"end": 51}, {"start": 73,"end": 3}, {"start": 62,"end": 22}, {"start": 58,"end": 24}, {"start": 52,"end": 11}, {"start": 46,"end": 15}, {"start": 43,"end": 17}, {"start": 32,"end": 5}]
toWinComments = ["Better Luck Next Time !", "You Are So Close !", "Oops, Just Missed It !"]

def drawBoard(act, aw):
    board = [
        [i for i in range(100, 90, -1)],
        [i for i in range(81, 91)],
        [i for i in range(80, 70, -1)],
        [i for i in range(61, 71)],
        [i for i in range(60, 50, -1)],
        [i for i in range(41, 51)],
        [i for i in range(40, 30, -1)],
        [i for i in range(21, 31)],
        [i for i in range(20, 10, -1)],
        [i for i in range(1, 11)]
    ]
    fakeList = board    ##creating icons on board
    for lst in range(len(fakeList)):
        for item in range(len(fakeList[lst])):
            for snake in allSnakes:     ##creating snakes on board (red)
                if(fakeList[lst][item] == snake["start"]):
                    fakeList[lst][item] = Fore.RED + str(fakeList[lst][item])
                    
            for ladder in allLadders:   ##creating ladders on board (green)
                if(fakeList[lst][item] == ladder["start"]):
                    fakeList[lst][item] = Fore.GREEN + str(fakeList[lst][item])
                    
            for player in allPlayersInfo:      ##changing player's position
                if(player["isHere"] == fakeList[lst][item]):
                    fakeList[lst][item] = player["color"]
                    break
    
    ##printing board
    print("\n------------------------------------------------------------------------------")  ##printing board
    for lst in fakeList:
        for item in lst:
            print(" ", Fore.WHITE + Style.BRIGHT + str(item), end="\t")
        print("\n------------------------------------------------------------------------------")
    
    print()
    lockedPlayersList = []
    for i in allPlayersInfo:        ##checking for locked players
        if(not i["unlocked"]):
            lockedPlayersList.append(i)
            
    if(lockedPlayersList != []):
        print()
        print(Fore.CYAN + f"   Players in Queue To Unlock:- ", end="")
        for record in lockedPlayersList:
            if(not record["unlocked"]):
                print(record["color"], end="\t".expandtabs(3))
        print("\n")
        
    if(aw):     ##to announce when winner is declared
        announceWinner(act)
    
    if(not aw):     #game will continue when winner not declared
        sleep(0.5)
        print(Fore.GREEN + f"   {allPlayersInfo[act]['color']} - {allPlayersInfo[act]['name']}'s Turn !")
        print()
        sleep(0.5)
        print(Fore.CYAN + "   Press Enter To Roll Dice !")
        input()
        rollDice(act, aw)

def  rollDice(act, aw):
    faces = [
"""\t+---------+
\t|         |
\t|   🔴    |
\t|         |
\t+---------+""",
"""\t+---------+
\t| 🔴      |
\t|         |
\t|     🔴  |
\t+---------+""",
"""\t+---------+
\t| 🔴      |
\t|   🔴    |
\t|     🔴  |
\t+---------+""",
"""\t+---------+
\t| 🔴  🔴  |
\t|         |
\t| 🔴  🔴  |
\t+---------+""",
"""\t+---------+
\t| 🔴  🔴  |
\t|   🔴    |
\t| 🔴  🔴  |
\t+---------+""",
"""\t+---------+
\t| 🔴  🔴  |
\t| 🔴  🔴  |
\t| 🔴  🔴  |
\t+---------+"""
]
    num = randint(0, 5)
    print()
    sleep(0.5)
    print(faces[num])
    sleep(0.5)
    print()
    print(Fore.MAGENTA + f"   You Got A - {num + 1} !")
    print()
    #creating increment
    if(allPlayersInfo[act]["unlocked"]):
        if((allPlayersInfo[act]["isHere"] + num + 1) <= 100):
            allPlayersInfo[act]["isHere"] = allPlayersInfo[act]["isHere"] + num + 1
            
            for snake in allSnakes:     ##checking if snake bites player
                if(allPlayersInfo[act]["isHere"] == snake["start"]):
                    print()
                    print(Fore.RED + f"    x_x  Snake Bites {allPlayersInfo[act]['name']}  x_x")
                    print()
                    sleep(0.2)
                    print(Fore.RED + f"        Fell From {snake['start']} -> {snake['end']}")
                    allPlayersInfo[act]["isHere"] = snake["end"]
                    print()
                    break

            for ladder in allLadders:       ##checking if player climbs ladder
                if(allPlayersInfo[act]["isHere"] == ladder["start"]):
                    print()
                    print(Fore.GREEN + f"    ^_^  {allPlayersInfo[act]['name']} Climbs A Ladder  ^_^")
                    print()
                    sleep(0.2)
                    print(Fore.GREEN + f"        Climbed From {ladder['start']} -> {ladder['end']}")
                    allPlayersInfo[act]["isHere"] = ladder["end"]
                    print()
                    break
        else:
            print()
            sleep(0.5)
            print(Fore.YELLOW + f"\t{choice(toWinComments)}")
            print()
            
    if(allPlayersInfo[act]["isHere"] == 100):   ##declaring winner
        aw = True
    
    if(num == 5):   #unlocking on 6
        if(not allPlayersInfo[act]["unlocked"]):
            allPlayersInfo[act]["unlocked"] = True
            allPlayersInfo[act]["isHere"] = 1
            sleep(0.5)
            print(f"   {allPlayersInfo[act]['color']} - {allPlayersInfo[act]['name']} Has Unlocked !")
    elif(num != 5 and (not allPlayersInfo[act]["unlocked"])):
        sleep(0.5)
        print(Fore.RED + "   -_- Not Yet Unlocked -_-")
        print()
    sleep(0.5)
        
    if(not aw):
        if(act < len(allPlayersInfo) - 1):
            act += 1
        else:
            act = 0
    
    drawBoard(act, aw)

def main():
    print(Fore.MAGENTA + "\tWelcome To - Snakes & Ladders !!!".expandtabs(2))
    print("\t1) Start New Game.".expandtabs(4))
    print("\t2) Rules.".expandtabs(4))
    print("\t3) Quit.".expandtabs(4))
    print()
    choice = input(Fore.YELLOW + Style.BRIGHT + "\tYour Choice >>> ")
    print()
    if(choice == "1" or choice.lower() == "start new game" or choice.lower() == "start"):
        print(Fore.MAGENTA + "\t??? How Many Players ???  (Max = 4  &  Min = 2)".expandtabs(2))
        print()
        noInfo = True
        while noInfo:
            playerNum = input("    Number Of Players >>> ")
            print()
            if(playerNum.isdigit()):
                playerNum = int(playerNum)
            elif(playerNum.isalpha()):
                if(playerNum.lower() == "two"):
                    playerNum = 2
                elif(playerNum.lower() == "three"):
                    playerNum = 3
                elif(playerNum.lower() == "four"):
                    playerNum = 4
                else:
                    print(Fore.RED + "  !!! INVALID INPUT !!!")
                    print()
                    continue
            else:
                print(Fore.RED + "  !!! INVALID INPUT !!!")
                print()
                continue
                
            ##finally rendering number
            if(playerNum >= 2 and playerNum <= 4):
                noInfo = False
                break
            elif(playerNum < 2):
                print(Fore.YELLOW + "  !!! You Must Enter Minimum 2 Players !!!")
                print()
                continue
            elif(playerNum > 4):
                print(Fore.YELLOW + "  !!! Maximum 4 Players Can Play !!!")
                print()
                continue
            
        ##taking another information
        plNum = 1
        allColors = [f'{emoji.emojize(":red_heart:")} ',emoji.emojize(":yellow_heart:"),emoji.emojize(":green_heart:"),emoji.emojize(":blue_heart:"), emoji.emojize(":purple_heart:")]
        
        for i in range(playerNum):
            singleInfo = {"name": f"Player{plNum}", "isHere": 0, "color": "", "unlocked": False}
            ##taking name of players
            name = input(f"   Player{plNum}'s Name >>> ").capitalize()
            if(name == '' or name == " "):
                pass
            else:
                singleInfo["name"] = name
            ##taking color of players
            color = None
            while True:
                initialColor = 1
                print()
                print(Fore.MAGENTA + "  Pick One Color !")
                print()
                for color in allColors:
                    print(f"\t{initialColor}) {color}")
                    initialColor+=1
                print()
                color = input("  Enter Color Number >>> ")
                if(color.isdigit()):
                    if(int(color)-1 >= 0 and int(color)-1 < len(allColors)):
                        color = int(color)
                        print()
                        break
                    else:
                        print(Fore.YELLOW + "  !!! Color Value Out Of Range !!!")
                        print()
                        continue
                else:
                    print(Fore.RED + "  !!! INVALID INPUT !!!")
                    print()
                    continue
            singleInfo["color"] = f"{allColors[color-1]}"
            allColors.pop(color - 1)      #removing used color
            allPlayersInfo.append(singleInfo)   #inserting info
            plNum += 1
        sleep(0.5)
        announcedWinner = False
        activePlayer = 0
        print(Fore.GREEN + Style.BRIGHT + "    <---- Game Started ---->")
        print()
        print(Fore.GREEN + f"   {allPlayersInfo[activePlayer]['color']} - {allPlayersInfo[activePlayer]['name']}'s Turn !")
        print()
        sleep(0.2)
        print(Fore.MAGENTA + "    Press Enter To Roll Dice !")
        input()
        rollDice(activePlayer, announcedWinner)
        
    elif(choice == "2" or choice.lower() == "rules"):
        showRules()
    elif(choice == "3" or choice.lower() == "quit"):
        print(Fore.CYAN + "\t<---- BYE ---->")
        pass
    else:
        print(Fore.RED + "   !!! INVALID CHOICE !!!")
        print()
        main()

def showRules():
    print()
    print(Fore.MAGENTA + "   ------------------------------- RULES -------------------------------")
    print()
    sleep(0.5)
    print("     1) To Unlock Your Piece, You Must get a '6' on Rolling the Dice.")
    sleep(1)
    dice = """+---------+
             | 🔴  🔴  |
             | 🔴  🔴  |
             | 🔴  🔴  |
             +---------+"""
    print(f"       As :- {dice}")
    print()
    sleep(1)
    print("     2) The Green Numbers on Board are Ladders.")
    sleep(1)
    print("       All Ladders :-")
    sleep(0.5)
    for i in allLadders:
        print(f"         {i['start']} \t {Fore.GREEN + '-->'} \t {Fore.WHITE + str(i['end'])}")
        sleep(0.2)
    print()
    sleep(1)
    print("     3) The Red Numbers on Board are Snakes.")
    sleep(1)
    print("       All Snakes :-")
    sleep(0.5)
    for i in allSnakes:
        print(f"         {i['start']} \t {Fore.RED + '-->'} \t {Fore.WHITE + str(i['end'])}")
        sleep(0.2)
    print()
    sleep(1)
    print("     4) Every Player Will Get One Turn Per Round.")
    print()
    sleep(1)
    print("     5) First Player Reaching '100' Will be Considered as Winner.")
    print()
    sleep(1)
    print(Fore.MAGENTA + "   ---------------------------------------------------------------------")
    print()
    sleep(1)
    main()

def announceWinner(act, allPlayersInfo = allPlayersInfo):
    sleep(1)
    print()
    print(Fore.MAGENTA + "\t<----------  GAME OVER  ---------->")
    print()
    sleep(0.6)
    print(Fore.CYAN + f"    Winner is {allPlayersInfo[act]['color']} - {allPlayersInfo[act]['name']} !")
    print()
    sleep(0.5)
    print("----------------------------------------------------------------------------------")
    print()
    while True:
        print("   Choose One Option !")
        print("     1) Restart Game.")
        print("     2) Main Menu.")
        print("     3) Quit.")
        print()
        choice = input("\tYour Choice >>> ")
        print()
        if(choice == "1" or choice.lower() == "restart game" or choice.lower() == "restart"):
            for i in range(len(allPlayersInfo)):
                allPlayersInfo[i]["isHere"] = 0
                allPlayersInfo[i]["unlocked"] = False
            announcedWinner = False
            activePlayer = 0
            print()
            print(Fore.GREEN + Style.BRIGHT + "    <---- Game Started ---->")
            print()
            print(Fore.GREEN + f"   {allPlayersInfo[activePlayer]['name']}'s Turn !")
            sleep(0.2)
            print(Fore.MAGENTA + "    Press Enter To Roll Dice !")
            input()
            rollDice(activePlayer, announcedWinner)
        elif(choice == "2" or choice.lower() == "main menu" or choice.lower() == "main" or choice.lower() == "menu"):
            try:
                while allPlayersInfo != []:
                    allPlayersInfo.pop()
            except EOFError:
                pass
            print("----------------------------------------------------------------------------------")
            print()
            main()
            break
        elif(choice == "3" or choice.lower() == "quit"):
            print(Fore.CYAN + "    <---- BYE ---->")
            print()
            break
        else:
            print(Fore.RED + "\t!!! INVALID INPUT !!!")
            print()
    quit()

if __name__ == "__main__":
    main()
