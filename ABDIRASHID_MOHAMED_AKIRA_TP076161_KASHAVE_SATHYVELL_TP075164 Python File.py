#ABDIRASHID MOHAMED AKIRA, KASHAVE SATHYVELL A/L SATHYVELL
#TP076161, TP075164


import os
import datetime

# Define a function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()


def user_initialization():
    userFile = "users.txt"

    # Check if users.txt file exists
    if not os.path.exists(userFile) or (os.path.exists(userFile) and os.stat(userFile).st_size == 0):
        # Initialize the user data only if it doesn't exist or is empty
        with open(userFile, 'w', newline='') as user_file:
            stars = '*' * 150
            user_file.write(stars + '\n')

            # Write the header line with rjust(20)
            header = "USER_ID".rjust(20) + "NAME".rjust(20) + "PASSWORD".rjust(20) + "CONFIRM PASSWORD".rjust(20) + "TELEPHONE NO".rjust(20) + "USER TYPE".rjust(20)
            user_file.write(header + '\n')
            user_file.write(stars + '\n')

            # Define the initial users and their data
            initial_users = [
                {"user_id": "Akira64", "name": "Doe", "password": "Kingr123", "confirm_password": "Kingr123", "telephone_no": "555-123-4567", "user_type": "admin"},
                {"user_id": "Kashave85", "name": "Smith", "password": "Kashave456", "confirm_password": "Kashave456", "telephone_no": "555-987-6543", "user_type": "customer"},

            ]

            for user in initial_users:
                # Add the initial user details
                entry = user["user_id"].rjust(20) + user["name"].rjust(20) + user["password"].rjust(20) + user["confirm_password"].rjust(20) + user["telephone_no"].rjust(20) + user["user_type"].rjust(20)
                user_file.write(entry + '\n')

# Check if user data has already been initialized
userFile = "users.txt"
if not os.path.exists(userFile) or (os.path.exists(userFile) and os.stat(userFile).st_size == 0):
    user_initialization()



# Function to check user credentials

def authenticate_user():
    user_id = input("Enter your user ID: ")
    password = input("Enter your password: ")

    # Read user data from the file
    user_data = read_user_data()

    for user in user_data:
        if user[0] == user_id and user[2] == password:
            return user[5]  # Return the user type

    print("Invalid user ID or password. Access denied.")
    return None

# Function to read user data from the file
def read_user_data():
    user_data = []
    if os.path.exists('users.txt'):
        with open('users.txt', 'r') as read_file:
            lines = read_file.readlines()

        if len(lines) > 2:
            lines = lines[2:]  # Skip the header

            for line in lines:
                columns = line.strip().split()
                if len(columns) >= 6:
                    user_data.append(columns)

    return user_data



def main_menu():
    stars = '*' * 150
    print(stars)
    print("\t\t\t\t\t\t\t\t\t\t\t\tINVENTORY MANAGEMENT SYSTEM FOR PERSONAL PROTECTIVE EQUIPMENT (PPE)")
    while True:
        print(stars)
        print('\t\t\t\t\t\t\t\t\t\t\t\t************************************************')
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tMain Menu:")
        print('\t\t\t\t\t\t\t\t\t\t\t\t************************************************')
        print("\t\t\t\t\t\t\t\t\t\t\t\t1. User Management")
        print("\t\t\t\t\t\t\t\t\t\t\t\t2. Inventory Update Management")
        print("\t\t\t\t\t\t\t\t\t\t\t\t3. Item Inventory Tracking")
        print("\t\t\t\t\t\t\t\t\t\t\t\t4. Search Functionalities")
        print("\t\t\t\t\t\t\t\t\t\t\t\t5. Item Supplying")
        print("\t\t\t\t\t\t\t\t\t\t\t\t6. Exit")
        print(stars,"\n")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            user_type = authenticate_user()
            if user_type:
                if user_type == "admin":
                    print('ACCESS GRANTED')
                    user_management_menu()
        elif choice == '2':
            inventory_management_menu()
        elif choice == '3':
            item_inventory_tracking()
        elif choice == '4':
            search_functionalities()
        elif choice == '5':
            supplier_details()

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5/6).")

def user_management_menu():
    while True:
        print('\t\t\t\t\t\t\t\t\t\t\t\t************************************************')
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tUser Management Menu")
        print('\t\t\t\t\t\t\t\t\t\t\t\t************************************************')
        print("\t\t\t\t\t\t\t\t\t\t\t\t1. Add User")
        print("\t\t\t\t\t\t\t\t\t\t\t\t2. Delete User")
        print("\t\t\t\t\t\t\t\t\t\t\t\t3. Modify User")
        print("\t\t\t\t\t\t\t\t\t\t\t\t4. Search User")
        print("\t\t\t\t\t\t\t\t\t\t\t\t5. Return to Main Menu")
        print('*'*150)

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            add_user()
        elif choice == '2':
            delete_user()
        elif choice == '3':
            modify()
        elif choice == '4':
            search_user()
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5).")




