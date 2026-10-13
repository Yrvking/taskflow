"""Demo del proyecto. Ejecutar con: python -m taskflow"""
from taskflow import GestorTareas, __version__


def mostrar(titulo, tareas):
    print(titulo)
    for tarea in tareas:
        estado = "[x]" if tarea.completada else "[ ]"
        print(f"  {estado} #{tarea.id} {tarea.titulo} ({tarea.prioridad})")


def main():
    gestor = GestorTareas()
    gestor.agregar("Configurar el repositorio en GitHub", "alta")
    gestor.agregar("Escribir el README", "media")
    gestor.agregar("Repasar el material de la clase", "baja")
    gestor.agregar("Revisar el PR de la pareja", "alta")
    gestor.completar(1)

    print(f"TaskFlow v{__version__}")
    mostrar("Todas las tareas:", gestor.listar())
    mostrar("Prioridad alta (TF-8):", gestor.filtrar_por_prioridad("alta"))
    mostrar("Búsqueda 'readme' (TF-9):", gestor.buscar_texto("readme"))

    r = gestor.resumen()
    print(f"Resumen (TF-10): {r['completadas']}/{r['total']} completadas · "
          f"{r['pendientes']} pendientes · {r['avance']} % de avance")

    try:
        gestor.agregar("  escribir el readme ")
    except ValueError as error:
        print(f"Duplicado rechazado (TF-11): {error}")


if __name__ == "__main__":
    main()
