# Semana 11 – Sistema de Gestión de Inventario (POO + JSON)

## Descripción
En este proyecto desarrollé un sistema de inventario para una tienda usando POO. A través de un menú en consola puedo **agregar, buscar, actualizar, eliminar y mostrar** productos. Cada producto maneja datos básicos: **ID (único), nombre, cantidad y precio**.

## ¿Por qué usé JSON?
En clase trabajamos el CRUD guardando la información en colecciones mientras el programa está ejecutándose. En mi caso, además de eso, usé **JSON** porque la guía pide **guardar y cargar** el inventario desde un archivo. Así, cuando cierro el programa, los productos **no se borraran**: se guardan en `data/inventario.json` y al volver a ejecutar el sistema se cargan automáticamente para continuar con el mismo inventario.

## Colecciones usadas
- **Diccionario (`dict`)**: guardo los productos por ID, lo que ayuda a encontrarlos de una manera mnas rapida, sencilla y puedo modificarlos sin complicarme.  
- **Conjunto (`set`)**: lo uso para asegurar que no existan IDs repetidos.  
- **Lista (`list`)**: me sirve para mostrar el inventario completo y para presentar los resultados cuando busco por nombre.  

## Archivos del proyecto
- `producto.py`: clase **Producto**  
- `inventario.py`: clase **Inventario** (maneja las colecciones y el archivo JSON)  
- `main.py`: menú e interacción con el usuario  
- `data/inventario.json`: archivo donde queda guardado el inventario  

## Ejecución
`python main.py`