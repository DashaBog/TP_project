import global_names


class Monster:

    def __init__(self, name):
        self.__name = name
        self.__x = 0
        self.__y = 0
        self.point = 0
        self.__hp = global_names.MONSTERS_STATS[name][0]
        self.__damage = global_names.MONSTERS_STATS[name][1]
        self.__speed = global_names.MONSTERS_STATS[name][2]
        self.__cost = global_names.MONSTERS_STATS[name][3]
        self.injured = False

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        self.__point = point

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        self.__damage = damage

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    """def spawn(self):
        for i in global_names.MONSTERS:
            if not i.point:
                i.point = 1
                break
    """

    def move(self):
        if self.point:
            if global_names.PATH[self.point + 1][1] - \
                    global_names.PATH[self.point][1]:
                if global_names.PATH[self.point + 1][1] > \
                        global_names.PATH[self.point][1]:
                    if self.x + self.speed < 40:
                        self.x += self.speed
                    else:
                        self.x = self.speed - (40 - self.x)
                        self.point += 1
                        if self.point >= len(global_names.PATH) - 2:
                            self.finish()
                else:
                    if 40 + (self.x - self.speed) >= 0:
                        self.x -= self.speed
                    else:
                        self.x = (-1 * (self.x - self.speed) + (
                                self.x - self.speed)) / 2
                        self.point += 1
                        if self.point >= len(global_names.PATH) - 2:
                            self.finish()
            elif global_names.PATH[self.point + 1][0] - \
                    global_names.PATH[self.point][0]:
                if global_names.PATH[self.point + 1][0] > \
                        global_names.PATH[self.point][0]:
                    if self.y + self.speed < 40:
                        self.y += self.speed
                    else:
                        self.y = self.speed - (40 - self.y)
                        self.point += 1
                        if self.point >= len(global_names.PATH) - 2:
                            self.finish()
                else:
                    if 40 + (self.y - self.speed) >= 0:
                        self.y -= self.speed
                    else:
                        self.y = (-1 * (self.y - self.speed) + (
                                self.y - self.speed)) / 2
                        self.point += 1
                        if self.point >= len(global_names.PATH) - 2:
                            self.finish()

        return self

    def injure(self):
        pass

    def kill(self):
        global_names.MONSTERS.pop(global_names.MONSTERS.index(self))
        global_names.CASTLE.money += self.cost

    def finish(self):
        global_names.MONSTERS.pop(global_names.MONSTERS.index(self))
        global_names.CASTLE.hp -= self.damage
        if global_names.CASTLE.hp <= global_names.EMPTY:
            global_names.CASTLE.destroy()


class Bugbear(Monster):
    def __init__(self):
        super().__init__("Bugbear")


class Hobgoblin(Monster):
    def __init__(self):
        super().__init__("Hobgoblin")


class Runner(Monster):
    def __init__(self):
        super().__init__("Runner")


class MonsterCreator:
    def create(self, name):
        monster = None
        if name == "Bugbear":
            monster = Bugbear()
        elif name == "Hobgoblin":
            monster = Hobgoblin()
        elif name == "Runner":
            monster = Runner()
        return monster
