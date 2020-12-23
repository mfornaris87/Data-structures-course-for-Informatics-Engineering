import pickle


lines = 0
with open('./my_movies.txt', mode='r+') as r_file:
    for each_line in r_file:
        lines += 1
        print('{:>4} {}'.format(lines, each_line.rstrip()))

with open('./escribir.txt', mode='w') as w_file:
    w_file.write('Esto es una prueba')

with open('./escribir.txt', mode='a') as w_file:
    w_file.writelines('\n')
    w_file.writelines('Esto es una linea adicional en el archivo anterior')
    # otra forma de escribir, esta si pone saltos de linea
    print(file=w_file)
    print('Esta es otra linea', file=w_file)
    print('Ultima prueba', file=w_file)

with open('./mi_lista.dat', mode='wb') as wb_file:
    mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    pickle.dump(mi_lista, wb_file)

with open('./mi_lista.dat', mode='rb') as rb_file:
    my_list = pickle.load(rb_file)
    print("Mi lista original era %s" % my_list)
