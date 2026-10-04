import random
player = 100
computer = 100
Punch = "1"
Kick = "2"
SpAttack = "3"
print("==== BATTLE ====")
print(f"Player HP : {player}")
print(f"Computer HP : {computer}")
print("1.Punch")
print("2.Kick")
print("3.Special Attack")
while player > 0 and computer > 0:
     com = random.choice(["1","2","3"])

     Attack = input("Choose One Attack : ")


     if Attack == Punch:
         print("You used Punch!")
         computer = computer - 10
         print(f"10 damage to computer- {computer}")
     elif Attack == Kick:
         print("You used Kick!")
         computer = computer - 15
         print(f"15 damage to computer- {computer}")

     elif Attack == SpAttack:
         print("You used Special Attack!")
         computer = computer - 25
         print(f"25 damage to computer- {computer}")

     if com == Punch:
                 print("Computer Attacks!")
                 player = player - 10
                 print(f"10 damage to player - {player}")
        
     elif com == Kick:
                 print("Computer Attacks!")
                 player = player - 15
                 print(f"15 damage to player - {player}")
        
     elif com == SpAttack:
                 print("Computer used Special Attack!")
                 player = player - 25
                 print(f"25 damage to player - {player}")


     if player == 0:
         print(f"Your HP : {player}")
         print(f"Computer HP : {computer}")
         print("You Lost!")
         exit()


     elif computer == 0:
         print(f"Computer HP : {computer}")
         print(f"Your HP : {player}")
         print("You Won!")
         exit()

     elif player == 0 and computer == 0:
         print("Both Lose!")
         exit()

     else:
         print("Continue")