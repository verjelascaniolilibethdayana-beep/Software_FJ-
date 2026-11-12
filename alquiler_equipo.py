"""
Proyecto: Software FJ
Archivo: alquiler_equipo.py

Descripción:
Clase para representar un servicio de alquiler de equipos.
El módulo incluye una clase base temporal para permitir que el
archivo funcione mientras el compañero 2 sube servicio.py.

Nota:
Cuando exista servicio.py en el repositorio, Python usará esa
clase automáticamente. Si no existe, se usa una versión temporal
mínima para evitar errores y permitir el avance del proyecto.
"""

# Intento importar la clase real del compañero 2.
# Si todavía no existe, se usa una clase temporal para no bloquear el trabajo.
try:
    from servicio import Servicio  # type: ignore
except ImportError:
    class Servicio:
        """Clase temporal mientras se integra servicio.py."""
        def __init__(self, identificador, nombre_servicio, precio_base):
            self.identificador = identificador
            self.nombre_servicio = nombre_servicio
            self.precio_base = precio_base


class AlquilerEquipo(Servicio):
    """
    Representa el servicio de alquiler de equipos.
    Hereda de Servicio y agrega información propia del alquiler.
    """

    def __init__(self, identificador, nombre_servicio, precio_base,
                 nombre_equipo, dias_alquiler, disponible=True):
        # Inicializa los atributos heredados del servicio base.
        super().__init__(identificador, nombre_servicio, precio_base)

        # Inicializa los atributos propios del alquiler.
        self.nombre_equipo = nombre_equipo
        self.dias_alquiler = dias_alquiler
        self.disponible = disponible

    @property
    def nombre_equipo(self):
        # Retorna el nombre del equipo.
        return self._nombre_equipo

    @nombre_equipo.setter
    def nombre_equipo(self, valor):
        # Valida que el nombre del equipo sea un texto no vacío.
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del equipo no puede estar vacío.")
        self._nombre_equipo = valor.strip()

    @property
    def dias_alquiler(self):
        # Retorna la cantidad de días de alquiler.
        return self._dias_alquiler

    @dias_alquiler.setter
    def dias_alquiler(self, valor):
        # Valida que los días de alquiler sean un entero positivo.
        if not isinstance(valor, int):
            raise TypeError("Los días de alquiler deben ser un número entero.")
        if valor <= 0:
            raise ValueError("Los días de alquiler deben ser mayores que cero.")
        self._dias_alquiler = valor

    @property
    def disponible(self):
        # Retorna el estado de disponibilidad.
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        # Valida que la disponibilidad sea booleana.
        if not isinstance(valor, bool):
            raise TypeError("La disponibilidad debe ser True o False.")
        self._disponible = valor

    def calcular_costo(self):
        # Calcula el costo total multiplicando el precio base por los días.
        return self.precio_base * self.dias_alquiler

    def verificar_disponibilidad(self):
        # Retorna True si el equipo está disponible.
        return self.disponible

    def mostrar_informacion(self):
        # Construye un resumen legible del alquiler.
        estado = "Disponible" if self.disponible else "No disponible"
        return (
            f"ID: {self.identificador} | "
            f"Servicio: {self.nombre_servicio} | "
            f"Equipo: {self.nombre_equipo} | "
            f"Días: {self.dias_alquiler} | "
            f"Precio por día: ${self.precio_base:,.2f} | "
            f"Costo total: ${self.calcular_costo():,.2f} | "
            f"Estado: {estado}"
        )
