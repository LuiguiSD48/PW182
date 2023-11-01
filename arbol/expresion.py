import math

class Nodo:
    def __init__(self, valor):
        self.valor=valor
        self.izquierdo=None
        self.derecho=None
        
def evaluar_arbol_expression(nodo,valores):
    if isinstance(nodo.valor,int):
        return nodo.valor
    if nodo.valor=="x":
        return valores["x"]
    if nodo.valor=='+':    
        return evaluar_arbol_expression(nodo.izquierdo,valores) + evaluar_arbol_expression(nodo.derecho,valores)
    if nodo.valor=='-':    
        return evaluar_arbol_expression(nodo.izquierdo,valores) - evaluar_arbol_expression(nodo.derecho,valores) 
    if nodo.valor=='*':    
        return evaluar_arbol_expression(nodo.izquierdo,valores) * evaluar_arbol_expression(nodo.derecho,valores)
    if nodo.valor=='/':    
        derecha= evaluar_arbol_expression(nodo.derecho, valores)
        if derecha !=0:
            return evaluar_arbol_expression(nodo.izquierda, valores)/derecha
    
        else:
            raise ValueError("Division por 0")
        
arbol_expresion=Nodo('+')
arbol_expresion.izquierdo=Nodo('-')
arbol_expresion.izquierdo.izquierdo=Nodo(2)
arbol_expresion.izquierdo.derecho=Nodo('x')
arbol_expresion.izquierdo.izquierdo.izquierdo=Nodo(-1)
arbol_expresion.izquierdo.izquierdo.derecho=Nodo(3)
arbol_expresion.izquierdo.izquierdo.izquierdo.izquierdo=Nodo(1)
arbol_expresion.izquierdo.izquierdo.izquierdo.derecho=Nodo('x')
arbol_expresion.izquierdo.izquierdo.izquierdo.izquierdo.izquierdo=Nodo(-2)
arbol_expresion.izquierdo.izquierdo.izquierdo.izquierdo.derecho=Nodo('x')
arbol_expresion.derecho=Nodo(5)

while True:
    try:
        x=float(input("Ingresa un valor para x (o q para salir)")) 
        if x=='q':
            break
        valores={'x':x}
        resultado=evaluar_arbol_expression(arbol_expresion,valores)
        print(f"El resultado de la expresion para x = {x} es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print(f"\nSaliendo del programa")
        break
    