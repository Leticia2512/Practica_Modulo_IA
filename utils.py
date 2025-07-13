# funciones.py

import os
import fitz 

def convert_pdfs_a_txt(carpeta_pdf="data"):
    """
    Convierte automáticamente todos los archivos PDF en una carpeta a archivos de texto (.txt).

    Parámetros:
    ----------
    carpeta_pdf : str
        Ruta de la carpeta que contiene los archivos PDF. Por defecto es 'data'.

    Salida:
    -------
    Archivos .txt guardados en la misma carpeta, uno por cada PDF procesado.
    """
    for archivo in os.listdir(carpeta_pdf):
        if archivo.endswith(".pdf"):
            ruta_pdf = os.path.join(carpeta_pdf, archivo)
            nombre_txt = os.path.splitext(archivo)[0] + ".txt"
            ruta_txt = os.path.join(carpeta_pdf, nombre_txt)

            with fitz.open(ruta_pdf) as doc:
                texto = ""
                for pagina in doc:
                    texto += pagina.get_text()

            with open(ruta_txt, "w", encoding="utf-8") as f:
                f.write(texto)

            print(f"Convertido: {archivo} → {nombre_txt}")
