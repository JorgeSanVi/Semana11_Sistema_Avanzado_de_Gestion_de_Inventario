class Producto:
    def __init__(self, producto_id: str, nombre: str, cantidad: int, precio: float):
        # Guardamos datos limpios (sin espacios extra)
        self._id = str(producto_id).strip()
        self._nombre = str(nombre).strip()
        self._cantidad = int(cantidad)
        self._precio = float(precio)

        # Validaciones básicas para no guardar valores incorrectos
        if not self._id:
            raise ValueError("El ID no puede estar vacío.")
        if not self._nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if self._cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        if self._precio < 0:
            raise ValueError("El precio no puede ser negativo.")

    # Obtener datos (getters)
    def get_id(self) -> str:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def get_cantidad(self) -> int:
        return self._cantidad

    def get_precio(self) -> float:
        return self._precio

    # Modificar datos (setters) con control simple
    def set_nombre(self, nombre: str) -> None:
        nombre = str(nombre).strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre

    def set_cantidad(self, cantidad: int) -> None:
        cantidad = int(cantidad)
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = cantidad

    def set_precio(self, precio: float) -> None:
        precio = float(precio)
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = precio

    # Para guardar el producto en inventario.json
    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    # Para reconstruir el producto cuando se carga el JSON
    @staticmethod
    def from_dict(data: dict) -> "Producto":
        return Producto(
            data.get("id", ""),
            data.get("nombre", ""),
            data.get("cantidad", 0),
            data.get("precio", 0.0)
        )

    def __str__(self) -> str:
        # Forma simple de mostrar el producto en consola
        return f"{self._id} | {self._nombre} | {self._cantidad} | ${self._precio:.2f}"