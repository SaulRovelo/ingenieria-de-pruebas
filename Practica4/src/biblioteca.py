class Libro:
    def __init__(self, titulo, autor, paginas):
        if not isinstance(titulo, str) or not isinstance(autor, str):
            raise TypeError("Título y autor deben ser strings")
        if not isinstance(paginas, int) or paginas <= 0:
            raise ValueError("El número de páginas debe ser un entero positivo")
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def descripcion(self):
        return f"{self.titulo} por {self.autor}, {self.paginas} páginas"

class Usuario:
    def __init__(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un string")
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if not isinstance(libro, Libro):
            raise TypeError("Solo se puede prestar un objeto Libro")
        self.libros_prestados.append(libro)
        return f"{libro.titulo} prestado a {self.nombre}"

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            return f"{libro.titulo} devuelto por {self.nombre}"
        else:
            raise ValueError(f"{self.nombre} no tiene prestado {libro.titulo}")
