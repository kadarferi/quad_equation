import re
import math

# ------------------------------------------------------------------

def quad_eq_coefs(eq):
    '''
    F�ggv�ny a stringk�nt megadott m�sodfok� egyenlet param�tereinek 
    kinyer�s�re
    Az 1-et is ki kell �rni, pl: 1*x^2 + 2*x + 1
  
    Args:
        eq (str): A m�sodfok� egyenlet

    Returns:
        a, b, c (float): Az egy�tthat�k
        None: ha a bemenet nem egy m�sodfok� egyenlet
    '''
    
    # Regul�ris kifejez�s az "a*x^2 + b*x + c = 0" form�tumra
    pattern = r"^\s*([+-]?\s*\d+(\.\d+)?)\s*\*\s*x\^2" + \
                "\s*([+-]?\s*\d+(\.\d+)?)\s*\*\s*x"    + \
                "\s*([+-]?\s*\d+(\.\d+)?)"             + \
                "\s*=\s*0\s*$"

    # Megkeress�k az illeszked�st a mint�ban
    match = re.match(pattern, eq)

    if match:
        # Az 'a', 'b', �s 'c' �rt�kek kinyer�se
        a = float(match.group(1).replace(' ', ''))
        b = float(match.group(3).replace(' ', ''))
        c = float(match.group(5).replace(' ', ''))
        return a, b, c
    return None

