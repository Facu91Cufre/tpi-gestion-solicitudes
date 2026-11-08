from abc import ABC, abstractmethod

from src.domain.Solicitud import Solicitud


class SolicitudRepositoryBase(ABC):
    @abstractmethod
    def guardar(self, solicitud: Solicitud) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, id_solicitud: int) -> Solicitud | None:
        pass

    @abstractmethod
    def obtener_todas(self) -> list[Solicitud]:
        pass