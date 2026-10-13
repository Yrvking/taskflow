# Clase 3 · Requerimientos con Jira y entrega final — Resolución de actividades

Autor: Yrving Leon (@Yrvking)

## Mini-check de conceptos (Descubre)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Diferencia Scrum vs Kanban en Jira | **Scrum trabaja con backlog y sprints; Kanban con flujo continuo sin sprints.** |
| 2 | Escalón hacia arriba en el burndown | **Se agregó trabajo después de iniciar el sprint (scope creep).** |
| 3 | Banda "In Review" que se ensancha en el CFD | **Cuello de botella en la revisión de código.** |
| 4 | Campo que asocia historia con épica | **Parent** (reemplazó a Epic Link). |
| 5 | Anti-patrón con story points | **Usarlos como KPI de productividad individual.** |
| 6 | "Como usuario quiero que la app sea mejor" incumple… | **Estimable y Testeable.** |

## Reto 1 · Del pedido vago a historias de usuario

**Requerimientos funcionales detectados:** encontrar rápido lo importante (filtrar por prioridad y buscar por texto), saber cuánto se ha avanzado, evitar tareas duplicadas y mostrar el avance en la página del proyecto.

**No funcionales implícitos:** la búsqueda debe ignorar mayúsculas/minúsculas (usabilidad) y debe seguir respondiendo bien con muchas tareas (rendimiento).

| Épica | Elemento | Tipo |
|-------|----------|------|
| Gestión de tareas | Como usuario quiero filtrar mis tareas por prioridad para atender primero lo urgente. | Historia (TF-8) |
| Gestión de tareas | Como usuario quiero buscar tareas por una palabra del título para encontrarlas sin recorrer toda la lista. | Historia (TF-9) |
| Gestión de tareas | El sistema acepta dos tareas con el mismo título ("Preparar demo"). | **Bug** (TF-11) |
| Visibilidad del proyecto | Como usuario quiero ver cuántas tareas llevo completadas y el porcentaje de avance para saber cómo voy. | Historia (TF-10) |
| Visibilidad del proyecto | Como coordinadora quiero ver el avance en la página del proyecto para no tener que abrir el código. | Historia (TF-12) |

Verificación INVEST: todas son independientes entre sí, describen la necesidad y no la solución, aportan valor visible, son estimables, caben en un sprint y tienen criterios verificables.

**Criterios de aceptación · TF-9 Buscar por texto**

```text
DADO que tengo las tareas "Escribir README" y "Preparar demo"
CUANDO busco "readme"
ENTONCES veo solo "Escribir README" (la búsqueda ignora mayúsculas)

DADO cualquier lista de tareas
CUANDO busco un texto vacío o solo espacios
ENTONCES el sistema me indica que debo escribir un texto
```

**¿Algún pedido es un bug?** Sí: "se me duplican cosas" describe un defecto del comportamiento actual, no una funcionalidad nueva.

## Reto 2 · Planning poker (referencia: "Eliminar tarea por id" = 2 pts)

| Elemento | Estimación | Razonamiento |
|----------|-----------:|--------------|
| Filtrar tareas por prioridad | **3** | Similar a eliminar, más validación de prioridad y 3 pruebas. |
| Buscar por texto (sin mayúsculas) | **3** | Lógica simple pero con normalización y caso de texto vacío. |
| Resumen de avance (total, completadas, pendientes, %) | **5** | Varios cálculos, redondeo y caso borde de división entre cero. |
| Bug: títulos duplicados | **2** | Un cambio pequeño en `agregar()` y una prueba. |
| Mostrar el resumen en el sitio web | **5** | Toca HTML y el flujo de despliegue; incertidumbre sobre cómo llevar los datos al sitio. |
| Guardar las tareas en un archivo y recuperarlas | **8** | Mayor incertidumbre: formato (JSON/CSV), archivo corrupto, ruta. Si llegara a 13, dividir en "guardar" y "cargar". |

## Reto 3 · Simulación de una semana de sprint

1. **Día 1:** empezar **TF-11** (bug pequeño, valor inmediato) y **TF-8**: no dependen entre sí. TF-10 es la más grande; conviene empezarla en cuanto haya capacidad.
2. **Día 2:** **no** empezar un tercer elemento: con WIP 2 la regla es terminar antes de empezar. Esa persona debe ayudar revisando PRs.
3. **Día 3:** el cuello de botella es **In Review**. Acción: revisar PRs cada mañana antes de programar.
4. **Día 4:** "Guardar en archivo" (8 pts) **no se acepta**: pondría en riesgo el Sprint Goal. Va al Product Backlog para el siguiente planning. Si se aceptara, el burndown mostraría un escalón hacia arriba.
5. **Día 5:** al completar el sprint, TF-10 se mueve **al siguiente sprint o al backlog**; no se marca como terminada ni se divide a última hora para aparentar avance.

## Reto 4 · Lectura de gráficos

1. Patrón "todo se termina el último día": **Sprint B** (línea plana y caída al final). Acción de retro: dividir historias de más de 5 puntos y revisar PRs a diario.
2. Se agregó trabajo durante el sprint: **Sprint C** (escalón hacia arriba y no llega a cero). Acción: proteger el Sprint Goal; los pedidos nuevos van al backlog.
3. Sprint saludable: **Sprint A** (sigue la línea ideal y llega a cero).
4. Comprometido 20, 24, 18 y terminado 16, 17, 15 → **comprometer ≈ 16 puntos**: velocity = (16 + 17 + 15) / 3 = 16. Se planifica con lo terminado, no con lo comprometido.

## Reto 5 · ¿Scrum o Kanban?

| Equipo | Recomendación | Motivo |
|--------|---------------|--------|
| Mesa de ayuda TI | **Kanban** | Trabajo impredecible: flujo continuo, límites WIP y foco en lead time. |
| Equipo de nueva app | **Scrum** | PO dedicado, demos quincenales: cadencia, Sprint Goal y reviews. |
| Equipo de datos | **Scrumban** o Scrum con ~20 % de capacidad reservada para imprevistos (o dos tableros) | Mezcla trabajo planificable con pedidos sin aviso. |

## Hito 3 (Aplica)

- Backlog listo para importar: [`jira/backlog_taskflow.csv`](../jira/backlog_taskflow.csv) y guía paso a paso en [`jira/GUIA_JIRA.md`](../jira/GUIA_JIRA.md).
- Código del Sprint 1 (TF-8 a TF-11) con 8 pruebas nuevas en `tests/test_sprint1.py`; total 17 pruebas.
- Ramas, commits y PRs con la clave de Jira (`feature/TF-8-filtrar-prioridad`, etc.) para la trazabilidad.
- Retrospectiva y lecciones aprendidas en el README final.
