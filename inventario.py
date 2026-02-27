import json  # para guardar y cargar inventario.json
from pathlib import Path  # para manejar rutas y crear la carpeta si no existe
from producto import Producto  # usamos la clase Producto


class Inventario:
    def __init__(self):
        # Diccionario: productos por ID (rápido para buscar)
        self._productos = {}  # {"id": Producto}

        # Set: ayuda a evitar IDs repetidos
        self._ids = set()

    def agregar_producto(self, producto: Producto) -> tuple:
        pid = producto.get_id()

        if pid in self._ids:
            return (False, "Ya existe un producto con ese ID.")

        self._productos[pid] = producto
        self._ids.add(pid)
        return (True, "Producto agregado correctamente.")

    def eliminar_producto(self, producto_id: str) -> tuple:
        producto_id = str(producto_id).strip()

        if producto_id not in self._productos:
            return (False, "No se encontró un producto con ese ID.")

        self._productos.pop(producto_id, None)
        self._ids.discard(producto_id)  # no da error si no existe
        return (True, "Producto eliminado correctamente.")

    def actualizar_producto(self, producto_id: str, nueva_cantidad=None, nuevo_precio=None) -> tuple:
        producto_id = str(producto_id).strip()

        if producto_id not in self._productos:
            return (False, "No se encontró un producto con ese ID.")

        producto = self._productos[producto_id]

        try:
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
        except ValueError as e:
            return (False, f"Error al actualizar: {e}")

        return (True, "Producto actualizado correctamente.")

    def buscar_por_nombre(self, texto: str) -> list:
        # Búsqueda parcial por nombre (devuelve lista)
        texto = str(texto).strip().lower()
        resultados = []

        for p in self._productos.values():
            if texto in p.get_nombre().lower():
                resultados.append(p)

        return resultados

    def listar_productos(self) -> list:
        return list(self._productos.values())

    def mostrar(self) -> None:
        productos = self.listar_productos()

        if not productos:
            print("\nInventario vacío.\n")
            return

        print("\nID | Nombre | Cantidad | Precio")
        print("-" * 40)
        for p in productos:
            print(f"{p.get_id()} | {p.get_nombre()} | {p.get_cantidad()} | ${p.get_precio():.2f}")
        print()

    def guardar_en_json(self, ruta_archivo: str) -> tuple:
        # Crea carpeta si no existe (data/)
        ruta = Path(ruta_archivo)
        ruta.parent.mkdir(parents=True, exist_ok=True)

        data = [p.to_dict() for p in self._productos.values()]

        try:
            ruta.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            return (True, f"Inventario guardado en {ruta}")
        except OSError as e:
            return (False, f"No se pudo guardar el archivo: {e}")

    def cargar_desde_json(self, ruta_archivo: str) -> tuple:
        ruta = Path(ruta_archivo)

        # Si no existe, no es falla: inicia vacío
        if not ruta.exists():
            return (False, "No existe inventario.json todavía. Se iniciará vacío.")

        try:
            contenido = ruta.read_text(encoding="utf-8").strip()
            data = json.loads(contenido) if contenido else []
        except (OSError, json.JSONDecodeError) as e:
            return (False, f"No se pudo cargar el archivo: {e}")

        self._productos.clear()
        self._ids.clear()

        for item in data:
            prod = Producto.from_dict(item)
            pid = prod.get_id()

            if pid and pid not in self._ids:
                self._productos[pid] = prod
                self._ids.add(pid)

        return (True, f"Inventario cargado. Productos: {len(self._productos)}")