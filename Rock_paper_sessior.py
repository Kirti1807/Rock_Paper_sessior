'''
   This is a simple game in which one player is user and another one is computer.
   in this we use random library of python to chose random charcter from a list
'''

import random
# s>p r>s p>r
user=0
computer=0
print('you play 10 turns lets see who wins...')
for i in range(10):
    print("choose 'p' for paper, 'r' for rock, 's' foe sessior")
    user_choice = input('whats your choice: ')
    computer_choice = random.choice(['p','r','s'])
    print(f"{computer_choice} is computer's choice ")
    if user_choice == computer_choice:
        
        print('tie.....')
    else:
        if (user_choice == 's' and computer_choice == 'p') or (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r'):
            print('horeee YOU win this turn')
            user=user+1
        else :
            print('oppsss YOU lost this turn')
            computer=computer+1
if user > computer :
    print('wow YOU won  more matches then computer ')
elif user == computer :
    print('both YOU and COMPUTER won equal matches')
else :
    print ('oppsss YOU won less matches then computer')
