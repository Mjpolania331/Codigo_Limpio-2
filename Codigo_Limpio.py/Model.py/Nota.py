class Nota:
    def __init__(self, titulo, contenido, categoria):
        self.titulo = titulo
        self.contenido = contenido
        self.categoria = categoria
        self.fecha_creacion = self.obtener_fecha_actual()
        self.enlaces = []

    def obtener_fecha_actual(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def agregar_enlace(self, otra_nota):
        self.enlaces.append(otra_nota.titulo)

    def __str__(self):
        return f"Título: {self.titulo}\nContenido: {self.contenido}\nCategoría: {self.categoria}\nFecha: {self.fecha_creacion}\nEnlaces: {', '.join(self.enlaces)}"