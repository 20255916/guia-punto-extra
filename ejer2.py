numero= int(input())
#% da el residuo de una division, entonces si el residuo es 0 el numero es par

if numero %2 == 0:
    s= numero+2 
    z= numero-1
    print(s)
    print(z)
else: 
    s= numero+1
    z= numero-2
    print(s)
    print(z)

