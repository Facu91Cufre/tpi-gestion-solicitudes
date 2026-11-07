# Etapa 3: Diagnóstico de Deuda Técnica y Code Smells

## 1. Introducción
En este documento se registra el inventario de las debilidades técnicas e inconsistencias de diseño detectadas en la versión base del sistema de gestión de solicitudes académicas, con el fin de justificar las tareas de refactoring posterior.

## 2. Inventario de Code Smells

| Code Smell | Evidencia | Ubicación | Impacto | Riesgo de Mantenimiento | Prioridad de Corrección |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *Violación de Responsabilidad Única y Monolito en interfaz* | Toda la lógica de control, interacción por consola, validaciones y manipulación de datos vive en un único bloque procedural sin separación de módulo. | Archivo main.py completo | Alta complejidad y acoplamiento severo entre la interfaz y la lógica. | Muy Alto | Alta |
| *Ausencia de encapsulamiento en entidades* | Las entidades se manejan como diccionarios genéricos planos o tuplas en lugar de objetos con comportamiento propio. | Módulo de datos o estructuras en memoria (listas de solicitudes) | Falta de tipado estricto y dispersión de la lógica de validación de los campos de cada entidad. | Medio-Alto | Alta |
| *Uso de Cadenas Mágicas para Estados* | Comparaciones de texto plano (ej. estado == "Pendiente") | Funciones de cambio de estado y filtros en la lógica de negocio. | Alta probabilidad de errores tipográficos y rotura silenciosa de lógica ante cambios en la redacción. | Medio | Media |
| *Acoplamiento Fuerte con la Capa de Persistencia en Memoria* | Modificación y lectura de colecciones globales compartidas sin abstracción de datos de por medio. | Funciones que operan directamente sobre una lista global (solicitudes = []). | Imposibilidad de migrar en el futuro a una base de datos. | Alto | Alta |
| *Manejo deficiente o Inexistente de Excepciones Robustas* | Validación manual muy básica mediante condicionales sueltas que pueden fallar ante ingresos inesperados. | Bloques de entrada (input) en el menú principal. | Incrementa la probabilidad de cierres abruptos del sistema por excepciones no controladas. | Bajo en código, pero crítico para la experiencia de usuario. | Media |
| *Funciones de Búsqueda y Filtrado Acopladas* | Uso repetitivo de listas complejas o anidadas directamente dentro del menú para filtrar por estado o responsable. | Funciones de listado y reporte en el script principal | Baja cohesión y duplicación de lógica de consulta si se requiere filtrar por otros criterios en el futuro. | Medio | Media |
| *Ausencia de Pruebas Unitarias Automatizadas* | Al estar toda la lógica mezclada con código e inputs, es imposible realizar pruebas unitarias automáticas de forma aislada. | Estructura general del proyecto. Ausencia de directorio tests/ | Cero test automatizado, obligando a realizar pruebas manuales por consola ante cada modificación. | Muy Alto | Alta |
| *Variables Globales y Estado Compartido* | Declaración de variables de estado y listas compartidas directamente en la raíz del proyecto. | Main.py | Violación del principio de encapsulamiento y ocultamiento de información. | Medio | Media |

## 3. Conclusión del Diagnóstico
El contraste entre la calidad externa e interna justifica la necesidad de refactorizar de manera profunda el sistema. Un software de este tipo genera deuda técnica altísima, encareciendo así el costo de cualquier cambio a futuro y volviendo el sistema muy frágil ante posibles regresiones.