
import openpyxl


"""
La función LeeFichero
"""
def LeeFichero(nom_fich, nom_hoja):

    documento = openpyxl.load_workbook(nom_fich)  # Abrimos el excel
    hoja = documento[nom_hoja]  # En hoja cargamos la hoja de Excel (sabemos el nombre de la hoja)

    lista = []

    for row in hoja.values:
        lista.append(row)  # Obtenemos una lista en la que cada elelmento es la fila (tupla)

    lista.pop(0)  # Eliminamos el primer elemento que es la cabecera
    documento.close()
    return lista





print (LeeFichero("Países-y-Capitales-del-Mundo.xlsx", "Hoja1"))
