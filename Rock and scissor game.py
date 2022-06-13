# Build a game version 1.0
# Rock and Scissor
#User input 
import random

while True:
    user2=str(input ('''Are you ready!!!!!!
              Start Game........
              Please choose 
              Rock !!
              Paper!!
              Scissor!!....
              .....................
              type 'exit' to end game!    
              '''))
    user = user2.lower()
#list of character Rock,Scissor,and Paper
   # print(user)
    cpu2=['rock','scissor','paper']
#Random for cpu output
    cpu=random.choice(cpu2)
   # print(cpu)

#Condition for game for tie
    if user == cpu :
         print ("This is a tie both are ", user )
        # break
         
#user
# Condition for Rock beat Scissor
    elif user == 'rock' and cpu=='scissor':
        print ("User wins ", user ,"beats scissor")
       # break
        
#condion for paper beat rock
    elif user == 'paper' and cpu =='rock':
        print("User wins ", user ,"beat Rock" )
       # break
        
#condition for scissor beat paper
    elif user =='scissor' and cpu =='paper':
        print("User wins ", user , "beat paper")
        #break
 # Condition for Rock beat Scissor       
    elif cpu=='rock' and user =='scissor' :
        print ("cpu wins", cpu,"beat Scissor") 
        #break
 #condion for paper beat rock       
    elif cpu=='paper' and user =='rock' :
        print ("cpu win ", cpu ,"beat Rock")
        #break
#condition for scissor beat paper      
    elif cpu =='scissor' and user =='paper':
       print("cpu wins ", cpu , "beat Paper")
      # break
# exit Game
    elif  user == 'exit': 
      print ("Thanks for playing......")
      break
 #Try again      
    elif  user != 'rock' or user!= 'paper' or user!='scisor' :
        print ("Try again")
       # break

   


    
