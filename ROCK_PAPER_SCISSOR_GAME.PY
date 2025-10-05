import random
l=["rock","paper","scissor"]
"""
rock vs paper> paper win
rock vs scissor > rock win
paper vs scissor > scissor win
"""
user_count=0
computer_count=0
while True:
    user_chioce=int(input("""
                    start game
                1.  Yes
                2.  NO/Exit                    
                          """))
    if user_chioce==1:
          for a in range(1,6):
               user_input=int(input("""
                             1. rock
                             2.scissor
                             3.paper              
                                    """))
               if user_input==1:
                    user_chioce="rock"
               elif user_input==2:
                    user_chioce="scissor"
               elif user_input==3:
                    user_chioce="paper"
                    computer_chioce=random.choice(l)
                    if computer_chioce==user_chioce:
                         print("computer value",computer_chioce)
                         print("user value",user_chioce)
                         print("game draw")
                         user_count=user_count+1
                         computer_count=computer_count+1
                    elif user_chioce=="rock" and computer_chioce=="scissor" or user_chioce=="paper" and computer_chioce=="rock" or user_chioce=="scissor" and computer_chioce=="paper":
                         print("computer value",computer_chioce)
                         print("user value",user_chioce)
                         user_count=user_count+1
                         print("you win")
                    else:
                       print("computer value",computer_chioce)
                       print("user value",user_chioce)
                       computer_count=computer_count+1
                       print("computer win")
                       if user_count==computer_count:
                            print("final game draw")
                            print("user score",user_count)
                            print("computer score",computer_count)
                       elif user_count>computer_count:
                            print("finally you win game")
                            print("user score",user_count)
                            print("computer score",computer_count)
                       else:
                            print("fainal computer win game")
                            print("user score",user_count)
                            print("computer score",computer_count)     
               else:
                    break                    

