# ==========================================
# EXCEPCIONES PERSONALIZADAS DEL SISTEMA
# ==========================================
# Estas clases son creadas para manejar errores especificos del sistema y diferenciar las novedades en la simulacion
class ValidationError(Exception):
    """Error de validacion de datos de entrada."""
    pass

class ReservaError(Exception):
    """Error critico durante el procesamiento de una reserva."""
    pass

class OperacionNoPermitidaError(Exception):
    """Error cuando una operacion produce un resultado invalido."""
    pass
