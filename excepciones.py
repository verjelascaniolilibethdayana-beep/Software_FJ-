"""Excepciones de dominio para Software FJ.

Se diferencian fallos de validación, disponibilidad y operaciones de
reservas para que cada módulo pueda actuar sin detener la aplicación.
"""


class SoftwareFJError(Exception):
    """Error controlado propio del sistema de gestión Software FJ."""


class DatosInvalidosError(SoftwareFJError, ValueError):
    """Los datos suministrados no cumplen las reglas de validación."""


class ClienteInvalidoError(DatosInvalidosError):
    """La información del cliente es inválida o está incompleta."""


class ServicioInvalidoError(DatosInvalidosError):
    """El servicio tiene parámetros o precios no permitidos."""


class ServicioNoDisponibleError(SoftwareFJError):
    """El servicio solicitado no se encuentra disponible."""


class ReservaInvalidaError(SoftwareFJError):
    """No se puede crear o procesar la reserva solicitada."""


class EstadoReservaError(ReservaInvalidaError):
    """La reserva no permite la transición de estado solicitada."""


class CalculoCostoError(SoftwareFJError, ArithmeticError):
    """Se produjo un valor inconsistente en el cálculo de un costo."""


def exigir_texto(valor, campo):
    """Comprueba que un dato sea texto no vacío y lo devuelve limpio."""
    if not isinstance(valor, str) or not valor.strip():
        raise DatosInvalidosError(f"{campo} debe ser un texto no vacío.")
    return valor.strip()


def exigir_entero_positivo(valor, campo):
    """Rechaza números negativos, cero, fracciones y valores booleanos."""
    if isinstance(valor, bool) or not isinstance(valor, int) or valor <= 0:
        raise DatosInvalidosError(f"{campo} debe ser un entero mayor que cero.")
    return valor