def add_user():
    def user_details(name, user_id, password, confirm_password, telephone_no, user_type):
        def read_user_data():
            user_data = []  # Create a list to store user data

            # Open the file for reading
            with open('users.txt', 'r') as read_file:
                lines = read_file.readlines()

            # Skip the header line
            lines = lines[2:]

            # Loop through each line and split it into columns
            for line in lines:
                columns = line.strip().split()
                if len(columns) >= 6:
                    user_data.append(columns)  # Append the entire row as user data

            return user_data

        def write_user_data(user_data):
            # Open the file for writing (overwrite the existing file)
            with open('users.txt', 'w') as write_file:
                # Write the stars line above the header
                stars = '*' * 150
                write_file.write(stars + '\n')

                # Write the header line with rjust(20)
                header = "USER_ID".rjust(20) + "NAME".rjust(20) + "PASSWORD".rjust(20) + "CONFIRM PASSWORD".rjust(20) + "TELEPHONE NO".rjust(20) + "USER TYPE".rjust(20)
                write_file.write(header + '\n')

                # Write the stars line below the header
                write_file.write(stars + '\n')

                # Write each user's data with rjust(20) for each column
                for user in user_data:
                    user_line = user[0].rjust(20) + user[1].rjust(20) + user[2].rjust(20) + user[3].rjust(20) + user[4].rjust(20) + user[5].rjust(20)
                    write_file.write(user_line + '\n')


        user = []
        user.append(user_id)
        user.append(name)
        user.append(password)
        user.append(confirm_password)
        user.append(telephone_no)
        user.append(user_type)
        with open('users.txt', 'a') as user_file:
                user_line = user[0].rjust(20) + user[1].rjust(20) + user[2].rjust(20) + user[3].rjust(20) + user[4].rjust(20) + user[5].rjust(20)
                user_file.write(user_line + '\n')

    def read_user_data():
        passwords = []
        user_ids = []
    #open the file for reading
        with open('users.txt','r') as read_file:
            lines = read_file.readlines()
    #skip the header line
            lines = lines[1:]

    #loop through each line and split it into columns
        for line in lines:
            columns = line.strip().split()
            if len(columns) >= 4:
                user_Id = columns[0]
                pssword = columns[2]
                passwords.append(pssword)
                user_ids.append(user_Id)
        return passwords,user_ids

    # Function to check the password
    def check_password(new_password, existing_passwords):
        for pssword in existing_passwords:
            if pssword == new_password:
                return False
        return True

    def check_user_id (NEw_id, EXisting_passwords):
        for user_Id in EXisting_passwords:
            if user_Id == NEw_id:
                return False
        return True

    existing_passwords,EXisting_passwords = read_user_data()

    #MAIN MENU
    name = input("Enter user's name: ")
    # Check if the name is at least 3 characters long
    while len(name) < 3:
        print("Please enter a name with at least 3 characters.")
        name = input("Enter your name: ")

    user_id = input("Enter  user's ID: ")
    while len(user_id) < 3:
        print("Choose a valid user ID at least 4 characters:")
        user_id = input("Enter  user's ID: ")

    #EXisting_passwords = read_user_data()
    #check if user id already exists
    while not check_user_id(user_id, EXisting_passwords):
        print("User ID already exists please choose another:")
        user_id = input("Enter another user id: ")

    password = input("Enter user's password: ")
    # Check if the password has at least 6 characters, including uppercase, lowercase, and numbers
    while len(password) < 6 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password):
        print("Password should have at least 6 characters with upper and lower case letters and numbers.")
        password = input("Enter user's password: ")

    #check if password already exists
    #existing_passwords = read_user_data()
    while not check_password(password, existing_passwords):
        print("Password is too similar to an existing user's password. Please choose a different one.")
        password = input("Enter another password: ")

    confirm_password = input("Confirm your password: ")

    # Check if the confirmed password matches the original password
    while password != confirm_password:
        print("Passwords do not match. Please try again.")
        confirm_password = input("Confirm your password: ")

    telephone_no = input("Enter user's telephone number: ")

    # Check if the telephone number has exactly 10 digits
    while len(telephone_no) != 10:
        print("Telephone number should have exactly 10 digits.")
        telephone_no = input("Enter user's telephone number: ")

    user_type = input("Enter  user type (admin or staff): ")
    print("User added successfully!")

    continue_choice = input("Do you want to continue adding users? (yes/no): ").lower()
    while continue_choice not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue_choice = input("Do you want to continue adding users? (yes/no): ").lower()
        if continue_choice == 'no':
            break

    user_details(name, user_id, password, confirm_password, telephone_no, user_type)




