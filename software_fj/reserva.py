# ==========================================
# GESTOR DE RESERVAS
# ==========================================
import logging
from cliente import Cliente
from servicio import Servicio
from excepciones import ValidationError, ReservaError


class Reserva:
    """Motor central que procesa reservas con manejo robusto de excepciones."""

    def __init__(self, cliente, servicio, cantidad_tiempo):
        if not isinstance(cliente, Cliente):
            raise ValidationError("Objeto Cliente invalido en la Reserva.")
        if not isinstance(servicio, Servicio):
            raise ValidationError("Objeto Servicio invalido en la Reserva.")

        self.cliente = cliente
        self.servicio = servicio
        self.cantidad_tiempo = cantidad_tiempo
        self.estado = "PENDIENTE"
        logging.info(f"Intencion de reserva PENDIENTE para {cliente.nombre}.")

    def procesar_reserva(self, impuesto=0.0, descuento=0.0):
        logging.info("Procesando reserva...")
        costo_final = 0
        try:
            costo_final = self.servicio.calcular_costo_final(
                self.cantidad_tiempo, impuesto, descuento
            )
        except ReservaError as re:
            self.estado = "FALLIDA"
            logging.error(
                f"[ERROR MANEJADO] Problema en calculo: {re} - Causa: {re.__cause__}"
            )
            raise
        except Exception as e:
            self.estado = "ERROR CRITICO"
            logging.critical(f"[FALLO INESPERADO] Excepcion general: {e}")
            raise
        else:
            self.estado = "CONFIRMADA EXITOSAMENTE"
            resumen = (
                f"EXITO: Resumen | {self.cliente.nombre} | "
                f"{self.servicio.nombre_servicio} | Total: ${costo_final:.2f}"
            )
            logging.info(resumen)
            return resumen
        finally:
            logging.info(
                f"--- Estado final Reserva ({self.cliente.nombre}): {self.estado} ---\n"
            )