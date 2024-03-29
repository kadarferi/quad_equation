import re
import math

# ------------------------------------------------------------------

def quad_eq_coefs(eq):
    '''
    Függvény a stringként megadott másodfokú egyenlet paramétereinek 
    kinyerésére
    Az 1-et is ki kell írni, pl: 1*x^2 + 2*x + 1
  
    Args:
        eq (str): A másodfokú egyenlet

    Returns:
        a, b, c (float): Az együtthatók
        None: ha a bemenet nem egy másodfokú egyenlet
    '''
    
    # Reguláris kifejezés az "a*x^2 + b*x + c = 0" formátumra
    pattern = r"^\s*([+-]?\s*\d+(\.\d+)?)\s*\*\s*x\^2" + \
                "\s*([+-]?\s*\d+(\.\d+)?)\s*\*\s*x"    + \
                "\s*([+-]?\s*\d+(\.\d+)?)"             + \
                "\s*=\s*0\s*$"

    # Megkeressük az illeszkedést a mintában
    match = re.match(pattern, eq)

    if match:
        # Az 'a', 'b', és 'c' értékek kinyerése
        a = float(match.group(1).replace(' ', ''))
        b = float(match.group(3).replace(' ', ''))
        c = float(match.group(5).replace(' ', ''))
        return a, b, c
    return None

