from utils.sheets_reader import leer_todas_las_hojas
from agents.delta import Delta
from agents.barbarito import Barbarito
from agents.paquito import Paquito
from utils.logger import log

# IDs de tus hojas
SHEETS = {
    "unificado": "1_WPcxC227gmZminK5AGOJ3vrK7Zjcl4xNb3GxGWxx-0",
    "albaranes": "1zB-snLBoO_lkiK0mq-MYyDUwxm5-S8VM"
}

# Carga todas las pestañas de cada documento
datos_unificado = leer_todas_las_hojas(SHEETS["unificado"])
datos_albaranes = leer_todas_las_hojas(SHEETS["albaranes"])

# Inicializa agentes
delta = Delta()
barbarito = Barbarito()
paquito = Paquito()

# 1) Delta analiza métricas
for registro in datos_unificado.get("Métricas", []):
    log(delta.analizar_roi(registro))

# 2) Barbarito planifica entregas y valida entradas
for item in datos_unificado.get("Stock", []):
    log(barbarito.planificar_entrega(item))
for registro in datos_albaranes.get("Albaranes Entrantes", []):
    log(barbarito.validar_entrada(registro))

# 3) Paquito audita inconsistencias en métricas y albaranes
# Combina ambos diccionarios para iterar por pestañas comunes
todos = {**datos_unificado, **datos_albaranes}
for hoja in ["Métricas", "Albaranes Entrantes", "Albaranes Salientes"]:
    for registro in todos.get(hoja, []):
        log(paquito.auditar_registro(registro))
