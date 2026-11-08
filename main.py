from src.repository.SolicitudRepositoryMemoria import SolicitudRepositoryMemoria
from src.services.SolicitudService import SolicitudService
from src.ui.menu import iniciar_menu


def main():
    repo = SolicitudRepositoryMemoria()
    service = SolicitudService(repo)
    iniciar_menu(service)

if __name__ == "__main__":
    main()