"""
══════════════════════════════════════════════════════════════════════════════════════════════════
                                FUNDAMENTALS - PYTHON DATA TYPES
══════════════════════════════════════════════════════════════════════════════════════════════════
                            D O C U M E N T A T I O N   C R E D I T S
══════════════════════════════════════════════════════════════════════════════════════════════════
 Document Author:  @iamjoshuepjr
 GitHub Profile:   https://github.com/iamjoshuepjr
 Creation Date:    November 26, 2026
 Project:          Python Fundamentals - Data Types
 Project Status:   Active Learning - Data Types 
 Code Version:     1.0.0
"""

# =========================================
#          SESION 1 - DATA TYPES
# =========================================

# var_name: type      -> indicates reference to the data type we are using (type hint)
# the type() function -> allows us to know the data type of the variable
# the id() function   -> allows us to know the memory address in which the value is stored

# 1. String (str)

document_type_code: str = "CC"
compilance_status_code: str = "APROVED"
transaction_reference_id: str = "TXN-2026-994810-A"
account_number: str = "009-123456-78"
ach_clearing_code: str = "00"
mdm_golden_record_id: str = "MDM-CO-99481023"
account_trier_label: str = "Private Banking"

print()
print()
print("          =============================================")
print("                      AEGIS SOVEREIGN BANK             ")
print("          =============================================")
print(f"          Document Type Code:      {document_type_code}")
print(f"          Compilance Status Code:  {compilance_status_code} ")
print(f"          Transaction Referece ID: {transaction_reference_id}")
print(f"          Account Number:          {account_number}") 
print(f"          ACH Clearing Code:       {ach_clearing_code}") 
print(f"          MDM Golden Record ID:    {mdm_golden_record_id}")
print(f"          Account Trier Label:     {account_trier_label} ")
print("          =============================================")
print("                           METADATA")
print("          =============================================")
print("           1. document_type_code")
print(f"             Datatype    -> {type(document_type_code).__name__}")
print(f"             Memory ID   -> {id(document_type_code)}")
print(f"             Is String  -> {isinstance(document_type_code, str)}\n")
print("           2. compilance_status_code")
print(f"             Datatype    -> {type(compilance_status_code).__name__}")
print(f"             Memory ID   -> {id(compilance_status_code)}")
print(f"             Is String  -> {isinstance(compilance_status_code, str)}\n")
print("           3. transaction_reference_id")
print(f"             Datatype    -> {type(transaction_reference_id).__name__}")
print(f"             Memory ID   -> {id(transaction_reference_id)}")
print(f"             Is String  -> {isinstance(transaction_reference_id, str)}\n")
print("           4. account_number")
print(f"             Datatype    -> {type(account_number).__name__}")
print(f"             Memory ID   -> {id(account_number)}")
print(f"             Is String  -> {isinstance(account_number, str)}\n")
print("           5. ach_clearing_code")
print(f"             Datatype    -> {type(ach_clearing_code).__name__}")
print(f"             Memory ID   -> {id(ach_clearing_code)}")
print(f"             Is String  -> {isinstance(ach_clearing_code, str)}\n")
print("           6. mdm_golden_record_id")
print(f"             Datatype    -> {type(mdm_golden_record_id).__name__}")
print(f"             Memory ID   -> {id(mdm_golden_record_id)}")
print(f"             Is String  -> {isinstance(mdm_golden_record_id, str)}\n")
print("           7. account_trier_label")
print(f"             Datatype    -> {type(account_trier_label).__name__}")
print(f"             Memory ID   -> {id(account_trier_label)}")
print(f"             Is String   -> {isinstance(account_trier_label, str)}")
print(f"\n        ")