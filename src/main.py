# src/main.py

from clicker_center_screen import auto_click_center_screen
# from clicker_confirm_button import auto_click_confirm_button

def main_menu():
    while True:
        print("\nAutoClicker Testing Development Kit")
        print("1. 3s Auto Clicker Center Screen")
        print("2. Auto Click Confirm Button")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            auto_click_center_screen()
        elif choice == '2':
            pass
            # auto_click_confirm_button()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
