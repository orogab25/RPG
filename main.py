from classes.game import Person,Bcolors
from classes.magic import Spell
from classes.inventory import Item

import random

#Black magic
fire=Spell("Fire",10,100,"black")
thunder=Spell("Thunder",10,100,"black")
blizzard=Spell("Blizzard",10,100,"black")
meteor=Spell("Meteor",20,200,"black")
quake=Spell("Quake",14,140,"black")

#White magic
cure=Spell("Cure",12,120,"white")
cura=Spell("Cura",18,200,"white")

#Items
healing_potion=Item("Healing potion","healing_potion","Heals 50 HP",50)
high_healing_potion=Item("High healing potion","healing_potion","Heals 100 HP",100)
super_healing_potion=Item("Super healing potion","healing_potion","Heals 200 HP",200)
elixer=Item("Elixer","elixer","Fully restores HP/MP of one party member.",9999)
mega_elixer=Item("Mega elixer","elixer","Fully restores HP/MP of all party members.",9999)
grenade=Item("Grenade","grenade","Deals 200 damage.",200)

#Player property
player_spells=[fire,thunder,blizzard,meteor,cure,cura]

player_items=[{"item":healing_potion,"quantity":5},
              {'item':elixer,"quantity":1},
              {"item":grenade,"quantity":3}]

player2_items=[{"item":healing_potion,"quantity":5},
              {'item':elixer,"quantity":1},
              {"item":grenade,"quantity":3}]

player3_items=[{"item":healing_potion,"quantity":5},
              {'item':elixer,"quantity":1},
              {"item":grenade,"quantity":3}]

#Characters
player=Person("Valos",500,50,50,50,player_spells,player_items)
player2=Person("Nick",500,50,50,50,player_spells,player2_items)
player3=Person("Robot",500,50,50,50,player_spells,player3_items)

enemy=Person("Enemy1",1000,25,25,25,[],[])
enemy2=Person("Enemy2",1200,25,25,25,[],[])
enemy3=Person("Enemy3",900,25,25,25,[],[])

players=[player,player2,player3]
enemies=[enemy,enemy2,enemy3]

#Battle
print(Bcolors.FAIL+"\nBattle!\n"+Bcolors.ENDC)
battle=True
fallen=[]

while battle:
    print("=================")

    for player in players:
        player.get_stats()

    print("-----------------")

    for enemy in enemies:
        enemy.get_enemy_stats()

    print("=================")

    for player in players:
        print("\n"+player.name)
        print("-----------------")
        player.show_actions()
        choice=int(input("Choose action:"))-1
        running=True

        #Attack
        if choice==0:
            dmg=player.generate_damage()
            player.show_enemies(enemies)
            choice_enemy=int(input("Choose an enemy:"))-1
            enemies[choice_enemy].take_damage(dmg)
            print("You attacked",enemies[choice_enemy].name,"for",dmg,"points of damage.")

        # Magic
        while choice == 1 and running==True:
            print("-----------------")
            player.show_magic()
            choice_spell = int(input("Choose spell:")) - 1

            if choice_spell==-1:
                continue

            spell = player.magic[choice_spell]

            if player.get_mp() < spell.cost:
                print(Bcolors.FAIL, "Not enough mana.", Bcolors.ENDC)
                continue

            dmg_spell = spell.generate_damage()

            # White
            if spell.type == "white":
                player.show_players(players)
                choice_player = int(input("Choose an enemy:")) - 1
                players[choice_player].heal_damage(dmg_spell)
                print("You healed",players[choice_player].name,"for", dmg_spell, "points of damage.")

            # Black
            elif spell.type == "black":
                player.show_enemies(enemies)
                choice_enemy = int(input("Choose an enemy:")) - 1
                enemies[choice_enemy].take_damage(dmg_spell)
                print("You attacked",enemies[choice_enemy].name,"for", dmg_spell, "points of damage.")

            player.reduce_mp(spell.cost)
            running=False

        #Items
        while choice == 2 and running==True:
            print("-----------------")
            player.show_items()
            choice_item = int(input("Choose item:")) - 1

            if choice_item==-1:
                continue

            item = player.items[choice_item]["item"]

            if player.items[choice_item]["quantity"]==0:
                print("No more left.")
                continue

            player.items[choice_item]["quantity"]-=1

            # Healing potion
            if item.type == "healing_potion":
                player.heal_damage(item.prop)
                print("You healed for ", item.prop, "points of damage.")

            # Elixir
            if item.type == "elixir":
                player.show_players(players)
                choice_player = int(input("Choose an enemy:")) - 1
                player[choice_player].hp=player.maxhp
                player[choice_player].mp=player.maxmp
                print("You healed",player[choice_player].name,"to max HP/MP.")

            # Grenade
            elif item.type == "grenade":
                player.show_enemies(enemies)
                choice_enemy = int(input("Choose an enemy:")) - 1
                enemies[choice_enemy].take_damage(item.prop)
                print("You attacked",enemies[choice_enemy].name,"for", item.prop, "points of damage.")

            running = False

        if enemies[choice_enemy].get_hp() == 0:
            print(Bcolors.OKGREEN,enemies[choice_enemy].name,"has been defeated!", Bcolors.ENDC)
            del enemies[choice_enemy]

        if len(enemies)==0:
            print("You won!")
            battle=False
            break

    for enemy in enemies:
        enemy_choice=random.randrange(0,3)
        target = random.randrange(0, len(players))

        if enemy_choice==0:
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print("\nEnemy attacked", players[target].name, "for ", enemy_dmg, "points of damage.")

        elif enemy_choice==1:
            enemy_choice_spell=random.randrange(0,len(enemy.magic))
            enemy_spell=enemy.magic[enemy_choice_spell]
            enemy_dmg_spell=enemy_spell.generate_damage()

        if players[target].get_hp() == 0:
            print(Bcolors.FAIL,players[target].name,"has fallen!", Bcolors.ENDC)
            fallen+=players[target]
            del players[target]

        if len(players)==0:
            print("You lost!")
            battle = False
            break
