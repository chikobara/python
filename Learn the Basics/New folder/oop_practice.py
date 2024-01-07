class Item :
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity: 0):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}','{self.quantity}')"
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.quantity



item1 = Item("phone" , 100 , 3)
item2 = Item("laptop" , 500 ,10)
item3 = Item("hdd", 90, 9)

print(Item.all)