# Semana 11 – Sistema Avanzado de Gestión de Inventario (POO + JSON)

## 1. Descripción
En este proyecto desarrollé un sistema de inventario para una tienda usando **Programación Orientada a Objetos**.  
El programa permite registrar productos, consultarlos y mantener la información guardada en un archivo **JSON**, para que los datos no se pierdan al cerrar el sistema.

## 2. Relación con el tema de estudio (Semana 11)
Este trabajo se basa en el contenido de la Semana 11 sobre **colecciones en Python**, aplicándolas en un caso real:

- **Diccionario (`dict`)**: almacena los productos por **ID** para encontrarlos rápido.
- **Conjunto (`set`)**: ayuda a evitar **IDs repetidos**.
- **Lista (`list`)**: se usa para mostrar el inventario y devolver resultados de búsquedas.

## 3. Funcionalidades del sistema
Desde el menú en consola se puede:
1. **Añadir** productos (ID, nombre, cantidad, precio)
2. **Eliminar** productos por ID
3. **Actualizar** cantidad y/o precio
4. **Buscar** por nombre (coincidencia parcial)
5. **Mostrar** todo el inventario
6. **Guardar** inventario en `data/inventario.json`
0. **Salir** (guardando antes de cerrar)

## 4. Estructura del proyecto
- `producto.py`: clase **Producto** (modelo del producto).
- `inventario.py`: clase **Inventario** (gestiona colecciones y el archivo JSON).
- `main.py`: menú interactivo (interfaz por consola).
- `data/inventario.json`: archivo donde se guarda el inventario (persistencia).

## 5. Cómo ejecutar
1. Abre la carpeta del proyecto en VSCode.
2. En la terminal ejecuta:
   - `python main.py`
3. Usa el menú para operar el inventario.

## 6. Notas finales
- Si `data/inventario.json` no existe, el sistema inicia con inventario vacío y lo crea al guardar.
- Se incluyeron **comentarios en el código** para explicar la lógica y facilitar la revisión.
