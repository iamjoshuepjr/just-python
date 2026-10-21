"""
══════════════════════════════════════════════════════════════════════════════════════════════════
                             FUNDAMENTALS - PYTHON DATA TYPES
══════════════════════════════════════════════════════════════════════════════════════════════════
 In computing, data serves as the raw material that we process and transform into useful, 
 structured information. To manage this data correctly, systems rely on data types—a 
 classification mechanism that defines how information is stored in memory, what operations 
 are permitted on it, and how it must be interpreted through integers, decimals, text strings, 
 and booleans.
══════════════════════════════════════════════════════════════════════════════════════════════════
                            D O C U M E N T A T I O N   C R E D I T S
══════════════════════════════════════════════════════════════════════════════════════════════════
 Document Author:  @iamjoshuepjr
 GitHub Profile:   https://github.com/iamjoshuepjr
 Creation Date:    October 19, 2026
 Project:          Python Fundamentals - Data Types
 Project Status:   Active Learning - Data Types
 Code Version:     1.0.0
"""

# =========================================
#          SESION 1 - DATA TYPES
# =========================================

# var_name: type       -> indicates reference to the data type we are using (type hint)
# the type() function -> allows us to know the data type of the variable
# the id() function   -> allows us to know the memory address in which the value is stored

# 1. Integer (int)
customer_id: int = 789236412

print()
print("+-----------------------------------+")
print("-           Int Data Type           -")
print("+-----------------------------------+")
print(f"  Variable value: {customer_id}")
print(f"  Data type: {type(customer_id)}")
print(f"  Memory address: {id(customer_id)}")
print("+-----------------------------------+\n")

# 2. Float (float)
account_balance: float = 5986365.89
print()
print("+-----------------------------------+")
print("-          Float Data Type          -")
print("+-----------------------------------+")
print(f"  Variable value: {account_balance} USD")
print(f"  Data type: {type(account_balance)}")
print(f"  Memory address: {id(account_balance)}")
print("+-----------------------------------+\n")


# 3. Strings (str)
account_number = "ACC-987654321"
print()
print("+-----------------------------------+")
print("-         String Data Type          -")
print("+-----------------------------------+")
print(f"Variable value: {account_number}")
print(f"Data Type: {type(account_number)}")
print(f"Memory address: {id(account_number)}")


# 4. Booelans 
is_account_active = True

print()
print("+-----------------------------------+")
print("-       Booleans Data Type          -")
print("+-----------------------------------+")
print(f"Variable value: {is_account_active}")
print(f"Data Type: {type(is_account_active)}")
print(f"Memory address: {id(is_account_active)}")
