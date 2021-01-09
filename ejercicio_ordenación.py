import random;
 
# función que genera una matriz con datos aleatorios
# recibe como parámetro la matriz a rellenar, la cantidad de matrizes y la longitud de estos
def generarDatos(pMatriz,pX,pY):
  for x in range(0,pX):
    arr = [];
    for j in range(0,pY):
      n = random.randint(1, 100);
      arr.append(n);

    matriz.append(arr);
    
# función que recibe por parametro jn string y una matriz y pints su contenido línea por línea
def pintarDatos(cadena,matriz):
  print(cadena)
  for x in matriz:
    print(x)

# función que recibe una matriz de enteros y lo ordena 
def ordenarMatriz(matriz, pX, pY):
  #en este bucle sacamos los datos de la matriz y lo pasamos a un array normal
  auxArray = [];
  for x in matriz:
    for h in x:
      auxArray.append(h);
  
  # en este bucle ordenamos el array anterior usando el algoritmo de burbuja
  # el metodo range acepta hasta tres parametros:
  # el primero es donde empieza el bucle
  # el segundo es donde termina el bucle
  # el tercero es la iterancion entre elementos que por defecto es 1
  for numPasada in range(len(auxArray)-1,0,-1):
        for i in range(numPasada):
            if auxArray[i]>auxArray[i+1]:
                temp = auxArray[i]
                auxArray[i] = auxArray[i+1]
                auxArray[i+1] = temp
  
  # bucle que a traves del array anterior introduce en la matriz de nuevo los numeros pero ordenador
  for x in range(0,pX):
    arr = [];
    for j in range(0,pY):
      arr.append(auxArray.pop(0));
    matriz[x] = arr;

# matriz donde vamos a insertar los enteros     
matriz = [];
# numero de elementos en la matriz
x = 7;
# longitud de los elementos de las matrizes
y = 8;
generarDatos(matriz,x,y);
pintarDatos("MATRIZ SIN ORDENAR",matriz);
ordenarMatriz(matriz, x, y);
pintarDatos("MATRIZ ORDENADA",matriz);
