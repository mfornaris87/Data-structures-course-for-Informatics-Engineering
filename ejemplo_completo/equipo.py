class Equipo:
    def __init__(self, no_orden, garantia='No', marca='', modelo='', annos_explotacion=0, consumo=0, tension=110):
        self._no_orden = no_orden
        self._garantia = garantia
        self._marca = marca
        self._modelo = modelo
        self._annos_explotacion = annos_explotacion
        self._consumo = consumo
        self._tension = tension

    @property
    def no_orden(self):
        return self._no_orden

    @no_orden.setter
    def no_orden(self, value):
        self._no_orden = value

    @property
    def garantia(self):
        return self._garantia

    @garantia.setter
    def garantia(self, value):
        self._garantia = value

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def annos_explotacion(self):
        return self._annos_explotacion

    @annos_explotacion.setter
    def annos_explotacion(self, value):
        self._annos_explotacion = value

    @property
    def consumo(self):
        return self._consumo

    @consumo.setter
    def consumo(self, value):
        self._consumo = value

    @property
    def tension(self):
        return self._tension

    @tension.setter
    def tension(self, value):
        self._tension = value
