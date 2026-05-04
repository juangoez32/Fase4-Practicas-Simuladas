# ==========================================
# MODULO PRINCIPAL - MENU Y SIMULACION
# ==========================================
import sys
import os

# Agregar software_fj al path para imports relativos
sys.path.insert(0, os.path.dirname(__file__))

import logger  # Inicializa el logging al importar
import logging

from cliente import Cliente
from servicio import ReservaDeSala, AlquilerEquipos, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ValidationError, ReservaError

# Simulacion, ejecuta pruebas para verificar el correcto funcionamiento 
def simular_10_operaciones():
    print("\n--- INICIANDO DIAGNOSTICO AUTOMATICO DE ROBUSTEZ ---")
    logging.info("=========== NUEVA SESION DE PRUEBAS AUTOMATICAS ===========")

    s_auditorio = ReservaDeSala("Auditorio", 150)
    s_redes = AlquilerEquipos("Routers Cisco", 200)
    s_seguridad = AsesoriaEspecializada("Pentesting", 400)
    operaciones = 0

    def ejecutor(titulo, func):
        nonlocal operaciones
        operaciones += 1
        print(f"\nOp {operaciones}: {titulo}")
        try:
            func()
        except ValidationError as ve:
            print(f"[X] ValidationError capturado a salvo -> {ve}")
            logging.warning(f"Simulacion Op{operaciones}: {ve}")
        except ReservaError as re:
            print(f"[X] ReservaError capturado a salvo -> {re}")
            logging.error(f"Simulacion Op{operaciones}: {re}")
        except Exception as e:
            print(f"[X] Exception general evitada -> {e}")
            logging.error(f"Simulacion Op{operaciones} Exception: {e}")

    ejecutor("Cliente Valido",
             lambda: print(Cliente("1", "Empresa A", "a@a.com").obtener_detalles()))
    ejecutor("Cliente Invalido (Correo malo)",
             lambda: Cliente("2", "Pepe", "correo_malo.com"))
    ejecutor("Cliente Invalido (Nombre corto)",
             lambda: Cliente("3", "A", "a@a.com"))

    def op_4():
        c = Cliente("4", "Soluciones IT", "it@soluciones.com")
        res = Reserva(c, s_seguridad, 3)
        print(res.procesar_reserva(impuesto=0.15))
    ejecutor("Reserva Valida (Asesoria + Impuestos)", op_4)

    def op_5():
        c = Cliente("5", "Fallos Corp", "f@f.com")
        res = Reserva(c, s_auditorio, -5)
        res.procesar_reserva()
    ejecutor("Reserva Invalida (Horas negativas en Sala)", op_5)

    def op_6():
        c = Cliente("6", "Error Tech", "e@tech.com")
        res = Reserva(c, s_auditorio, 2)
        print(res.procesar_reserva(descuento=5000))
    ejecutor("Reserva Invalida (Costo negativo por descuento excesivo)", op_6)

    def op_7():
        Reserva("NoSoyObjetoCliente", s_redes, 5)
    ejecutor("Reserva con Cliente invalido (inyeccion erronea)", op_7)

    def op_8():
        servicios = [s_auditorio, s_redes, s_seguridad]
        for s in servicios:
            print("Polimorfismo:", s.obtener_detalles())
    ejecutor("Demostracion de Polimorfismo exitoso", op_8)

    def op_9():
        c = Cliente("9", "Crash Test", "c@dummy.com")
        res = Reserva(c, s_redes, "Cinco")  # TypeError nativo de Python
        res.procesar_reserva()
    ejecutor("Error Critico tipo nativo de Python capturado", op_9)

    def op_10():
        c = Cliente("10", "Fin Prueba", "fin@prueba.com")
        res = Reserva(c, s_auditorio, 10)
        print(res.procesar_reserva())
    ejecutor("La app SIEMPRE termina viva (Prueba 10 exitosa)", op_10)

    print("\n--- SIMULACION COMPLETADA: LA APP NUNCA SE CERRO POR ERROR ---")

# Interfaz de consola para interactuar con el sistema
def menu_interactivo():
    while True:
        print("\n=== SOFTWARE FJ - SISTEMA DE GESTION (POO) ===")
        print("1. Ejecutar Simulacion Calificable (10 Operaciones Robustas)")
        print("2. Registrar Cliente Manual (Jugar con Validaciones)")
        print("3. Salir")
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            simular_10_operaciones()
        elif opcion == "2":
            print("\n-- Registro de Nuevo Cliente --")
            id_cli = input("Ingresa ID: ")
            nom_cli = input("Ingresa Nombre (min 3 letras): ")
            mail_cli = input("Ingresa Correo (con @): ")
            try:
                nuevo = Cliente(id_cli, nom_cli, mail_cli)
                logging.info(f"[Registro Manual] Nuevo cliente creado: {nuevo.nombre}")
                print(f"[EXITO] -> {nuevo.obtener_detalles()}")
            except ValidationError as ve:
                logging.warning(f"[Registro Manual Fallido]: {ve}")
                print(f"[ERROR CAPTURADO] El cliente no se creo porque: {ve}")
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida.")
# Abre el menu, solo si el archivo se ejecuta directamente 

if __name__ == "__main__":
    menu_interactivo()
