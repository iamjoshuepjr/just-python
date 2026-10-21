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
print("+--------------------------------------------------+")
print("-                    Int Data Type                 -")
print("+--------------------------------------------------+")
print(f"  Variable Name:            customer_id")
print(f"  Variable Value:           {customer_id}")
print(f"  Variable Data type:       {type(customer_id)}")
print(f"  Variable Memory Address:  {id(customer_id)}")
print("+--------------------------------------------------+")

branch_code: int = 404
print(f"  Variable Name:            branch_code")
print(f"  Variable Value:           {branch_code}")
print(f"  Variable Data type:       {type(branch_code)}")
print(f"  Variable Memory Address:  {id(branch_code)}")
print("+--------------------------------------------------+\n")

# 2. Float (float)

account_balance: float = 5986365.89
print()
print("+--------------------------------------------------+")
print("-                   Float Data Type                -")
print("+--------------------------------------------------+")
print(f"  Variable Name:            account_balance")
print(f"  Variable Value:           {account_balance} USD")
print(f"  Variable Data type:       {type(account_balance)}")
print(f"  Variable Memory Address:  {id(account_balance)}")
print("+--------------------------------------------------+")

interest_rate: float = 18.5
print(f"  Variable Name:            interest_rate")
print(f"  Variable Value:           {interest_rate} % APY")
print(f"  Variable Data type:       {type(interest_rate)}")
print(f"  Variable Memory Address:  {id(interest_rate)}")
print("+--------------------------------------------------+\n")

# 3. Strings (str)

account_number = "ACC-987654321"
print()
print("+--------------------------------------------------+")
print("-                 String Data Type                 -")
print("+--------------------------------------------------+")
print(f"  Variable Name:            account_number")
print(f"  Variable Value:           {account_number}")
print(f"  Variable Data Type:       {type(account_number)}")
print(f"  Variable Memory Address:  {id(account_number)}")
print("+--------------------------------------------------+")

card_holder_name: str = "Victoria Jackson"
print(f"  Variable Name:            card_holder_name")
print(f"  Variable Value:           {card_holder_name}")
print(f"  Variable Data Type:       {type(card_holder_name)}")
print(f"  Variable Memory Address:  {id(card_holder_name)}")
print("+--------------------------------------------------+\n")

# 4. Booelans 
is_account_active = True

print()
print("+--------------------------------------------------+")
print("-               Booleans Data Type                 -")
print("+--------------------------------------------------+")
print(f"  Variable Name:           is_account_active")
print(f"  Variable Value:          {is_account_active}")
print(f"  Variable Data Type:      {type(is_account_active)}")
print(f"  Variable Memory Address: {id(is_account_active)}")
print("+--------------------------------------------------+")

is_fraud_detected = False
print(f"  Variable Name:           is_fraud_detected")
print(f"  Variable Value:          {is_fraud_detected}")
print(f"  Variable Data Type:      {type(is_fraud_detected)}")
print(f"  Variable Memory Address: {id(is_fraud_detected)}")
print("+--------------------------------------------------+\n")