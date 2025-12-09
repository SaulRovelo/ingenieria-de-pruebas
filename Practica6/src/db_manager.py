class DBManager:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    # --- Métodos para Clientes ---
    def add_cliente(self, nombre, correo):
        """Agrega un nuevo cliente verificando que el correo sea válido."""
        if "@" not in correo:
            raise ValueError("Correo inválido: debe contener '@'")
        self.cursor.execute(
            'INSERT INTO clientes (nombre, correo) VALUES (?, ?)', (nombre, correo)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_clientes(self):
        """Devuelve todos los clientes registrados"""
        self.cursor.execute('SELECT * FROM clientes')
        return self.cursor.fetchall()

    def delete_cliente(self, cliente_id):
        """Elimina un cliente por su ID"""
        self.cursor.execute('DELETE FROM clientes WHERE id=?', (cliente_id,))
        self.conn.commit()

    # --- Métodos para Libros ---
    def add_libro(self, titulo, precio):
        """Agrega un libro nuevo si el precio es válido"""
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser un número positivo")
        self.cursor.execute(
            'INSERT INTO libros (titulo, precio) VALUES (?, ?)', (titulo, precio)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_libros(self):
        """Devuelve todos los libros registrados"""
        self.cursor.execute('SELECT * FROM libros')
        return self.cursor.fetchall()

    def delete_libro(self, libro_id):
        """Elimina un libro por su ID"""
        self.cursor.execute('DELETE FROM libros WHERE id=?', (libro_id,))
        self.conn.commit()

    # --- Métodos para Compras ---
    def registrar_compra(self, cliente_id, libro_id, fecha):
        """Registra una compra si los IDs existen"""
        # Verificar existencia del cliente y libro
        self.cursor.execute("SELECT id FROM clientes WHERE id=?", (cliente_id,))
        if not self.cursor.fetchone():
            raise ValueError("El cliente no existe")

        self.cursor.execute("SELECT id FROM libros WHERE id=?", (libro_id,))
        if not self.cursor.fetchone():
            raise ValueError("El libro no existe")

        # Insertar compra
        self.cursor.execute(
            'INSERT INTO compras (cliente_id, libro_id, fecha) VALUES (?, ?, ?)',
            (cliente_id, libro_id, fecha)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_compras(self):
        """Devuelve todas las compras registradas"""
        self.cursor.execute(
            'SELECT c.id, cl.nombre, l.titulo, c.fecha \
             FROM compras c \
             JOIN clientes cl ON c.cliente_id = cl.id \
             JOIN libros l ON c.libro_id = l.id'
        )
        return self.cursor.fetchall()

    def delete_compra(self, compra_id):
        """Elimina una compra por su ID"""
        self.cursor.execute('DELETE FROM compras WHERE id=?', (compra_id,))
        self.conn.commit()