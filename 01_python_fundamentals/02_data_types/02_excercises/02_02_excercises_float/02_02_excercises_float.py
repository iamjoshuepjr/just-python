"""
══════════════════════════════════════════════════════════════════════════════════════════════════
                                FUNDAMENTALS - PYTHON DATA TYPES
══════════════════════════════════════════════════════════════════════════════════════════════════
                            D O C U M E N T A T I O N   C R E D I T S
══════════════════════════════════════════════════════════════════════════════════════════════════
 Document Author:  @iamjoshuepjr
 GitHub Profile:   https://github.com/iamjoshuepjr
 Creation Date:    November 25, 2026
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

# 1. Float (float)

available_liquidity: float = 14736749.32
annual_percentage_yiled: float = 11.80
fx_spot_rate: float = 1.0845
overdraft_limit: float = 650900.00
interbank_fee_rate: float = 0.0015
reserve_requeriment_ratio: float = 0.08
pending_settlement_amount: float = 525000.00


print()
print("          =============================================")
print("                      AEGIS SOVEREIGN BANK             ")
print("          =============================================")
print(f"          Available Liquidity:       {available_liquidity:,}")
print(f"          Anual Percentage Yiled:    {annual_percentage_yiled} ")
print(f"          FX Spot Rate:              {fx_spot_rate}")
print(f"          Overdraft Limit:           {overdraft_limit:,}")
print(f"          Reserve Requeriment Ratio: {reserve_requeriment_ratio}")
print(f"          Pending Settlement Amount: {pending_settlement_amount:,} ")
print("          =============================================")
print("                           METADATA")
print("          =============================================")
print("           1. available_liquidity")
print(f"             Datatype    -> {type(available_liquidity).__name__}")
print(f"             Memory ID   -> {id(available_liquidity)}")
print(f"             Is Float    -> {isinstance(available_liquidity, float)}\n")
print("           2. annual_percentage_yiled")
print(f"             Datatype    -> {type(annual_percentage_yiled).__name__}")
print(f"             Memory ID   -> {id(annual_percentage_yiled)}")
print(f"             Is Float    -> {isinstance(annual_percentage_yiled, float)}\n")
print("           3. fx_spot_rate")
print(f"             Datatype    -> {type(fx_spot_rate).__name__}")
print(f"             Memory ID   -> {id(fx_spot_rate)}")
print(f"             Is Float    -> {isinstance(fx_spot_rate, float)}\n")
print("           4. overdraft_limit")
print(f"             Datatype    -> {type(overdraft_limit).__name__}")
print(f"             Memory ID   -> {id(overdraft_limit)}")
print(f"             Is Float    -> {isinstance(overdraft_limit, float)}\n")
print("           5. interbank_fee_rate")
print(f"             Datatype    -> {type(interbank_fee_rate).__name__}")
print(f"             Memory ID   -> {id(interbank_fee_rate)}")
print(f"             Is Float    -> {isinstance(interbank_fee_rate, float)}\n")
print("           6. reserve_requeriment_ratio")
print(f"             Datatype    -> {type(reserve_requeriment_ratio).__name__}")
print(f"             Memory ID   -> {id(reserve_requeriment_ratio)}")
print(f"             Is Float    -> {isinstance(reserve_requeriment_ratio, float)}\n")
print("           7. pending_settlement_amount")
print(f"             Datatype    -> {type(pending_settlement_amount).__name__}")
print(f"             Memory ID   -> {id(pending_settlement_amount)}")
print(f"             Is Float    -> {isinstance(pending_settlement_amount, float)}\n")
print()