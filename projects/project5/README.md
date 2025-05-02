Hello, hello! Here I will break down the structures I chose to use for each function and component. Just a little note though, as you go through my program and all it's documentation, you may notice it gets more sparce in some spots. This is because I started to run out of time, and I had to study for my other finals...

1. Menu
For the menu, I decided that it would be best if I used a list to store the data. I would store the drink (with all it's related information) in an object. Thus is would be a fixed list of objects, that could be iterated over to display each of the drinks and their price/ingredients.
2. Customer Orders
I know that for the customer orders, it would probably be best to store it in a queue (since that has the First in First out function) but for my program I decided to use a list. If I had more time I would have chosen to do a linked list instead. This is because a linked list allows for the program to remove elements from the list. I wanted to implement one of the bonus features (but ran out of time). Additionally with this, all orders will be stored in a list, so users can see what has been previously ordered, and reorder it. 
3. Order Confirmation
For this, I didn't really store the confirmation into a data structure, I just printed the stored customer order.
4. Open Orders Queue
I was initially going to store the queues in an actual queue (and this would be the best option hands down), but I ran into some issues with my program, so I unfortunately had to switch it to a list. However, with more time and resources to help me with the errors I ran into, I would change this to a circular queue.
5. Completed Orders
I stored all the completed orders into an Array Stack. I definitely could have just gone with an array or list, but I like the stack because if I wanted to add a feature where you would look at the most recently completed order, this would be a good structure. Honestly though, there's no reason to use a stack over some other structure. There's no special features I really needed in order to store this data. I just like the stacks's built-in functions more than others. However, I did store the count (that I would later use for the end-of-day) report in a bag, since it keeps track of the count, which is nice.

Known Errors:
- When the user inputs an invalid response to any of the questions (with the exception of a few) the program will break and return and error. Example: When the program prompts the user to input a number between 1 and 5 for their drink, if the user puts a word or the number 6, an error will occur. 
- The formatting is weird for display current orders and end-of-day reports. When I tried to tidy these up, I ran into tons of errors, so I just had to accept them...There also might be some weird formatting in other portions, sorry.
- When placing an order, it doesn't ask the user if they want to confirm there order..I didn't realize I was missing this until I was doing the code snippets below. I would add it in, but this project is already two hours overdo..

Future Goals:
- If I had more time and will-power, I would have loved to implement all the bonus features. I would also spend time tidying up the visuals more and adding in the little things I forgot/missed!

Sample Runs: (NOTE: To Run Program, run Project 5 in Bug Terminal)
Welcome to the Bearcat Bistro! ✨

1.DISPLAY MENU

📋 Main Menu:
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
Enter your choice:1

🍒 Bearcat Bistro Menu:
1.Mocha - 5.75
2.Chai Latte - 5.35
3.Iced Tea - 3.75
4.Black Coffee - 3.25
5.Italian Soda - 5.75

2.TAKE NEW ORDER

Enter your choice:2
What's your name? Lola
How many drinks will you be ordering? 2
Drink #1:Enter Drink Number (1-5): 3
Any Customizations for Iced Tea: Extra Ice
Drink #2:Enter Drink Number (1-5): 5
Any Customizations for Italian Soda: Strawberry Flavor, Whipped Cream
📋 Order Summary for Lola:
-Iced Tea (Medium) - Extra Ice
-Italian Soda (Medium) - Strawberry Flavor, Whipped Cream
✅ Order Placed Successfully

3.VIEW OPEN ORDERS

Enter your choice:3
🦊 Open Bearcat Orders 🕑
1. Lola: ['Chai Latte (Vanilla)']

4.MARK NEXT ORDER AS COMPLETE

Enter your choice:4
✅ Completed Order for Lola!

5.VIEW END OF DAY REPORT

Enter your choice:5
📊 End of Day Report
----------------------------------------
Drink Name - Qty Sold - Total Sales
Mocha - 0 - $0.0
Chai Latte - 1 - $5.35
Iced Tea - 0 - $0.0
Black Coffee - 0 - $0.0
Italian Soda - 0 - $0.0
Total Revenue: $5.35

6.EXIT

Enter your choice:6
📊 End of Day Report
----------------------------------------
Drink Name - Qty Sold - Total Sales
Mocha - 0 - $0.0
Chai Latte - 1 - $5.35
Iced Tea - 0 - $0.0
Black Coffee - 0 - $0.0
Italian Soda - 0 - $0.0
Total Revenue: $5.35
Exiting the program, have a nice day! ✨


