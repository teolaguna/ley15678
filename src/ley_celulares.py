# ===========================================================================================
# Laboratorio de Programación (LPR 5° Año) — E.E.S.T. N° 1 "Eduardo Ader"
# Vicente López
# ===========================================================================================
# ACTIVIDAD 10 BIS: Simulador de Normativa de Celulares en el Aula (Ley 15.678)
# DOCENTE: Mansilla Muñoz York Elías y Yamil Ganduglia
# ESTUDIANTE: Teo Laguna
# ===========================================================================================

print("==================================================")
print("=== SISTEMA DE ASESORAMIENTO NORMATIVO ESCOLAR ===")
print("==================================================\n")

# Simulamos las variables de contexto del aula
autorizacion_docente = False   # Cambiar a True si el profe habilitó la actividad digital
emergencia_familiar = False   # Cambiar a True si fue validado por preceptores

print(f"Estado de Autorización Docente: {autorizacion_docente}")
print(f"Estado de Emergencia Validada : {emergencia_familiar}\n")

# Estructura de decisión
if autorizacion_docente == True:
    print("[ACCESO PERMITIDO] El celular solo para estudiar y para aprender (Fines Pedagogicos).")
elif emergencia_familiar == True:
    print("[CANALIZACION INSTITUCIONAL] Gestionar la comunicacion urgente a traves de preceptoria y/o direccion.")
else:
    print("[RESTRICCION LEY 15.678] Tu celular debe permanecer guardado en la mochila.")

print("==================================================")