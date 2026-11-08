from enum import Enum


class EstadoSolicitud(Enum):
    PENDIENTE = "Pendiente"
    APROBADA = "Aprobada"
    RECHAZADA = "Rechazada"
    EN_PROCESO = "En Proceso"