
# Week 7 Assignment - Shopping List Manager

shopping_list = []

while True:
    print("\nMy Shopping List")
    print("add / remove / show / done")

    choice = input("What would you like to do? ").lower().strip()

    if choice == "add":
        item = input("Enter the item to add: ").strip()

        if item:
            shopping_list.append(item)
            print(item, "has been added to your list.")
        else:
            print("Please enter an item.")

    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed from your list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if shopping_list:
            print("Items on my shopping list:")
            for item in shopping_list:
                print("-", item)
        else:
            print("Your shopping list is empty.")

    elif choice == "done":
        print("Thank you for using my shopping list. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose add, remove, show, or done.")
