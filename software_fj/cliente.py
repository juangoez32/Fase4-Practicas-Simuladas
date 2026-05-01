# ==========================================
# CLASE ABSTRACTA ENTIDAD Y CLASE CLIENTE
# ==========================================
from abc import ABC, abstractmethod
from excepciones import ValidationError


class Entidad(ABC):
    """Clase base abstracta para todas las entidades del sistema."""

    @abstractmethod
    def obtener_detalles(self):
        pass


class Cliente(Entidad):
    """Representa un cliente con encapsulamiento robusto."""

    def __init__(self, identificacion, nombre, email):
        self.identificacion = identificacion
        self.nombre = nombre
        self.email = email

    @property
    def identificacion(self):
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValidationError("Validacion: La identificacion debe ser texto.")
        self._identificacion = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if len(valor) < 3:
            raise ValidationError("Validacion: El nombre debe tener al menos 3 letras.")
        self._nombre = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" not in valor:
            raise ValidationError("Validacion: El correo es invalido (falta '@').")
        self._email = valor

    def obtener_detalles(self):
        return f"Cliente: {self.nombre} (ID: {self.identificacion})"