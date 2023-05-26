# Calcular cor amarelo
"""
 R -> 10 11 8 10.5
 G -> 20 22 21 20
 B -> 15 17 16 15
"""

r = [10,11,8,10.5]
g =  [20 ,22 ,21, 20]
b = [15, 17, 16, 15]

def calculoMS(cor):
    m = 0
    m2 = 0
    for i in cor:
        m += i
        m2 += i**2

    M = m/len(cor)
    S = (m2/len(cor) - M**2)**(1/2)
    
    return M, S
print(calculoMS(r))
print(calculoMS(g))
print(calculoMS(b))