import random

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self,name,hp,mp,atk,df,magic,items):
        self.maxhp=hp
        self.hp=hp
        self.maxmp=mp
        self.mp=mp
        self.atkl=atk-10
        self.atkh=atk+10
        self.df=df
        self.magic=magic
        self.items=items
        self.actions=["Attack","Magic","Items"]
        self.name=name

    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)

    def take_damage(self,dmg):
        self.hp-=dmg
        if self.hp<0:
            self.hp=0
        return self.hp

    def heal_damage(self,dmg):
        self.hp += dmg
        if self.hp>self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self,cost):
        self.mp-=cost
        if self.mp<0:
            self.mp=0

    def show_actions(self):
        print("Actions:")
        i=1
        for action in self.actions:
            print(str(i),".",action)
            i+=1

    def show_magic(self):
        print("Magic:")
        i=1
        for spell in self.magic:
            print(str(i),".",spell.name,"(cost:",str(spell.cost)+")")
            i+=1

    def show_items(self):
        print("Items:")
        i=1
        for item in self.items:
            print(str(i),".",item["item"].name,":",item["item"].desc,"(x",item["quantity"],")")
            i+=1

    def show_players(self,players):
        print("Players:")
        i=1
        for player in players:
            print(str(i),".",player.name)
            i+=1

    def show_enemies(self,enemies):
        print("Enemies:")
        i=1
        for enemy in enemies:
            print(str(i),".",enemy.name)
            i+=1

    def get_stats(self):
        str_name=self.name+":"
        str_hp=str(self.hp)+"/"+str(self.maxhp)
        str_mp=str(self.mp)+"/"+str(self.maxmp)
        bar_hp=""
        bar_mp=""
        bar_hp_left=""
        bar_mp_left=""
        bar_hp_ticks=(self.hp/self.maxhp)*100/4
        bar_mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while len(str_name)<10:
            str_name+=" "

        while len(str_hp)<9:
            str_hp=" "+str_hp

        while len(str_mp)<7:
            str_mp=" "+str_mp

        while bar_hp_ticks>0:
            bar_hp+="█"
            bar_hp_ticks-=1

        while len(bar_hp_left+bar_hp)<25:
            bar_hp_left+="█"

        while bar_mp_ticks>0:
            bar_mp+="█"
            bar_mp_ticks-=1

        while len(bar_mp_left+bar_mp)<10:
            bar_mp_left+="█"

        print(str_name+"  "+str_hp+" |"+Bcolors.OKGREEN+bar_hp+Bcolors.ENDC+bar_hp_left+"|  "
              +str_mp+" |"+Bcolors.OKBLUE+bar_mp+Bcolors.ENDC+bar_mp_left+"|")

    def get_enemy_stats(self):
        str_name=self.name+":"
        str_hp=str(self.hp)+"/"+str(self.maxhp)
        str_mp=str(self.mp)+"/"+str(self.maxmp)
        bar_hp=""
        bar_mp=""
        bar_hp_left=""
        bar_mp_left=""
        bar_hp_ticks=(self.hp/self.maxhp)*100/4
        bar_mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while len(str_name)<10:
            str_name+=" "

        while len(str_hp)<9:
            str_hp=" "+str_hp

        while len(str_mp)<7:
            str_mp=" "+str_mp

        while bar_hp_ticks>0:
            bar_hp+="█"
            bar_hp_ticks-=1

        while len(bar_hp_left+bar_hp)<25:
            bar_hp_left+="█"

        while bar_mp_ticks>0:
            bar_mp+="█"
            bar_mp_ticks-=1

        while len(bar_mp_left+bar_mp)<10:
            bar_mp_left+="█"

        print(str_name+"  "+str_hp+" |"+Bcolors.FAIL+bar_hp+Bcolors.ENDC+bar_hp_left+"|  "+str_mp+" |"+Bcolors.OKBLUE+bar_mp+Bcolors.ENDC+bar_mp_left+"|")

