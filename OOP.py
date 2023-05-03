class Dog:
    def bark(self): # имя self для первого аргумента метода это общепринятое правило
        print('Bow-wow!')

my_dog = Dog()
my_dog.bark()      # вызовется функция Dog.say_wow с параметром self = my_dog
another_dog = Dog()
another_dog.bark()
