def menu():
    gestor = GestorNotas()

    while True:
        print("\nGestor de Notas")
        print("1. Crear cuenta")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            contrasena = input("Contraseña: ")
            if gestor.crear_cuenta(nombre, contrasena):
                print("Cuenta creada exitosamente.")
            else:
                print("El usuario ya existe.")

        elif opcion == "2":
            nombre = input("Nombre: ")
            contrasena = input("Contraseña: ")
            usuario = gestor.iniciar_sesion(nombre, contrasena)

            if usuario:
                print(f"\nBienvenido, {nombre}")
                while True:
                    print("\nMenú de Usuario")
                    print("1. Crear nota")
                    print("2. Editar nota")
                    print("3. Eliminar nota")
                    print("4. Mostrar mis notas")
                    print("5. Cambiar contraseña")
                    print("6. Cerrar sesión")
                    subopcion = input("Elige una opción: ")

                    if subopcion == "1":
                        titulo, contenido, categoria = pedir_datos_nota()
                        usuario.crear_nota(titulo, contenido, categoria)
                        print("Nota creada.")

                    # Otras opciones de menú...

            else:
                print("Credenciales incorrectas.")

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()