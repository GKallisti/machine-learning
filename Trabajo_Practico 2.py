import numpy as np

vector_py = [1, 2, 3, 4, 5]
vector_np = np.array([1, 2, 3.5, 4, 5])
print("Vector en Python puro:", vector_py)
print("Vector en NumPy:", vector_np)
# Vector en Python puro: [1, 2, 3, 4, 5]
# Vector en NumPy: [1. 2. 3.5 4. 5. ]

vector_py = [1, 2, 3, 4, 5]
vector_np = np.array([1, 2, 3, 4, 5])
suma_py = [x + 2 for x in vector_py]
suma_np = vector_np *2
#print("Suma en Python puro:", suma_py)
#print("Suma en NumPy:", suma_np)
vector_py*2

vector_py = [1, 2, 3, 4, 5]
vector_np = np.array([1, 2, 3, 4, 5])
segmento_py = vector_py[1:4]
segmento_np = vector_np[1:4]
print("Segmento en Python puro:", segmento_py)
print("Segmento en NumPy:", segmento_np)

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])
suma_vector = vector_a + vector_b
print("Suma de vectores:", suma_vector)

ventas_diarias = np.array(
    #Lun,Mar,Mie,Jue,Vie,Sab,Dom
    [[20, 15, 25, 30, 18, 22, 24],  #Producto A
    [12, 20, 14, 8, 15, 18, 16],    #Producto B
    [35, 28, 32, 30, 26, 24, 30],   #Producto C
    [40, 38, 45, 42, 39, 41, 37]    #Producto D
    ]
)

print("Matriz de ventas diarias:",ventas_diarias)

#==== FORMAS DE RECORRER UNA MATRIZ FIJADA LA COLUMNA J=1
#    Calcula la suma total del dia lunes
suma=0
for i in range(4):
  print(ventas_diarias[i,1])
  suma=suma+ventas_diarias[i,1]
print('la suma total del lunes es:', suma)

#===== IMPLEMENTACIÓN DE UN MÉTODO DE NUMPY
# Sumar las ventas por día (sumar las columnas)
ventas_por_dia = np.sum(ventas_diarias, axis=0)
print("Total de ventas por día:",ventas_por_dia)


############### EJERCICIOS PARTE 1:  NUMERO 2   ##########################################

#import numpy as np

n = int(input("Ingresa la cantidad de elementos en la lista: "))

lista_numeros = []

for i in range(n):
    numero = float(input(f"Ingrese el elemento {i+1}: "))
    while numero <= 0:
        print("Por favor, ingresa un número real positivo.")
        numero = float(input(f"Ingrese el elemento {i+1}: "))
    lista_numeros.append(numero)

# Convertir la lista en un vector de NumPy
vector_numpy = np.array(lista_numeros)

print("Vector de NumPy resultante:", vector_numpy)


################### EJERCICIOS PARTE 1: NUMERO 3   ########################################

num_filas = int(input("Ingresa la cantidad de filas de la tabla: "))
num_columnas = int(input("Ingresa la cantidad de columnas de la tabla: "))

tabla_datos = []

for i in range(num_filas):
    fila = []
    for j in range(num_columnas):
        dato = float(input(f"Ingrese el dato de la fila {i+1}, columna {j+1}: "))
        fila.append(dato)
    tabla_datos.append(fila)

matriz_numpy = np.array(tabla_datos)

print("Tabla ingresada en formato lista:")
for fila in tabla_datos:
    print(fila)

print("Tabla ingresada en formato array de NumPy:\n", matriz_numpy)

fila1 = int(input("Ingresa la posición de la primera fila a sumar (empezando desde 0): "))
fila2 = int(input("Ingresa la posición de la segunda fila a sumar (empezando desde 0): "))

suma_filas = matriz_numpy[fila1] + matriz_numpy[fila2]

print("Vector resultado de la suma de las filas:", suma_filas)



#################### EJERCICIOS PARTE 1: NUMERO 4   ########################################

productos = ['arroz', 'harina', 'fideo', 'yerba', 'azucar']
valores_iniciales = np.array([145.6, 100, 89.90, 700, 95])

