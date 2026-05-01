# ==========================================
# EXCEPCIONES PERSONALIZADAS DEL SISTEMA
# ==========================================

class ValidationError(Exception):
    """Error de validacion de datos de entrada."""
    pass

class ReservaError(Exception):
    """Error critico durante el procesamiento de una reserva."""
    pass

class OperacionNoPermitidaError(Exception):
    """Error cuando una operacion produce un resultado invalido."""
    pass