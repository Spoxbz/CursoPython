# importando funciones de los modulos
from file_info import save_files_info
from monitor import monitor_files

# Directorio a monitorear y archivos de configuración
directory_to_monitor = "C:/Users/Msi Bravo/Desktop/Cursopython/CursoPython/Dia4/RutaMonitorear"
info_file = "files_info.json"
monitor_interval = 10 # Intervalo de monitoreo en segundos, ajustado a 10 segundos

# Guardar la información inicial de los archivos
save_files_info(directory_to_monitor, info_file)

# Iniciar el monitoreo de archivos
monitor_files(directory_to_monitor, info_file, monitor_interval)
