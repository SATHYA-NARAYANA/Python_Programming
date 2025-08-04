class ListManager:
    def __init__(self):
        self.my_list = []

    def insert_data(self):
        pass

    def append_data(self):
        pass

    def clear_data(self):
        pass

    def update_data(self):
        pass

    def delete_data(self):
        pass

    def read_data(self):
        pass

    def operations(self):
        while True:
            operation = input("Enter your choice (C-create, R-read, U-update, P-print, D-delete, Q-quit): ").upper()

            if operation == 'Q':
                break

            elif operation == 'C':
                print('Do you want to insert or append? (I/A)')
                choice = input("Enter your choice (I/A): ").upper()
                if choice == 'A':
                    data = input("Enter data to append: ")
                    self.my_list.append(data)
                    print(f"Data '{data}' appended to the list.")
                elif choice == 'I':
                    print("Insert not implemented yet.")
                    break
                else:
                    print("Invalid choice. Please try again.")

# Create instance and call operations
manager = ListManager()
manager.operations()
