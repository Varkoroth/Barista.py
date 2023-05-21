print ("Hello, welcome to the DarkArmy CoffeeShop!\n")

name = input("What is your name?\n \n")

print("\nHello " + name + ", thank you for coming in today!\n")

menu = "Black Coffee, Espresso, Latte, Cappucino, Ice Latte"
price = 3

print("What would you like from our menu? Here's what we're serving.\n" + menu + "\n")

while True:
	order = input()

	if order == "Black Coffee" or order == "Espresso" or order == "Latte" or order == "Cappucino" or order == "Ice Latte":
		break
		
	else:
		print("\nSorry, we do not serve this!\n")
		
quantity = input("\nHow many would you like?\n\n")
bill = price * int(quantity)

print("\nYour total is $" + str(bill) + "! Your order will be ready in a bit.\n")

input("Press Enter to pay and leave!")

exit
