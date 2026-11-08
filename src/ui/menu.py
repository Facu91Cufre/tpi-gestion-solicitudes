from src.domain.Estudiante import Estudiante
from src.domain.Responsable import Responsable


def iniciar_menu(service):
    print("--- GESTIÓN DE SOLICITUDES ACADÉMICAS ---")
    print("1. Registrar nueva solicitud")
    print("2. Cambiar estado de solicitud")
    print("3. Asignar responsable a solicitud")
    print("4. Buscar / filtrar solicitudes")
    print("5. Listar reporte básico")
    print("6. Salir")
    
    while True:
        opcion = input("Elija una opcion (6 para salir): ").strip()

        if opcion == "1":
            print("Registrar Solicitud")
            try:
                legajo = input("Ingrese el legajo del estudiante: ")
                nombre = input("Ingrese el nombre del estudiante: ")
                tipo = input("Ingrese el tipo de solicitud (Ej: Certificado, Constancia): ")
                descripcion = input("Ingrese la descripción de la solicitud: ")

                estudiante = Estudiante(legajo, nombre)
                nuevo_id = len(service.obtener_solicitudes()) + 1
                service.registrar_solicitud(nuevo_id, estudiante, tipo, descripcion)

                print(f"Solicitud {nuevo_id} creada con éxito!")
            except ValueError as e:
                print(f"Error al registrar la solicitud: {e}")

        elif opcion == "2":
            print("Cambiar estado de solicitud")
            try:
                id_solicitud = int(input("Ingrese el ID de la solicitud: "))
                print("Estados válidos: PENDIENTE, EN_PROCESO, APROBADO, RECHAZADO")
                nuevo_estado = input("Ingrese el nuevo estado (Pendiente, En Proceso, Aprobada, Rechazada): ").strip()
                service.actualizar_estado_solicitud(id_solicitud, nuevo_estado)
                print("Estado actualizado con éxito.")
            except ValueError as e:
                print(f"Error al actualizar el estado: {e}")

        elif opcion == "3":
            print("Asignar responsable a solicitud")
            try:
                id_solicitud = int(input("Ingrese el ID de la solicitud a asignar: "))
                id_responsable = input("Ingrese el ID del responsable: ")
                nombre_responsable = input("Ingrese el nombre del área: ")
                responsable = Responsable(id_responsable, nombre_responsable)
                service.asignar_responsable_a_solicitud(id_solicitud, responsable)
                print("Responsable asignado con éxito.")
            except ValueError as e:
                print(f"Error al asignar responsable: {e}")

        elif opcion == "4":
            print("Buscar / filtrar solicitudes")
            try:
                id_solicitud = int(input("Ingrese el ID de la solicitud a buscar: "))
                solicitud = service.buscar_solicitud_por_id(id_solicitud)
                if solicitud:
                    print(f"Solicitud encontrada: ID: {solicitud.id_solicitud}, Estudiante: {solicitud.estudiante.nombre}, Tipo: {solicitud.tipo}, Estado: {solicitud.estado}")
                else:
                    print("Solicitud no encontrada.")
            except ValueError:
                print("Error: El ID debe ser un número.")

        elif opcion == "5":
            print("Listado de solicitudes")
            solicitudes = service.obtener_solicitudes()
            if not solicitudes:
                print("No hay solicitudes registradas.")
            else:
                for s in solicitudes:
                    print(f"ID: {s.id_solicitud}, Estudiante: {s.estudiante.nombre}, Tipo: {s.tipo}, Estado: {s.estado}")

        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
