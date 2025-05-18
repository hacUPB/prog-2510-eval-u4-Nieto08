import os, csv
import matplotlib as plt
import numpy as np 
ruta_archivo="\\Directorios\\prog-2510-eval-u4-Nieto08"
ruta_archivotxt="\\Directorios\\prog-2510-eval-u4-Nieto08\\archivotxt.txt"
ruta_archivocsv= "\\Directorios\\prog-2510-eval-u4-Nieto08\\Operaciones_Salidas.csv"
def contar_palabra():
    with open(ruta_archivotxt, "r") as archivo:
        contenido= archivo.read().split()
    return len(contenido)
def contar_caracteres():
    with open(ruta_archivotxt, "r") as archivo:
        cont= []
        contenido= archivo.read()
        for i in contenido:
            caracteres= i.split()
            cont+= caracteres
    return len(cont)
def cambiar_palabra(palabra_vieja, palabra_nueva):
    with open(ruta_archivotxt, "r") as archivo:
        contenido= archivo.readlines()
        variable= ""
        for linea in contenido:
            contenido_separado = linea.split()
            for palabra in range(len(contenido_separado)):
                if contenido_separado[palabra] == palabra_vieja:
                    contenido_separado[palabra] = palabra_nueva
            contenido_modificado = " ".join(contenido_separado)
            variable+= contenido_modificado+"\n" 
        with open(ruta_archivotxt, 'w',) as archivo:
            archivo.write(variable)
    return  
def mostrar_lineas(n_filas):
    mostrar_lineas= ""
    with open(ruta_archivocsv, "r") as archivo:
        lector= archivo.readlines()
        for i in range(n_filas):
            mostrar_lineas += lector[i]
    return mostrar_lineas

def calcular_estadisticas():
    pesos = []
    horas = []
    
    try:
        with open(ruta_archivocsv, 'r',) as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Saltar encabezado (si existe)
            
            for fila in lector:
                try:
                    pesos.append(float(fila[2]))  # Columna 3 (peso)
                    horas.append(float(fila[8]))  # Columna 9 (hora)
                except (ValueError, IndexError):
                    continue  # Ignorar filas con datos inválidos
        
        if not pesos or not horas:
            return "No hay datos válidos en las columnas especificadas."
        
        peso_media= sum(pesos) / len(pesos)
        peso_maximo= max(pesos)
        peso_Mínimo= min(pesos)

        hora_Media= sum(horas) / len(horas)
        hora_Máximo = max(horas)
        hora_Mínimo= min(horas)
        texto= (f"{peso_media}{peso_maximo}{peso_Mínimo}{hora_Media}{hora_Máximo}{hora_Mínimo}")
            
        
        return texto
    
    except FileNotFoundError:
        return "Error: Archivo no encontrado."
    except Exception as e:
        return f"Error inesperado: {str(e)}"

def main():
    print ("*"*50)
    menu= int(input(f"digite el número asignado: \n1.\tlistar todos los archivos disponibles \n2.\tprocesar archivo de texto(txt) \n3.\tprocesar archivo separado por comas(csv) \n4.\tSalir \n" ))
    print ("*"*50)
    while menu in range(4):
        if menu == 1:
            print ("*"*50)
            contenido = os.listdir(ruta_archivo)                         #info de ia 
            print (contenido)
            print ("*"*50)
            menu= int(input(f"digite el número asignado: \n1.\tlistar todos los archivos disponibles \n2.\tprocesar archivo de texto(txt) \n3.\tprocesar archivo separado por comas(csv) \n4.\tSalir \n" ))
        elif menu == 2:
            menut= int(input("opciones: \n1.\tContar números de palabras y caracteres\n2.\tReemplazar una palabra por otra\n3.\tHistograma de ocurrencia de las vocales\n"))
            if menut == 1:
                    print(f"palabras: {contar_palabra()} caracteres: {contar_caracteres()}")
            elif menut == 2:
                palabra_vieja= input("¿que palabra deseas reemplazar?: ")
                palabra_nueva= input("¿por cual palabra deseas cambiarla?: ")
                contenido= cambiar_palabra(palabra_vieja, palabra_nueva)
                print("listo") 
            elif menut == 3: 
                with open(ruta_archivotxt, "r") as archivo:
                   plt.hist(archivo, bins=30, edgecolor= "green")  #crea el histograma
                   plt.title("histograma")
                   plt.xlabel("valores")
                   plt.ylabel("frecuencia")
                   plt.show()
            else:
                break
        elif menu == 3:
            menuc= int(input(f"digite el número asignado: \n1.\tMostrar las 15 primeras filas \n2.\tCalcular estadísticas \n3.\tGraficar una columna completa con los datos \n"))
            if menuc == 1:
                print (f"documento: {mostrar_lineas(15)}")
            elif menuc == 2:
                print(calcular_estadisticas())
            elif menuc == 3:
                pass
        else:
            break 
if __name__== "__main__":
    main()