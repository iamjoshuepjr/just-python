"""
══════════════════════════════════════════════════════════════════════════════════════════════════
                             FUNDAMENTALS - STRING LITERALS
══════════════════════════════════════════════════════════════════════════════════════════════════
 Python uses: 
 1. Single quotes (')
 2. Double quotes ("), 
 3. Triple single quotes ('''), and triple-double (\"\"\") quotes to denote string literals.
 
 Key Takeaways:
 1. Single and double quotes are interchangeable for single-line strings.
 2. Using single quotes inside double quotes (or vice versa) avoids escaping characters.
 3. Triple quotes allow multiline strings, ideal for receipt templates and documentation.
══════════════════════════════════════════════════════════════════════════════════════════════════
                            D O C U M E N T A T I O N   C R E D I T S
══════════════════════════════════════════════════════════════════════════════════════════════════
 Document Author:  @iamjoshuepjr
 GitHub Profile:   https://github.com/iamjoshuepjr
 Creation Date:    October 16, 2026
 Project:          Python Fundamentals - First Program - String Literals
 Project Status:   Active Learning - Python Basics & String Literals
 Code Version:     1.0.0

"""

# 1. Single coutes for short idetifiers
bank_code = 'AGS'

# 2. Double quotes when the text contains apostrophes or single quotes
bank_name = "Aegis Sovereing Bank"
account_alias = "Valery's Personal Checking Account"

# 3. Triple double quotes for multiline bankig notices or disclousures
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

# Printing string literals output
print(bank_code)
print(bank_name)
print(account_alias)
print(terms_and_conditions)