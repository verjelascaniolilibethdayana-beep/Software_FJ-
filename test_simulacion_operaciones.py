"""Pruebas de integración de la simulación. Ejecutar: python -m unittest -v."""

import unittest
from unittest.mock import patch

from cliente import Cliente
from alquiler_equipo import AlquilerEquipo
from servicio import ReservaSala
from reserva import Reserva
from excepciones import ReservaInvalidaError, DatosInvalidosError, EstadoReservaError
from simulacion_operaciones import ejecutar_simulacion


class PruebasSoftwareFJ(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("C101", "Ana López", "ana@example.com", "3123456789")

    def test_alquiler_valido_y_costo(self):
        equipo = AlquilerEquipo("A101", "Equipos", 50000, "Laptop", 3, True)
        self.assertTrue(equipo.verificar_disponibilidad())
        self.assertEqual(equipo.calcular_costo(), 150000)

    def test_alquiler_rechaza_dias_negativos(self):
        with self.assertRaises(ValueError):
            AlquilerEquipo("A102", "Equipos", 50000, "Laptop", -2, True)

    def test_alquiler_rechaza_nombre_vacio(self):
        with self.assertRaises(ValueError):
            AlquilerEquipo("A103", "Equipos", 50000, "", 2, True)

    def test_disponibilidad_exige_booleano(self):
        with self.assertRaises(TypeError):
            AlquilerEquipo("A104", "Equipos", 50000, "Laptop", 2, "True")

    def test_reserva_valida_se_confirma_y_procesa(self):
        sala = ReservaSala("S101", "Salas", 30000, "Principal", 2, True)
        reserva = Reserva("R101", self.cliente, sala, 2)
        reserva.confirmar()
        self.assertEqual(reserva.estado, "Confirmada")
        self.assertFalse(sala.verificar_disponibilidad())
        self.assertEqual(reserva.procesar(), 60000)
        self.assertEqual(reserva.estado, "Procesada")

    def test_reserva_rechaza_duracion_invalida(self):
        sala = ReservaSala("S102", "Salas", 30000, "Principal", 2, True)
        for duracion in (-1, 0, True):
            with self.subTest(duracion=duracion):
                with self.assertRaises(ReservaInvalidaError):
                    Reserva("R102", self.cliente, sala, duracion)

    def test_reserva_rechaza_sala_ocupada(self):
        sala = ReservaSala("S103", "Salas", 30000, "Ocupada", 2, False)
        reserva = Reserva("R103", self.cliente, sala, 2)
        with self.assertRaises(ReservaInvalidaError):
            reserva.confirmar()
        self.assertEqual(reserva.estado, "Pendiente")

    @patch("simulacion_operaciones.registrar_error")
    @patch("simulacion_operaciones.registrar_evento")
    @patch("simulacion_operaciones.configurar_logging")
    def test_simulacion_integrada_registra_eventos(self, configurar, evento, error):
        resultados = ejecutar_simulacion(mostrar=False)
        self.assertTrue(configurar.called)
        self.assertTrue(evento.called)
        self.assertTrue(any("Reserva procesada correctamente" in r for r in resultados))
        self.assertTrue(any("Servicio no disponible detectado" in r for r in resultados))
        self.assertTrue(error.called, "Se deben registrar las validaciones rechazadas")

    def test_encadenamiento_de_excepciones(self):
        sala = ReservaSala("S104", "Salas", 10000, "Sala A", 1, True)
        with self.assertRaises(ReservaInvalidaError) as contexto:
            Reserva("R104", self.cliente, sala, -3)
        self.assertIsInstance(contexto.exception.__cause__, DatosInvalidosError)

    def test_calculo_con_descuento_impuesto(self):
        sala = ReservaSala("S105", "Salas", 50000, "Sala B", 2, True)
        reserva = Reserva("R105", self.cliente, sala, 2)
        self.assertEqual(reserva.calcular_total(), 100000)
        self.assertEqual(reserva.calcular_total(descuento=.1), 90000)
        self.assertEqual(reserva.calcular_total(descuento=.1, impuesto=.19), 107100)

    def test_rechaza_tasas_invalidas(self):
        sala = ReservaSala("S106", "Salas", 10000, "Sala C", 2, True)
        reserva = Reserva("R106", self.cliente, sala, 2)
        for valor in (-.1, 1.1, True, "10"):
            with self.subTest(valor=valor):
                with self.assertRaises(ReservaInvalidaError):
                    reserva.calcular_total(descuento=valor)

    def test_procesar_sin_confirmar(self):
        sala = ReservaSala("S107", "Salas", 10000, "Sala D", 2, True)
        reserva = Reserva("R107", self.cliente, sala, 2)
        with self.assertRaises(EstadoReservaError):
            reserva.procesar()
        self.assertEqual(reserva.estado, "Pendiente")

    def test_cancelacion_restituye_disponibilidad(self):
        sala = ReservaSala("S108", "Salas", 10000, "Sala E", 2, True)
        reserva = Reserva("R108", self.cliente, sala, 2)
        reserva.confirmar()
        self.assertFalse(sala.disponible)
        reserva.cancelar()
        self.assertTrue(sala.disponible)
        with self.assertRaises(EstadoReservaError):
            reserva.cancelar()

    def test_logs_guardan_validaciones(self):
        import logging
        from tempfile import TemporaryDirectory
        from pathlib import Path
        from configuracion_logs import configurar_logging
        logger = logging.getLogger("software_fj")
        anteriores = logger.handlers[:]
        try:
            for h in anteriores: logger.removeHandler(h)
            with TemporaryDirectory() as temporal:
                ruta = Path(temporal) / "registro.log"
                configurar_logging(ruta=ruta)
                ejecutar_simulacion(mostrar=False)
                for h in logger.handlers: h.flush()
                texto = ruta.read_text(encoding="utf-8")
                self.assertIn(" | INFO | ", texto)
                self.assertIn(" | ERROR | ", texto)
                self.assertIn("Reserva de servicio no disponible", texto)
        finally:
            for h in logger.handlers[:]:
                logger.removeHandler(h)
                h.close()
            for h in anteriores: logger.addHandler(h)


if __name__ == "__main__":
    unittest.main()