valores_actualizados = np.copy(valores_iniciales)
valores_actualizados[productos.index('arroz')] *= 2
valores_actualizados[productos.index('harina')] *= 2
valores_actualizados[productos.index('azucar')] *= 2
valores_actualizados[productos.index('fideo')] *= 1.75
valores_actualizados[productos.index('yerba')] *= 1.75

print("Valores iniciales de los productos:")
print(valores_iniciales)

print("\nValores actualizados de los productos:")
print(valores_actualizados)

##################### EJERCICIOS PARTE 1: NUMERO 5   ########################################


# Comando/Función            |    Operación/Funcionalidad	                                      | Resultado	                        Ejemplo
#1   np.array([lista])	     |     Crea un vector o matriz con NumPy	                          |  np.array([1.6, 2, 0, 6.75])
#2 	np.sqrt(vector)	         |     Calcula la raíz cuadrada de cada elemento del vector           |  np.sqrt(vector_np)
#3	np.random.rand(n)	     |     Genera un vector con valores aleatorios entre 0 y 1            |  np.random.rand(5)
#4	np.ones((n))	         |     Crea un vector con valores de 1                                | np.ones((3))
#5	np.zeros((n))	         |     Crea un vector con valores de 0	                              | np.zeros((3))
#6	np.min(array)	         |     Calcula el valor mínimo del vector o matriz	                  | np.min(vector_np)
#7	np.max(array)	         |     Calcula el valor máximo del vector o matriz	                  | np.max(vector_np)
#8	np.where(CONDICIÓN)	     | Devuelve los índices donde se cumple una condición sobre el vector |	np.where(vector_np > 1)
#9	np.random.shuffle(MATRIZ)|	Mezcla aleatoriamente las filas de una matriz	                         | Ver Ejercicio Parte 2
#10	array.shape[n]	         |   Devuelve las dimensiones de la matriz en la posición n	                 | Ver Ejercicio Parte 2
#11	np.sum(array, axis=n)    |	Calcula la suma a lo largo del eje n	                                 |  Ver Ejercicio Parte 1
#12	np.arange(a, b, p)	     |   Crea un vector con valores espaciados con paso p en el intervalo [a, b) |	np.arange(0, 10, 0.1)


######################### EJERCICIOS PARTE 2: NUMERO 1   ########################################


dataset = np.array([[25, 1, 7, 100, 1],
                    [30, 2, 5, 120, 0],
                    [22, 1, 6, 80, 1],
                    [28, 1, 6, 90, 0],
                    [35, 2, 4, 130, 1],
                    [32, 2, 6, 110, 1],
                    [26, 1, 8, 95, 1],
                    [24, 1, 5, 85, 0],
                    [29, 2, 7, 115, 1],
                    [31, 2, 6, 105, 0]])

np.random.shuffle(dataset)

filas_entrenamiento = int(0.7 * dataset.shape[0])  
filas_prueba = dataset.shape[0] - filas_entrenamiento

array_entrenamiento = dataset[:filas_entrenamiento]
array_prueba = dataset[filas_entrenamiento:]

print("Matriz con filas mezcladas:")
print(dataset)
print("\nArray de Entrenamiento:")
print(array_entrenamiento)
print("\nArray de Prueba:")
print(array_prueba)

