from datastructures.linkedlist import LinkedList
from datastructures.array import Array
from datastructures.arraystack import ArrayStack
from datastructures.bag import Bag
import copy

class Menu:
    """This Class is what stores each of the drinks into an object, which is added to the array in the main program"""
    def __init__(self, name:str, size:str, price:float) -> None:
        """
        Initializes the drink to be added to the menu with the given drink name, size, and price.

        Args:
            name(str): The name of the drink.
            size (str): The size of the drink, which is always medium as per the project instructions.
            price(float): The price of the drink, stored as a float because it's a decimal.

        Returns:
            None
        """
        self._name = name
        self._size = size
        self._price = price
    
    def get_name(self) -> str:
        """
        Used to return the name of the drink without users directly accessing the self._name variable.

        Args:
            None

        Returns:
            str: self._name
        """
        return self._name
    
    def get_size(self) -> str:
        """
        Used to return the size of the drink without users directly accessing the self._size variable
        
        Args:
            None
        
        Returns:
            str: self._size
        """
        return self._size
    
    def get_price(self) -> float:
        """
        Used to return the price of the drink without users directly accessing the self._price variable.
        
        Args:
            None
        
        Returns:
            float: self._price"""
        return self._price
    
    def display_drink(self) -> str:
        """Displays the drink
        
        Args:
            None
        
        Returns:
            str
        """
        return (f"{self._name} - {self._price}")

class CustomerOrder:
    """This is where all the Customer's drinks are stored"""
    def __init__(self, name:str)-> None:
        """
        Initializes the customer, and the list that all their drinks will be stored in.

        Args:
            name(str): Customer's name
        
        Returns:
            None
        """
        self._name = name
        self._order = []

    def add_drink(self, drink: str, size: str, price: float, customization: str) -> None:
        """
        Where the user will add a drink to the current orders linked list

        Arg:
            drink(str): the drink name
            size (str): the drink size
            price (float): the drink cost

        Return:
            None

        """
        drink = OrderItem(drink,size,price,customization)
        self._order.append(drink) #This may be the issue?
        #Need to somehow add order to history

    def get_order(self):
        """returns order
        
        Args:
            None
            
        Returns: 
        List
        """
        return self._order
    
    def drink_name(self, index: int):
        """Returns the drink name
        
        Args:
            index(str)
            
        Returns:
            str
        """
        return self._order[index].drink()
    
    def drink_price(self,index:int):
        """Returns the drink price
        
        Args:
            index(int)
            
        Returns:
        str
        """
        return self._order[index].price()
    
    def drink_size(self, index:int):
        """returns drink size
        Args: 
            index(int)
        Returns:
            str"""
        return self._order[index].size()
    
    def drink_customization (self, index:int):
        """returns drink customization
        Args:
            index(int)
            
        Returns:
            str
        """
        return self._order[index].customization()
    
    def name(self):
        """Returns customer name
        Args:
            None
        Returns:
            str
            """
        return self._name
    



    def display_order(self):   #FIX, ITS NOT PRINTING CORRECTLY
        """This is how the order is displayed
        Arg:
        None
        
        Return:
        str
        """
        temp_list = []
        for i in range(len(self._order)):
            temp_list.append(f"{self._order[i]._drink} ({self._order[i]._customization})")

        return (f"{self._name}: {str(temp_list)}")

class OrderItem:
    def __init__ (self, drink:str, size:str, price:float, customization:str) -> None:
        """Initializes Order
        Args:
            drink(str): drink name
            size(str): drink size (medium)
            price(float): price of drink
            customization(str): Customer's customization they inputted
        
        Returns:
            None"""
        self._drink = drink
        self._size = size
        self._price = price
        self._customization = customization

    def drink(self):
        """returns drink name
        
        Args:
            None
        Return:
            str
        """
        return self._drink
    
    def size(self):
        """returns drink size (always medium, in this program)
        Args:
            None
        Returns;
            str"""
        return self._size
    
    def price(self):
        """Returns price of drink

        Args:
            None
        Returns:
            str
        """
        return self._price
    
    def customization(self):
        """returns the customer's customization
        
        Args:
            None
        Returns:
            str """
        return self._customization
    
