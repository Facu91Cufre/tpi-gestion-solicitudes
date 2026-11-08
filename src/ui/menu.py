from src.domain.DatosSolicitud import DatosSolicitud
from src.domain.Responsable import Responsable


def mostrar_menu():
    print("--- GESTIÓN DE SOLICITUDES ACADÉMICAS ---")
    print("1. Registrar nueva solicitud")
    print("2. Cambiar estado de solicitud")
    print("3. Asignar responsable a solicitud")
    print("4. Buscar / filtrar solicitudes")
    print("5. Listar reporte básico")
    print("6. Salir")


def iniciar_menu(service):

    while True:
        mostrar_menu()
        opcion = input("Elija una opcion (6 para salir): ").strip()

        if opcion == "1":
            registrar_solicitud(service)
        elif opcion == "2":
            cambiar_estado(service)
        elif opcion == "3":
            asignar_responsable(service)
        elif opcion == "4":
            buscar_solicitud(service)
        elif opcion == "5":
            listar_solicitudes(service)
        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break


def pedir_id(mensaje: str) -> int:
    try:
        return int(input(mensaje))
    except ValueError:
        raise ValueError("El ID debe ser un número entero.")

def formatear_solicitud(s) -> str:
    return f"ID: {s.id_solicitud}, Estudiante: {s.estudiante.nombre}, Tipo: {s.tipo}, Estado: {s.estado}"


def registrar_solicitud(service):
    print("Registrar Solicitud")
    try:
        legajo = int(input("Ingrese el legajo del estudiante: "))
        nombre = input("Ingrese el nombre del estudiante: ")
        tipo = input("Ingrese el tipo de solicitud (Ej: Certificado, Constancia): ")
        descripcion = input("Ingrese la descripción de la solicitud: ")
        datos = DatosSolicitud(legajo, nombre, tipo, descripcion)
        nuevo_id = service.registrar_solicitud(datos)

        print(f"Solicitud {nuevo_id} creada con éxito!")
    except ValueError as e:
        print(f"Error al registrar la solicitud: {e}")

def cambiar_estado(service):
    print("Cambiar estado de solicitud")
    try:
        id_solicitud = pedir_id("Ingrese el ID de la solicitud: ")
        service.buscar_solicitud_por_id(id_solicitud)
        print("Estados válidos: PENDIENTE, EN_PROCESO, APROBADA, RECHAZADA")
        nuevo_estado = input("Ingrese el nuevo estado (Pendiente, En Proceso, Aprobada, Rechazada): ").strip()
        service.actualizar_estado_solicitud(id_solicitud, nuevo_estado)
        print("Estado actualizado con éxito.")
    except ValueError as e:
        print(f"Error al actualizar el estado: {e}")

def asignar_responsable(service):
    print("Asignar responsable a solicitud")
    try:
        id_solicitud = pedir_id("Ingrese el ID de la solicitud a asignar: ")
        id_responsable = input("Ingrese el ID del responsable: ")
        nombre_area = input("Ingrese el nombre del área: ")
        service.asignar_responsable_a_solicitud(id_solicitud, Responsable(id_responsable, nombre_area))
        print("Responsable asignado con éxito.")
    except ValueError as e:
        print(f"Error al asignar responsable: {e}")

def buscar_solicitud(service):
    print("Buscar / filtrar solicitudes")
    try:
        id_solicitud = pedir_id("Ingrese el ID de la solicitud a buscar: ")
        solicitud = service.buscar_solicitud_por_id(id_solicitud)
        print(f"Solicitud encontrada: {formatear_solicitud(solicitud)}")
    except ValueError as e:
        print(f"Solicitud no encontrada o ID inválido: {e}")

def listar_solicitudes(service):
    print("Listado de solicitudes")
    solicitudes = service.obtener_solicitudes()
    if not solicitudes:
        print("No hay solicitudes registradas.")
        return
    for s in solicitudes:
        print(formatear_solicitud(s))
