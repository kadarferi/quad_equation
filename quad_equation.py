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

# ------------------------------------------------------------------

def quad_eq_solver(a, b, c):
    '''
    F�ggv�ny a m�sodfok� egyenlet megold�s�ra val�s sz�mok halmaz�n
  
    Args:
        a, b, c (float): Az egy�tthat�k

    Returns:
        x1, x2 (float): A megold�sok
        None: Ha nincs val�s megold�s
    '''
    # Diszkrimin�ns
    dis = b*b - 4*a*c

    if dis >= 0: 
        dis_sqrt = math.sqrt(dis)
        x1 = (-b + dis_sqrt) / (2 * a)
        x2 = (-b - dis_sqrt) / (2 * a)
        return x1, x2
    return None

# ------------------------------------------------------------------
# P�lda a fenti f�ggv�nyek alkalmaz�s�ra

eq = " -1*x^2 - 2.1 * x + 1 = 0"

coefs = quad_eq_coefs(eq)
if coefs:
    print('Egyenlet: ' + eq)
    print(f'Egy�tthat�k: a= {coefs[0]}, b= {coefs[1]}, c= {coefs[2]}')
    x = quad_eq_solver(*coefs)
    if x:
        print(f'Az egyenlet megold�sai: {x[0]}, {x[1]}.')
    else:
        print('Az egyenletnek nincs val�s megold�sa.')
else:
    print('Nem megfelel� form�tum� egyenlet!')

