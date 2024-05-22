# 5.- Listado de tareas: escribe un programa que permita al usuario agregar, eliminar, y mostrar una lista de tareas pendientes.
def main():
  tareas = []  

  while True:
    print("\nMenú de tareas pendientes:")
    print("1. Mostrar lista")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Ingrese la opción deseada (1-4): ")

    if opcion == "1":
      if not tareas:
        print("La lista de tareas está vacía.")
      else:
        for indice, tarea in enumerate(tareas):
          print(f"{indice + 1}. {tarea}")

    elif opcion == "2":
      nueva_tarea = input("Ingrese la nueva tarea: ")
      tareas.append(nueva_tarea)
      print("Tarea agregada correctamente.")

    elif opcion == "3":
      if not tareas:
        print("La lista de tareas está vacía.")
      else:
        for indice, tarea in enumerate(tareas):
          print(f"{indice + 1}. {tarea}")

        indice_eliminar = int(input("Ingrese el número de la tarea a eliminar: ")) - 1

        if 0 <= indice_eliminar < len(tareas):
          del tareas[indice_eliminar]
          print("Tarea eliminada correctamente.")
        else:
          print("Número de tarea inválido.")

    elif opcion == "4":
      print("Saliendo del programa...")
      break
    else:
      print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
  main()