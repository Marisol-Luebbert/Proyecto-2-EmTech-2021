# -*- coding: utf-8 -*-
"""
@author: Marisol 
"""
#Importamos librerías
import csv
import matplotlib.pyplot as plt
import numpy 

#Vamos a crear la lista de datos generales y la lista de datos por año de la empresa
datos = []
year_2015 = []
year_2016 = []
year_2017 = []
year_2018 = []
year_2019 = []
year_2020 = []

#Vamos a abrir el archivo de datos de la empresa
with open("synergy_logistics_database.csv", "r") as database:
  #Lo abrimos en forma de diccionario
    leyendo = csv.DictReader(database)

    for registro in leyendo:
      #Vamos a hacer una lista de todos los datos de la base de datos
      datos.append(registro)

      #Vamos a llenar cada lista con los registros de acuerdo al año
      if registro["year"] == "2015":
        year_2015.append(registro)
      
      elif registro["year"] == "2016":
        year_2016.append(registro)
      
      elif registro["year"] == "2017":
        year_2017.append(registro)
      
      elif registro["year"] == "2018":
        year_2018.append(registro)

      elif registro["year"] == "2019":
        year_2019.append(registro)

      else:
        year_2020.append(registro)

#Vamos a verificar las ganancias totales de la empresa 
def totales (lista):
  contador = 0
  #Cada lista será por año
  for elemento in lista:
    #Se suman las ganancias
    contador += int(elemento['total_value'])
  return contador

total_2015 = totales(year_2015)
total_2016 = totales(year_2016)
total_2017 = totales(year_2017)
total_2018 = totales(year_2018)
total_2019 = totales(year_2019)
total_2020 = totales(year_2020)

ganar = "GANANCIAS GENERADAS AL AÑO"
print(ganar.center(50,"="))
print("En el 2015: ", total_2015, "\nEn el 2016: ", total_2016, "\nEn el 2017: ", total_2017, "\nEn el 2018: ", total_2018, "\nEn el 2019: ",total_2019, "\nEn el 2020: ", total_2020)

#Vamos a hacerlo más visual
eje_x = [2015,2016,2017,2018,2019,2020]
eje_y = [total_2015,total_2016,total_2017,total_2018,total_2019,total_2020]
#Generamos la gráfica de barras
plt.bar(eje_x, eje_y, color = "green")
#Titulo en el eje y
plt.ylabel('Ganancias generadas')
#Titulo en el eje x
plt.xlabel('Año')
# Título de Gráfica
plt.title('Ganancias generadas por año')
# Mostramos Gráfica
plt.show()

#OPCIÓN 1

#Vamos a definir la función de importaciones y exportaciones, de donde obtenemos el total de procesos y dinero que implican cada uno
#Requerimos de una lista de datos y una dirección, es decir, Exports o Imports
def rutas_exp_imp(lista, direccion):
    #El contador de importaciones/exportaciones
    contador = 0
    #El contador de dinero por viaje
    dinero = 0
    #Listas para colocar los datos revisados
    rutas_contadas = []
    rutas_conteo = []

    for ruta in lista:
      #Verificamos que estemos viendo Exportaciones o importaciones en cada elemento de la lista
        if ruta["direction"] == direccion:
          #Anotamos el origen y el destino de la ruta
            ruta_proceso = [ruta["origin"], ruta["destination"]]

            #Si la ruta con la que estamos trabajando no está en la lista de las contadas, empezamos a contarla
            if ruta_proceso not in rutas_contadas:
                #Ahora, vamos a comparar la lista completa con la ruta que estamos analizando
                for ruta_comparar in lista:
                  #Se hace la comparación
                    if ruta_proceso == [ruta_comparar["origin"], ruta_comparar["destination"]]:
                      #Si son iguales, se cuentan el número de exportaciones/importaciones con esa ruta
                        contador += 1
                        #Se hace una suma del dinero generado por la ruta
                        dinero += int(ruta_comparar["total_value"])

                #La ruta ya cuenta, entonces la agregamos en las contadas
                rutas_contadas.append(ruta_proceso)
                #Agregamos los datos a una lista, donde también viene el contador y el dinero generado
                rutas_conteo.append([ruta["origin"], ruta["destination"], dinero, contador])
                #Las variables regresan a cero para empezar con la siguiente ruta
                contador = 0
                dinero = 0
    #Nos vamos a fijar en las ganancias por ruta
    rutas_conteo.sort(reverse = True, key = lambda x:x[2])
    return rutas_conteo

#Si hacemos la cuenta de exportaciones e importaciones por cada uno de los años
conteo_exp_2015 = rutas_exp_imp(year_2015,"Exports")
conteo_imp_2015 = rutas_exp_imp(year_2015,"Imports")
conteo_exp_2016 = rutas_exp_imp(year_2016,"Exports")
conteo_imp_2016 = rutas_exp_imp(year_2016,"Imports")
conteo_exp_2017 = rutas_exp_imp(year_2017,"Exports")
conteo_imp_2017 = rutas_exp_imp(year_2017,"Imports")
conteo_exp_2018 = rutas_exp_imp(year_2018,"Exports")
conteo_imp_2018 = rutas_exp_imp(year_2018,"Imports")
conteo_exp_2019 = rutas_exp_imp(year_2019,"Exports")
conteo_imp_2019 = rutas_exp_imp(year_2019,"Imports")
conteo_exp_2020 = rutas_exp_imp(year_2020,"Exports")
conteo_imp_2020 = rutas_exp_imp(year_2020,"Imports")

