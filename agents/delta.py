class Delta:
    def __init__(self):
        self.role = "Métricas & ROI"

    def calcular_roi(self, ingresos, costos):
        return (ingresos - costos) / costos
