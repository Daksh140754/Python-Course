import random
playing=True
number=str(random.randint(0,9))
print("I will generate the numbers from 0 to9,and you have to guess the number one ata  a time!")
print("The game ends when you get a Hero!!!")
guess=input("Give me your guess!:")
while playing:
    if number==guess:
        print("You win the game")
        print("The number is:",number)
        break
    else:
        print("Your guess isn't quite right, Please try again!!")