def delete_user():
    def read_user_data():
        user_data = []  # Create a list to store user data

        # Open the file for reading
        with open('users.txt', 'r') as read_file:
            lines = read_file.readlines()

        # Skip the header line
        lines = lines[2:]

        # Loop through each line and split it into columns
        for line in lines:
            columns = line.strip().split()
            if len(columns) >= 6:
                user_data.append(columns)  # Append the entire row as user data

        return user_data

    def write_user_data(user_data):
        # Open the file for writing (overwrite the existing file)
        with open('users.txt', 'w') as write_file:
            # Write the stars line above the header
            stars = '*' * 150
            write_file.write(stars + '\n')

            # Write the header line with rjust(20)
            header = "USER_ID".rjust(20) + "NAME".rjust(20) + "PASSWORD".rjust(20) + "CONFIRM PASSWORD".rjust(20) + "TELEPHONE NO".rjust(20) + "USER TYPE".rjust(20)
            write_file.write(header + '\n')

            # Write the stars line below the header
            write_file.write(stars + '\n')

            # Write each user's data with rjust(20) for each column
            for user in user_data:
                user_line = user[0].rjust(20) + user[1].rjust(20) + user[2].rjust(20) + user[3].rjust(20) + user[4].rjust(20) + user[5].rjust(20)
                write_file.write(user_line + '\n')

    def delete_user_by_id(user_id, user_data):
        deleted = False

        for user in user_data:
            if user[0] == user_id:  # Check if the user_id matches
                confirmation = input("Are you sure you want to delete this user? (YES or NO): ").strip().upper()

                if confirmation == 'YES':
                    user_data.remove(user)  # Remove the user from the user_data list
                    deleted = True
                    print("User deleted successfully.")
                    break
                else:
                    print("User not deleted.")

        if not deleted:
            print("User not found.")

    # Main program
    existing_users = read_user_data()

    user_id_to_delete = input("Enter the User ID to delete: ").strip()

    delete_user_by_id(user_id_to_delete, existing_users)

    # Update the file with the modified data (excluding the deleted user)
    write_user_data(existing_users)




def modify():
    def read_user_data():
        user_data = []  # Create a list to store user data

        # Open the file for reading
        with open('users.txt', 'r') as read_file:
            lines = read_file.readlines()

        # Skip the header line
        lines = lines[2:]

        # Loop through each line and split it into columns
        for line in lines:
            columns = line.strip().split()
            if len(columns) >= 6:
                user_data.append(columns)  # Append the entire row as user data

        return user_data

    def write_user_data(user_data):
        # Open the file for writing (overwrite the existing file)
        with open('users.txt', 'w') as write_file:
            # Write the stars line above the header
            stars = '*' * 150
            write_file.write(stars + '\n')

            # Write the header line with rjust(20)
            header = "USER_ID".rjust(20) + "NAME".rjust(20) + "PASSWORD".rjust(20) + "CONFIRM PASSWORD".rjust(20) + "TELEPHONE NO".rjust(20) + "USER TYPE".rjust(20)
            write_file.write(header + '\n')

            # Write the stars line below the header
            write_file.write(stars + '\n')

            # Write each user's data with rjust(20) for each column
            for user in user_data:
                user_line = user[0].rjust(20) + user[1].rjust(20) + user[2].rjust(20) + user[3].rjust(20) + user[4].rjust(20) + user[5].rjust(20)
                write_file.write(user_line + '\n')

    while True:
        user_id_to_modify = input("Enter USER_ID of the user you want to modify: ")
        user_data = read_user_data()  # Read the existing user data

        # Search for the user by userId and display their current details if found
        user_found = False
        for user in user_data:
            if user[0] == user_id_to_modify:
                print(f"**********Previous Details for USER_ID '{user_id_to_modify}':************")
                print(f"\tName: {user[1]}")
                print(f"\tPassword: {user[2]}")
                print(f"\tConfirm Password: {user[3]}")
                print(f"\tTelephone No: {user[4]}")
                print(f"\tUser Type: {user[5]}")
                print(f"**********Previous Details for USER_ID '{user_id_to_modify}':************")

                print("\n***********Select the fields you want to modify (choose either(1,2,3,4)):**************")
                print("1. Name")
                print("2. Password")
                print("3. Confirm Password")
                print("4. Telephone No")
                print("5. User Type")
                print("\n***********Select the fields you want to modify (choose either(1,2,3,4)):**************")
                selected_fields = input("Enter the numbers of the fields to modify: ").split(',')

                for field in selected_fields:
                    if field == '1':
                        user[1] = input("New Name: ")
                    elif field == '2':
                        user[2] = input("New Password: ")
                    elif field == '3':
                        user[3] = input("New Confirm Password: ")
                    elif field == '4':
                        user[4] = input("New Telephone No: ")
                    elif field == '5':
                        user[5] = input("New User Type: ")

                user_found = True
                break

        if user_found:
            write_user_data(user_data)  # Write the modified user data back to the file
            print(f"User with USER_ID '{user_id_to_modify}' modified successfully.")
        else:
            print(f"User with USER_ID '{user_id_to_modify}' not found.")

        continue_choice = input("Do you want to continue modifying this user? (yes/no): ").lower()
        if continue_choice != 'yes':
            continue_modifying_another_user = input("Do you want to continue modifying another user? (yes/no): ").lower()
            if continue_modifying_another_user != 'yes':
                break


def search_user():
    def read_user_data():
        user_data = []  # Create a list to store user data

        # Open the file for reading
        with open('users.txt', 'r') as read_file:
            lines = read_file.readlines()

        # Skip the header line
        lines = lines[1:]

        # Loop through each line and split it into columns
        for line in lines:
            columns = line.strip().split()
            if len(columns) >= 4:
                user_data.append(columns)  # Append the entire row as user data

        return user_data

    def search_user_by_id(user_id, user_data):
        for row in user_data:
            if row[0] == user_id:  # Check if the user_id matches
                return row  # Return the entire row for the matched user

        return None  # User not found

    existing_users = read_user_data()

    user_id = input("Enter user ID to search: ")

    found_user = search_user_by_id(user_id, existing_users)

    if found_user:
        print("******User Details:********************")
        print("\t**User ID:", found_user[0])
        print("\t**Name:", found_user[1])
        print("\t**Password:", found_user[2])
        print("\t**Confirm Password:", found_user[3])
        print("\t**Telephone No:", found_user[4])
        print("\t**User Type:", found_user[5])
        print("******User Details:**********************")
    else:
        print("User not found")



