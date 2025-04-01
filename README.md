# Inventory Management System for Personal Protective Equipment (PPE)

## Project Overview
This console-based application provides a comprehensive solution for managing Personal Protective Equipment (PPE) inventory. It facilitates tracking, distribution, and monitoring of essential protective gear used in healthcare settings.

## Features

### User Management
- **User Authentication**: Secure login system with role-based access control
- **User Registration**: Add new users with validation for credentials
- **User Modification**: Update existing user information
- **User Deletion**: Remove users from the system
- **User Search**: Find specific users by ID

### Inventory Update Management
- **Item Quantity Updates**: Record receipt and distribution of PPE items
- **Stock Verification**: Check current quantities of specific items
- **Hospital Information Management**: Update hospital contact details

### Item Inventory Tracking
- **Total Available Quantities**: View all items with their current stock levels
- **Low Stock Alerts**: Identify items with fewer than 25 boxes remaining
- **Item-Specific Tracking**: Monitor individual item quantities
- **Time Period Analysis**: Track items received within a specified date range

### Search Functionalities
- **Distribution Search**: Find items distributed to specific hospitals
- **Supply Search**: Track items received from particular suppliers

### Item Supplying
- **Supplier Management**: Record and maintain supplier details
- **Distribution Tracking**: Monitor supply chain and distribution logistics

## File Structure
The system uses text files for data persistence:
- `users.txt`: User account information
- `ppe.txt`: PPE inventory data
- `transactions.txt`: Record of all inventory movements
- `hospitals.txt`: Hospital information
- `supplier.txt`: Supplier details

## Requirements
- Python 3.x
- Operating system that supports command-line interface

## Installation and Usage
1. Clone the repository or download the source code
2. Navigate to the project directory
3. Run the script:
   ```
   python inventory_management.py
   ```
4. Navigate through the menu system using numeric inputs

## Sample Usage

### Main Menu
```
**************************************************
                Main Menu:
**************************************************
1. User Management
2. Inventory Update Management
3. Item Inventory Tracking
4. Search Functionalities
5. Item Supplying
6. Exit
```

### Accessing User Management
```
Enter your choice (1/2/3/4/5/6): 1
Enter your user ID: Akira64
Enter your password: Kingr123
ACCESS GRANTED
```

## Data Format
The application automatically initializes with sample data including:
- Admin user credentials
- Basic PPE items (Head Cover, Face Shield, Mask, Gloves, Gown, Shoe Covers)
- Hospital information (4 sample hospitals)

## Authentication
Default admin credentials:
- **User ID**: Akira64
- **Password**: Kingr123

## Authors
- **Abdirashid Mohamed Akira
- **Kashave Sathyvell A/L Sathyvell

## License
This project is provided for educational purposes. All rights reserved. part of Asia pacific University module

---

*This README provides basic information about the PPE Inventory Management System. For detailed documentation, check here 
