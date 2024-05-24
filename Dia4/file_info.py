import os
import hashlib
import json

def get_file_checksum(file_path):
    """
    Calcula el hash SHA256 de un archivo.
    
    Parámetros:
    file_path (str): La ruta del archivo.
    
    Retorna:
    str: El hash SHA256 del archivo en formato hexadecimal.
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def collect_files_info(directory):
    """
    Recorre un directorio y recoge información sobre los archivos.
    
    Parámetros:
    directory (str): La ruta del directorio a monitorear.
    
    Retorna:
    dict: Un diccionario con las rutas de los archivos como claves y sus hashes como valores.
    """
    files_info = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            files_info[file_path] = get_file_checksum(file_path)
    return files_info

def save_files_info(directory, output_file):
    """
    Guarda la información de los archivos en un archivo JSON.
    
    Parámetros:
    directory (str): La ruta del directorio a monitorear.
    output_file (str): La ruta del archivo donde se guardará la información.
    """
    files_info = collect_files_info(directory)
    with open(output_file, "w") as json_file:
        json.dump(files_info, json_file, indent=4)
