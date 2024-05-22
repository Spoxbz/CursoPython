# 5.- Listado de tareas: escribe un programa que permita al usuario agregar, eliminar, y mostrar una lista de tareas pendientes.
def main():
    tasks = []  

    while True:
        print("\nMenú de tareas pendientes:")
        print("1. Agregar tarea")
        print("2. Mostrar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")

        option = input("Escoja una opción a realizar (1-4): ")

        if option == "1":
            newTask = input("Ingrese una nueva tarea: ")
            tasks.append(newTask)
            print("La tarea se agregó correctamente.")

        elif option == "2":
            if not tasks:
                print("Su lista de tareas está vacía.")
            else:
                print("Lista total de tareas")
                for index, task in enumerate (tasks):
                    print(f"#{index} -> {task}")

        elif option == "3":
            if not tasks:
                print("Su lista de tareas está vacía.")
            else:
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task}")

                index_to_delete = int(input("Ingrese el número de tarea que quiera eliminar: ")) - 1

                if 0 <= index_to_delete < len(tasks):
                    del tasks[index_to_delete]
                    print("Tarea eliminada.")
                else:
                    print("Número incorrecto o no existe.")

        elif option == "4":
            print("...Cerrando TodoList")
            break
        else:
            print("Opción incorrecta. Intente de nuevo.")

if __name__ == "__main__":
    main()