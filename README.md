# TaskFlow  ![CI](https://github.com/Yrvking/taskflow/actions/workflows/ci.yml/badge.svg)

Gestor de tareas en Python · Proyecto integrador DevOps & Project Management.

Sitio: https://yrvking.github.io/taskflow/ · Jira: https://yrving333.atlassian.net (proyecto TF)

## Equipo

- Yrving Leon — @Yrvking (yrvingleon@hotmail.com)
- Modalidad: trabajo individual (sin pareja de revisión)

## Funcionalidades (con la clave de Jira de cada una)

| Funcionalidad | Método | Jira |
|---------------|--------|------|
| Agregar, completar y listar tareas con prioridad | `agregar()`, `completar()`, `listar()` | TF-4 |
| Eliminar tareas por id (sin reutilizar ids) | `eliminar()` | TF-5 |
| Filtrar tareas por prioridad | `filtrar_por_prioridad()` | TF-8 |
| Buscar tareas por texto (ignora mayúsculas) | `buscar_texto()` | TF-9 |
| Resumen de avance (total, completadas, pendientes, %) | `resumen()` | TF-10 |
| Rechazo de títulos duplicados | `agregar()` | TF-11 |

## Cómo ejecutarlo y probarlo

```bash
python -m venv .venv
source .venv/bin/activate        # Windows (Git Bash): source .venv/Scripts/activate
pip install -r requirements.txt
python -m taskflow               # demo con filtro, búsqueda y resumen
python -m pytest -v              # 17 passed
```

## Flujo de trabajo

- Estrategia: GitHub Flow · merge: squash · `main` protegida (ruleset `proteger-main`)
- Convenciones: ramas `tipo/TF-n-descripcion`, Conventional Commits, PRs con plantilla
- Ruleset: PR obligatorio (0 aprobaciones requeridas por trabajo individual, como indica la Clase 2), checks `test (3.11)`, `test (3.12)`, `test (3.13)` requeridos y actualizados, sin force push ni borrado

## CI/CD

- `ci.yml`: pruebas en Python 3.11–3.13 en cada PR y push a `main`
- `deploy.yml`: pruebas + publicación en GitHub Pages en cada merge a `main`

## Gestión ágil

- Épicas: TF-1 Gestión de tareas · TF-2 Calidad y automatización · TF-3 Visibilidad del proyecto
- Sprint 0 (Hitos 1 y 2): TF-4 a TF-7 · velocity **11 pts**
- Sprint 1 · Goal: *"Encontrar tareas rápido y conocer el avance"* · TF-8, TF-9, TF-10, TF-11 · comprometido 13 / terminado 13 · velocity **13 pts**
- Burndown y sprint report: ver `docs/evidencias/`
- Backlog importable: [`jira/backlog_taskflow.csv`](jira/backlog_taskflow.csv) · guía: [`jira/GUIA_JIRA.md`](jira/GUIA_JIRA.md)

## Evidencias

| PR | Título | Jira |
|----|--------|------|
| [#2](https://github.com/Yrvking/taskflow/pull/2) | docs: describe el proyecto en el README | — |
| [#3](https://github.com/Yrvking/taskflow/pull/3) | docs: agrega plantilla de pull request | — |
| [#4](https://github.com/Yrvking/taskflow/pull/4) | ci: ejecuta pruebas en cada pull request | TF-6 |
| [#5](https://github.com/Yrvking/taskflow/pull/5) | feat: permite eliminar tareas por id | TF-5 |
| [#6](https://github.com/Yrvking/taskflow/pull/6) | ci: publica el sitio del proyecto en GitHub Pages | TF-7 |
| [#7](https://github.com/Yrvking/taskflow/pull/7) | docs: marca el Hito 2 como completo y agrega evidencias | — |
| [#8](https://github.com/Yrvking/taskflow/pull/8) | docs: actividades de clase y backlog de Jira | — |
| [#9](https://github.com/Yrvking/taskflow/pull/9) | TF-11 fix: rechaza tareas con títulos duplicados | TF-11 |
| [#10](https://github.com/Yrvking/taskflow/pull/10) | TF-8 feat: filtrar tareas por prioridad | TF-8 |
| [#11](https://github.com/Yrvking/taskflow/pull/11) | TF-9 feat: buscar tareas por texto | TF-9 |
| [#12](https://github.com/Yrvking/taskflow/pull/12) | TF-10 feat: resumen de avance | TF-10 |
| [#13](https://github.com/Yrvking/taskflow/pull/13) | TF-15 docs: cierre del Sprint 1 y versión 1.0.0 | TF-15 |

- Workflows: https://github.com/Yrvking/taskflow/actions
- Releases: [v0.2.0](https://github.com/Yrvking/taskflow/releases/tag/v0.2.0) · [v1.0.0](https://github.com/Yrvking/taskflow/releases/tag/v1.0.0)
- Capturas: [`docs/evidencias/`](docs/evidencias/)
- Actividades de clase resueltas: [`actividades/`](actividades/)

## Retrospectiva del Sprint 1

| Mantener | Mejorar | Acción (clave Jira) |
|----------|---------|---------------------|
| Escribir primero las pruebas a partir de los criterios de aceptación | Los PRs esperaban revisión y se acumulaban en In Review | Revisar PRs cada mañana antes de programar (TF-16) |
| PRs pequeños, uno por elemento, con la clave de Jira | Algunas tarjetas se movían tarde en el tablero | Activar las reglas de automatización rama → In Progress y PR fusionado → Done |
| CI con matrix como red de seguridad antes de cada merge | — | — |

## Lecciones aprendidas

- Proteger `main` con un ruleset cambia el hábito: todo cambio pasa por PR, revisión y CI.
- Los criterios Dado/Cuando/Entonces se traducen casi literalmente en pruebas automáticas: ese es el puente entre Jira y GitHub Actions.
- Incluir la clave de Jira en ramas, commits y PRs da trazabilidad completa desde el requerimiento hasta el sitio publicado.
- Velocity se calcula con lo terminado, no con lo comprometido.
