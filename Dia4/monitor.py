import time
import json
from file_info import collect_files_info
from alerts import log_alert, remove_alert, record_confirmation, is_confirmed

def ask_user_confirmation(message):
    """
    Pregunta al usuario si una acción es correcta.
    
    Parámetros:
    message (str): El mensaje que describe la acción.
    
    Retorna:
    bool: True si el usuario confirma la acción, False de lo contrario.
    """
    while True:
        response = input(f"{message} ¿Es correcta esta acción? (s/n): ").strip().lower()
        if response in ["s", "n"]:
            return response == "s"
        else:
            print("Respuesta no válida. Por favor ingrese 's' o 'n'.")

def monitor_files(directory, info_file, interval):
    """
    Monitorea los archivos en el directorio cada 'interval' segundos.
    
    Parámetros:
    directory (str): La ruta del directorio a monitorear.
    info_file (str): La ruta del archivo JSON con la información inicial de los archivos.
    interval (int): El intervalo de tiempo entre cada monitoreo en segundos.
    """
    with open(info_file, "r") as json_file:
        original_files_info = json.load(json_file)

    while True:
        current_files_info = collect_files_info(directory)
        for file_path, original_checksum in original_files_info.items():
            current_checksum = current_files_info.get(file_path)
            if current_checksum is None:
                message = f"Archivo eliminado: {file_path}"
                if not is_confirmed(message):
                    if ask_user_confirmation(message):
                        record_confirmation(message)
                    else:
                        log_alert(message)
            elif current_checksum != original_checksum:
                message = f"Archivo modificado: {file_path}"
                if not is_confirmed(message):
                    if ask_user_confirmation(message):
                        record_confirmation(message)
                    else:
                        log_alert(message)
        
        for file_path in current_files_info:
            if file_path not in original_files_info:
                message = f"Archivo agregado: {file_path}"
                if not is_confirmed(message):
                    if ask_user_confirmation(message):
                        record_confirmation(message)
                    else:
                        log_alert(message)

        time.sleep(interval)
