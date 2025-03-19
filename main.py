
Helado = {}
Helados = []

idContador = 0

print("*****Helados frozen*****")
print("1. Agregar helado a la lista")
print("2. Mostrar un helado de la lista")
print("3. Modificar un helado de la lista")
print("4. Eliminar helado de la lista")
print("5. Salir")

opcion = 100
while opcion != 5:
    opcion = int(input("Digita una opcion"))

    if opcion == 1:

        print("creando lista/")
        nombre = input("Ingrese el nombre del helado: ")
        descripcion = input("Ingrese la descripción del helado: ")
        precio = int(input("Ingrese el precio del helado: "))


    if precio.isdigit():
        precio = precio(int)
        Helado = {
            "id": idContador,
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio
        }
        Helados.append(Helado)
        idContador += 1
        print("Helado creado correctamente.")
    else:

      if opcion == 2:

          for heladoIT in Helados:
            print(heladoIT["nombre"],heladoIT["precio"])


    if opcion == 3:

        idModificar = input("ingrese el helado a modificar")
        if idModificar.isdigit():
            idModificar = int(idModificar)

    if opcion == 4:

        print("--- Eliminar un helado ---")
        idEliminar: int = int(input("Ingrese el ID del helado a eliminar: "))


    for Helado in Helados:
        if Helado["id"] == idEliminar:
            Helados.remove(Helado)
            print("Helado eliminado correctamente.")

    if opcion == 5:
        print("saliendo")
        break