def read_ppe_data():
    ppe_data = []  # Create a list to store user data

    # Open the file for reading
    with open('ppe.txt', 'r') as read_file:
        lines = read_file.readlines()

    # Skip the header line
    lines = lines[2:]

    # Loop through each line and split it into columns
    for line in lines:
        columns = line.strip().split()
        if len(columns) >= 4:
            ppe_data.append(columns)  # Append the entire row as user data

    return ppe_data

def write_ppe_data(ppe_data):
    # Open the file for writing (overwrite the existing file)
    with open('ppe.txt', 'w') as write_file:
        # Write the stars line above the header
        stars = '*' * 150
        write_file.write(stars + '\n')

        # Write the header line with rjust(20)
        header = "SUPPLIER CODE".rjust(20) + "ITEM CODE".rjust(20) + "  QUANTITY IN STORE(BOXES)".rjust(20) + "ITEM NAME".rjust(20)
        write_file.write(header + '\n')

        # Write the stars line below the header
        write_file.write(stars + '\n')


       # Write each user's data with rjust(20) for each column
        for item in ppe_data:
           if item is not None:
               if len(item) >= 5 and item[4] != " ":
                   item[3] = item[3] + ' ' + item[4]
               else:
                   item[3] = item[3]

           item_line = item[0].rjust(20) + item[1].rjust(20) + item[2].rjust(20) + item[3].rjust(20)
           write_file.write(item_line + '\n')

def read_hospital_data():
    hospital_data = []  # Create a list to store user data

    # Open the file for reading
    with open('hospitals.txt', 'r') as read_file:
        lines = read_file.readlines()

    # Skip the header line
    lines = lines[2:]

    # Loop through each line and split it into columns
    for line in lines:
        columns = line.strip().split()
        if len(columns) >= 3:
            hospital_data.append(columns)  # Append the entire row as user data

    return hospital_data

def write_hospital_data(hospital_data):
    # Open the file for writing (overwrite the existing file)
    with open('hospitals.txt', 'w') as write_file:
        # Write the stars line above the header
        stars = '*' * 150
        write_file.write(stars + '\n')

        # Write the header line with rjust(20)
        header = "HOSPITAL CODE".rjust(20) + "HOSPITAL NAME".rjust(20) + "CONTACT NO.".rjust(20)
        write_file.write(header + '\n')

        # Write the stars line below the header
        write_file.write(stars + '\n')

        # Write each user's data with rjust(20) for each column
        for hospital in hospital_data:
            hospital_line = hospital[0].rjust(20) + hospital[1].rjust(20) + hospital[2].rjust(20)
            write_file.write(hospital_line + '\n')

def update_hospital(hospital_code):
    while True:
        hospital_data = read_hospital_data()  # Read the existing user data

        # Search for the user by userId and display their current details if found
        hospitalFound = False
        for hospital in hospital_data:
            if hospital[0] == hospital_code:
                print(f"******************** Previous Details for HOSPITAL CODE: '{hospital_code}':********************")
                print(f"\tHospital Name: {hospital[1]}")
                print(f"\tContact No.: {hospital[2]}")
                print(f"******************** Previous Details for HOSPITAL CODE: '{hospital_code}':********************")

                print("\n***********Select the fields you want to modify (choose either 1 OR 2):**************")
                print("1. Hospital Name")
                print("2. Contact No.")
                print("\n***********Select the fields you want to modify (choose either 1 OR 2):**************")
                selected_fields = input("Enter the number of the field to modify: ").split(',')


                for field in selected_fields:
                    if field == '1':
                        hospital[1] = input("New Hospital Name: ")
                    elif field == '2':
                        hospital[2] = input("New Contact No.: ")

                hospitalFound = True
                break

        if hospitalFound:
            write_hospital_data(hospital_data)  # Write the modified hospital data back to the file
            print(f"Hospital with HOSPITAL CODE '{hospital_code}' modified successfully.")
        else:
            print(f"Hospital with HOSPITAL CODE '{hospital_code}' not found.")

        continue_choice = input("Do you want to continue modifying this Hospital? (yes/no): ").lower()
        if continue_choice != 'yes':
            break


