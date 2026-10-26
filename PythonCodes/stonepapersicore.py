import random

choices=('r','p','s')
# choices.append('r')

user=input('rock,paper,or scissors?(r/p/s.):').lower()
if user not in choices:
    print("invalid choice ! ")

c_choice=random.choice(choices)
if user=='r':
    print("rock")
elif user=='s':
    print("scissors")
else:
    print("paper")

print(f'my choice {user}' )

if c_choice=='r':
    print("rock")
elif c_choice=='s':
    print("scissors")
else:
    print("paper")


print(f'computer choice {c_choice}' )

    
""" 31;20

https://youtu.be/yVl_G-F7m8c?si=AdHn0nWjZ9JCe8Sc """