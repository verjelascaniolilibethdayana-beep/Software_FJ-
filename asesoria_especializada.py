"""
Proyecto: Software FJ
Archivo: asesoria_especializada.py

Descripción:
Este módulo implementa el servicio de asesoría especializada.
La clase hereda de Servicio y valida datos como el área de
asesoría, la duración de la sesión y la disponibilidad.

Nota:
Se intenta importar la clase real desde servicio.py. Si ese
archivo aún tiene problemas o no existe, se usa una clase base
temporal para no bloquear el avance del proyecto.
"""

# Intento importar la clase real del proyecto.
# Si el archivo servicio.py aún no está listo, se usa una
# versión temporal para seguir avanzando.
try:
    from servicio import Servicio
except Exception:
    class Servicio:
        """Clase temporal mientras se integra servicio.py."""

        def __init__(self, identificador, nombre_servicio, precio_base):
            self.identificador = identificador
            self.nombre_servicio = nombre_servicio
            self.precio_base = precio_base


class AsesoriaEspecializada(Servicio):
    """
    Representa un servicio de asesoría especializada.
    Hereda de Servicio y agrega datos propios de la asesoría.
    """

    def __init__(
        self,
        identificador,
        nombre_servicio,
        precio_base,
        area_especialidad,
        horas,
        disponible=True
    ):
        # Inicializa los atributos heredados del servicio base.
        super().__init__(identificador, nombre_servicio, precio_base)

        # Inicializa los atributos propios del servicio.
        self.area_especialidad = area_especialidad
        self.horas = horas
        self.disponible = disponible

    @property
    def area_especialidad(self):
        # Retorna el área de la asesoría.
        return self._area_especialidad

    @area_especialidad.setter
    def area_especialidad(self, valor):
        # Valida que el área sea un texto no vacío.
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El área de especialidad no puede estar vacía.")
        self._area_especialidad = valor.strip()

    @property
    def horas(self):
        # Retorna la cantidad de horas de la asesoría.
        return self._horas

    @horas.setter
    def horas(self, valor):
        # Valida que las horas sean un número entero positivo.
        if not isinstance(valor, int):
            raise TypeError("Las horas deben ser un número entero.")
        if valor <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")
        self._horas = valor

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
        # Calcula el costo total multiplicando la tarifa base por las horas.
        return self.precio_base * self.horas

    def verificar_disponibilidad(self):
        # Retorna True si la asesoría está disponible.
        return self.disponible

    def mostrar_informacion(self):
        # Construye un resumen legible del servicio.
        estado = "Disponible" if self.disponible else "No disponible"
        return (
            f"ID: {self.identificador} | "
            f"Servicio: {self.nombre_servicio} | "
            f"Área: {self.area_especialidad} | "
            f"Horas: {self.horas} | "
            f"Precio por hora: ${self.precio_base:,.2f} | "
            f"Costo total: ${self.calcular_costo():,.2f} | "
            f"Estado: {estado}"
        )
