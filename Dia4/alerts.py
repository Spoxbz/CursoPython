def log_alert(message):
    """
    Registra las alertas en un archivo.
    
    Parámetros:
    message (str): El mensaje de la alerta.
    """
    with open("alerts.log", "a") as log_file:
        log_file.write(f"{message}\n")

def remove_alert(message):
    """
    Elimina una alerta del archivo de registro si el usuario confirma que el cambio es correcto.
    
    Parámetros:
    message (str): El mensaje de la alerta que se va a eliminar.
    """
    try:
        with open("alerts.log", "r") as log_file:
            lines = log_file.readlines()
        with open("alerts.log", "w") as log_file:
            for line in lines:
                if line.strip("\n") != message:
                    log_file.write(line)
    except FileNotFoundError:
        pass

def record_confirmation(message):
    """
    Registra un cambio confirmado por el usuario.
    
    Parámetros:
    message (str): El mensaje del cambio confirmado.
    """
    with open("confirmed_changes.log", "a") as log_file:
        log_file.write(f"{message}\n")

def is_confirmed(message):
    """
    Verifica si un cambio ya ha sido confirmado por el usuario.
    
    Parámetros:
    message (str): El mensaje del cambio a verificar.
    
    Retorna:
    bool: True si el cambio ya ha sido confirmado, False de lo contrario.
    """
    try:
        with open("confirmed_changes.log", "r") as log_file:
            confirmed_changes = log_file.readlines()
        return f"{message}\n" in confirmed_changes
    except FileNotFoundError:
        return False
