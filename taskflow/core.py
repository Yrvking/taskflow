"""Lógica principal de TaskFlow."""
from dataclasses import dataclass

PRIORIDADES = ("baja", "media", "alta")


@dataclass
class Tarea:
    id: int
    titulo: str
    prioridad: str = "media"
    completada: bool = False


class GestorTareas:
    """Guarda las tareas en memoria y aplica las reglas del negocio."""

    def __init__(self):
        self._tareas = []
        self._siguiente_id = 1

    def agregar(self, titulo, prioridad="media"):
        titulo = titulo.strip()
        if not titulo:
            raise ValueError("El título no puede estar vacío")
        if prioridad not in PRIORIDADES:
            raise ValueError(f"Prioridad inválida: {prioridad}")
        if any(t.titulo.lower() == titulo.lower() for t in self._tareas):
            raise ValueError(f"Ya existe una tarea llamada '{titulo}'")
        tarea = Tarea(self._siguiente_id, titulo, prioridad)
        self._tareas.append(tarea)
        self._siguiente_id += 1
        return tarea

    def completar(self, tarea_id):
        tarea = self.buscar(tarea_id)
        tarea.completada = True
        return tarea

    def listar(self, solo_pendientes=False):
        if solo_pendientes:
            return [t for t in self._tareas if not t.completada]
        return list(self._tareas)

    def filtrar_por_prioridad(self, prioridad):
        """TF-8: tareas con la prioridad indicada, en orden de creación."""
        if prioridad not in PRIORIDADES:
            raise ValueError(f"Prioridad inválida: {prioridad}")
        return [t for t in self._tareas if t.prioridad == prioridad]

    def buscar_texto(self, texto):
        """TF-9: tareas cuyo título contiene el texto (ignora mayúsculas)."""
        texto = texto.strip().lower()
        if not texto:
            raise ValueError("El texto de búsqueda no puede estar vacío")
        return [t for t in self._tareas if texto in t.titulo.lower()]

    def resumen(self):
        """TF-10: total, completadas, pendientes y porcentaje de avance."""
        total = len(self._tareas)
        completadas = sum(1 for t in self._tareas if t.completada)
        avance = round(completadas * 100 / total) if total else 0
        return {
            "total": total,
            "completadas": completadas,
            "pendientes": total - completadas,
            "avance": avance,
        }

    def eliminar(self, tarea_id):
        tarea = self.buscar(tarea_id)   # lanza KeyError si no existe
        self._tareas.remove(tarea)
        return tarea

    def buscar(self, tarea_id):
        for tarea in self._tareas:
            if tarea.id == tarea_id:
                return tarea
        raise KeyError(f"No existe la tarea {tarea_id}")
