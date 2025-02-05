"""
TIENDA DE PRODUCTOS
Crea una superclase Producto con:
• Un atributo nombre.
• Un método mostrar_info() que imprime el nombre del producto.

Crea las siguientes subclases:
• Electrónica: Agrega un atributo marca y muestra la información del producto con su marca.
• Ropa: Agrega un atributo talla y muestra la información con la talla incluida.
• Libro: Agrega un atributo autor y muestra el autor junto con el nombre del libro.

Objetivo: Implementa la herencia correctamente.
• Usa super().__init__() para llamar al constructor de la superclase.
• Crea una lista con diferentes productos y muestra su información.
"""

# Superclase Producto
class Producto:
    def __init__(self, nombre):
        self.nombre = nombre.title()
    
    def mostrar_info(self):
        return f'Nombre del producto: "{self.nombre}".'
    
# Subclase Electrónica - Contiene el atributo nombre de la superclase Producto y el atributo marca de esta subclase
class Electrónica(Producto):
    def __init__(self, nombre, marca):
        super().__init__(nombre)
        self.marca = marca.title()

# Reutiliza la función mostrar_info() de la superclase Producto más un mensaje personalizado para esta subclase
    def mostrar_info(self):
        return f'{super().mostrar_info()}\nEste producto es de marca "{self.marca}".\n'
    
# Subclase Ropa - Contiene el atributo nombre de la superclase Producto y el atributo talla de esta subclase
class Ropa(Producto):
    def __init__(self, nombre, talla):
        super().__init__(nombre)
        self.talla = talla.upper()
        
# Reutiliza la función mostrar_info() de la superclase Producto más un mensaje personalizado para esta subclase
    def mostrar_info(self):
        return f'{super().mostrar_info()}\nEsta prenda es de talla {self.talla}.\n'
    
# Subclase Libro - Contiene el atributo nombre de la superclase Producto y el atributo autor de esta subclase
class Libro(Producto):
    def __init__(self, nombre, autor):
        super().__init__(nombre)
        self.autor = autor.title()
        
# Reutiliza la función mostrar_info() de la superclase Producto más un mensaje personalizado para esta subclase
    def mostrar_info(self):
        return f'{super().mostrar_info()}\n"{self.nombre}" es un libro del autor {self.autor}.\n'
    
# Función que contiene un título principal y una lista de productos utilizando la lógica de las subclases
def listado_productos():
    print('\nCatálogo de productos:\n')
    return [
        Electrónica('Galaxy S25 Ultra', 'Samsung'),
        Ropa('Vestido One Shoulder Kaia', 'L'),
        Libro('Acerca de Roderer', 'Guillermo Martinez')
    ]
    
# Bucle que recorre el listado de productos de la función listado_productos() e imprime su respectiva información
for producto in listado_productos():
    print(producto.mostrar_info())
    
# Mensaje de cierre
print('Estos han sido los productos disponibles en nuestro catálogo. Adiós 👋\n')