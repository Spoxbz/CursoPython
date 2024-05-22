"""
Escribir un script que lea el contenido de un archivo llamado colaboradores.txt donde están los siguientes datos:
	DAVID ALMEIDA
	PABLO ARAON
	JUAN VALDIVIEZO
	CARLOS LOJA
	ALAN LEVON
	DANIEL SARZOSA
	PABLO GRANADOS
	ELVIS CRESPO
	JUAN MEJIA
	MARIA PABON
	GUSTAVO SORIA
El programa debe imprimir en pantalla los primeros 5 colaboradores por defecto si no se especifica un número de colaboradores a mostrar, y debe permitir agregar nuevos colaboradores al mismo archivo siempre y cuando no superen los 15.

Organizar el código usando funciones y usando sentencias de control correspondientes.

"""

def leer_colaboradores(archivo, maximo=5):
  """
  Lee el contenido de un archivo y devuelve una lista de colaboradores.

  Args:
    archivo: El nombre del archivo a leer.
    maximo: El número máximo de colaboradores a mostrar (por defecto 5).

  Returns:
    Una lista con los colaboradores del archivo, hasta un máximo de 'maximo'.
  """

  colaboradores = []

  try:
    with open(archivo, "r") as f:
      for linea in f:
        colaborador = linea.strip()
        colaboradores.append(colaborador)
  except FileNotFoundError:
    print(f"Error: El archivo '{archivo}' no se encontró.")
    return []

  # Mostrar solo los 'maximo' primeros colaboradores
  return colaboradores[:maximo]


def mostrar_colaboradores(colaboradores):
  """
  Muestra una lista de colaboradores en pantalla.

  Args:
    colaboradores: La lista de colaboradores a mostrar.
  """

  if not colaboradores:
    print("No hay colaboradores para mostrar.")
    return

  print("Lista de colaboradores:")
  for i, colaborador in enumerate(colaboradores, start=1):
    print(f"{i}. {colaborador}")


def agregar_colaborador(archivo, nombre):
  """
  Agrega un nuevo colaborador al archivo.

  Args:
    archivo: El nombre del archivo a modificar.
    nombre: El nombre del nuevo colaborador.
  """

  try:
    with open(archivo, "a") as f:
      f.write(f"{nombre}\n")
    print(f"Colaborador '{nombre}' agregado correctamente.")
  except Exception as e:
    print(f"Error al agregar el colaborador: {e}")


def main():
  """
  Función principal del programa.
  """

  # Leer colaboradores del archivo
  colaboradores = leer_colaboradores("colaboradores.txt")

  # Mostrar colaboradores
  mostrar_colaboradores(colaboradores)

  # Preguntar si se desea agregar un colaborador
  while True:
    opcion = input("¿Desea agregar un nuevo colaborador? (s/n): ").lower()

    if opcion != "s" and opcion != "n":
      print("Opción no válida. Ingrese 's' o 'n'.")
      continue

    if opcion == "n":
      break

    # Solicitar nombre del nuevo colaborador
    nombre = input("Ingrese el nombre del nuevo colaborador: ")

    # Verificar si se supera el límite de colaboradores
    if len(colaboradores) >= 15:
      print("Error: Se ha alcanzado el límite máximo de 15 colaboradores.")
      continue

    # Agregar colaborador al archivo y a la lista
    agregar_colaborador("colaboradores.txt", nombre)
    colaboradores.append(nombre)

    # Mostrar mensaje de éxito
    print("Colaborador agregado exitosamente.")


if __name__ == "__main__":
  main()
