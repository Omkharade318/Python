import random

def check(comp, user):
    if comp == user:
      return 0
  
    if (comp == 1  and user == 2 ):
        return -1
    
    if (comp == 2 and user == 3):
        return -1
    
    if (comp == 3 and user == 1):
        return -1
    
    return 1

comp = random.randint(1,3)
user = int (input("Press 1 for Stone, 2  for Scissors and 3 for Paper:  "))

score = check(comp, user)

print("You choose:",user)
print("Computer choose:",comp )

if (score == 0):
    print("Its a draw")
elif (score == -1):
    print("You Lose") 
else:
    print("You won")       