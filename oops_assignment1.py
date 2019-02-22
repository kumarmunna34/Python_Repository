class Product:
    def __init__(x,name,cost_price,sales_price,discount):
        x.name = name
        x.cost_price = cost_price
        x.sales_price = sales_price
        x.discount = discount
    def get(y):
        print("Available products are: \n1. mobile\n2. laptop\n3. tablet")
        choice = int(input("Enter your choice of product: "))
        return choice
    def get_cost_price(prod):
        return prod.cost_price
    def get_sales_price(prod):
        return prod.sales_price
    def get_discount(prod):
        return prod.discount  
mobile = Product("mi",10000,15000,"10%")
laptop = Product("hp",35000,40000,"15%")
tablet = Product("kindle",9000,10000,"5%")
choice = mobile.get()
if choice == 1:
    print("product: ",mobile.name,",cost price: ",mobile.get_cost_price(),",sales price: ",mobile.get_sales_price(),",discount: ",mobile.get_discount())
elif choice == 2:
    print("product: ",laptop.name,",cost price: ",laptop.get_cost_price(),",sales price: ",laptop.get_sales_price(),",discount: ",laptop.get_discount())
elif choice == 3:
    print("product: ",tablet.name,",cost price: ",tablet.get_cost_price(),",sales price: ",tablet.get_sales_price(),",discount: ",tablet.get_discount())