from random import randint
class fighter:
  def __init__(self, name, health = 120, armour = 3, weapon = 6):
    self.name = name
    self.health = health
    self.armour = armour
    self.weapon = weapon
  def __repr__(self):
    print("Hi my name is {name}. I am a fighter, I have {health} hp a {armour} armour class and a {weapon} weapon class".format(name = self.name, health = self.health,armour = self.armour,weapon = self.weapon))  
  def melee_attack(self, target):
    roll = randint(1, 20)
    power = (roll + self.weapon) / target.armour
    dmg = round(power)
    target.health = target.health - dmg
    print("{name}, swings at {target} for {dmg} damage".format(name = self.name, target = target.name, dmg = dmg))
  def buff(self):
    self.armour = self.armour + 1
    print("{name} raised their shield".format(name = self.name))
  def special_attack(self, target):
    roll = randint(1, 20)
    power = (roll + 10 + self.weapon) / target.armour 
    dmg = round(power)
    target.health = target.health - dmg
    print("{name} recklessly attacks {target} for {dmg} damage".format(name = self.name, target = target.name, dmg = dmg))

class rouge:
  def __init__(self, name, health = 100, armour = 2, weapon = 3):
    self.name = name
    self.health = health
    self.armour = armour
    self.weapon = weapon
  def melee_attack(self, target):
    roll = randint(1, 20)
    power = (roll + self.weapon) / target.armour
    dmg = round(power)
    target.health = target.health - dmg
    print("{name}, swings at {target} for {dmg} damage".format(name = self.name, target = target.name, dmg = dmg))
  def __repr__(self):
    print("Hi my name is {name}. I am a rogue I have {heath} hp a {armour} armour class and a {weapon} weapon class".format(name = self.name, health = self.health, armour = self.armour, weapon = self.weapon))
  def buff(self):
    self.weapon = self.weapon + 3
    print("{name} poisons their weapon".format(name = self.name))
  def special_attack(self, target):
    roll = randint(1, 20)
    power = roll + self.weapon  
    dmg = round(power)
    target.health = target.health - dmg
    print("{name} attacks {target} sliding through their armour for {dmg} damage".format(name = self.name, target = target.name, dmg = dmg))
class sorcerer:
  def __init__(self, name, health = 80, armour = 1, weapon = 1):
    self.name = name
    self.health = health
    self.armour = armour
    self.weapon = weapon 
  def melee_attack(self, target):
    roll = randint(1, 20)
    power = (roll + self.weapon) / target.armour
    dmg = round(power)
    target.health = target.health - dmg
    print("{name}, swings at {target} for {dmg} damage".format(name = self.name, target = target.name, dmg = dmg))   
  def __repr__(self):
    print("Hi my name is {name}. I am a sorcerer I have {heath} hp a {armour} armour class and a {weapon} weapon class".format(name =self.name, health = self.health, armour = self.armour, weapon = self.weapon))  
  def buff(self):
    self.health = self.health + 10
    print("{name} uses healing magic on themself".format(name = self.name))
  def special_attack(self, target):
    target.health = target.health - 15
    print("{name} throws a fireball at {target}".format(name = self.name, target = target.name))
bobo = fighter("BoBo")
hyphen = rouge("Hyphen")
futt = sorcerer("Futt")


def duel(player1, player2):
  print("{player1} challenges {player2} to a duel  \n FIGHT".format(player1 = player1.name, player2 = player2.name))

  while player1.health > 0 and player2.health > 0:
    play1_move = (input("{player1} what move do you make? \n 1.) melee attack \n 2.) buff \n 3.) special attack".format(player1 = player1.name)))
    if play1_move == "1":
      player1.melee_attack(player2)
    elif play1_move == "2":
      player1.buff()
    elif play1_move == "3": 
      player1.special_attack(player2)
    else:
      print("you failed to make a move next time select 1 2 or 3")

    play2_move = (input("{player2} what move do you make? \n 1.) melee attack \n 2.) buff \n 3.) special attack".format(player2 = player2.name)))
    if play2_move == "1":
      player2.melee_attack(player1)
    elif play2_move == "2":
      player2.buff()
    elif play2_move == "3": 
      player2.special_attack(player1)
    else:
      print("you failed to make a move next time select 1 2 or 3")

  if player1.health > 0:
    print ("{player1} has defeated {player2}".format(player1 = player1.name, player2 = player2.name))
  else: print("{player2} has defeated {player1}".format(player1 = player1.name, player2 = player2.name))        
    

play1_char = input("player 1 pick your hero \n 1.) BoBo the fighter \n 2.) Hyphen the rogue \n 3.) Futt the sorcerer")
if play1_char == "1": player1 = bobo 
elif play1_char == "2": player1 = hyphen
elif play1_char == "3": player1 = futt 
print("player 1 has selected {name}".format(name = player1.name)) 
play2_char = input("player 2 pick your hero \n 1.) BoBo the fighter \n 2.) Hyphen the rogue \n 3.) Futt the sorcerer")
if play2_char == "1": player2 = bobo 
elif play2_char == "2": player2 = hyphen
elif play2_char == "3": player2 = futt 
print("player 2 has selected {name}".format(name = player1.name))

duel(player1, player2)