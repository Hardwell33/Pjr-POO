import character
import random
import ennemis
import dice

# Créer une instance de dé
dice = dice.Dice(color="black", faces=6)

# Créer des instances de personnages
player = character.Character("Player", 100, 10, 5, dice)
enemy = random.choice(ennemis.ENNEMIES).create_enemy(dice)
druid = character.Druid("Druid", 120, 8, 6, dice, 20)

# Faire combattre le joueur et le druide contre l'ennemi
player.attack(enemy)
druid.heal(player)
player.attack(enemy)

# Afficher les caractéristiques des personnages
print(player)
print(enemy)
print(druid)