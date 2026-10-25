print("Welcome to the Python Coffee Shop!! ☕☕")
order_list = []
def menu():
    print("\n========= COFFEE SHOP MENU =========")
    print(" [1] Hot Coffee\t\t--$2.50")
    print(" [2] Cold Coffee\t--$5.00")
    print(" [3] Cappuccino\t\t--$3.30")
    print(" [4] Donuts\t\t--$4.00")
    print(" [5] Sandwich\t\t--$8.00")
    print("====================================")
    print("\nWhat would you like to do next?")
    print("👉 Type '1' to start a new order")
    print("👉 Type '2' to view your current shopping list")
    print("👉 Type '3' to close the application and exit")
    print("====================================")

while True:
    # Display the newly formatted menu
    menu()

    # Clearer input prompt using an explicit visual cue
    
    action = input("\nEnter choice (just the number 1, 2, or 3): ")
    
    # Action 1
    
    if action == "1":
        print("\n--- Placing an Order ---")
        order = input("Enter the item number (1-5) you wish to add to your cart: ")
        if order == "1":
            print("A Hot Coffee has been added to your cart!")
            order_list.append(("Hot Coffee", 2.50))
        elif order == "2":
            print("A Cold Coffee has been added to your cart!")
            order_list.append(("Cold Coffee", 5.00))
        elif order == "3":
            print("A Cappuccino has been added to your cart!")
            order_list.append(("Cappuccino", 3.30))
        elif order == "4":
            print("A Donut has been added to your cart!")
            order_list.append(("Donut", 4.00))
        elif order == "5":
            print("A Sandwich has been added to your cart!")
            order_list.append(("Sandwich", 8.00))
        else:
            print("❌ Invalid item number! Please choose 1-5.")
    # Action 2
    
    elif action == "2":
        print("\n--- Your Shopping List ---")
        if len(order_list) == 0:
            print("Your cart is empty!")
            
        else:
            billing_total=0
            for item, price in order_list:
                print(f"• {item}: ${price:.2f}")
                billing_total += price
            print(f"---------------------------\n💰 Total Bill: ${billing_total:.2f}")
            
    #Action 3
            
    elif action == "3" and len(order_list) != 0:
         print("\n❌ You cannot exit yet! You must pay your bill first.")
         print("--- Your Unpaid Bill ---")
         billing_total=0
         for item, price in order_list:
             print(f"• {item}: ${price:.2f}")
             billing_total += price
         print(f"---------------------------\n💰 Total Bill: ${billing_total:.2f}")
         print("====================================")
         break
            
    elif action == "3" and len(order_list) == 0:
        print("\nThank you for visiting the Python Coffee Shop! Goodbye! ☕")
        break
    
    else:
        print("❌ Invalid choice! Please type 1, 2, or 3.")
