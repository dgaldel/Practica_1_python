# hacer un pseudocodigo para introducir las edades de los 25 alumnos de la clase
# y sacar la edad mayor , la edad menor , numero de edades pares , numero de edades # impares y el factorial del mayor primo 
import random

contador = 0;
mayor = 0;
menor = 0;
total_pares = 0;
total_impares= 0;
mayor_primo=0;
boolean = 0;
for contador in range(0, 25):
  print("Introduce una edad");
  numero = random.randint(1, 20) #int(input());
  print(numero);
  if contador == 0:
    mayor = numero;
    menor = numero;
  else :
    if numero > mayor:
      mayor = numero;
    if numero < menor:
      menor = numero;
    
  if (numero % 2) == 0:
    total_pares +=1;
  else :
    total_impares+=1;
  boolean = 0;
  if numero == 1 :
    boolean= 1;
  else :
    if numero == 2:
      boolean = 1;
    else :
      j = 2;

      for j in range(2,numero-1):
        if (numero % j) == 0:
          if numero > mayor_primo:
            boolean=1;
    
      if boolean == 0:
        if numero > mayor_primo:
          mayor_primo = numero;

if mayor_primo != 0:
  print("mayor primo:");
  print(mayor_primo);
  factorial_total = 1
  while mayor_primo > 1:
      factorial_total *= mayor_primo
      mayor_primo -= 1

  print("factorial:")
  print(factorial_total);
print("mayor:")
print(mayor);
print("menor:")
print(menor);
print("total_pares:")
print(total_pares);
print("total impares:")
print(total_impares);
