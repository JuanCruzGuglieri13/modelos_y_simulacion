# Metodo "mid square" de Von Neumann

def vonNeumann(u):
    u = (u**2 // 100) % 10000
    return u

list = []
x = 3792
for i in range(13):
    list.append(x)
    x_i = vonNeumann(x)
    x = x_i
    

print(list)