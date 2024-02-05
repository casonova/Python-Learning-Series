class Player:
    def __init__(self, name, hp, mp):
        self.name=name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffilated"

    def add_skill(self, skill, mana):
        if skill not in self.skills.keys():
            self.skills[skill] = mana
            return f"Skill {skill} added to the collection of the player {self.name}"
        return "Skill already added"
    
    def player_info(self):
        skills = '\n'.join([f"{skill} - {mana}" for skill, mana in self.skills.items()])
        return f"Name: {self.name}\nGuild:{self.guild}\nHP:{self.hp}\nMP:{self.mp}\n{skills}"


player1 = Player("Player1",50,50)
player1.add_skill("Sword",30)
player1.add_skill("Sheild",20)
print(player1.player_info())
        