def update_stock(item_code):
    while True:
        ppe_data = read_ppe_data()  # Read the existing ppe data

        # Search for the item by item_code and display their current details if found
        found_item = False
        for item in ppe_data:
            if item[1] == item_code:
                print(f"********Current Available Quantity for ITEM_CODE: '{item_code}':********")
                print(f"\tItem Code: {item[1]}")
                print(f"\tQuantity: {item[2]}")
                print(f"************************************************************************")

                print("\n**************** Was the item distributed or received: ****************")
                print("1. Received")
                print("2. Distributed")
                print("\n***********************************************************************")
                selected_fields = input("Enter the number of boxes received/distributed: ").split(',')

                for field in selected_fields:
                    if field == '1':
                        supplier_code = input("What is the supplier code? ")
                        while supplier_code != item[0]:
                            print("Supplier information does not match. Please try again.")
                            supplier_code = input("What is the supplier code? ")
                        received_quantity = int(input("Boxes Received: "))
                        item[2] = str(int(item[2]) + received_quantity)
                        record_transaction(item_code, 'R', received_quantity, supplier_code)

                    elif field == '2':
                        hospital_code = input("What is the hospital code? ")
                        while hospital_code != 'HosC1' and hospital_code != 'HosC2' and hospital_code != 'HosC3' and hospital_code != 'HosC4':
                            print("Hospital information not valid. Please try again.")
                            hospital_code = input("What is the hospital code? ")
                        distributed_quantity = int(input("Boxes Distributed: "))
                        while int(item[2]) - distributed_quantity < 0:
                            print("Insufficient Stock Available")
                            print("Available stock: " + item[2] + " Boxes")
                            distributed_quantity = int(input("Boxes Distributed: "))
                        item[2] = str(int(item[2]) - distributed_quantity)
                        record_transaction(item_code, 'D', distributed_quantity, hospital_code)

                found_item = True
                break

        if found_item:
            write_ppe_data(ppe_data)  # Write the modified quantity data back to the file
            print(f"Item with ITEM CODE '{item_code}' updated successfully.")
        else:
            print(f"Item with ITEM CODE '{item_code}' not found.")

        continue_choice = input("Was this item distributed or received by/to someone else: ").lower()
        if continue_choice != 'yes':
            break


def record_transaction(item_code, operation, quantity, code):
    transactionFile = 'transactions.txt'  # Define the path to the users.txt file
    timestamp = datetime.datetime.now().replace(microsecond=0)

    # Check if the user ID already exists in the file
    if os.path.exists(transactionFile):
        with open(transactionFile, 'a+') as transaction_file:
            # Check if the file is empty and write a header row if it is
            if os.stat(transactionFile).st_size == 0:
                stars = '*' * 150
                transaction_file.write(stars + '\n')

                # Write the header line with rjust(20)
                header = "ITEM CODE".rjust(20) + "HOSPITAL/SUPPLIER CODE".rjust(30) + "RECEIVED/DISTRIBUTED(R/D)".rjust(
                    30) + "QUANTITY CHANGE".rjust(30) + "TIME OF DELIVERY".rjust(30)
                transaction_file.write(header + '\n')

                # Write the stars line below the header
                transaction_file.write(stars + '\n')

    transaction = []
    transaction.append(item_code)
    transaction.append(code)
    transaction.append(operation)
    transaction.append(str(quantity))
    transaction.append(str(timestamp))

    with open(transactionFile, 'a') as transaction_file:
        transaction_line = transaction[0].rjust(15) + transaction[1].rjust(25) + transaction[2].rjust(30) + transaction[3].rjust(35) + transaction[4].rjust(35)
        transaction_file.write(transaction_line + '\n')

def read_transactions():
    transaction_data = []

    if not os.path.exists('transactions.txt'):
        return transaction_data  # Return an empty list if the file doesn't exist

    with open('transactions.txt', 'r') as transaction_file:
        lines = transaction_file.readlines()

    # Skip the header lines
    lines = lines[2:]

    for line in lines:
        columns = line.strip().split()
        if len(columns) >= 5:
            transaction_data.append(columns)

    return transaction_data

def stock_quantity(item_code, ppe_data):
    for row in ppe_data:
        if row[1] == item_code:  # Check if the user_id matches
            return row  # Return the entire row for the matched user

    return None  # User not found


# Check stock quantity of item
def check_stock_quantity(item_code):
    item_data = read_ppe_data()
    if item_code in item_data:
        return int(item_data[item_code])
    return 0

# Track items with stock less than 25
def track_low_stock_items():
    ppe_data = read_ppe_data()  # Read the data from the file

    low_stock_items = []  # Create a list to store low stock items

    for item in ppe_data:
        item_code = item[1]
        quantity = int(item[2])

        if quantity < 25:
            low_stock_items.append((item_code, quantity))

    if len(low_stock_items) > 0:
        print("\n***********************************************************************")
        print("Items with Stock Quantity Less than 25 Boxes:")
        for item_code, quantity in low_stock_items:
            print(f"Item Code: {item_code}, Quantity: {quantity}")
        print("\n***********************************************************************")
    else:
        print("No Items are in low stock")


def check_quantity(item_code, ppe_data):
    for row in ppe_data:
        if row[1] == item_code:  # Check if the user_id matches
            return row  # Return the entire row for the matched user

    return None  # User not found


# Track received items during specific time period
def track_items_by_time_period(start_date, end_date):
    transactions = read_transactions()  # Read all transactions from 'transactions.txt'

    start_datetime = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    tracked_transactions = []

    for transaction in transactions:
        timestamp = datetime.datetime.strptime(transaction[4], "%Y-%m-%d")

        if start_datetime <= timestamp <= end_datetime and transaction[2] == 'R':
            tracked_transactions.append(transaction)

    return tracked_transactions

# Print total available quantity of all items sorted by item code
def print_total_available_quantity():
    ppe_data = read_ppe_data()  # Read the PPE data from the file

    # Sort the data by item code (index 1) in ascending order
    ppe_data.sort(key=lambda item: item[1])

    # Initialize a dictionary to store the total quantity for each item code
    total_quantity = {}

    # Calculate the total quantity for each item code
    for item in ppe_data:
        item_code = item[1]
        quantity = int(item[2])
        if item_code in total_quantity:
            total_quantity[item_code] += quantity
        else:
            total_quantity[item_code] = quantity

    # Print the total available quantity for each item code
    print("Total available quantity of all items sorted by item code:")
    for item_code, quantity in sorted(total_quantity.items()):
        print(f"Item Code: {item_code}, Total Quantity: {quantity}")


