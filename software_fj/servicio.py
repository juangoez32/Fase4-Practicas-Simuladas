# ==========================================
# CAPA DE SERVICIOS (Herencia + Polimorfismo)
# ==========================================
from abc import abstractmethod
from cliente import Entidad
from excepciones import ReservaError, OperacionNoPermitidaError


class Servicio(Entidad):
    """Clase base abstracta para todos los servicios ofrecidos."""

    def __init__(self, nombre_servicio, tarifa_base):
        self.nombre_servicio = nombre_servicio
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo_final(self, tiempo, impuesto=0.0, descuento=0.0):
        """Calcula el costo total con impuestos y descuentos opcionales."""
        pass


class ReservaDeSala(Servicio):
    """Servicio de reserva de sala por horas."""

    def calcular_costo_final(self, horas, impuesto=0.0, descuento=0.0):
        try:
            if horas <= 0:
                raise ValueError("Las horas de reserva no pueden ser cero ni negativas.")
            subtotal = self.tarifa_base * horas
            total = subtotal + (subtotal * impuesto) - descuento
            if total < 0:
                raise OperacionNoPermitidaError("Costo negativo por exceso de descuento.")
            return total
        except ValueError as e:
            raise ReservaError("Fallo grave al calcular Reserva de la Sala.") from e

    def obtener_detalles(self):
        return f"Sala: {self.nombre_servicio} [Tarifa/Hr: ${self.tarifa_base}]"


class AlquilerEquipos(Servicio):
    """Servicio de alquiler de equipos por dias."""

    def calcular_costo_final(self, dias, impuesto=0.0, descuento=0.0):
        subtotal = self.tarifa_base * dias
        return max(subtotal + (subtotal * impuesto) - descuento, 0)

    def obtener_detalles(self):
        return f"Equipos: {self.nombre_servicio} [Tarifa/Dia: ${self.tarifa_base}]"


class AsesoriaEspecializada(Servicio):
    """Servicio de asesoria tecnica por sesiones con fee fijo."""

    def calcular_costo_final(self, sesiones, impuesto=0.0, descuento=0.0):
        subtotal = (self.tarifa_base * sesiones) + 50  # Fee tecnico fijo
        return subtotal + (subtotal * impuesto) - descuento

    def obtener_detalles(self):
        return f"Asesoria Tecnica: {self.nombre_servicio} [Tarifa/Sesion: ${self.tarifa_base} + Fee $50]"