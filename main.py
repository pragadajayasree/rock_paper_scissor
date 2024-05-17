rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line
import random
p=int(input("enter 0-rock,1-paper,2-scissor"))
q=random.randint(0,2)
if(p==0):
 print(rock)
elif(p==1):
 print(paper)
else:
  print(scissors)
print("computers choice")
if(q==0):
 print(rock)
elif(q==1):
 print(paper)
else:
  print(scissors)
if(p==0):
  if(q==0):
    print("tie");
  elif(q==1):
    print("you lose")
  else:
    print("you win")
elif(p==1):
  if(q==0):
    print("you win")
  elif(q==1):
    print('tie')
  else:
    print("you lose")
else:
  if(q==0):
    print("you lose")
  elif(q==1):
    print("you win")
  else:
    print("tie")