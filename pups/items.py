
class Item:
    def __init__(self, name,stats=None, durability=1, unbreakable=False, ):
        self.name = name
        self.stats = stats
        self.durability = durability
        self.unbreakable = unbreakable

    def use(self):
        if self.durability <= 0:
            return None
        if not self.unbreakable:
            self.durability -= 1
        return self.stats

    def is_broken(self):
        return self.durability <= 0


class Weapon(Item):
    def __init__(self, name,stats = None, durability=5, unbreakable=False, ):
        Item.__init__(self, name, stats, durability, unbreakable)

    def damage(self):
        return self.damage - self.durability