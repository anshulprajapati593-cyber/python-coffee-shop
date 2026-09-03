print("Welcome to the Python Coffee Shop!! ☕☕")
order_list = []
def menu():
    print("\n========= COFFEE SHOP MENU =========")
    print(" [1] Hot Coffee")
    print(" [2] Cold Coffee")
    print(" [3] Cappuccino")
    print(" [4] Donuts")
    print(" [5] Sandwich")
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

    if action == "1":
        print("\n--- Placing an Order ---")
        order = input("Enter the item number (1-5) you wish to add to your cart: ")
        if order == "1":
            print("A Hot Coffee has been added to your cart!")
            order_list.append("Hot Coffee")
        elif order == "2":
            print("A Cold Coffee has been added to your cart!")
            order_list.append("Cold Coffee")
        elif order == "3":
            print("A Cappuccino has been added to your cart!")
            order_list.append("Cappuccino")
        elif order == "4":
            print("A Donut has been added to your cart!")
            order_list.append("Donut")
        elif order == "5":
            print("A Sandwich has been added to your cart!")
            order_list.append("Sandwich")
        else:
            print("❌ Invalid item number! Please choose 1-5.")
    elif action == "2":
        print("\n--- Your Shopping List ---")
        if len(order_list) == 0:
            print("Your cart is empty!")
        else:
            for item in order_list:
                print(f"• {item}")
    elif action == "3":
        print("\nThank you for visiting the Python Coffee Shop! Goodbye! ☕")
        break
    else:
        print("❌ Invalid choice! Please type 1, 2, or 3.")
