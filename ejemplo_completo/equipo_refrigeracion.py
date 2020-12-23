from ejemplo_completo.equipo import Equipo


class EquipoRefrigeracion(Equipo):

    def __init__(self, no_orden, garantia, marca, modelo, annos_explotacion, consumo, tension, volumen, cant_camaras):
        super().__init__(no_orden, garantia, marca, modelo, annos_explotacion, consumo, tension)
        self._volumen = volumen
        self._cant_camaras = cant_camaras

    @property
    def volumen(self):
        return self._volumen

    @volumen.setter
    def volumen(self, value):
        self._volumen = value

    @property
    def cant_camaras(self):
        return self._cant_camaras

    @cant_camaras.setter
    def cant_camaras(self, value):
        self._cant_camaras = value
