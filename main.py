from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random



fire = Spell('fire',10,100,'black')
thunder = Spell('Thunder',10,100,'black')
blizzard = Spell('Blizzard',10,100,'black')
meteor = Spell('Meteor',20,200,'black')
quake = Spell('Quake',14,140,'black')

cure = Spell('Cure',12,120,'white')
cura = Spell('Cura',18,200,'white')

potion = Item("Potion", "potion", "heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "heals 100 HP",100)
superpotion = Item("Super-Potion", "potion", "heals 500 HP",500)
elixer = Item("Elxier","elxier","Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElxier", "elxier", "Fully restores party's MP/HP", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_magic = [fire,thunder,blizzard,meteor,cure,cura]
player_items = [{'item':potion,'quantity': 5},{'item':hipotion,'quantity': 5},
                {'item':superpotion,'quantity': 5},{'item':elixer,'quantity': 5},
                {'item':hielixer,'quantity': 5},{'item':grenade,'quantity': 5}]

player1 = Person('Jay',4600,65,500,34,player_magic,player_items)
player2 = Person('Red',4600,65,500,34,player_magic,player_items)
player3 = Person('Kil',4600,65,500,34,player_magic,player_items)

enemy1 = Person('Mean',11200,65,750,25,[],[])
enemy2 = Person('Weak',1250,130,560,300,[],[])
enemy3 = Person('Weak',1250,130,560,300,[],[])

players=[player1,player2,player3]
enemies = [enemy1,enemy2,enemy3]

running = True

print(bcolors.FAIL + bcolors.BOLD + "An enemy attacks" + bcolors.ENDC)


while running:
    print('+++++++++++++++++')
    print('\n\n')
    print('NAME                 HP                                     MP')

    for player in players:
        player.get_stats()

    print('\n\n')
    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("    Choose Action:")
        index = int(choice) - 1
        print('You chose', choice)

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            print('You attacked ' + enemies[enemy].name + ' for', dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + ' has been defeated')
                del enemies[enemy]
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input('    Choose Magic:')) - 1

            if magic_choice == -1:
                continue

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
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + ' has been defeated')
                    del enemies[enemy]
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose Item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]['item']
            if player.items[item_choice]['quantity'] == 0:
                print(bcolors.FAIL + '\n' + 'None left...' + bcolors.ENDC)
                continue

            player.items[item_choice]['quantity'] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print( bcolors.OKGREEN + "\n" + item.name + " Heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == 'elxier':
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + '\n' + item.name + ' fully restores MP/HP' + bcolors.ENDC)
            elif item.type == 'attack':
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + '\n' + item.name + ' deals', str(item.prop), 'points of damage to ' + enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + ' has been defeated')
                    del enemies[enemy]


            print('---------------')
            print('Enemy HP:', bcolors.FAIL + str(enemy.get_hp()) + '/' + str(enemy.get_max_hp()) + bcolors.ENDC + '\n')
            print('Your HP:', bcolors.OKGREEN +str(player.get_hp())+ '/' + str(player.get_max_hp()) + bcolors.ENDC + '\n')
            print('Your MP:', bcolors.OKBLUE + str(player.get_mp())+ '/' + str(player.get_max_mp()) + bcolors.ENDC + '\n')

    enemy_choice = 1
    target = random.randrange(0,3)


    enemy_dmg = enemies[0].generate_damage()
    players[target].take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() ==0:
            defeated_players += 1

    if defeated_enemies == 2:
        print(bcolors.OKGREEN + 'You win!' + bcolors.ENDC)
        running = False

    elif defeated_players == 2:
        print(bcolors.FAIL + 'You Lost' + bcolors.ENDC)
        running = False