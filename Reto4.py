import os, csv
import matplotlib.pyplot  as plt
ruta_archivo= os.getcwd()
ruta_archivotxt= os.path.join(ruta_archivo, "archivotxt.txt")
ruta_archivocsv= os.path.join(ruta_archivo, "Operaciones_Salidas.csv")
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
    texto = ""

    with open(ruta_archivocsv, 'r',) as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Saltar encabezado (si existe)
        
        for fila in lector:
            pesos.append(float(fila[2]))  # Columna 3 (peso)

            hora = fila[8].split(":")[0]  # Hora
            minutos = fila[8].split(":")[1]  # Minutos
            horas.append(float(hora) + float(minutos)/60)  # Convertir a horas decimales
    
    peso_media= sum(pesos) / len(pesos)
    peso_maximo= max(pesos)
    peso_Mínimo= min(pesos)

    hora_media= sum(horas) / len(horas)
    hora_maxima = max(horas)
    hora_minima= min(horas)

    
    texto += "PESO:\n"
    texto += (f"Peso medio: {peso_media:.3f}\nPeso maximo: {peso_maximo}\nPeso minimo: {peso_Mínimo}\n")
    texto += "\nHORA DE SALIDA:\n"
    texto += (f"Hora media: {convertir_hora(hora_media)}\nHora maxima: {convertir_hora(hora_maxima)}\nHora minima: {convertir_hora(hora_minima)}\n")
        
    return texto
def convertir_hora(hora_decimal):
    horas = int(hora_decimal)
    minutos = int(round((hora_decimal - horas) * 60))
    return f"{horas:02}:{minutos:02}"

def mostrar_histograma():
    with open(ruta_archivotxt, "r") as archivo:
        conteo_vocales={"A":0,"E":0,"I":0,"O":0,"U":0}
        for text in archivo:
            for letras in text.split():
                for vocal in letras.upper():
                    try:
                        if vocal in conteo_vocales:
                            conteo_vocales[vocal] += 1 
                    except ValueError:
                        print ("no es vocal")

        plt.title("Histograma")
        plt.xlabel("Vocales")
        plt.ylabel("Frecuencia")
        
        x_pos = range(5) # 5 Vocales
        plt.bar(x_pos, list(conteo_vocales.values()), width=0.7, color="pink", edgecolor="purple")
        # centrar las x
        plt.xticks(x_pos, list(conteo_vocales.keys()))  
        plt.show()
def graficar():
    with open(ruta_archivocsv, 'r',) as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Saltar encabezado (si existe)
        datos = {}    # mapas 
        conteo = {}

        for fila in lector:
            aerolinea = fila[4]  # Columna 5 (aerolinea)
            peso = float(fila[2])  # Columna 3 (peso)

            if aerolinea in datos:          
                datos[aerolinea] += peso    # si aerolinea está en datos, sumamos el peso
                conteo[aerolinea] += 1      # conteo de aerolineas
            else:
                datos[aerolinea] = peso
                conteo[aerolinea] = 1

        for aerolinea in datos:
            datos[aerolinea] = float(datos[aerolinea]/ conteo[aerolinea])  # (Calcular el promedio)

        # Obtener las 50 aerolíneas más frecuentes
        top_50_aerolineas = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:50]  #info de ia para ordenar de mayor a menor la frecuencia de aerolineas
        datos_filtrados = {}
        for x in top_50_aerolineas:                     #tomar las 50 primeros datos 
            datos_filtrados[x[0]] = datos[x[0]]
        
        fig, ax = plt.subplots(figsize=(len(datos_filtrados) * 0.2, 6))            
        ax.scatter(list(datos_filtrados.keys()), list(datos_filtrados.values()), color="purple", edgecolors="black")
        ax.set_title("Peso promedio por Aerolínea (Top 50 más frecuentes)")
        ax.set_xlabel("Aerolínea")
        ax.set_ylabel("Peso Promedio")
        plt.xticks(rotation=90)
        plt.tight_layout(pad=2.0)
        plt.show()

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
                contenido= cambiar_palabra(palabra_vieja.strip(), palabra_nueva.strip())   # strip, para quitar los espacios
                print("listo") 
            elif menut == 3: 
                mostrar_histograma()
            else:
                break
        elif menu == 3:
            menuc= int(input(f"digite el número asignado: \n1.\tMostrar las 15 primeras filas \n2.\tCalcular estadísticas \n3.\tGraficar una columna completa con los datos \n"))
            if menuc == 1:
                print (f"documento: {mostrar_lineas(15)}")
            elif menuc == 2:
                print(calcular_estadisticas())
            elif menuc == 3:
                graficar()   
        else:
            break 
if __name__== "__main__":
    main()