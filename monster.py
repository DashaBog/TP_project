import cell
import global_names


class Monster:
    stats = {"Bugbear": [12, 1, 1, 1], "Hobgoblin": [20, 2, 1, 5], "Runner": [4, 1, 3, 1]}

    def __init__(self, name):
        self.__name = name
        self.__x = 0
        self.__y = 0
        self.point = 0
        self.__hp = self.stats[name][0]
        self.__damage = self.stats[name][1]
        self.__speed = self.stats[name][2]
        self.__cost = self.stats[name][3]
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

    def move(self, CASTLE, PLAY, LEVELS, SPAWNER, MENU):
        """
                Перемещает монстра в соответствии  с его скоростью
                """
        if global_names.PATH[self.point + 1][1] - \
                global_names.PATH[self.point][1]:
            if global_names.PATH[self.point + 1][1] > \
                    global_names.PATH[self.point][1]:
                if self.x + self.speed < cell.Cell.SIZE:
                    self.x += self.speed
                else:
                    self.x = self.speed - (cell.Cell.SIZE - self.x)
                    self.point += 1
                    if self.point >= len(global_names.PATH) - 2:
                        PLAY, LEVELS, SPAWNER, CASTLE, MENU = self.finish(CASTLE, PLAY, LEVELS, SPAWNER, MENU)
            else:
                if cell.Cell.SIZE + (self.x - self.speed) >= 0:
                    self.x -= self.speed
                else:
                    self.x = (-1 * (self.x - self.speed) + (
                            self.x - self.speed)) / 2
                    self.point += 1
                    if self.point >= len(global_names.PATH) - 2:
                        PLAY, LEVELS, SPAWNER, CASTLE, MENU = self.finish(CASTLE, PLAY, LEVELS, SPAWNER, MENU)
        elif global_names.PATH[self.point + 1][0] - \
                global_names.PATH[self.point][0]:
            if global_names.PATH[self.point + 1][0] > \
                    global_names.PATH[self.point][0]:
                if self.y + self.speed < cell.Cell.SIZE:
                    self.y += self.speed
                else:
                    self.y = self.speed - (cell.Cell.SIZE - self.y)
                    self.point += 1
                    if self.point >= len(global_names.PATH) - 2:
                        PLAY, LEVELS, SPAWNER, CASTLE, MENU = self.finish(CASTLE, PLAY, LEVELS, SPAWNER, MENU)
            else:
                if cell.Cell.SIZE + (self.y - self.speed) >= 0:
                    self.y -= self.speed
                else:
                    self.y = (-1 * (self.y - self.speed) + (
                            self.y - self.speed)) / 2
                    self.point += 1
                    if self.point >= len(global_names.PATH) - 2:
                        PLAY, LEVELS, SPAWNER, CASTLE, MENU = self.finish(CASTLE, PLAY, LEVELS, SPAWNER, MENU)

        return PLAY, LEVELS, SPAWNER, CASTLE, MENU

    def kill(self, CASTLE):
        """
        Убивает монстра
        """
        global_names.MONSTERS.pop(global_names.MONSTERS.index(self))
        CASTLE.money += self.cost

    def finish(self, CASTLE, PLAY, LEVELS, SPAWNER, MENU):
        """
        Запускается если монстр дошел до замка
        """
        global_names.MONSTERS.pop(global_names.MONSTERS.index(self))
        CASTLE.hp -= self.damage
        if CASTLE.hp <= global_names.EMPTY:
            PLAY, LEVELS, SPAWNER, CASTLE, MENU = CASTLE.destroy(PLAY, LEVELS, SPAWNER, CASTLE, MENU)
        return PLAY, LEVELS, SPAWNER, CASTLE, MENU


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