#Un ejemplo de las importaciones en cierto año 
#titulo = "IMPORTACIONES 2020"
#print(titulo.center(50,"="))
#print(["Origen","Destino","Ingresos de ruta","Conteo total"])
#print(*conteo_imp_2020[0:10], sep="\n")

#Tomando la OPCIÓN 3 como idea
#Vamos a obtener el porcentaje que representa cada una de las rutas para la ganancia total del año
def porcentajes_rutas (lista):
  suma_total = 0
  paises = []
  for elemento in lista:
    #Hacemos la suma total del año
    suma_total += elemento[2]
  
  porcentaje_ruta = 0
  suma_rutas = 0
  rutas_contadas = []
  paises_contados = []

  for ruta in lista:
    #Obtenemos el porcentaje que representa del total
    porcentaje_ruta = round((ruta[2]/suma_total)*100,2)
    #Generamos la lista de los elementos considerando el porcentaje 
    rutas_contadas.append([ruta[0],ruta[1],ruta[2], ruta[3], porcentaje_ruta])
    porcentaje_ruta = 0

  return suma_total, rutas_contadas

total_imp_2015, rutas_imp_porciento_2015 = porcentajes_rutas(conteo_imp_2015)
total_exp_2015, rutas_exp_porciento_2015 = porcentajes_rutas(conteo_exp_2015)

total_imp_2016, rutas_imp_porciento_2016 = porcentajes_rutas(conteo_imp_2016)
total_exp_2016, rutas_exp_porciento_2016 = porcentajes_rutas(conteo_exp_2016)

total_imp_2017, rutas_imp_porciento_2017 = porcentajes_rutas(conteo_imp_2017)
total_exp_2017, rutas_exp_porciento_2017 = porcentajes_rutas(conteo_exp_2017)

total_imp_2018, rutas_imp_porciento_2018 = porcentajes_rutas(conteo_imp_2018)
total_exp_2018, rutas_exp_porciento_2018 = porcentajes_rutas(conteo_exp_2018)

total_imp_2019, rutas_imp_porciento_2019 = porcentajes_rutas(conteo_imp_2019)
total_exp_2019, rutas_exp_porciento_2019 = porcentajes_rutas(conteo_exp_2019)

total_imp_2020, rutas_imp_porciento_2020 = porcentajes_rutas(conteo_imp_2020)
total_exp_2020, rutas_exp_porciento_2020 = porcentajes_rutas(conteo_exp_2020)

#Tomamos como ejemplo el 2020
oye = "GANANCIAS GENERADAS EN EL 2020 DE IMPORTACIONES"
print(oye.center(50,"="))
print("El total de ganancias obtenidas en el 2020 fue de: ",total_imp_2020)
oye2 = "Rutas acomodadas de acuerdo a la ganancia"
print(oye2.center(50,"="))
print(["Origen","Destino","Ingresos de ruta","Conteo total","% del total"])
print(*rutas_imp_porciento_2020, sep ="\n") 

#OPCIÓN 2
#Vamos a definir la función para obtener el uso de los diferentes medios de transporte.
def transporte (lista):
  #Vamos a crear una lista de los tipos de transporte con la cantidad de veces que se usó
  transportes = []
  #Vimos que las posibilidades son Mar, aire, riel y carretera
  posibles_transportes = ["Sea", "Air", "Rail", "Road"]
  #El contador
  contador = 0

  for transporte_yes in posibles_transportes:
    for ruta in lista:
      #Vamos a comparar las listas para identificar los transportes
      if ruta["transport_mode"] == transporte_yes:
        contador += 1
    #Creamos la lista de los transportes
    transportes.append([transporte_yes,contador])
    contador = 0

  return transportes

transportes_top_2015 = transporte(year_2015)
transportes_top_2016 = transporte(year_2016)
transportes_top_2017 = transporte(year_2017)
transportes_top_2018 = transporte(year_2018)
transportes_top_2019 = transporte(year_2019)
transportes_top_2020 = transporte(year_2020)

#Vamos a hacer una gráfica comparativa de los medios de transporte por año
labels = ['Sea', 'Air', 'Rail', 'Road']
t_2015 = []
t_2016 = []
t_2017 = []
t_2018 = []
t_2019 = []
t_2020 = []
for transportation in transportes_top_2015:
  t_2015.append(transportation[1])
for transportation in transportes_top_2016:
  t_2016.append(transportation[1])
for transportation in transportes_top_2017:
  t_2017.append(transportation[1])
for transportation in transportes_top_2018:
  t_2018.append(transportation[1])
for transportation in transportes_top_2019:
  t_2019.append(transportation[1])
