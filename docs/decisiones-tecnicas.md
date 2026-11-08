# Decisiones técnicas

En este documento explicamos las decisiones que tomamos durante el trabajo y por qué.

---

## 1. Usar Python con un menú por consola

**Decisión:** el sistema es un programa de consola hecho en Python.

**Por qué:** la consigna pide un sistema simple. Lo importante del trabajo es mejorar la calidad del código, no la interfaz. Python es el lenguaje que más manejamos.

---

## 2. Separar el código en capas

**Decisión:** dividimos el código en cuatro carpetas:

- `src/domain/` → las clases del sistema (Solicitud, Estudiante, Responsable, Estado)
- `src/repository/` → guardar y buscar solicitudes
- `src/services/` → la lógica del sistema
- `src/ui/` → el menú

**Por qué:** en la versión inicial todo estaba en `main.py` y era difícil de leer y de modificar. Con las capas, cada parte tiene una sola tarea (principio SRP).

---

## 3. Guardar los datos en memoria, con una clase base para el repositorio

**Decisión:** las solicitudes se guardan en una lista en memoria (`SolicitudRepositoryMemoria`). Esa clase hereda de una clase base (`SolicitudRepositoryBase`).

**Por qué:** la consigna permite guardar los datos en memoria, y así el sistema sigue siendo simple. La clase base permite, en el futuro, guardar en un archivo o en una base de datos creando otra clase, sin tocar el service ni el menú (principio DIP).

---

## 4. Usar un Enum para los estados

**Decisión:** los estados (Pendiente, En Proceso, Aprobada, Rechazada) están definidos en `EstadoSolicitud`.

**Por qué:** antes eran textos sueltos repetidos en varios lugares, y un error de tipeo podía romper el sistema sin que nos diéramos cuenta. Ahora están en un solo lugar.

---

## 5. El service genera el ID y crea el estudiante

**Decisión:** el menú solo pide los datos. El service se encarga de crear el `Estudiante` y de generar el ID de la solicitud.

**Por qué:** el menú tiene que encargarse solo de mostrar y pedir datos. La lógica tiene que estar en el service.

---

## 6. Usar `DatosSolicitud` solo para registrar solicitudes

**Decisión:** creamos la clase `DatosSolicitud` y la usamos únicamente en `registrar_solicitud`.

**Por qué:** era el único método que recibía muchos datos sueltos (4). Los demás reciben 1 o 2 parámetros, así que usarla ahí no aportaba nada y complicaba el código.


