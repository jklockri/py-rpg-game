from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

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
player_items = [potion,hipotion,superpotion,elixer,hielixer]

player = Person(460,65,60,34,player_magic,player_items)
enemy = Person(1200,65,45,25,[],[])

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
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose Item: ")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]

        if item.type == "potion":
            player.heal(item.prop)
            print( bcolors.OKGREEN + "\n" + item.name + " Heals for", str(item.prop), "HP" + bcolors.ENDC)


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