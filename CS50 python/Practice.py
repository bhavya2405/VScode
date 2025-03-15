# print even numbers and the count between 1 and 10

""" # atl + shift + A
count = 0

for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        count += 1
print(f"We have {count} even numbers")
 """


# Class for game character

class character:

    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def speed_boost(self):
        self.speed *= 2

    def damage_boost(self, multiplier):
        self.damage *= multiplier


warrior = character(100, 49, 30)


print(warrior.speed)

warrior.speed_boost()
print(warrior.speed)

warrior.damage_boost(2)
print(warrior.damage)
