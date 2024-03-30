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

# ------------------------------------------------------------------

def quad_eq_solver(a, b, c):
    '''
    Függvény a másodfokú egyenlet megoldására valós számok halmazán
  
    Args:
        a, b, c (float): Az együtthatók

    Returns:
        x1, x2 (float): A megoldások
        None: Ha nincs valós megoldás
    '''
    # Diszkrimináns
    dis = b*b - 4*a*c

    if dis >= 0: 
        dis_sqrt = math.sqrt(dis)
        x1 = (-b + dis_sqrt) / (2 * a)
        x2 = (-b - dis_sqrt) / (2 * a)
        return x1, x2
    return None

# ------------------------------------------------------------------
# Példa a fenti függvények alkalmazására

eq = " -1*x^2 - 2.1 * x + 1 = 0"

coefs = quad_eq_coefs(eq)
if coefs:
    print('Egyenlet: ' + eq)
    print(f'Együtthatók: a= {coefs[0]}, b= {coefs[1]}, c= {coefs[2]}')
    x = quad_eq_solver(*coefs)
    if x:
        print(f'Az egyenlet megoldásai: {x[0]}, {x[1]}.')
    else:
        print('Az egyenletnek nincs valós megoldása.')
else:
    print('Nem megfelelõ formátumú egyenlet!')

