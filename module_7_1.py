class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def name(self):
        return self.name


class Shop:
    def __init__(self, __file_name='products.txt'):
        self.__file_name = __file_name

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read()

    def add(self, *products):
        with open(self.__file_name, 'a') as file:
            for i in products:
                if Product.__str__(i) in open(self.__file_name).read():
                    print(f'Продукт {Product.name(i)} уже есть в магазине')
                else:
                    file.write(Product.__str__(i) + '\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
