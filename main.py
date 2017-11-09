from classes.game import Person, bcolors
from classes.magic import Spell

fire = Spell('fire',10,100,'black')
thunder = Spell('Thunder',10,100,'black')
blizzard = Spell('Blizzard',10,100,'black')
meteor = Spell('Meteor',20,200,'black')
quake = Spell('Quake',14,140,'black')

cure = Spell('Cure',12,120,'white')
cura = Spell('Cura',18,200,'white')



magic =[{'name': 'fire' , 'cost': 10, 'dmg': 100},
        {'name': 'thunder', 'cost': 12, 'dmg': 124},
        {'name': 'blizzard', 'cost': 10, 'dmg': 100}]

player = Person(460,65,60,34,[fire,thunder,blizzard,meteor,cure,cura])
enemy = Person(1200,65,45,25,[])

running = True

print(bcolors.FAIL + bcolors.BOLD + "An enemy attacks" + bcolors.ENDC)


while running:
    print('+++++++++++++++++')
    player.choose_action()
    choice = input("Choose Action:")
    index = int(choice) - 1
    print('You chose', choice)

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print('You attacked for', dmg, "points of damage. Enemy HP:", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input('Choose Magic:')) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_dmg()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL +"\nNot enough MP\n" +bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == 'white':
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + '\n' + spell.name + ' heals for', str(magic_dmg), 'HP' + bcolors.ENDC)
        elif spell.type == 'black':
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

        print('---------------')
        print('Enemy HP:', bcolors.FAIL + str(enemy.get_hp()) + '/' + str(enemy.get_max_hp()) + bcolors.ENDC + '\n')
        print('Your HP:', bcolors.OKGREEN +str(player.get_hp())+ '/' + str(player.get_max_hp()) + bcolors.ENDC + '\n')
        print('Your MP:', bcolors.OKBLUE + str(player.get_mp())+ '/' + str(player.get_max_mp()) + bcolors.ENDC + '\n')

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "Player HP", player.get_hp())

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN +'You win!' + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + 'You Lost' + bcolors.ENDC)
        running = False