class BistroSystem:
    def __init__(self, menu):
        """Initializes the Bistro System
        Args:
            menu(List): The drink menu
        Returns:
            None"""
        self._open_orders = []
        self._completed_orders = ArrayStack(5)
        self._total_orders = Bag()
        self._menu = menu

    def add_order(self, order) -> None:
        """Adds an order to the total orders (for end of day report) and to the current open orders.
        Arg:
            order(Object): order being added to the system's history.
        Returns:
            None
            """
        for i in range(len(order.get_order())):
            self._total_orders.add(order.drink_name(i))
        self._open_orders.append(order)
        

    def current_order(self):
        """Returns the current order being worked on
        Arg:
            None
        Returns:
            Object"""
        return (self._open_orders[0])
    
    def open_orders(self) -> None:
        """Prints all the open orders
        Arg:
            None
        Returns:
            None"""
        for i in range(len(self._open_orders)):
            print(f"{i+1}. {self._open_orders[i].display_order()}")

    def complete_order(self):
        """Marks the current order as complete and adds it to the completed orders data structure
        
        Args:
            None
        Returns:
            Str"""
        if len(self._open_orders) == 0:
            return ("❌ There are not current orders!")
        completed_order = self.current_order()
        self._completed_orders.push(completed_order)
        self._open_orders.pop()
        return (f"✅ Completed Order for {completed_order.name()}!") #left off here
    
    def total_sales(self):
        """Prints the total sales from the day (end of day report)
        Arg:
            None
        Returns:
            None"""
        total_revenue = 0
        print(f"Drink Name - Qty Sold - Total Sales")
        for drink in self._menu:
            count = (self._total_orders.count(drink.get_name()))
            individual_rev = (count * drink.get_price())
            total_revenue += individual_rev
            print (f"{drink.get_name()} - {count} - ${str(individual_rev)}")
             #PICK UP FROM HERE
        print(f"Total Revenue: ${total_revenue}")

            
        #multiply drink cost by the count to get revenue per drink, print each drink with quantity sold (count) 
        #, total revenue per drink, and total total revenue
    
    def run():
        """The Main program that runs
        Arg:
            None
        
        Returns:
            Depends"""
        drinks = [
            Menu("Mocha", "Medium", 5.75),
            Menu("Chai Latte", "Medium", 5.35),
            Menu("Iced Tea", "Medium", 3.75),
            Menu("Black Coffee", "Medium", 3.25),
            Menu("Italian Soda", "Medium", 5.75)
            ]
        main_stuff = BistroSystem(drinks)

        print ("Welcome to the Bearcat Bistro! ✨")
        while True:
            userinput= input("\n📋 Main Menu:\n" \
            "1. Display Menu\n" \
            "2. Take New Order\n" \
            "3. View Open Orders\n" \
            "4. Mark Next Order as Complete\n" \
            "5. View End-of-Day Report\n" \
            "6. Exit\n"
            "Enter your choice:")

            if userinput == "1":
                    print("\n🍒 Bearcat Bistro Menu:")
                    for i in range(len(drinks)): #THIS GOES WITH OPTION 1
                        print (f"{i+1}.{drinks[i].display_drink()}")
            elif userinput == "2":
                #Take new order
                name = input("What's your name? ")
                order = CustomerOrder(name)
                num_drinks = input("How many drinks will you be ordering? ")
                drink_num = None
                drink_name = None
                drink_price = None
                drink_size = None
                if not isinstance(int(num_drinks), int):
                    print ("❌ I'm sorry, an error occured, please try to place your order again...")
                else:
                    for i in range(int(num_drinks)):
                        drink_num = 0
                        drink_num = (int(input(f"Drink #{i+1}:Enter Drink Number (1-5): ")) - 1)
                        drink_name = drinks[drink_num].get_name()
                        drink_price= drinks[drink_num].get_price()
                        drink_size= drinks[drink_num].get_size()
                        customization = input (f"Any Customizations for {drinks[drink_num].get_name()}: ")
                        order.add_drink(drink_name,drink_size,drink_price, customization)
                    
                    print(f"📋 Order Summary for {name}:")
                    drinks_in_order = order.get_order()
                    for drink in drinks_in_order:
                        print(f"-{drink.drink()} (Medium) - {drink.customization()}")
                    main_stuff.add_order(order)
                    print("✅ Order Placed Successfully")

            elif userinput == "3":
                #View Open Orders
                print("🦊 Open Bearcat Orders 🕑")
                main_stuff.open_orders()
            elif userinput == "4":
                print(main_stuff.complete_order())
            elif userinput == "5":
                #View End-of_Day Report
                print(f"📊 End of Day Report\n----------------------------------------")
                main_stuff.total_sales()
            elif userinput == "6":
                print(f"📊 End of Day Report\n----------------------------------------")
                main_stuff.total_sales()
                print ("Exiting the program, have a nice day! ✨")
                exit()
            else:
                print( "\n ❌ Invalid Input. Please select one of the options!")








