# Generadores congruenciales lineales

# a: multiplicador
# c: incremento
# M: modulo
# y_0 semilla

def randMixto(a,c,M,u):
    return (a*u+c) % M

def randMulti(a,M,u):
    return (a*u) % M

def generador(y_0, Nsim, a, c, M):
    list = [y_0]
    
    for i in range(Nsim):
        y_i = randMixto(a, c, M, y_0)
        y_0 = y_i
        list.append(y_0)
        
    return list
        
resultado = generador(y_0=0, Nsim=16, a=5, c=3, M=16)
print(resultado)