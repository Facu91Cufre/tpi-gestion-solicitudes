# Etapa 7: Checklist de code review

Aplicamos el mismo checklist a la versión inicial (tag `estado-inicial`) y a la versión refactorizada (tag `etapa-refactoring`) para ver qué mejoró.

---

## Checklist

| N° | Punto a revisar | Versión inicial | Versión refactorizada | Observación |
| :--- | :--- | :---: | :---: | :--- |
| 1 | El código está separado en capas | ❌ | ✅ | Antes todo estaba en `main.py`. Ahora está dividido en domain, repository, services y ui. |
| 2 | Las funciones son cortas y hacen una sola cosa | ❌ | ✅ | Antes `main()` tenía todo el menú. Ahora cada opción tiene su propia función. |
| 3 | No hay textos "hardcodeados" repetidos | ❌ | ✅ | Antes los estados eran textos sueltos. Ahora están en el Enum `EstadoSolicitud`. |
| 4 | La búsqueda por ID no está repetida | ❌ | ✅ | Antes estaba copiada en las opciones 2 y 3. Ahora está en `buscar_por_id` del repositorio. |
| 5 | Los datos están encapsulados | ❌ | ✅ | Antes se usaba una lista suelta en `main`. Ahora la maneja el repositorio. |
| 6 | Los métodos no reciben muchos parámetros sueltos | ❌ | ✅ | Ahora `registrar_solicitud` recibe un solo objeto, `DatosSolicitud`. |
| 7 | Un estado inválido muestra un error claro | ❌ | ✅ | Antes decía "Estado no válido." y después "actualizado a: …". Ahora muestra solo el error. |

---

## Feedback y correcciones realizadas

| N° | Problema encontrado | Corrección | Dónde |
| :--- | :--- | :--- | :--- |
| 1, 5 | Todo el sistema en un solo archivo, con una lista suelta | Separación en capas (Move Method) | `src/domain`, `src/repository`, `src/services`, `src/ui` |
| 2 | Función del menú muy larga | Extract Method | `src/ui/menu.py` |
| 3, 7 | Estados como textos sueltos y mensaje contradictorio | Enum de estados | `src/domain/Estados.py` |
| 4 | Búsqueda por ID repetida | Mover la búsqueda al repositorio | `src/repository/SolicitudRepositoryMemoria.py` |
| 6 | Muchos parámetros sueltos al registrar | Introduce Parameter Object | `src/domain/DatosSolicitud.py` |

---

## Criterios de aceptación

Consideramos que el código está aceptado cuando:

1. Todos los puntos del checklist están en ✅ en la versión refactorizada.
2. Todos los casos de `pruebas.md` dan ✅.

Los dos criterios se cumplen.
