# Software FJ — Sistema de clientes, servicios y reservas

Proyecto académico de programación orientada a objetos en Python, sin base de datos.
Incluye clientes, alquiler de equipos, reservas de salas y asesorías especializadas.

## Ejecutar en Windows o Linux

Requiere Python 3.10 o superior. No utiliza paquetes externos.
Desde la carpeta donde está `main.py`:

```bash
python main.py
python simulacion_operaciones.py
python -m unittest -v test_simulacion_operaciones
```

La simulación realiza operaciones válidas e inválidas y continúa cuando una
validación falla. Los eventos y errores controlados se registran en
`logs/software_fj.log` (la carpeta se genera automáticamente).

## Estructura

- `main.py`: recorrido principal por servicios y reservas.
- `entidad.py`, `cliente.py`: entidades y validaciones de clientes.
- `servicio.py`, `alquiler_equipo.py`, `asesoria_especializada.py`: servicios.
- `reserva.py`: transición de estados y cálculo con descuento/impuesto opcionales.
- `excepciones.py`: excepciones del dominio y utilidades de validación.
- `configuracion_logs.py`: registro INFO y ERROR en archivo.
- `simulacion_operaciones.py`: escenarios válidos e inválidos.
- `test_simulacion_operaciones.py`: pruebas automatizadas.

## Trabajo colaborativo

Los cambios de simulación y registro fueron preparados en la rama
`ajustes-yefrin-simulacion-logs` y presentados para revisión en el
[Pull Request #2](https://github.com/verjelascaniolilibethdayana-beep/Software_FJ-/pull/2).
Las correcciones finales de este paquete deben subirse a esa rama y revisarse
antes de su integración a `main`.

## Nota sobre pruebas

Las pruebas automatizadas verifican casos relevantes pero no demuestran
formalmente la ausencia de todos los fallos. Mantener los módulos y las
pruebas juntos, revisar el contenido de los logs y validar cualquier
modificación antes de integrarla al repositorio compartido.
