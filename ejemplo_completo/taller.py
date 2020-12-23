from ejemplo_completo.equipo import Equipo
from ejemplo_completo.equipo_refrigeracion import EquipoRefrigeracion
from ejemplo_completo.equipo_climatizacion import EquipoClimatizacion


class Taller:

    def __init__(self):
        self._equipos = []

    @property
    def equipos(self):
        return self._equipos

    def insertar_equipo(self, equipo):
        if self._equipos is None:
            self._equipos[0] = equipo
            self.guardar_equipos()
        for item in self._equipos:
            if equipo.no_orden == item.no_orden:
                print("Ya existe un equipo con ese codigo")
            else:
                self._equipos.append(Equipo(equipo))
                self.actualizar_equipos(equipo)

    def eliminar_equipo(self, no_orden):
        idx_equipo = 0
        equipo = Equipo()
        for item in self._equipos:
            if no_orden == item.no_orden:
                equipo = item
                idx_equipo = self._equipos.index(equipo)
        self._equipos.pop(idx_equipo)
        self.guardar_equipos()
        return equipo

    # Determinar la marca y el modelo del equipo que se reparó dado el número de la orden de reparación
    def inciso_b(self, no_orden):
        for item in self._equipos:
            if no_orden == item.no_orden:
                return item.marca, item.modelo
        return 'No se ha encontrado el equipo solicitado'

    # Determinar la marca y el número de la orden de reparación del aire acondicionado con más años de explotación
    # reparado en el taller
    def inciso_c(self):
        m = 0
        e = Equipo()
        for item in self._equipos:
            if item is EquipoClimatizacion and item.tipo_climatizacion == 'Aire acondicionado' and item.annos_explotacion > m:
                m = item.annos_explotacion
                e = item
        return e.no_orden, e.marca

    # Determinar el consumo medio en watts de los refrigeradores de dos cámaras reparados en el taller
    def inciso_d(self):
        total_consumo = 0
        cantidad = 0
        for item in self._equipos:
            if isinstance(item, EquipoRefrigeracion) and item.cant_camaras == 2:
                total_consumo += item.consumo
                cantidad += 1
        return total_consumo//cantidad

    # Determinar el listado de los datos de los refrigeradores reparados en el taller que consuman 220v
    def inciso_e(self):
        refrigeradores_220 = []
        for item in self._equipos:
            if item is EquipoRefrigeracion and item.consumo == 220:
                refrigeradores_220.append(item)
        return refrigeradores_220

    def mostrar_equipos(self):
        with open('./files/equipos.txt', mode='r') as f:
            equipos = []
            e = Equipo()
            for line in f:
                if line.strip('\t')[9] == '-' and line.strip('\t')[10] == '-':
                    e = EquipoRefrigeracion()
                    e.volumen = int(line.strip('\t')[7])
                    e.cant_camaras = int(line.strip('\t')[8])
                elif line.strip('\t')[7] == '-' and line.strip('\t')[8] == '-':
                    e = EquipoClimatizacion()
                    e.tipo_climatizacion = line.strip('\t')[9]
                    e.capacidad_toneladas = line.strip('\t')[10]
                e.no_orden = line.strip('\t')[0]
                e.garantia = line.strip('\t')[1]
                e.marca = line.strip('\t')[2]
                e.modelo = line.strip('\t')[3]
                e.annos_explotacion = int(line.strip('\t')[4])
                e.consumo = int(line.strip('\t')[5])
                e.tension = int(line.strip('\t')[6])
                equipos.append(e)
            print(
                'numero_orden\ttiene_garantia\tmarca\tmodelo\tannos_explotacion\tconsumo\ttension\t'
                'volumen\tcant_camaras\ttipo_climatizacion\tcapacidad_toneladas')
            for item in equipos:
                print()




    def guardar_equipos(self):
        with open('/home/maite/Documents/files/equipos.txt', mode='w+') as f:
            print(
                'numero_orden\ttiene_garantia\tmarca\tmodelo\tannos_explotacion\tconsumo\ttension\t'
                'volumen\tcant_camaras\ttipo_climatizacion\tcapacidad_toneladas', file=f, sep='\t')
            for item in self._equipos:
                if isinstance(item, EquipoRefrigeracion):
                    print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t-\t-'.format(str(item.no_orden),
                                                                                     str(item.garantia),
                                                                                     str(item.marca), str(item.modelo),
                                                                                     str(item.annos_explotacion),
                                                                                     str(item.consumo),
                                                                                     str(item.tension),
                                                                                     str(item.volumen),
                                                                                     str(item.cant_camaras)), file=f, sep='\t')
                elif isinstance(item, EquipoClimatizacion):
                    print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t-\t-\t{7}\t{8}'.format(str(item.no_orden),
                                                                                     str(item.garantia),
                                                                                     str(item.marca), str(item.modelo),
                                                                                     str(item.annos_explotacion),
                                                                                     str(item.consumo),
                                                                                     str(item.tension),
                                                                                     str(item.tipo_climatizacion),
                                                                                     str(item.capacidad_toneladas)), file=f, sep='\t')


    def actualizar_equipos(self, equipo):
        with open('/home/maite/Documents/files/equipos.txt', mode='a') as f:
            if isinstance(equipo, EquipoRefrigeracion):
                print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t-\t-'.format(str(equipo.no_orden),
                                                                                     str(equipo.garantia),
                                                                                     str(equipo.marca), str(equipo.modelo),
                                                                                     str(equipo.annos_explotacion),
                                                                                     str(equipo.consumo),
                                                                                     str(equipo.tension),
                                                                                     str(equipo.volumen),
                                                                                     str(equipo.cant_camaras)))
            elif isinstance(equipo, EquipoClimatizacion):
                print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t-\t-\t{7}\t{8}'.format(str(equipo.no_orden),
                                                                                     str(equipo.garantia),
                                                                                     str(equipo.marca), str(equipo.modelo),
                                                                                     str(equipo.annos_explotacion),
                                                                                     str(equipo.consumo),
                                                                                     str(equipo.tension),
                                                                                     str(equipo.tipo_climatizacion),
                                                                                     str(equipo.capacidad_toneladas)))

