class Enemy:
    def __init__(self, name: str, hp: int, attack_power: int):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.attack_power = attack_power
        self.friendship = 0

    def display_enemy_stats(self):
        return f"{self.name} - HP: {self.hp}/{self.maxhp}"

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0