############################# EJERCICIOS PARTE 2: NUMERO 2   ########################################
##información
poblacionArgentina1=[
['PROVINCIA','CANTIDAD DE HABITANTES','CONSUMO EN MWH','SUPERFICIE EN KM^2'],
['Buenos Aires','17.569.053',' 16543722',' 305907'],
['Córdoba','3.978.984',' 10606601','164708'],
['Santa Fe','3.556.522',' 13078203',' 133249'],
['Ciudad Autónoma de Buenos Aires','3.120.612','51712507',' 201'],
['Mendoza','2.014.533',' 5652519',' 149069'],
['Tucumán','1.703.186','3208711','22.524'],
['Salta','1.440.672',' 2214796',' 155341'],
['Entre Ríos','1.426.426','3906353','78384'],
['Misiones','1.280.960','2845762',' 29911'],
['Corrientes','1.197.553','2997612',' 89123'],
['Chaco','1.142.963','3045380',' 99763'],
['Santiago del Estero','1.054.028',' 1811277',' 136934'],

['San Juan','818.234',' 2381940',' 88296'],
['Jujuy','797.955',' 1136336',' 53244'],
['Río Negro','762.067',' 1984782','202169'],
['Neuquén','726.590','1834879',' 94422'],
['Formosa','606.041',' 1388311','75488'],
['Chubut','603.120','1646029',' 224302'],
['San Luis','540.905',' 1780881','75347'],
['Catamarca','429.556',' 1337032','101486'],
['La Rioja','384.607','1572290',' 91494'],
['La Pampa','366.022','915781',' 143493'],
['Santa Cruz','333.473',' 1025648',' 244458'],
['Tierra del Fuego, Antártida e Islas del Atlántico Sur','190.641',' s/d ',' 37131']]
poblacionArgentina=np.array(poblacionArgentina1)
print(poblacionArgentina)
[['PROVINCIA' 'CANTIDAD DE HABITANTES' 'CONSUMO EN MWH'
'SUPERFICIE EN KM^2']
['Buenos Aires' '17.569.053' ' 16543722' ' 305907']
['Córdoba' '3.978.984' ' 10606601' '164708']
['Santa Fe' '3.556.522' ' 13078203' ' 133249']
['Ciudad Autónoma de Buenos Aires' '3.120.612' '51712507' ' 201']
['Mendoza' '2.014.533' ' 5652519' ' 149069']
['Tucumán' '1.703.186' '3208711' '22.524']
['Salta' '1.440.672' ' 2214796' ' 155341']
['Entre Ríos' '1.426.426' '3906353' '78384']
['Misiones' '1.280.960' '2845762' ' 29911']
['Corrientes' '1.197.553' '2997612' ' 89123']
['Chaco' '1.142.963' '3045380' ' 99763']
['Santiago del Estero' '1.054.028' ' 1811277' ' 136934']
['San Juan' '818.234' ' 2381940' ' 88296']
['Jujuy' '797.955' ' 1136336' ' 53244']
['Río Negro' '762.067' ' 1984782' '202169']
['Neuquén' '726.590' '1834879' ' 94422']
['Formosa' '606.041' ' 1388311' '75488']
['Chubut' '603.120' '1646029' ' 224302']
['San Luis' '540.905' ' 1780881' '75347']
['Catamarca' '429.556' ' 1337032' '101486']
['La Rioja' '384.607' '1572290' ' 91494']
['La Pampa' '366.022' '915781' ' 143493']
['Santa Cruz' '333.473' ' 1025648' ' 244458']
['Tierra del Fuego, Antártida e Islas del Atlántico Sur' '190.641'
' s/d ' ' 37131']]




num_filas, num_columnas = poblacionArgentina.shape
print("Cantidad de filas:", num_filas)
print("Cantidad de columnas:", num_columnas)

# Obtener el índice de la fila con la mayor cantidad de habitantes
indice_max_habitantes = np.argmax(poblacionArgentina[1:, 1].astype(float)) + 1

# Mostrar la información de la provincia con mayor cantidad de habitantes
print("Provincia con mayor cantidad de habitantes:")
print(poblacionArgentina[indice_max_habitantes])

# Calcular los totales de cada columna
totales = ['Totales']
for columna in range(1, num_columnas):
    total = np.sum(poblacionArgentina[1:, columna].astype(float))
    totales.append(str(total))

poblacionArgentina = np.vstack((poblacionArgentina, totales))

print("Tabla con fila de totales:")
print(poblacionArgentina)

######################### EJERCICIOS PARTE 2: NUMERO 3   ########################################

import matplotlib.pyplot as plt

# Rango de valores para x (dominio)
x = np.linspace(-10, 10, 400)

y1 = 3 * x - 2

y2 = 2 * x + 4 * x**2 + 2

y3 = np.abs(x)

y4 = np.where(x != 0, 1 / x, np.inf)

y5 = x**(-0.5)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Graficar cada función en su respectivo conjunto de ejes
axes[0, 0].plot(x, y1)
axes[0, 0].set_title("y = 3x - 2")

axes[0, 1].plot(x, y2)
axes[0, 1].set_title("y = 2x + 4x^2 + 2")

axes[1, 0].plot(x, y3)
axes[1, 0].set_title("y = |x|")

axes[1, 1].plot(x[x > 0], y4[x > 0])  
axes[1, 1].set_title("y = 1/x")

plt.tight_layout()

plt.show()



