from anti_afk.anti_afk_manager import AntiAFKManager


def main_menu():
    manager = AntiAFKManager()
    while True:
        print("\nAutoClicker Testing Development Kit")
        print("1. Anti AFK + Anti Starve")
        print("2. Anti Starve")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            manager.start()
        elif choice == '2':
            pass
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