for transportation in transportes_top_2020:
  t_2020.append(transportation[1])

x = numpy.arange(len(labels))  # the label locations
width = 0.1  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - 5*width/2, t_2015, width, label='2015')
rects2 = ax.bar(x - 3*width/2, t_2016, width, label='2016')
rects3 = ax.bar(x - width/2, t_2017, width, label='2017')
rects4 = ax.bar(x + width/2, t_2018, width, label='2018')
rects5 = ax.bar(x + 3*width/2, t_2019, width, label='2019')
rects6 = ax.bar(x + 5*width/2, t_2020, width, label='2020')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Conteo de rutas')
ax.set_title('Medios de transporte por año')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()

#OPCIÓN 3
#Vamos  a crear una función para obtener el %, pero por país de origen
def porcentaje_pais(lista_porciento):
  #Definamos una lista donde vamos a considerar solo a los paises origen
  contados = []
  lista_paises = []
  contador = 0
  contador_2 = 0
  for pais in lista_porciento:
    actual = pais[0]

    if actual in contados:
      continue

    for elemento in lista_porciento: 
      if actual == elemento[0]:
        contador += elemento[4]
        contador_2 += elemento[3]

    contados.append(actual)
    lista_paises.append([actual,contador,contador_2])
    contador = 0
    contador_2 = 0
  lista_paises.sort(reverse = True, key = lambda x : x[1])
  return lista_paises

#Ganancias de los paises por exportaciones e importaciones
pais_imp_2015 = porcentaje_pais(rutas_imp_porciento_2015)
pais_exp_2015 = porcentaje_pais(rutas_exp_porciento_2015)
pais_imp_2016 = porcentaje_pais(rutas_imp_porciento_2016)
pais_exp_2016 = porcentaje_pais(rutas_exp_porciento_2016)
pais_imp_2017 = porcentaje_pais(rutas_imp_porciento_2017)
pais_exp_2017 = porcentaje_pais(rutas_exp_porciento_2017)
pais_imp_2018 = porcentaje_pais(rutas_imp_porciento_2018)
pais_exp_2018 = porcentaje_pais(rutas_exp_porciento_2018)
pais_imp_2019 = porcentaje_pais(rutas_imp_porciento_2019)
pais_exp_2019 = porcentaje_pais(rutas_exp_porciento_2019)
pais_imp_2020 = porcentaje_pais(rutas_imp_porciento_2020)
pais_exp_2020 = porcentaje_pais(rutas_exp_porciento_2020)

#Tomamos como ejemplo las importaciones de 2020
print("GANANCIAS POR PAIS DE IMPORTACIONES 2020")
print(["País origen","% del año","Conteo"])
print(*pais_imp_2020, sep = "\n")

#OPCIÓN 3 GENERAL
#Vamos  a crear una función para obtener el %, pero por país de origen
def porcentaje_general(lista):
  #Definamos una lista donde vamos a considerar solo a los paises origen
  contados = []
  lista_paises = []
  contador = 0
  contador_2 = 0
  total = 0
  #Vamos a obtener la suma total del año analizado
  for coso in lista:
    total += int(coso["total_value"])
  for pais in lista:
    actual = pais["origin"]

    if actual in contados:
      continue

    for elemento in lista: 
      #Verificamos cuantas veces el país se encuentra como origen
      if actual == elemento["origin"]:
        #Vamos a sumar las ganancias por pais
        contador += int(elemento["total_value"])
        contador_2 += 1
    #Acomodamos los países ya analizados para evitar errores
    contados.append(actual)
    #Agregamos los elementos de cada país a la lista
    lista_paises.append([actual,round((contador/total)*100,2),contador_2])
    contador = 0
    contador_2 = 0
  lista_paises.sort(reverse = True, key = lambda x : x[1])
  return lista_paises

lista_general_2015 = porcentaje_general(year_2015)
print("PAISES CON GANANCIAS GENERALES 2015")
print(["País origen","% del total","# de convenios"])
print(*lista_general_2015, sep = "\n")

lista_general_2016 = porcentaje_general(year_2016)
print("PAISES CON GANANCIAS GENERALES 2016")
print(["País origen","% del total","# de convenios"])
print(*lista_general_2016, sep = "\n")

lista_general_2017 = porcentaje_general(year_2017)
print("PAISES CON GANANCIAS GENERALES 2017")
print(["País origen","% del total","# de convenios"])
print(*lista_general_2017, sep = "\n")

lista_general_2018 = porcentaje_general(year_2018)
print("PAISES CON GANANCIAS GENERALES 2018")
print(["País origen","% del total","# de convenios"])
print(*lista_general_2018, sep = "\n")

lista_general_2019 = porcentaje_general(year_2019)
print("PAISES CON GANANCIAS GENERALES 2019")
print(["País origen","% del total","# de convenios"])
print(*lista_general_2019, sep = "\n")

lista_general_2020 = porcentaje_general(year_2020)
print("PAISES CON GANANCIAS GENERALES 2020")
print(["País origen","% del total","# de convenios"])
print(*lista_general_2020, sep = "\n")