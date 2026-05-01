# ==========================================
# CONFIGURACION CENTRALIZADA DE LOGGING
# ==========================================
import logging
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), 'logs.txt')

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_logger():
    return logging.getLogger('software_fj')