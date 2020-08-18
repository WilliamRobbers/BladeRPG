print("Hello, Welcome to BladeRPG!\n")
print("Available classes: (Warrior, Knight, Wizard, Medic)")
PlrClasses = input("Choose 2 classes (seperated by a space): ").split()
classes = {}
classes["plr1"] = [PlrClasses[0]]
classes["plr2"] = [PlrClasses[1]]

print(classes)

#Warrior - Dual Tomohawks, Rush Ability(+DMG, -DEF)
#Knight - Claymore, Sturdy Shield(+DEF, -DMG)
#Wizard - Staff, Blast(DMG to all opponents. 3 round cooldown)
#Medic - Bandages, Heal Surge(Heals entire team. 3 round cooldown)
