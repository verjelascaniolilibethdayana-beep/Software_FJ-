"""Registro centralizado de eventos y errores para Software FJ.

Uso:
    from configuracion_logs import configurar_logging, registrar_error
    logger = configurar_logging()
    logger.info("Cliente registrado")

Los mensajes de error se guardan en logs/software_fj.log. La carpeta
se crea automáticamente; si no hay permiso para escribir, se utiliza
un manejador de consola para no bloquear la ejecución del programa.
"""

import logging
from pathlib import Path

NOMBRE_LOGGER = "software_fj"


def configurar_logging(ruta=None, nivel=logging.INFO):
    """Configura una sola vez el logger y devuelve el mismo objeto.

    ``ruta`` permite elegir otro destino durante las pruebas.
    """
    logger = logging.getLogger(NOMBRE_LOGGER)
    logger.setLevel(nivel)
    logger.propagate = False
    if logger.handlers:
        return logger

    destino = Path(ruta) if ruta is not None else Path(__file__).resolve().parent / "logs" / "software_fj.log"
    formato = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    try:
        destino.parent.mkdir(parents=True, exist_ok=True)
        manejador = logging.FileHandler(destino, encoding="utf-8")
    except OSError as error:
        manejador = logging.StreamHandler()
        manejador.setFormatter(formato)
        logger.addHandler(manejador)
        logger.warning("No fue posible abrir el archivo de logs: %s", error)
        return logger

    manejador.setFormatter(formato)
    logger.addHandler(manejador)
    return logger


def registrar_error(operacion, error, *, incluir_traza=False):
    """Registra un error controlado e identifica la operación afectada.

    Usar dentro de un bloque ``except`` cuando se requiera la traza.
    """
    logger = configurar_logging()
    logger.error("Operación '%s' fallida: %s: %s", operacion,
                 type(error).__name__, error, exc_info=incluir_traza)


def registrar_evento(mensaje, *argumentos):
    """Registra una operación exitosa o un evento relevante."""
    configurar_logging().info(mensaje, *argumentos)
