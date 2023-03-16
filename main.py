import time
import os
import random
import pymongo
from pymongo import MongoClient as MC
client = MC(os.environ['mongodb'])
db = client['CatCapitalistDB']['userData']
reward = random.randint(40, 67)
funArr = ["Cats are believed to be the only mammals who don’t taste sweetness.", "Cats can jump up to six times their length.", "Cats’ claws all curve downward, which means that they can’t climb down trees head-first. Instead, they have to back down the trunk.", "Cats’ rough tongues can lick a bone clean of any shred of meat.", "Cats walk like camels and giraffes: They move both of their right feet first, then move both of their left feet. No other animals walk this way.", "Cats have 230 bones, while humans only have 206.", "Cats’ collarbones don’t connect to their other bones, as these bones are buried in their shoulder muscles.", "Cats have an extra organ that allows them to taste scents on the air, which is why your cat stares at you with her mouth open from time to time.", "Though cats can notice the fast movements of their prey, it often seems to them that slow-moving objects are actually stagnant.", "According to Wilde, a slow blink is a “kitty kiss.” This movement shows contentment and trust.", "Cats may yawn as a way to end a confrontation with another animal. Think of it as their “talk to the hand” gesture.", "When cats hit you with retracted claws, they’re playing, not attacking.", "Cats are very fussy about their water bowls; some prefer to ignore their bowls entirely in favor of drinking from the sink faucet.", "Some cats love the smell of chlorine.", "For some reason, cats really dislike citrus scents.", "Maria Assunta left her cat, Tomasso, her entire $13 million fortune when she died in 2011.", "A group of kittens is called a “kindle.”", "A house cat could beat superstar runner Usain Bolt in the 200 meter dash.", "Cats dream, just like people do."]

def newUser():
	newUSERNAME = input('Please create a username: ')
	newPASSWORD = input('Please create a password')

	

	if len(newUSERNAME) < 5:
		print('Username must be at least 5 characters')
		newUser()

	

first = input('Are you a new or returning user?\n\n1. New User\n2. Returning User\n\ninput: ')

if first == 1:
	newUser()
elif first == 2:
	returningUser()
else:

os.system('clear')

catnip = 0
cats = 12
tiredCats = 0
catFood = 30
chubbo = 1

def stat():
  print(f"Catnip: {catnip}\ncatfood: {catFood}\ncats: {cats}\ntired cats: {tiredCats}")

def sprinkles():
  global counter
  counter = 0
  os.system('clear')
  quit = 0
  while quit == 0:
    os.system('clear')
    print("""
Sprinkles
 /\\_/\\
( o.o ) 
 > ^ <
    """)
    print("How can I help you today?\n-------------------------\n1 - Cat catalouge\n2 - Fun fact\n3 - leave")
    choice = input("input: ")
    if choice == "1":
      os.system('clear')
      print("""
-----------------------------------------
    /\\_____/\\
   /  o   o  \\
  ( ==  ^  == )
   )         (
  (           )
 ( (  )   (  ) )
(__(__)___(__)__)
Cat: Chubbo
info: Sells catfood. Sends order requests at the back office, and gives rewards in return for task completion. Likes to watch soap-operas and binge eat...
-----------------------------------------
 /\\_/\\
( o.o ) 
 > ^ <
Cat: Sprinkles
info: One of the managers of Cat Corp. Gives fun facts about cats and also bearer of the Cat Catalogue, which holds information about all the important cats in the corporation. Sprinkles smells of wheat bread and chicken noodle soup...
-----------------------------------------
|\\---/|
| o_o |
 \\_^_/
Cat: Socks
info: Informant and helper. Notifies cats of upcoming events. Likes to eat paper...
-----------------------------------------
 _._     _,-'""`-._
(,-.`._,'(       |\\`-/|
    `-.-' \\ )-`( , o o)
          `-    \\`_`"'-
Cat: Friskers
Info: Slightly crazed. No one knows how he even ended up in the corporation, no one recalls hiring him. Friskers claimed to have caught The Red Dot...
-----------------------------------------
      |\\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\\ (  `'-'
    '---''(_/--'  `-'\\_)
Cat: Tuna-Can
info: Lazy cat who doesn't do much. Other cats wonder why Tuna-Can hasn't been fired yet for lack of productive work. Likes to sleep in the Managers office alot...
-----------------------------------------
      """)
      input("return: ")
    if choice == "2":
      os.system('clear')
      print(funArr[counter])
      counter += 1
      if counter == 19:
        counter = 0
      input("return: ")
    if choice == "3":
      quit = 1
      os.system('clear')
      
