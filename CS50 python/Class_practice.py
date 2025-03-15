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

    def take_damage(self, amount):
        self.health -= amount


# creating a child class
class Warrior(character):
    def __init__(self, health, damage, speed):
        # super() is used to call the parent class constructor
        super().__init__(health, damage, speed)
        self.toughness_modifier = 0.90

    def take_damage(self, amount):
        modified_amount = amount * self.toughness_modifier
        super().take_damage(modified_amount)


"""  ## can be done like this too but for clarity I did above way 
    def take_damage(self, amount):
        amount *= self.toughness_modifier
        super().take_damage(amount)
 """

warrior = Warrior(100, 49, 30)


warrior.take_damage(20)
print(f"The health of the warrior is {warrior.health}")


print(warrior.speed)


warrior.speed_boost()
print(warrior.speed)


warrior.damage_boost(2)
print(warrior.damage)