def inventory_management_menu():
    while True:
        print("\nInventory Management Menu:")
        print("1. Item Inventory Update")
        print("2. Return to Main Menu")

        choice = input("Enter your choice (1/2): ")


        if choice == '1':
            item_inventory_update()
        elif choice == '2':
            return
        else:
            print("Invalid choice. Please select a valid option (1/2).")



def inventory_initialization():
    ppeFile = "ppe.txt"

    # Check if PPE.TXT file exists
    if not os.path.exists(ppeFile) or (os.path.exists(ppeFile) and os.stat(ppeFile).st_size == 0):
        # Initialize the inventory only if it doesn't exist or is empty
        with open(ppeFile, 'w', newline='') as inventory_file:
            stars = '*' * 150
            inventory_file.write(stars + '\n')

            # Write the header line with rjust(20)
            header = "SUPPLIER CODE".rjust(20) + "ITEM CODE".rjust(20) + "  QUANTITY IN STORE(BOXES)".rjust(20) + "ITEM NAME".rjust(20)
            inventory_file.write(header + '\n')
            inventory_file.write(stars + '\n')

            # Define the initial items and their codes
            initial_items = [
                {"supplier_code": "Supp1", "item_code": "HC", "quantity": 100, "item_name": "Head Cover"},
                {"supplier_code": "Supp2", "item_code": "FS", "quantity": 100, "item_name": "Face Shield"},
                {"supplier_code": "Supp3", "item_code": "MS", "quantity": 100, "item_name": "Mask"},
                {"supplier_code": "Supp4", "item_code": "GL", "quantity": 100, "item_name": "Gloves"},
                {"supplier_code": "Supp1", "item_code": "GW", "quantity": 100, "item_name": "Gown"},
                {"supplier_code": "Supp3", "item_code": "SC", "quantity": 100, "item_name": "Shoe Covers"},
            ]

            for item in initial_items:
                # Add the initial quantity for each item
                entry = item["supplier_code"].rjust(20) + item["item_code"].rjust(20) + str(item["quantity"]).rjust(20) + item["item_name"].rjust(25)
                inventory_file.write(entry + '\n')

def transaction_initialization():
    transactionFile = "transactions.txt"
    # check if PPE.TXT file exits ,if not new is created
    if not os.path.exists(transactionFile):
        with open(transactionFile, 'w', newline='') as transaction_file:
            #if os.path.exists(transactionFile):
            if os.stat(transactionFile).st_size == 0:
                stars = '*' * 150
                transaction_file .write(stars + '\n')
                # Write the header line with rjust(20)
                header = "ITEM CODE".rjust(20) + "HOSPITAL/SUPPLIER CODE".rjust(30) + "RECEIVED/DISTRIBUTED(R/D)".rjust(30) + "QUANTITY CHANGE".rjust(30) + "TIME OF DELIVERY".rjust(30)
                transaction_file.write(header + '\n')

                transaction_file.write(stars + '\n')
transaction_initialization()


def hospital_initialization():
    hospitalFile = "hospitals.txt"
    # check if Hospital.TXT file exits ,if not new is created
    if not os.path.exists(hospitalFile):
        with open(hospitalFile, 'w', newline='') as hospital_file:
            #if os.path.exists(supplierFile):
            if os.stat(hospitalFile).st_size == 0:
                stars = '*' * 75
                hospital_file .write(stars + '\n')
        # Write the header line with rjust(20)
                header = "HOSPITAL CODE".rjust(20) + "HOSPITAL NAME".rjust(20) + "CONTACT N0.".rjust(20)
                hospital_file.write(header + '\n')

                hospital_file.write(stars + '\n')

                #write initial hospital info
                row1 = "HosC1".rjust(17) + "Hospital1".rjust(22) + "0123456789".rjust(20)
                row2 = "HosC2".rjust(17) + "Hospital2".rjust(22) + "0190294729".rjust(20)
                row3 = "HosC3".rjust(17) + "Hospital3".rjust(22) + "0123892740".rjust(20)
                row4 = "HosC4".rjust(17) + "Hospital4".rjust(22) + "0132947920".rjust(20)
                hospital_file.write(row1 + '\n')
                hospital_file.write(row2 + '\n')
                hospital_file.write(row3 + '\n')
                hospital_file.write(row4 + '\n')

hospital_initialization()


# Check if inventory has already been initialized
ppeFile = "ppe.txt"
if not os.path.exists(ppeFile) or (os.path.exists(ppeFile) and os.stat(ppeFile).st_size == 0):
    inventory_initialization()


