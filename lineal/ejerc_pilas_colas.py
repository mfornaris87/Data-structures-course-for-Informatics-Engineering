from lineal.linked_stack import LinkedStack
from lineal.linked_queue import LinkedQueue

# Clase practica de pilas
# Ejercicio 1
def SumarPrimeros(my_stack, n):
    temp = LinkedStack()
    suma = 0
    if my_stack.is_empty() or len(my_stack) <= 3:
        print("No hay numeros suficientes para sumar")
    else:
        for i in range(len(my_stack)):
            if i < n:
                suma += my_stack.peek()
            temp.push(my_stack.pop())
        while not temp.is_empty():
            my_stack.push(temp.pop())
    return suma

s = LinkedStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)

s.print_stack()
print(SumarPrimeros(s, 4))
s.print_stack()

# Ejercicio 2
def reverse():
    n = int(input("Introduzca un numero:"))
    s = LinkedStack()
    while n != 0:
        s.push(n)
        n = int(input("Introduzca un numero:"))
    s.print_stack()

reverse()

# Ejercicio 4
def cambiaSigno(my_stack):
    temp = LinkedStack()
    while not my_stack.is_empty():
        temp.push(-1 * my_stack.pop())
    while not temp.is_empty():
        my_stack.push(temp.pop())
    my_stack.print_stack()

cambiaSigno(s)

# def palindrome(palabra):
#     temp = LinkedStack()
#     aux = LinkedStack()
#     for i in range(len(palabra)):
#         temp.push(palabra[i])
#     while not temp.is_empty():
