from inventario import Inventario  # clase Inventario
from producto import Producto      # clase Producto
from pathlib import Path           # para armar la ruta correcta

# Ruta ABSOLUTA al JSON (para que siempre encuentre data/inventario.json)
BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "data" / "inventario.json"


def pedir_entero(mensaje: str) -> int:
    """Pide un entero hasta que el usuario lo ingrese correctamente."""
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Ingresa un número entero válido.")


def pedir_flotante(mensaje: str) -> float:
    """Pide un decimal (float) hasta que el usuario lo ingrese correctamente."""
    while True:
        try:
            return float(input(mensaje).strip())
        except ValueError:
            print("Ingresa un número válido (ej: 10.50).")


def mostrar_menu() -> None:
    """Muestra las opciones del sistema."""
    print("\n=== SISTEMA AVANZADO DE INVENTARIO ===")
    print("1) Añadir producto")
    print("2) Eliminar producto por ID")
    print("3) Actualizar cantidad o precio")
    print("4) Buscar por nombre")
    print("5) Mostrar inventario")
    print("6) Guardar inventario (JSON)")
    print("0) Salir")


def main():
    # IMPORTANTE: el inventario se crea UNA SOLA VEZ, antes del while
    inv = Inventario()

    # Al iniciar, intentamos cargar el JSON (si existe)
    ok, msg = inv.cargar_desde_json(RUTA_JSON)
    print(msg)

    while True:
        mostrar_menu()
        op = input("Elige una opción: ").strip()

        # 1) Añadir producto
        if op == "1":
            pid = input("ID (único): ").strip()
            nombre = input("Nombre: ").strip()
            cantidad = pedir_entero("Cantidad: ")
            precio = pedir_flotante("Precio: ")

            try:
                producto = Producto(pid, nombre, cantidad, precio)
                ok, msg = inv.agregar_producto(producto)
                print(msg)
            except ValueError as e:
                print(f"Error: {e}")

        # 2) Eliminar producto por ID
        elif op == "2":
            pid = input("ID a eliminar: ").strip()
            ok, msg = inv.eliminar_producto(pid)
            print(msg)

        # 3) Actualizar cantidad o precio
        elif op == "3":
            pid = input("ID a actualizar: ").strip()

            print("¿Qué deseas actualizar?")
            print("1) Cantidad")
            print("2) Precio")
            print("3) Ambos")
            sub = input("Opción: ").strip()

            nueva_cantidad = None
            nuevo_precio = None

            if sub in ("1", "3"):
                nueva_cantidad = pedir_entero("Nueva cantidad: ")
            if sub in ("2", "3"):
                nuevo_precio = pedir_flotante("Nuevo precio: ")

            ok, msg = inv.actualizar_producto(pid, nueva_cantidad, nuevo_precio)
            print(msg)

        # 4) Buscar por nombre (coincidencia parcial)
        elif op == "4":
            texto = input("Nombre o parte del nombre: ").strip()
            resultados = inv.buscar_por_nombre(texto)

            if not resultados:
                print("No se encontraron productos.")
            else:
                print(f"Coincidencias: {len(resultados)}")
                for p in resultados:
                    print(p)

        # 5) Mostrar inventario
        elif op == "5":
            inv.mostrar()

        # 6) Guardar manualmente en JSON
        elif op == "6":
            ok, msg = inv.guardar_en_json(RUTA_JSON)
            print(msg)

        # 0) Salir (guardamos antes de cerrar)
        elif op == "0":
            ok, msg = inv.guardar_en_json(RUTA_JSON)
            print(msg)
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    # Punto de inicio del programa
    main()