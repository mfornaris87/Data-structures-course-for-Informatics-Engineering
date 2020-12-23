from ejemplo_completo.taller import Taller, Equipo, EquipoRefrigeracion, EquipoClimatizacion


mi_taller = Taller()

def menu():
    print('Bienvenido al taller')
    print('1 Insertar un equipo')
    print('2 Eliminar un equipo')
    print('3 Buscar equipo por numero de orden')
    print('4 Aire acondicionado con mas annos de explotacion')
    print('5 Consumo de refrigeradores de 2 camaras')
    print('6 Refrigeradores de 220V')
    print('7 Mostrar listado de equipos')
    print('0 Exit')


if __name__ == '__main__':
    menu()
    opcion = int(input('Introduzca la opcion deseada:'))
    while opcion != 0:
        if opcion == 1:
            tipo_equipo = input('Introduzca el tipo de equipo que desea insertar: ')
            no_orden = input('Introduzca el numero de orden: ')
            garantia = input('Introduzca Si o No para indicar si el equipo esta en garantia:')
            marca = input('Introduzca la marca del equipo:')
            modelo = input('Introduzca el modelo del equipo:')
            annos_explotacion = int(input('Introduzca la cantidad de annos de explotacion del equipo:'))
            consumo = int(input('Introduzca el consumo en Watts del equipo:'))
            tension = int(input('Introduzca la tension del equipo, solo puede ser 110 o 220:'))
            # equipo = Equipo(no_orden)
            if tipo_equipo == 'Equipo de refrigeracion':
                volumen = int(input('Introduzca el volumen del refrigerador:'))
                cant_camaras = int(input('Introduzca la cantidad de camaras del refrigerador:'))
                equipo = EquipoRefrigeracion(no_orden, garantia, marca, modelo, annos_explotacion, consumo, tension, volumen, cant_camaras)
            elif tipo_equipo == 'Equipo de climatizacion':
                tipo_climatizacion = input("Introduzca el tipo de equipo de climatizacion, solo puede ser Aire acondicionado o split:")
                capacidad_toneladas = int(input("Introduzca la capadicad en toneladas del equipo"))
                equipo = EquipoClimatizacion(no_orden, tipo_climatizacion, capacidad_toneladas, garantia, marca, modelo, annos_explotacion, consumo, tension)
            else:
                print('Introduzca un tipo de equipo valido, solo pueden ser Equipo de refrigeracion o Equipo de climatizacion')

            # mi_taller.insertar_equipo(equipo)
            mi_taller.equipos.append(equipo)
            print(mi_taller.equipos[0].no_orden, mi_taller.equipos[0].marca)
            opcion = int(input('Introduzca la opcion deseada'))
        elif opcion == 2:
            no_orden = input('Introduzca el numero de orden del equipo que desea eliminar:')
            equipo = mi_taller.eliminar_equipo(no_orden)
            print("Se elimino el equipo: ", equipo.no_orden, equipo.marca, equipo.modelo, equipo.garantia, equipo.annos_explotacion, equipo.consumo, equipo.tension)
            opcion = int(input('Introduzca la opcion deseada'))
        elif opcion == 3:
            no_orden = input('Introduzca el numero de orden del equipo que desea buscar:')
            print(mi_taller.inciso_b(no_orden))
            opcion = int(input('Introduzca la opcion deseada'))
        elif opcion == 4:
            print("El aire acondicionado con mas annos de explotacion en el taller es: ", mi_taller.inciso_c())
            opcion = int(input('Introduzca la opcion deseada'))
        elif opcion == 5:
            print("El consumo medio de refrigeradores de 2 camaras es:", mi_taller.inciso_d())
            opcion = int(input('Introduzca la opcion deseada'))
        elif opcion == 6:
            print("Los refrigeradores 220 en el taller son:")
            for item in mi_taller.inciso_e():
                print("Numero de orden:", item.no_orden)
                print("Marca:", item.marca)
            opcion = int(input('Introduzca la opcion deseada'))
        elif opcion == 7:
            mi_taller.mostrar_equipos()



