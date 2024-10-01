class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь.
        self.sound = 'Frrr'  # звук, который издаёт лошадь.
        super().__init__()

    # dx - изменение дистанции, увеличивает x_distance на dx.
    def run(self, dx):
        self.x_distance += dx


class Eagle():

    def __init__(self):
        self.y_distance = 0  # Высота полёта.
        self.sound = 'I train eat, sleep, and repeat'  # Звук, который издаёт орёл (отсылка).

    # dy - изменение дистанции, увеличивает y_distance на dy.
    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def __init__(self):
        super().__init__()

    # Где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run и fly соответственно.
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    # Возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
    def get_pos(self):
        return [self.x_distance, self.y_distance]

    # который печатает значение унаследованного атрибута sound.
    def voice(self):
        print(self.sound)


def main():
    p1 = Pegasus()

    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())

    # print(Pegasus.mro())

    p1.voice()


if __name__ == '__main__':
    main()
