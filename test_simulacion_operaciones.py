"""Pruebas de integración de la simulación. Ejecutar: python -m unittest -v."""

import unittest
from unittest.mock import patch

from cliente import Cliente
from alquiler_equipo import AlquilerEquipo
from servicio import ReservaSala
from reserva import Reserva
from excepciones import ReservaInvalidaError, DatosInvalidosError
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
                with self.assertRaises(DatosInvalidosError):
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
        self.assertFalse(error.called, "La simulación correcta no debe registrar errores inesperados")


if __name__ == "__main__":
    unittest.main()
