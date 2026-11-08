# Etapa 6: Pruebas y verificación

Para comprobar que el refactoring no rompió el sistema, ejecutamos los mismos casos de prueba en las dos versiones:

- **Versión inicial:** tag `estado-inicial`
- **Versión refactorizada:** tag `etapa-refactoring`

Las pruebas son manuales: corrimos el programa, ingresamos los datos de cada caso y anotamos qué mostró.

---

## Casos de prueba

| N° | Qué probamos | Datos | Resultado esperado | Versión inicial | Versión refactorizada | ¿OK? |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| CP1 | Registrar una solicitud | 12345, Matias, Certificado, Certificado Analitico | Se crea la solicitud 1 | "Solicitud 1 creada con éxito!" | "Solicitud 1 creada con éxito!" | ✅ |
| CP2 | Cambiar estado | Solicitud 1 → "Aprobada" | El estado cambia a Aprobada | Cambia a Aprobada | Cambia a Aprobada | ✅ |
| CP3 | Cambiar estado de una solicitud que no existe | ID 99 | Avisa que no existe | "Solicitud no encontrada." | "No se encontró la solicitud con ID 99" | ✅ |
| CP4 | Asignar responsable | 1, R001, Tesoreria | Se asigna y el estado pasa a En Proceso | Asignado, En Proceso | Asignado, En Proceso | ✅ |
| CP5 | Buscar una solicitud que no existe | ID 99 | Avisa que no la encontró | "No se encontraron solicitudes…" | "Solicitud no encontrada." | ✅ |
| CP6 | Salir del sistema | Opción 6 | Se cierra el programa | Se cierra | Se cierra | ✅ |

---

## Conclusión

Los casos probados dan el mismo resultado en las dos versiones. Por eso consideramos que el refactoring no afectó estas funciones del sistema.

---

## Cómo repetir las pruebas

Desde la carpeta del repositorio:

```bash
git checkout estado-inicial      # versión inicial
python3 main.py

git checkout etapa-refactoring   # versión refactorizada
python3 main.py

git checkout main                # volver a la última versión
```

