class Player:
    def __init__(self, name: str):
        self.name = name
        self.hp = 100
        self.maxhp = 100
        self.exp = 0
        self.game_over = False
        self.gold = 100
        self.inventory = ['chicken leg', 'chicken leg']
        self.equipped_weapon = None

    def display_player_stats(self):
        return f"Name: {self.name}  HP: {self.hp}/{self.maxhp}  EXP: {self.exp}  Gold: {self.gold}"

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.game_over = True

    def heal(self, amount: int):
        self.hp += amount
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def equip_weapon(self, weapon):
        self.equipped_weapon = weapon

    def increase_exp(self):
        self.exp += 1
        self.maxhp += 10
        self.hp += 10