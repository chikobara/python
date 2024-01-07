class Item:
    def __init__(self, name:str , price:float, quantity:0, payrate:float):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.payrate = payrate

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.price * self.payrate
    
item1 = Item('phone', 100, 6 , 0.8)

print(item1.apply_discount())