def socks():
  os.system('clear')
  quit = 0
  while quit == 0:
    os.system('clear')
    print("""
   socks
  |\\---/|
  | o_o |
   \\_^_/
 """)
    string = ""
    if cats > 0:
      string += "There are still some cats that can be put to work.\n"
    if chubbo == 1:
      string += "Chubbo has an assignment for you in the back office.\n"
    if cats == 0 and tiredCats == 0:
      string += "You literally have zero cats in the corporation. Go hire some.\n"
    if catFood < cats + tiredCats:
      string += "You're running low on catFood. Go buy some.\n"
    print(f"{string}-------------------------\n1 - leave")
    choice = input("input: ")
    if choice == "1":
      quit = 1
      os.system('clear')
def managersOffice():
  global catnip
  global cats
  global tiredCats
  os.system('clear')
  quit = 0
  while quit == 0:
    os.system('clear')
    print(f"cats: {cats}\ntired cats: {tiredCats}")
    print("""
Tuna-Can
          |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)
    """)
    print("\"zzz\"\n-------------------------\n1 - hire cats\n2 - leave")
    choice = input("input: ")
    if choice == "1":
      os.system('clear')
      stat()
      print("How many cats would you like to hire? (15 Catnip per cat) or input 0 to buy max amount")
      try:
        amount = int(input("amount: "))  
        temp = amount * 15
        if temp <= catnip:
          cats += amount
          catnip -= amount * 15
        if amount == 0:
          while catnip >= 15:
            catnip -= 15
            cats += 1
        else:
          print(f"You don't have enough catnip for {num} cats.")
          input("return: ")
      except:
        pass
 
      
    if choice == "2":
      quit = 1
  os.system('clear')

chubboTask = random.randint(1, 4)
#making stuff
yarn = 0
feather = 0
bell = 0
cloth = 0

#made stuff

#5yarn
yarnBall = 0
#2cloth + 4yarn
toyMouse = 0
#1yarn + 3feather + 1bell
featherOnString = 0
#2feather + 2cloth + 1bell + 3yarn
toyBird = 0
def manafacturing():
  global yarn
  global feather
  global bell
  global cloth
  global yarnBall
  global toyMouse
  global featherOnString
  global toyBird
  global cats
  global tiredCats
  os.system('clear')
  quit = 0
  while quit == 0:
    os.system('clear')
    stat()
    print("""
-----------------------------
        Manafuctering
-----------------------------
      {';:'}
     {''}
     | |
 _-_-| |-_-_-_-_- ___-_-_
|~~~~~~~~~~~~~~~~{___}~~~|
|   |__|  |__|   |   |   |
|~~~~~~~~~~~~~~~~|~~~|~~~|

-------------------------""")
    print("1 - produce\n2 - craft\n3 - leave")
    choice = input("input: ")
    if choice == "1":
      quit2 = 0
      while quit2 == 0:
        os.system('clear')
        print(f"cats: {cats}\n\nyarn: {yarn}\nfeathers: {feather}\nbells: {bell}\ncloth: {cloth}\n-------------------------\n1 - make yarn\n2 - make feathers\n3 - make bells\n4 - make cloth\n5 - leave")
        choice2 = input("input: ")
        if choice2 != "5":
          try:
            amount = int(input("amount: "))
            if amount <= cats:
              cats -= amount
              tiredCats += amount
              if choice2 == "1":
                yarn += amount
              if choice2 == "2":
                feather += amount
              if choice2 == "3":
                bell += amount
              if choice2 == "4":
                cloth += amount
          except:
            pass
        if choice2 == "5":
          quit2 = 1
          os.system('clear')
    if choice == "2":
      quit2 = 0
      while quit2 == 0:
        os.system('clear')
        print(f"yarn: {yarn}\nfeathers: {feather}\nbells: {bell}\ncloth: {cloth}\n\nyarn balls: {yarnBall}\ntoy mice: {toyMouse}\nfeather on string: {featherOnString}\ntoy birds: {toyBird}\n-------------------------\n1 - make yarn balls(5yarn)\n2 - make toy mice(2cloth + 4yarn)\n3 - make feather on string(1yarn + 3feather + 1bell)\n4 - make toy birds(2feather + 2cloth + 1bell + 4yarn)\n5 - leave")
        choice = input("input: ")
        if choice != "5":
          try:
            amount = int(input("amount: "))
            if choice == "1":
              if amount * 5 <= yarn:
                yarn -= amount * 5
                yarnBall += amount
            if choice == "2":
              if amount * 2 <= cloth and amount * 4 <= yarn:
                yarn -= amount * 4
                cloth -= amount * 2
                toyMouse += 1
            if choice == "3":
              if amount <= yarn and amount * 3 <= feather and amount <= bell:
                yarn -= amount
                feather -= amount * 3
                bell -= amount
                featherOnString += 1
            if choice == "4":
              if amount * 2 <= feather and amount * 2 <= cloth and amount <= bell and amount * 4 <= yarn:
                feather -= amount * 2
                cloth -= amount * 2
                bell -= amount
                yarn -= amount * 4
                toyBird += 1
            if choice == "5":
              quit2 = 1
          except:
            pass
        if choice == "5":
          quit2 = 1
          os.system('clear')
    if choice == "3":
      quit = 1
      os.system('clear')
