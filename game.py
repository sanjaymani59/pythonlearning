""" print("HAND CRICKET GAME ")

score=0

while True:
    player = int(input("choose your runs(1-6):"))
    computer = 4

    if player <1 or player > 6:
        print("please choose between 1-6")
        continue

    print("computer choose",computer)
    if computer == player:
        print("you win",score)
        break
    else:
        score+=player 
        print("runs scored",player)
        print("Total score",score)

print("Game over")
"""

name= str("ram")
day= str("15 days of leave ")
year=int(2026)

print( name,  day , year)