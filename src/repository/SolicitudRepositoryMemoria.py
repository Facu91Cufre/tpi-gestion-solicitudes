from src.domain.Solicitud import Solicitud
from src.repository.SolicitudRepositoryBase import SolicitudRepositoryBase


class SolicitudRepositoryMemoria(SolicitudRepositoryBase):
    def __init__(self):
        self._solicitudes: list[Solicitud] = []

    def guardar(self, solicitud: Solicitud) -> None:
        self._solicitudes.append(solicitud)

    def buscar_por_id(self, id_solicitud: int) -> Solicitud | None:
        for solicitud in self._solicitudes:
            if solicitud.id_solicitud == id_solicitud:
                return solicitud
        return None

    def obtener_todas(self) -> list[Solicitud]:
        return list(self._solicitudes)