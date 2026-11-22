class product:
    def __init__(self,product_name,price):
        self.product_name=product_name
        self.price=price

    def display(self):
        print(self.product_name)
        print(self.price)

product_name1=input("enter the product")
price1=int(input("enter the price"))
p1=product(product_name1,price1)
product_name2=input("enter the product")
price2=int(input("enter the price"))
p2=product(product_name2,price2)
p1.display()
p2.display()