def backOffice():
  global catnip
  global yarnBall
  global featherOnString
  global toyBird
  global toyMouse
  global reward
  global catFood
  os.system('clear')
  quit = 0
  while quit == 0:
    os.system('clear')
    print(f"catnip: {catnip}\ncatfood: {catFood}\n")
    print("""
    Chubbo
    /\\_____/\\
   /  o   o  \\
  ( ==  ^  == )
   )         (
  (           )
 ( (  )   (  ) )
(__(__)___(__)__)

-------------------------
1 - buy food(1 catnip per catfood)
2 - check task
3 - leave
    """)
    blah = input("input: ")
    if blah == "1":
      try:
        amount = int(input("amount: "))
        if amount <= catnip:
          catFood += amount
          catnip -= amount
      except:
        pass
#6roghdfjvskdwgronejfbvksdjvnksjbvosjcbvsjdf vkjdfbcvkjx bdxkfjbgvkdjfbvkdjbcvkdfjbvbdfvd
    if blah == "2":
      quit2 = 1
      os.system('clear')
      while quit2 == 1:
        os.system('clear')
        print(f"catnip: {catnip}\n\nyarn balls: {yarnBall}\ntoy mice: {toyMouse}\nfeathers on strings: {featherOnString}\ntoy birds: {toyBird}")
        if chubboTask == 1:
          print(f"Task: yarn balls\nYou will get {reward} catnip per yarn ball given.\n-------------------------\n1 - give yarn balls\n2 - leave")
          choice = input("input: ")
          if choice == "1":
            try:
              amount = int(input("amount: "))
              if amount <= yarnBall:
                yarnBall -= amount
                catnip += reward * amount
            except:
              pass
          if choice == "2":
            quit2 = 0
        if chubboTask == 2:
          print(f"Task: toy mice\nYou will get {reward} catnip per toy mouse given.\n-------------------------\n1 - give toy mice\n2 - leave")
          choice = input("input: ")
          if choice == "1":
            try:
              amount = int(input("amount: "))
              if amount <= toyMouse:
                toyMouse -= amount
                catnip += reward * amount
            except:
              pass
          if choice == "2":
            quit2 = 0
        if chubboTask == 3:
          print(f"Task: feathers on strings\nYou will get {reward} catnip per feathers on strings given.\n-------------------------\n1 - give feathers on strings\n2 - leave")
          choice = input("input: ")
          if choice == "1":
            try:
              amount = int(input("amount: "))
              if amount <= featherOnString:
                featherOnString -= amount
                catnip += reward * amount
            except:
              pass
          if choice == "2":
            quit2 = 0
#this is a marker
        if chubboTask == 4:
          print(f"Task: toy birds\nYou will get {reward} catnip per toy bird given.\n-------------------------\n1 - give toy birds\n2 - leave")
          choice = input("input: ")
          if choice == "1":
            try:
              amount = int(input("amount: "))
              if amount <= toyBird:
                toyBird -= amount
                catnip += reward * amount
            except:
              pass
          if choice == "2":
            quit2 = 0
    if blah == "3":
      quit = 1
      os.system('clear')
          
         
         
def headquarters():
  global cats
  global tiredCats
  global chubboTask
  global catFood
  print("""
----------------------------
     Headquarters
----------------------------

Sprinkles      Socks 
 /\\_/\\        |\\---/|
( o.o )       | o_o |
 > ^ <         \\_^_/

----------------------------
  """)
  print(f"1 - Talk to Sprinkles\n2 - Talk to socks\n3 - Manager's office\n4 - Manafacturing\n5 - Back office\n6 - end day(consumes {cats + tiredCats} catfood)") 
  mlem = input("input: ")
  os.system('clear')
  if mlem == "1":
    sprinkles()
  if mlem == "2":
    socks()
  if mlem == "3":
    managersOffice()
  if mlem == "4":
    manafacturing()
  if mlem == "5":
    backOffice()
  if mlem == "6":
    cats += tiredCats
    tiredCats = 0
    catFood -= cats
    if catFood < 0:
      temp = catFood * -1
      cats -= temp
      catFood = 0
    chubboTask = random.randint(1, 4)
    if chubboTask == 1:
      reward = random.randint(40, 67)
while True:
  stat()
  headquarters()
  
  
