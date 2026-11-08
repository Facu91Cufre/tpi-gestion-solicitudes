from src.domain.Estudiante import Estudiante
from src.domain.Responsable import Responsable
from src.domain.Solicitud import Solicitud
from src.repository.SolicitudRepositoryBase import SolicitudRepositoryBase


class SolicitudService:
    def __init__(self, repository: SolicitudRepositoryBase):
        self._repository = repository

    def registrar_solicitud(self, id_solicitud: int, estudiante: Estudiante, tipo: str, descripcion: str) -> None:
        nueva_solicitud = Solicitud(id_solicitud, estudiante, tipo, descripcion)
        self._repository.guardar(nueva_solicitud)

    def obtener_solicitudes(self) -> list[Solicitud]:
        return self._repository.obtener_todas()

    def actualizar_estado_solicitud(self, id_solicitud: int, nuevo_estado: str):
        solicitud = self._repository.buscar_por_id(id_solicitud)
        if not solicitud:
            raise ValueError(f"No se encontró la solicitud con ID {id_solicitud}")
        solicitud.cambiar_estado(nuevo_estado)
        print(f"nuevo estado: {nuevo_estado}")

    def buscar_solicitud_por_id(self, id_solicitud: int) -> Solicitud | None:
        return self._repository.buscar_por_id(id_solicitud)

    def asignar_responsable_a_solicitud(self, id_solicitud: int, responsable: Responsable) -> None:
        solicitud = self._repository.buscar_por_id(id_solicitud)
        if not solicitud:
            raise ValueError(f"No se encontró la solicitud con ID {id_solicitud}")
        solicitud.asignar_responsable(responsable)