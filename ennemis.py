from character import Character
from dice import Dice 

class Zombie(Character):
    def __init__(self, name="Zombie", hp=20, attack_value=5, defense_value=5, dice=Dice("green", 6)):
        super().__init__(name, hp, attack_value, defense_value, dice)

    def compute_damages(self, roll, target):
        print(f" Zombie t'attaque !")
        return super().compute_damages(roll, target)
    
    def compute_raw_damages(self, damages, roll, attacker):
        print(f" Zombie est faible !")
        return super().compute_raw_damages(damages, roll, attacker)

    @staticmethod
    def create_enemy(dice):
        return Zombie("Zombie", hp=20, attack_value=5, defense_value=5, dice=dice)

class Zombie2_0(Zombie):
    def compute_damages(self, roll, target):
        print(f"🧟 Zombie robuste t'attaque ! (+2 dmg)")
        return super().compute_damages(roll, target) + 2
    
    def compute_raw_damages(self, damages, roll, attacker):
        print(f" Zobmie robuste a faim ! (-2 dmg)" )
        return super().compute_raw_damages(damages, roll, attacker) - 2
    
    @staticmethod
    def create_enemy(dice):
        return Zombie2_0("Zombie 2.0", hp=30, attack_value=7, defense_value=7, dice=dice)

class Zombie_guerrier(Zombie):
    def compute_damages(self, roll, target):
        print(f" Zombie guerrier t'attaque ! (+5 dmg)")
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):
        print(f" Zombie guerrier a faim ! (-5 dmg)")
        return super().compute_raw_damages(damages, roll, attacker) - 5
    
    @staticmethod
    def create_enemy(dice):
        return Zombie_guerrier("Zombie guerrier", hp=40, attack_value=10, defense_value=10, dice=dice)

class Skeletons(Character):
    def __init__(self, name="Squelettes", hp=20, attack_value=5, defense_value=3, dice=Dice("White", 6)):
        super().__init__(name, hp, attack_value, defense_value, dice)

    def compute_damages(self, roll, target):
        print(f" Squelette vous attaque ! (+3 dmg)")
        return super().compute_damages(roll, target) + 3
        
    def compute_raw_damages(self, damages, roll, attacker):
        print(f" Squelette prends des dégâts")
        return super().compute_raw_damages(damages, roll, attacker)

    @staticmethod
    def create_enemy(dice):
        return Skeletons("Squelettes", hp=20, attack_value=5, defense_value=3, dice=dice)

class Reinforced_Skeleton(Skeletons):
    def compute_damages(self, roll, target):
        print(f" Squelette renforcé vous attaque ! (+5 dmg)")

ENNEMIES = [Zombie, Zombie2_0, Zombie_guerrier, Skeletons, Reinforced_Skeleton]