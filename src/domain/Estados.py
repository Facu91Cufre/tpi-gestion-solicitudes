from enum import Enum


class EstadoSolicitud(Enum):
    PENDIENTE = "Pendiente"
    APROBADO = "Aprobado"
    RECHAZADO = "Rechazado"
    EN_PROCESO = "En Proceso"