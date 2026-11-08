# Sistema de Gestión de Solicitudes Académicas

Trabajo Práctico Integrador de **Metodología de Sistemas II**
Tecnicatura Universitaria en Programación — Universidad Tecnológica Nacional

**Integrantes:** Facundo Julián Cufré y Matías Julián D'Agostino
**Profesora:** Flavia Videla — **Tutor:** Samuel Walter Tocaimaza

---

## Descripción

Es un sistema de consola para gestionar solicitudes académicas de estudiantes (certificados, constancias, etc.). Permite registrar solicitudes, cambiar su estado, asignarles un responsable y consultarlas.

El objetivo del trabajo **no era agregar funcionalidades**, sino mejorar la calidad interna del código. Partimos de una versión inicial que funcionaba bien pero tenía todo en un solo `main.py`. A partir de ahí:

1. Diagnosticamos la deuda técnica y los code smells.
2. Aplicamos principios SOLID y Clean Code.
3. Hicimos un refactoring seguro (Move Method, Extract Method, Introduce Parameter Object y un Enum para los estados).
4. Verificamos con casos de prueba que el sistema siguiera funcionando igual.
5. Revisamos el código con un checklist de code review.

### Actores

- **Estudiante:** es quien genera la solicitud.
- **Responsable:** es el usuario o área asignada para evaluar la solicitud.

---

## Funcionalidades

El sistema se usa desde un menú por consola:

| Opción | Qué hace |
| :---: | :--- |
| 1 | **Registrar nueva solicitud**: se ingresan legajo y nombre del estudiante, tipo y descripción. La solicitud se crea en estado *Pendiente* con un ID automático. |
| 2 | **Cambiar estado de solicitud**: Pendiente, En Proceso, Aprobada o Rechazada. |
| 3 | **Asignar responsable a solicitud**: se ingresa el ID del responsable y el área. La solicitud pasa a *En Proceso*. |
| 4 | **Buscar / filtrar solicitudes**: se ingresa el ID y muestra la solicitud, o avisa si no existe. |
| 5 | **Listar reporte básico**: muestra todas las solicitudes registradas con su ID, estudiante, tipo y estado. |
| 6 | **Salir**: cierra el programa. |

Los datos se guardan en memoria, así que se pierden al cerrar el programa.

---

## Tecnologías

- **Python 3** (versión 3.10 o superior)
- Persistencia en memoria (sin base de datos)
- Git y GitHub para el control de versiones

No usa librerías externas, así que no hace falta instalar nada aparte de Python.

---

## Instalación y uso

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Facu91Cufre/tpi-gestion-solicitudes.git
   cd tpi-gestion-solicitudes
   ```

2. Ejecutar el programa desde la carpeta raíz del proyecto:

   ```bash
   python3 main.py
   ```

   En Windows puede ser `python main.py`.

### Ejemplo

```text
--- GESTIÓN DE SOLICITUDES ACADÉMICAS ---
1. Registrar nueva solicitud
2. Cambiar estado de solicitud
3. Asignar responsable a solicitud
4. Buscar / filtrar solicitudes
5. Listar reporte básico
6. Salir
Elija una opcion (6 para salir): 1
Registrar Solicitud
Ingrese el legajo del estudiante: 12345
Ingrese el nombre del estudiante: Matías
Ingrese el tipo de solicitud (Ej: Certificado, Constancia): Certificado
Ingrese la descripción de la solicitud: Certificado Analítico
Solicitud 1 creada con éxito!
```

---

## Estructura del proyecto

```text
tpi-gestion-solicitudes/
├── main.py                  # Punto de entrada: arma el repositorio, el service y arranca el menú
├── src/
│   ├── domain/              # Clases del sistema
│   │   ├── Solicitud.py
│   │   ├── Estudiante.py
│   │   ├── Responsable.py
│   │   ├── Estados.py       # Enum EstadoSolicitud
│   │   └── DatosSolicitud.py
│   ├── repository/          # Guardar y buscar solicitudes
│   │   ├── SolicitudRepositoryBase.py     # Clase base abstracta
│   │   └── SolicitudRepositoryMemoria.py  # Implementación en memoria
│   ├── services/            # Lógica del sistema
│   │   └── SolicitudService.py
│   └── ui/                  # Menú por consola
│       └── menu.py
└── docs/                    # Documentación del trabajo
```

El menú usa al service, el service usa al repositorio, y todas las capas usan las clases de dominio. El service depende de `SolicitudRepositoryBase` y no de la implementación en memoria, así que en el futuro se podría guardar en una base de datos creando otra clase, sin tocar el service ni el menú.

---

## Versiones (tags)

Cada etapa del trabajo está marcada con un tag:

| Tag | Qué contiene |
| :--- | :--- |
| `estado-inicial` | Versión base del sistema, con todo en `main.py` |
| `etapa-diagnostico` | Documentación de la deuda técnica y los code smells (Etapa 3) |
| `etapa-refactoring` | Código separado en capas, con Extract Method e Introduce Parameter Object |
| `etapa-docs` | Checklist de code review y decisiones técnicas |
| `etapa-pruebas` | Casos de prueba y verificación (Etapa 6) |
| `estado-refactorizado` | Estado final del código, con toda la documentación |

Para ver una versión en particular:

```bash
git checkout estado-inicial         # versión inicial
git checkout etapa-refactoring      # versión refactorizada
git checkout estado-refactorizado   # estado final
git checkout main                   # volver a la última versión
```

---

## Documentación

En la carpeta [`docs/`](docs/) está la documentación de cada etapa:

- [Diagnóstico de deuda técnica y code smells](docs/diagnostico-deuda-tecnica.md)
- [Decisiones técnicas](docs/decisiones-tecnicas.md)
- [Pruebas y verificación](docs/pruebas.md)
- [Checklist de code review](docs/checklist-code-review.md)

El desarrollo completo de las etapas está en el informe PDF del trabajo.