def item_inventory_update():
    # Main menu
    while True:
        print("\nItem Inventory Management System")
        print("1. Update Item Quantity")
        print("2. Check Stock Quantity")
        print("3. Update Hospital Data")
        print("4. Exit")

        choice = input("Which would you like to choose: ")

        if choice == '1':

            # Modify item data with ITEM_CODE and allow the user to continue updating the same item
            while True:
                item_code_to_update = input("Enter ITEM CODE of the item received/distributed: ").upper()
                update_stock(item_code_to_update)
                continue_updating_another_item = input(
                    "Where they any other items received/distributed? (yes/no): ").lower()
                if continue_updating_another_item != 'yes':
                    break

        elif choice == '2':
            existing_item = read_ppe_data()

            item_code = input("Enter Item Code to search: ")

            found_item = stock_quantity(item_code, existing_item)

            if len(found_item) >= 5 and found_item[4] != " ":
                name = found_item[3] + ' ' + found_item[4]
            else:
                name = found_item[3]

            if found_item:
                print("******Item Details:********************")
                print("\t**Item Code:", found_item[1])
                print("\t**Item Name:", name)
                print("\t**Quantity Available:", found_item[2])
                print("******Item Details:**********************")
            else:
                print("Item Code not found.")


        elif choice == '3':
            # Modify user data with USER_ID and allow the user to continue modifying the same user
            while True:
                hospital_code_to_modify = input("Enter HOSPITAL CODE of the hospital you want to modify information of: ")
                update_hospital(hospital_code_to_modify)
                continue_modifying_another_hospital = input(
                    "Do you want to continue modifying information for another hospital? (yes/no): ").lower()
                if continue_modifying_another_hospital != 'yes':
                    break

            print("Hospital data updated successfully.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
    # Implement Item Inventory Update
    pass

def item_inventory_tracking():
    # Main menu
    while True:
        print("\nItem Inventory Tracking System")
        print("1. Total Available Quantity for each Items")
        print("2. Low Stock Items")
        print("3. Available Quantity for Particular Item")
        print("4. Items Received During a Time Period")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print_total_available_quantity()

        elif choice == '2':
            # Call the function to print items with low stock
            track_low_stock_items()


        elif choice == '3':
            existing_item = read_ppe_data()
            item_code = input("Enter Item Code to search: ")
            found_item = check_quantity(item_code, existing_item)

            if found_item is not None:
                if len(found_item) >= 5 and found_item[4] != " ":
                    name = found_item[3] + ' ' + found_item[4]
                else:
                    name = found_item[3]

                print("******Item Details:********************")

                print("\t**Item Code:", found_item[1])
                print("\t**Item Name:", name)
                print("\t**Quantity Available:", found_item[2])

                print("******Item Details:**********************")

            else:
                print("Item Code not found.")


        elif choice == '4':
            start_date = input("Enter First Date Received (YYYY-MM-DD): ")
            end_date = input("Enter Last Date Received (YYYY-MM-DD): ")
            tracked_transactions = track_items_by_time_period(start_date, end_date)
            if not tracked_transactions:
                print("No items received during the specified time period.")
            else:
                print("Items received during the specified time period:")
                for transaction in tracked_transactions:
                    print(transaction)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


def search_functionalities():
    def read_user_data():
        user_data = []  # Create a list to store user data

        # Open the file for reading
        with open('transactions.txt', 'r') as read_file:
            lines = read_file.readlines()

        # Skip the header line
        lines = lines[2:]

        # Loop through each line and split it into columns
        for line in lines:
            columns = line.strip().split()
            if len(columns) >= 5:
                item_code = columns[0]
                code = columns[1]
                operation = columns[2]
                quantity = int(columns[3])
                date = columns[4]
                user_data.append([item_code, code, quantity, operation, date])

        return user_data

    def search_distribution(item_code, distribution_data, transaction_type):
        filtered_data = []

        for entry in distribution_data:
            if entry[0] == item_code and entry[3] == transaction_type:
                filtered_data.append(entry)

        if transaction_type == 'D':
            # Sum the distribution quantities for the same hospital
            summed_data = []
            for entry in filtered_data:
                hospital_code = entry[1]
                quantity = entry[2]
                date = entry[4]
                found = False
                for summed_entry in summed_data:
                    if summed_entry[1] == hospital_code:
                        summed_entry[2] += quantity
                        found = True
                        break
                if not found:
                    summed_data.append([item_code, hospital_code, quantity, 'D', date])

            return summed_data
        elif transaction_type == 'R':
            # Sum the received quantities for the same supplier
            summed_data = []
            for entry in filtered_data:
                supplier_code = entry[1]
                quantity = entry[2]
                date = entry[4]
                found = False
                for summed_entry in summed_data:
                    if summed_entry[1] == supplier_code:
                        summed_entry[2] += quantity
                        found = True
                        break
                if not found:
                    summed_data.append([item_code, supplier_code, quantity, 'R', date])

            return summed_data
        else:
            return filtered_data

    stored_code = read_user_data()

    while True:
        print("\nOptions:")
        print("1. Search for item distribution to Hospitals")
        print("2. Search for item received from Suppliers")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            item_code = input("Enter the item code: ")
            distribution_data = search_distribution(item_code, stored_code, 'D')

            if not distribution_data:
                print("No distribution data found for the item code.")
            else:
                print("Distribution data to Hospitals:")
                for entry in distribution_data:
                    print(f"Hospital Code: {entry[1]}, Distributed: {entry[2]}, Date: {entry[4]}")

        elif choice == '2':
            item_code = input("Enter the item code: ")
            received_data = search_distribution(item_code, stored_code, 'R')

            if not received_data:
                print("No received data found for the item code.")
            else:
                print("Data from Suppliers:")
                for entry in received_data:
                    print(f"Supplier Code: {entry[1]}, Received: {entry[2]}, Date: {entry[4]}")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")



def user_initialization():
    userFile = "supplier.txt"

    # Check if users.txt file exists
    if not os.path.exists(userFile) or (os.path.exists(userFile) and os.stat(userFile).st_size == 0):
        # Initialize the user data only if it doesn't exist or is empty
        with open(userFile, 'w', newline='') as user_file:
            stars = '*' * 150
            user_file.write(stars + '\n')

            # Write the header line with rjust(20)
            header = "supplier_code".rjust(20) + "NAME".rjust(20) + "TELEPHONE NO".rjust(20) + "distribution(IN BOXES)".rjust(20) + "item_code".rjust(20)
            user_file.write(header + '\n')
            user_file.write(stars + '\n')





# Check if supplier data has already been initialized
userFile = "supplier.txt"
if not os.path.exists(userFile) or (os.path.exists(userFile) and os.stat(userFile).st_size == 0):
    user_initialization()

def supplier_details():
    supplierFile = 'supplier.txt'

    def read_supplier_data():
        item_code = []
        if os.path.exists(supplierFile):
            with open(supplierFile, 'r') as file:
                lines = file.readlines()
                lines = lines[1:]  # Skip the header line
                for line in lines:
                    columns = line.strip().split()
                    if len(columns) >= 5:
                        item = columns[4]
                        item_code.append(item)
        return item_code

    def check_item_code(new_item, existing_code):
        for code in existing_code:
            if code == new_item:
                return False
        return True



    name = input("Enter supplier name: ")
    while len(name) < 3:
        print("Please enter a name with at least 3 characters.")
        name = input("Enter your name: ")

    tel_no = input("Enter supplier number:")
    while len(tel_no) != 10:
        print("Please enter 10 digits.")
        tel_no = input("Enter supplier number again:")

    existing_code = read_supplier_data()

    supplier_code = input("Choose supplier code (supp1, supp2, supp3, supp4): ")
    while supplier_code not in ["supp1", "supp2", "supp3", "supp4"]:
        supplier_code = input("Choose supplier code (supp1, supp2, supp3, supp4) again:")

    item_code = input("Enter item code (HC, FS, MS, GL, GW, SC): ")
    amount_distributed = ''

    while True:
        if item_code not in ["HC", "FS", "MS", "GL", "GW", "SC"]:
            item_code = input("Enter item code again.")
        elif check_item_code(item_code, existing_code):
            amount_distributed = input(
                "Enter amount of boxes distributed (Items are distributed in boxes with 24 items in each box):")
            break
        else:
            print("Item already supplied by another supplier.")
            item_code = input("Enter another item code:")
            amount_distributed = input(
                "Enter amount of boxes received (Items are received in boxes with 24 items in each box):")

    if not os.path.exists(supplierFile):
        with open(supplierFile, 'w', newline='') as supplier_File:
            stars = '*' * 150
            supplier_File.write(stars + '\n')
            header = "supplier_code".rjust(20) + "NAME".rjust(20) + "TELEPHONE_NO ".rjust(
                20) + " distribution(IN BOXES)".rjust(20) + "item_code".rjust(20)
            supplier_File.write(header + '\n')
            supplier_File.write(stars + '\n')

    supplier = []
    supplier.append(supplier_code)
    supplier.append(name)
    supplier.append(tel_no)
    supplier.append(amount_distributed)
    supplier.append(item_code)

    with open(supplierFile, 'a') as Supplier_file:
        supplier_line = supplier[0].rjust(20) + supplier[1].rjust(20) + supplier[2].rjust(20) + supplier[3].rjust(20) + \
                        supplier[4].rjust(20)
        Supplier_file.write(supplier_line + '\n')

    with open("ppe.txt", 'a') as inventory_file:
        if supplier[4] == 'HC':
            inventory_line = supplier[0].rjust(20) + supplier[4].rjust(20) + supplier[3].rjust(20) + 'Head Cover'.rjust(
                20)
            inventory_file.write(inventory_line + '\n')
        elif supplier[4] == 'FS':
            inventory_line = supplier[0].rjust(20) + supplier[4].rjust(20) + supplier[3].rjust(
                20) + 'Face Shield'.rjust(20)
            inventory_file.write(inventory_line + '\n')
        elif supplier[4] == 'MS':
            inventory_line = supplier[0].rjust(20) + supplier[4].rjust(20) + supplier[3].rjust(20) + 'Mask'.rjust(20)
            inventory_file.write(inventory_line + '\n')
        elif supplier[4] == 'GL':
            inventory_line = supplier[0].rjust(20) + supplier[4].rjust(20) + supplier[3].rjust(20) + 'Gloves'.rjust(20)
            inventory_file.write(inventory_line + '\n')
        elif supplier[4] == 'GW':
            inventory_line = supplier[0].rjust(20) + supplier[4].rjust(20) + supplier[3].rjust(20) + 'Gown'.rjust(20)
            inventory_file.write(inventory_line + '\n')
        else:
            inventory_line = supplier[0].rjust(20) + supplier[4].rjust(20) + supplier[3].rjust(
                20) + 'Shoe Covers'.rjust(20)
            inventory_file.write(inventory_line + '\n')

if __name__ == "__main__":
    main_menu()
clear_screen
