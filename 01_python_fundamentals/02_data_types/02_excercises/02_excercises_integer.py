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

print()
print("          =============================================")
print("                      AEGIS SOVEREIGN BANK             ")
print("          =============================================")
print(f"          Transaction Count: {transaction_count:,}")
print(f"          ATM: {atm_id} ")
print(f"          Failed Login Attempts: {failed_login_attempts} ")
print("          =============================================")
print("                           METADATA")
print("          =============================================")
print("           1. transaction_count")
print(f"             Datatype    -> {type(transaction_count).__name__}")
print(f"             Memory ID   -> {id(transaction_count)}")
print(f"             Is Integer  -> {isinstance(transaction_count, int)}\n")
print("           2. atm_id")
print(f"             Datatype    -> {type(atm_id).__name__}")
print(f"             Memory ID   -> {id(atm_id)}")
print(f"             Is Integer  -> {isinstance(atm_id, int)}\n")
print("           3. failed_login_attepmts")
print(f"             Datatype    -> {type(failed_login_attempts).__name__}")
print(f"             Memory ID   -> {id(failed_login_attempts)}")
print(f"             Is Intger   -> {isinstance(transaction_count, int)}")
print(f"\n        ")
print()