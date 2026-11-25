"""
══════════════════════════════════════════════════════════════════════════════════════════════════
                                FUNDAMENTALS - PYTHON DATA TYPES
══════════════════════════════════════════════════════════════════════════════════════════════════
                            D O C U M E N T A T I O N   C R E D I T S
══════════════════════════════════════════════════════════════════════════════════════════════════
 Document Author:  @iamjoshuepjr
 GitHub Profile:   https://github.com/iamjoshuepjr
 Creation Date:    November 19, 2026
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

transaction_count: int = 9652369854
atm_id: int = 45645123121481
failed_login_attempts: int = 3
customer_id: int = 120364
employee_id: int = 10546
branch_id: int = 319
credit_score: int = 908
daily_withdrawal_count: int = 5

print()
print("          =============================================")
print("                      AEGIS SOVEREIGN BANK             ")
print("          =============================================")
print(f"          Branch ID: {branch_id}")
print(f"          ATM: {atm_id} ")
print(f"          Transaction Count: {transaction_count:,}")
print(f"          Customer ID: {customer_id}") # Omit the thousands separator (:,) because this value represents an identifier, not a quantity.
print(f"          Employee ID: {employee_id}") # Omit the thousands separator (:,) because this value represents an identifier, not a quantity.
print(f"          Credit Score: {credit_score}")
print(f"          Failed Login Attempts: {failed_login_attempts} ")
print("          =============================================")
print("                           METADATA")
print("          =============================================")
print("           1. branch_id")
print(f"             Datatype    -> {type(branch_id).__name__}")
print(f"             Memory ID   -> {id(branch_id)}")
print(f"             Is Integer  -> {isinstance(branch_id, int)}\n")
print("           2. atm_id")
print(f"             Datatype    -> {type(atm_id).__name__}")
print(f"             Memory ID   -> {id(atm_id)}")
print(f"             Is Integer  -> {isinstance(atm_id, int)}\n")
print("           3. transaction_count")
print(f"             Datatype    -> {type(transaction_count).__name__}")
print(f"             Memory ID   -> {id(transaction_count)}")
print(f"             Is Integer  -> {isinstance(transaction_count, int)}\n")
print("           4. customer_id")
print(f"             Datatype    -> {type(customer_id).__name__}")
print(f"             Memory ID   -> {id(customer_id)}")
print(f"             Is Integer  -> {isinstance(customer_id, int)}\n")
print("           5. employee_id")
print(f"             Datatype    -> {type(employee_id).__name__}")
print(f"             Memory ID   -> {id(employee_id)}")
print(f"             Is Integer  -> {isinstance(employee_id, int)}\n")
print("           6. credit_score")
print(f"             Datatype    -> {type(credit_score).__name__}")
print(f"             Memory ID   -> {id(credit_score)}")
print(f"             Is Integer  -> {isinstance(credit_score, int)}\n")
print("           7. failed_login_attepmts")
print(f"             Datatype    -> {type(failed_login_attempts).__name__}")
print(f"             Memory ID   -> {id(failed_login_attempts)}")
print(f"             Is Intger   -> {isinstance(transaction_count, int)}")
print(f"\n        ")
print()