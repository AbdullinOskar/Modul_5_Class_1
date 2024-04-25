        # "Специальные методы классов"

# Создайте новый класс House
# Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
# Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors на параметр floors и
# выводить в консоль numberOfFloors
# Полученный код напишите в ответ к домашему заданию

class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors=5):
        self.numberOfFloors = floors
        print("Number of Floors: ", self.numberOfFloors)

home = House()
home2 = House()

print(home.numberOfFloors)
home.setNewNumberOfFloors(10)
home.setNewNumberOfFloors()

print(home2.numberOfFloors)
home2.setNewNumberOfFloors(20)
home2.setNewNumberOfFloors()
