from ejemplo_completo.equipo import Equipo


class EquipoClimatizacion(Equipo):

    def __init__(self, no_orden, tipo_climatizacion, capacidad_toneladas, garantia='No', marca='', modelo='', annos_explotacion=0, consumo=0, tension=110):
        super(EquipoClimatizacion, self).__init__(no_orden, garantia, marca, modelo, annos_explotacion, consumo, tension)
        self._tipo_climatizacion = tipo_climatizacion
        self._capacidad_toneladas = capacidad_toneladas

    @property
    def tipo_climatizacion(self):
        return self._tipo_climatizacion

    @tipo_climatizacion.setter
    def tipo_climatizacion(self, value):
        self._tipo_climatizacion = value

    @property
    def capacidad_toneladas(self):
        return self._capacidad_toneladas

    @capacidad_toneladas.setter
    def capacidad_toneladas(self, value):
        self._capacidad_toneladas = value
