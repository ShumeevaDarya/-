class Tech:
    def __init__(self, Model, Works, Price):
        self.Model = Model
        self.Works = Works
        self.Price = Price

    def get_Model(self):
        print(self.Model)

    def get_Works(self):
        print(self.Works)

    def get_Price(self):
        print(self.Price)

class Worker:
    def __init__(self, FIO, dol):
        self.FIO = FIO
        self.dol = dol

    def get_FIO(self):
        print(self.FIO)

    def get_dol(self):
        print(self.dol)

class Manager(Worker):

    def __init__(self, FIO, dol, tablet, consult_exp):
        super().__init__(FIO, dol)
        self.tablet = tablet
        self.consult_exp = consult_exp
        Managers.append(self.FIO)

    def check(self, Technic, Pokupatel):
        Technic.turn_on(Pokupatel)

    def sell(self, Model, Pokupatel):
        print('Товар ', Model, ' исправен, будете брать?')
        Pokupatel.buy()

    def reject(self, Model, Pokupatel):
        print('Товар ', Model, ' снят с продажи из-за неисправности')
        Pokupatel.reject()

class Cashier(Worker):

    def __init__(self, FIO, dol, sell_exp, uniform):
        super().__init__(FIO, dol, )
        self.sell_exp = sell_exp
        self.uniform = uniform
        Cashiers.append(self.FIO)

    def sell(self, Model, Pokupatel):
        print('*Пробивает товар ', Model, '*')
        Pokupatel.buy()
        self.receipt()

    def receipt(self):
        print('*Напечатал чек*')

class TV(Tech):
    def __init__(self, Model, Works, Price, size, resolution):
        super().__init__(Model, Works, Price)
        self.size = size
        self.resolution = resolution
        TVs.append(self.Model)

    def turn_on(self, Manager, Pokupatel):
        if (self.Works == 'working'):
            print('Телевизор работает, экран загорелся')
            Manager.sell(self, self.Model, Pokupatel)
        else:
            print('Телевизор не работает')
            Manager.reject(self, self.Model, Pokupatel)

class Notebook(Tech):
    def __init__(self, Model, Works, Price, size, resolution):
        super().__init__(Model, Works, Price)
        self.size = size
        self.resolution = resolution
        Notebooks.append(self.Model)

    def turn_on(self, Manager, Pokupatel):
        if (self.Workstate == 'working'):
            print('Ноутбук работает, всё запустилось')
            Manager.sell(self.Model, Pokupatel)
        else:
            print('Ноутбук не работает')
            Manager.reject(self.Model, Pokupatel)

class Monitor(Tech):
    def __init__(self, Model, Works, Price, size, resolution):
        super().__init__(Model, Works, Price)
        self.size = size
        self.resolution = resolution
        Monitors.append(self.Model)

    def turn_on(self, Manager, Pokupatel):
        if (self.Works == 'working'):
            print('Монитор работает, битых пикселей нет')
            Manager.sell(self.Model, Pokupatel)
        else:
            print('Монитор не работает')
            Manager.reject(self.Model, Pokupatel)

class Printer(Tech):
    def __init__(self, Model, Works, Price, colors, dpi):
        super().__init__(Model, Works, Price)
        self.colors = colors
        self.dpi = dpi
        Printers.append(self.Model)

    def turn_on(self, Manager, Pokupatel):
        if (self.Works == 'working'):
            print('Принтер работает, листы напечатаны')
            Manager.sell(self.Model, Pokupatel)
        else:
            print('Принтер не работает')
            Manager.reject(self.Model, Pokupatel)

class Microwave(Tech):
    def __init__(self, Model, Works, Price, Power, Max_Timer):
        super().__init__(Model, Works, Price)
        self.Power = Power
        self.Max_Timer = Max_Timer
        Microwaves.append(self.Model)

    def turn_on(self, Manager, Pokupatel):
        if (self.Works == 'working'):
            print('Монитор работает')
            Manager.sell(self.Model, Pokupatel)
        else:
            print('Монитор не работает')
            Manager.reject(self.Model, Pokupatel)

class Pokupatel:
    def __init__(self, FIO, Manager, Cashier):
        self.FIO = FIO
        self.Manager = Manager
        self.Cashier = Cashier

    def get_FIO(self):
        print(self.FIO)

    def chooseTechRequest(self, Techs):
        print('Вот полный список')
        show_TVs(Techs)

    def choose(self, Model):
        Model.turn_on(self.Manager, self)

    def buy(self):
        print('*Расплачивается и забирает товар*')

    def reject(self):
        print('Жаль, что не работает, я ухожу')

def show_TVs(TVs):
    print(TVs)

def show_Managers():
    print(Managers)

def show_Monitors():
    print(Monitors)

def show_Cashiers():
    print(Cashiers)

def show_Notebooks():
    print(Notebooks)

def show_Printers():
    print(Printers)

def show_Microwaves():
    print(Microwaves)

TVs = []
Managers = []
Monitors = []
Notebooks = []
Printers = []
Microwaves = []
Cashiers = []

Ivan = Manager('Ivan Ivanov', 'Starshiy', 'Samsung', '5')
Petr = Cashier('Petr Petrov', 'Mladshiy', '5', 'Blue')

Samsung = Notebook('Samsung', 'working', '68000', '13"', 'FullHD')
LG = Notebook('LG', '1working', '90000', '15.3"', 'FullHD')

Printer1 = Printer('Printer1', 'working', '70000', '2', '400')
Printer2 = Printer('Printer2', 'working', '40000', '128', '500')

Andrey = Pokupatel('Andreev Andrey', Ivan, Petr)
Andrey.chooseTVrequest()
Andrey.choose(Supra)