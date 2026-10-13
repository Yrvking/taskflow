# Guía Jira · Proyecto TaskFlow (Hito 3)

Cuenta: yrvingleon@hotmail.com · GitHub: @Yrvking · Clave del proyecto: **TF**

## 1. Sitio y proyecto

1. Entra a <https://www.atlassian.com/software/jira/free> y usa **Continuar con GitHub** (cuenta Yrvking) o el correo yrvingleon@hotmail.com.
2. Nombre del sitio sugerido: `yrvingleon-devops.atlassian.net`.
3. **Crear proyecto → Desarrollo de software → Scrum → Team-managed**. Nombre `TaskFlow`, clave `TF`.
4. **Board → … → Configurar tablero**: columnas `To Do → In Progress → In Review → Done` (crea `In Review` con categoría *En curso*).
5. Verifica que las historias tengan el campo **Story point estimate**.
6. **Configuración del proyecto → Acceso → Agregar personas**: tu pareja y el docente.

## 2. Backlog (importar en 2 minutos)

**Opción A · Importar CSV** (recomendado)

1. Menú de Jira → **Filtros / Elementos → Importar elementos desde CSV** (o *Configuración del sistema → Importación externa → CSV*).
2. Sube `jira/backlog_taskflow.csv`, proyecto **TaskFlow (TF)**.
3. Mapeo de columnas:

| Columna CSV | Campo de Jira |
|-------------|---------------|
| Issue ID | Issue ID |
| Issue Type | Tipo de elemento (Issue Type) |
| Summary | Resumen |
| Description | Descripción |
| Story point estimate | Story point estimate |
| Parent | Parent (principal) |

4. Importa. Como las filas van en orden, las claves quedan **TF-1 … TF-16** igual que en la guía del curso.

**Opción B · Manual:** crea los elementos en el mismo orden del CSV y asigna a cada uno su épica con **Agregar principal**.

| Clave | Tipo | Resumen | Parent | Pts | Sprint |
|-------|------|---------|--------|----:|--------|
| TF-1 | Épica | Gestión de tareas | — | — | — |
| TF-2 | Épica | Calidad y automatización | — | — | — |
| TF-3 | Épica | Visibilidad del proyecto | — | — | — |
| TF-4 | Historia | Agregar, completar y listar tareas con prioridad | TF-1 | 3 | Sprint 0 ✓ |
| TF-5 | Historia | Eliminar tareas por id | TF-1 | 2 | Sprint 0 ✓ |
| TF-6 | Tarea | Pipeline de CI con pruebas en 3 versiones de Python | TF-2 | 3 | Sprint 0 ✓ |
| TF-7 | Tarea | Publicar el sitio del proyecto en GitHub Pages | TF-3 | 3 | Sprint 0 ✓ |
| TF-8 | Historia | Filtrar tareas por prioridad | TF-1 | 3 | Sprint 1 |
| TF-9 | Historia | Buscar tareas por texto | TF-1 | 3 | Sprint 1 |
| TF-10 | Historia | Resumen de avance | TF-3 | 5 | Sprint 1 |
| TF-11 | Bug | Se aceptan tareas con títulos duplicados | TF-1 | 2 | Sprint 1 |
| TF-12 | Historia | Mostrar el avance del proyecto en el sitio web | TF-3 | 5 | Backlog |
| TF-13 | Tarea | Agregar lint con Ruff al CI | TF-2 | 2 | Backlog |
| TF-14 | Historia | Guardar las tareas en un archivo JSON | TF-1 | 8 | Backlog |
| TF-15 | Tarea | Cierre del Sprint 1: review, retro y release v1.0.0 | TF-3 | 1 | (después del sprint) |
| TF-16 | Tarea | Acción de retro: revisar PRs cada mañana | TF-2 | 1 | Sprint 2 |

## 3. Sprint 0 · Hitos 1 y 2

Backlog → **Crear sprint** → `Sprint 0 · Hitos 1 y 2` → arrastra TF-4 a TF-7 (11 pts) → **Iniciar sprint** → muévelos a Done → **Completar sprint**.

## 4. Conectar Jira con GitHub

1. Jira → **Aplicaciones → Explorar más aplicaciones → GitHub for Jira** (Atlassian, gratis) → Obtener.
2. **Conectar organización de GitHub** → autoriza → cuenta **Yrvking** → acceso al repositorio `taskflow`.
3. Tu `git config user.email` es `yrvingleon@hotmail.com`: debe ser el mismo correo de tu cuenta Atlassian para que funcionen los smart commits.
4. La app sincroniza el historial: las ramas, commits y PRs de TF-8 a TF-11 ya llevan la clave y aparecerán en el panel **Desarrollo**.

## 5. Sprint 1

- Crear **Sprint 1**, arrastrar TF-8, TF-9, TF-10, TF-11 (**13 pts**).
- Sprint Goal: **"Encontrar tareas rápido y conocer el avance"**. Duración: 1 semana.
- Definition of Ready: los 4 elementos tienen criterios de aceptación y estimación (ya vienen en el CSV).
- **Iniciar sprint** *antes* de ejecutar la fase Sprint 1 del script de publicación.

**Automatización opcional** (Configuración del proyecto → Automatización):

- Regla 1: *Rama creada* → transicionar el elemento a **In Progress**.
- Regla 2: *Pull request fusionado* → transicionar el elemento a **Done**.

Sin reglas, mueve las tarjetas a mano: rama creada → In Progress; PR abierto → In Review; merge → Done.

## 6. Cierre del sprint

1. **Completar sprint** cuando TF-8 a TF-11 estén en Done.
2. Capturas a guardar en `docs/evidencias/`: tablero final, Burndown, Sprint report, panel Desarrollo de TF-8 y backlog con épicas.
3. Crea TF-16 (acción de la retro) en el siguiente sprint.

## JQL útil

```text
project = TF AND sprint in openSprints()
project = TF AND parent = TF-1
project = TF AND type = Bug AND status != Done ORDER BY priority DESC
project = TF AND development[pullrequests].open > 0
```
