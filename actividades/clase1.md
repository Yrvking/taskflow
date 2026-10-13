# Clase 1 · Introducción a DevOps y Git/GitHub — Resolución de actividades

Autor: Yrving Leon (@Yrvking · yrvingleon@hotmail.com)

## Mini-check de conceptos (Descubre)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Afirmación correcta sobre Git y GitHub | **Git es el sistema de control de versiones; GitHub es una plataforma que aloja repositorios Git.** Git funciona en local; GitHub agrega nube y colaboración. |
| 2 | Comando que pasa cambios del working directory al staging | **`git add`** (`commit` guarda en el historial, `push` sube al remoto). |
| 3 | Equipo que despliega una vez al trimestre y tarda días en recuperarse | **Mejorar frecuencia de despliegue y tiempo de recuperación** (dos métricas DORA). |
| 4 | Versionar datos, modelos e hiperparámetros | **MLOps.** |

## Reto 1 · Caso RápidoPay

### Métricas DORA estimadas

| Métrica | RápidoPay | Nivel |
|---------|-----------|-------|
| Frecuencia de despliegue | ~1 cada 6 semanas | Baja |
| Lead time de cambios | Hasta 6 semanas o más (un commit espera al siguiente .zip) | Bajo |
| Tasa de fallo de cambios | ~33 % (1 de cada 3 despliegues) | Alta (mala) |
| Tiempo de recuperación | ~2 días | Bajo |

### Problemas, clasificación y práctica propuesta

| Problema | Tipo | Práctica DevOps | Herramienta del curso |
|----------|------|-----------------|------------------------|
| Código en carpeta compartida con `app_final_v3_ahora_si.zip` | Proceso | Control de versiones con ramas, PRs y revisión | Git + GitHub (Hito 1–2) |
| QA manual solo la semana previa | Automatización | Integración continua: pruebas automáticas en cada cambio | GitHub Actions (CI) |
| Despliegue manual de 40 pasos un sábado | Automatización | Despliegue automatizado y repetible desde `main` | GitHub Actions (CD) |
| "En mi máquina funciona" vs "el código vino roto" | Cultura | Responsabilidad compartida y post-mortems sin culpables | Issues / Jira para seguimiento |
| Lotes de 6 semanas | Proceso | Entregas pequeñas y frecuentes en sprints cortos | Jira (Scrum) |
| No saben por qué fallan ni cuánto tardan | Medición | Monitoreo y medición continua de métricas DORA | Dashboards, reportes de Jira y Actions |

### Si solo pudieran hacer un cambio este mes

Llevar todo el código a Git y ejecutar pruebas automáticas en cada cambio (CI). Es la base del resto: sin pruebas automáticas, desplegar más seguido solo multiplicaría los incidentes. Con CI, la tasa de fallo baja y se habilita después el despliegue continuo.

## Reto 2 · ¿DevOps, MLOps o DataOps?

| Escenario | Respuesta | Motivo |
|-----------|-----------|--------|
| A. Modelo de recomendación pierde precisión; reentrenar cada semana | **MLOps** | Deriva del modelo y reentrenamiento automático |
| B. Reporte con cifras duplicadas por carga doble nocturna | **DataOps** | Confiabilidad de un pipeline de datos |
| C. Cada PR ejecuta pruebas y al fusionar despliega la API | **DevOps** | CI/CD de software |
| D. Saber con qué versión de datos e hiperparámetros se entrenó el modelo | **MLOps** | Trazabilidad de experimentos y modelos |
| E. Servidores creados a mano; definirlos con archivos versionados | **DevOps** | Infraestructura como código |
| F. Validar nulos, rangos y esquema antes de publicar una tabla | **DataOps** | Pruebas de calidad de datos |

## Reto 3 · Recorrido por `pallets/flask` (consultado el 13/10/2026)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Última versión publicada | **3.1.3**, publicada el 19/02/2026 (la anterior, 3.1.2, es de agosto de 2025). |
| 2 | Issues abiertos | El número varía a diario; se revisa en la pestaña *Issues*. Los issues de Flask usan etiquetas (por ejemplo `bug`, `docs`) y muestran autor y fecha. |
| 3 | PR cerrado y fusionado | Los PRs fusionados de Flask muestran revisión de un mantenedor y los checks de los workflows *Tests* y *pre-commit*. |
| 4 | Workflows de GitHub Actions | `tests.yaml` (se dispara con `pull_request` y con `push` a `main`/`stable`, ignorando cambios solo en `docs/` y README), `pre-commit.yaml` (`pull_request` y `push`), `publish.yaml` (`push` de tags: publica la versión) y `lock.yaml` (`schedule` diario con cron: bloquea issues cerrados inactivos). |
| 5 | Qué pide a quien contribuye | La guía de contribución está en la documentación del proyecto (sección *Contributing*): discutir el cambio en un issue, trabajar en una rama, agregar pruebas y documentación, y pasar `pre-commit` y las pruebas. |
| 6 | Formato de los commits | Mensajes cortos en imperativo en inglés; no siguen estrictamente Conventional Commits. |

Observación: las actions de Flask están fijadas por SHA (`actions/checkout@<sha> # v7.0.1`), una buena práctica de seguridad de la cadena de suministro.

## Reto 4 · Git en vivo (sandbox)

La práctica se ejecutó completa; la salida real está en [`sandbox-git.txt`](sandbox-git.txt).

Respuestas a las preguntas de discusión:

1. **¿Por qué `untracked` tras el paso 2?** Git ve el archivo pero todavía no lo sigue: nunca pasó por el staging.
2. **¿`git commit` sin `git add`?** Git responde "nothing added to commit": solo confirma lo que está en staging (salvo `git commit -a` sobre archivos ya seguidos).
3. **El código de 7 caracteres en `git log --oneline`** es el inicio del hash SHA del commit, su identificador único.
4. **¿Por qué `git restore` es peligroso?** Descarta cambios del working directory que no estaban confirmados y Git no puede recuperarlos.

## Hito 1 (Aplica)

Resuelto en este repositorio: código base, 6 pruebas, README y commits con Conventional Commits. Los pasos de cuenta, 2FA y clave SSH se ejecutan con `scripts/00_preparar_entorno.sh`.
