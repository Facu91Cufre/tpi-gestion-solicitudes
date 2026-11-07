from gestion_solicitudes.modelos import Estudiante, Responsable, Solicitud


def main():
    solicitudes = []

    print("--- Sistema de Gestión de Solicitudes Académicas ---")

    while True:
        print("--- GESTIÓN DE SOLICITUDES ACADÉMICAS ---")
        print("1. Registrar nueva solicitud")
        print("2. Cambiar estado de solicitud")
        print("3. Asignar responsable a solicitud")
        print("4. Buscar / filtrar solicitudes")
        print("5. Listar reporte básico")
        print("6. Salir")

        opcion = input("Elija una opcion (6 para salir): ").strip()

        if opcion == "1":
            legajo = input("Ingrese el legajo del estudiante: ")
            nombre = input("Ingrese el nombre del estudiante: ")
            tipo = input("Ingrese el tipo de solicitud (Ej: Certificado, Constancia): ")
            descripcion = input("Ingrese la descripción de la solicitud: ")

            estudiante = Estudiante(legajo, nombre)
            nuevo_id = len(solicitudes) + 1
            solicitud = Solicitud(nuevo_id, estudiante, tipo, descripcion)
            solicitudes.append(solicitud)

            print(f"Solicitud {nuevo_id} creada con éxito!")

        elif opcion == "2":
            try:
                id_solicitud = int(input("Ingrese el ID de la solicitud a cambiar de estado: "))
                solicitud = next((s for s in solicitudes if s.id_solicitud == id_solicitud), None)
                if solicitud:
                    print("Estados disponibles: Pendiente, En Proceso, Aprobada, Rechazada")
                    nuevo_estado = input("Ingrese el nuevo estado de la solicitud: ")
                    solicitud.cambiar_estado(nuevo_estado)
                    print(f"Estado de la solicitud {id_solicitud} actualizado a: {nuevo_estado}")
                else:
                    print("Solicitud no encontrada.")
            except ValueError:
                print("Error: El ID debe ser un número.")

        elif opcion == "3":
            try:
                id_solicitud = int(input("Ingrese el ID de la solicitud a asignar: "))
                solicitud = next((s for s in solicitudes if s.id_solicitud == id_solicitud), None)
                if solicitud:
                    id_responsable = input("Ingrese el ID del responsable: ")
                    nombre_area = input("Ingrese el nombre del área del responsable: ")
                    responsable = Responsable(id_responsable, nombre_area)
                    solicitud.asignar_responsable(responsable)
                    print(f"Responsable {id_responsable} asignado a la solicitud {id_solicitud}.")
                else:
                    print("Solicitud no encontrada.")
            except ValueError:
                print("Error: El ID debe ser un número.")

        elif opcion == "4":
            criterio = input("Ingrese estado o tipo a filtrar: ").lower()
            filtradas = [s for s in solicitudes if criterio in s.estado.lower() or criterio in s.tipo.lower()]
            if not filtradas:
                print("No se encontraron solicitudes con ese criterio.")
            else:
                print(f"--- RESULTADOS DE BUSQUEDA: {len(filtradas)} ---")
                for s in filtradas:
                    print(f"ID: {s.id_solicitud}, \ntipo: {s.tipo} \nestado: {s.estado} \nEstudiante: {s.estudiante.nombre} (Legajo: {s.estudiante.legajo})")

        elif opcion == "5":
            total = len(solicitudes)
            pendientes = sum(1 for s in solicitudes if s.estado == "Pendiente")
            resuelta = sum(1 for s in solicitudes if s.estado in ["Aprobada", "Rechazada"])
            print("--- REPORTE BÁSICO ---")
            print(f"Total de solicitudes: {total}")
            print(f"Solicitudes pendientes: {pendientes}")
            print(f"Solicitudes resueltas: {resuelta}")

        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break        

if __name__ == "__main__":
    main()