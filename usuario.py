class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
<<<<<<< HEAD
        self.tareas.append(tarea)

def listarTareas(self):
   for tarea in self.tareas:
       if tarea.estaLista():
           print(f"La tarea {tarea.obtenerNombre()} está lista")
           print(f"La tarea {tarea.obtenerNombre()} no está lista")
=======
        self.tareas.append(tarea)
>>>>>>> 378ccc57e5ce0c75be926eddc77451bd4644cc48
