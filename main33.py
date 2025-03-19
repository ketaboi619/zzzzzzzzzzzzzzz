frutas = []

print("ingrese 10 frutas")
for i in range(10):

    nombre = input("Nombre de la fruta: ")
    precio = input("Precio de la fruta: ")

    while not precio.replace('.','.',1).isdigit():
        precio = float(precio)

        frutas.append({"nombre": nombre, "precio": precio})



        ##aqui se usa el lambda para darle la clave de que buscara por el precio
        frutasOrdenadas = sorted(frutas, key=lambda x: x["precio"], reverse=True)

        print("\nLista de frutas ordenadas de mayor a menor precio:")
        for fruta in frutasOrdenadas:
            print(f"Nombre: {fruta['nombre']}, Precio: ${fruta['precio']:.2f}")