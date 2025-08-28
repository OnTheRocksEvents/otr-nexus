from agents.tomeu import Tomeu
from agents.eolo import Eolo
from simulation.event_simulator import simular_evento
from utils.logger import log

tomeu = Tomeu()
eolo = Eolo()

log(tomeu.generar_presupuesto("Evento Ibiza 2025"))
log(eolo.analizar_mercado("Sector musical europeo"))
simular_evento("Festival OnTheRocks")
