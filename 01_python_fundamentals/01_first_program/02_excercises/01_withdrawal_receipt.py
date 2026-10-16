"""
══════════════════════════════════════════════════════════════════════════════════════════════════
                             FUNDAMENTALS - PYTHON & BANKING SYSTEMS
══════════════════════════════════════════════════════════════════════════════════════════════════
 Practical exercise focusing on String Literals: applying single quotes, double quotes
 and triple quotes to construct a dynamic and structured banking deposit receipt.
══════════════════════════════════════════════════════════════════════════════════════════════════
                            D O C U M E N T A T I O N   C R E D I T S
══════════════════════════════════════════════════════════════════════════════════════════════════
 Document Author:  @iamjoshuepjr
 GitHub Profile:   https://github.com/iamjoshuepjr
 Creation Date:    October 16, 2026
 Project:          Python Fundamentals - First Program - Excercises
 Project Status:   Active Learning - String Literals Exercise
 Code Version:     1.0.0

"""

# 1. Defining literals using single quotes (') for short identifier
atm_id = 'AGS_MED01'
transaction_code = '5310'

# 2. Defining using double quotes ("") for description and formatted text
operation_type = "AGS WALLET WITHDRAWAL"
card_mask = "************6502"
account_mask = "*******0000"

# 3. Defining using triple quotes ("""") for multiline blocks (legal disclaimer)
terms_and_conditions = """ 

======================================================
               TERMS AND CONDITIONS
======================================================
1. Minimum balance requirement: $100.00 USD
2. Daily ATM withdrawal limit:  $2,000.00 USD
3. Unauthorized transactions must be reported 
   within 24 hours of occurrence
4. We are the best Bank in the world around. 
"""
legal_disclaimer = """
               AEGIS SOVEREING BANK AND AGS WALLET
             TRANSACTION SUBJECT TO VERIFICATION AND
        APPROVAL BY AEGIS SOVEREING BANK FINANCIAL COMPANY
"""

# Structured console output (simulating the ATM receipt)
print()
print("      =============================================================")
print("                  OPERATION RECORD                 ")
print("      =============================================================")
print("               AUTOMATED TELLER MACHINE            ")
print("      =============================================================")
print("        ATM         DATE      TIME   TRANS  CODE    ")
print(f"       {atm_id}   16/10/26   17:03   1388  {transaction_code}")
print("      -------------------------------------------------------------")
print(f"              CARD NO:           {card_mask}")
print()
print(f"              OPERATION TYPE:     {operation_type}")
print(f"              ACCOUNT NUMBER:     {account_mask}")
print()
print("               AMOUNT:             $***45,985.00 USD")
print("               AVAILABLE BALANCE:  $***963,895.45 USD")
print("      -------------------------------------------------------------")
print(legal_disclaimer)
print("      =============================================================")
print()
