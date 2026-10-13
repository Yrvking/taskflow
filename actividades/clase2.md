# Clase 2 · GitHub: colaboración y CI/CD — Resolución de actividades

Autor: Yrving Leon (@Yrvking)

## Mini-check de conceptos (Descubre)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo llega un cambio a `main` en GitHub Flow? | **Mediante un Pull Request aprobado y con los checks en verde.** Con `main` protegida el push directo se rechaza. |
| 2 | Estrategia que deja un único commit por PR | **Squash and merge.** |
| 3 | Dos jobs sin `needs:` | **Se ejecutan en paralelo**, cada uno en su propio runner. |
| 4 | La función falla con lista vacía: prefijo | **bloqueante** (error funcional). |
| 5 | Entrega continua vs despliegue continuo | **En entrega continua el paso a producción requiere una aprobación manual**; el despliegue continuo lo automatiza también. |

## Reto 1 · Conflicto controlado en el sandbox

Ejecutado; salida real en [`sandbox-git.txt`](sandbox-git.txt). El conflicto apareció en `estado.md` (`UU`) y se resolvió combinando ambas versiones:

```text
Estado: listo para pruebas (versión 0.2)
```

Preguntas de cierre:

- **¿Por qué hubo conflicto?** Ambas ramas modificaron la misma línea desde el ancestro común; Git no puede decidir cuál es la correcta.
- **¿Qué muestra `--graph`?** Un commit de merge con dos padres: las dos historias se unen.
- **¿Cómo reducir conflictos?** Ramas cortas, PRs pequeños, `git pull` frecuente y coordinar quién toca qué archivo.

## Reto 2 · Revisión del PR #3 "feat: agrega eliminar y exportar tareas"

| Línea | Comentario |
|-------|-----------|
| 2–4 | **bloqueante:** se borra de la lista mientras se recorre con un `range` calculado al inicio; si la tarea no es la última, el índice se sale de rango (`IndexError`). Propuesta: `self._tareas.remove(self.buscar(tarea_id))`. |
| 5 | **bloqueante:** decrementar `_siguiente_id` hace que la próxima tarea reutilice un id existente → ids duplicados. Los ids no deben reutilizarse. |
| 2–5 | **pregunta:** si el id no existe la función no hace nada. ¿No debería lanzar `KeyError` como `buscar()`, por consistencia? |
| 11 | **bloqueante (seguridad):** se imprime un token en el código. Eliminarlo **y revocarlo**, porque ya quedó en el historial de Git. Los secretos van en variables de entorno o GitHub Secrets. |
| 8 | **sugerencia:** usar `with open(...)`; hoy el archivo nunca se cierra y queda abierto si ocurre un error. |
| 7 | **sugerencia:** `/tmp` no existe en Windows; recibir la ruta como parámetro obligatorio o usar `pathlib`. |
| 10 | **sugerencia:** si un título contiene comas el archivo queda mal formado; usar el módulo `csv`. |
| — | **bloqueante:** no hay pruebas. "Es poco código" no es razón: el CI no protegería estos cambios. |
| — | **sugerencia:** separar en dos PRs (eliminar / exportar): más fácil de revisar y de revertir. |
| 9 | **nit:** nombres de una letra (`f`, `t`); mejor `archivo` y `tarea`. |

**Decisión: Request changes** (4 bloqueantes, uno de seguridad). La implementación correcta de `eliminar()` está en `taskflow/core.py` con 3 pruebas (PR #3 del proyecto).

## Reto 3 · Workflow roto: 7 errores

1. `branch:` → debe ser **`branches:`**.
2. `pull_request` sin dos puntos → YAML inválido; debe ser **`pull_request:`**.
3. `runs-on: ubuntu` no es una etiqueta de runner válida → **`ubuntu-latest`**.
4. `actions/checkout` sin versión → **`actions/checkout@v5`**.
5. Bajo `with:` falta indentar `python-version` (2 espacios más).
6. La última línea usa **tabulación**; YAML solo admite espacios.
7. `run: pytest` no agrega la raíz del repo al path → `ModuleNotFoundError: taskflow`; usar **`python -m pytest`**.

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - name: Instalar Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: python -m pytest
```

Los errores 1, 2, 5 y 6 los detecta GitHub antes de ejecutar ("Invalid workflow file"); 3, 4 y 7 solo aparecen al correr.

## Reto 4 · ¿Qué estrategia de ramas recomiendo?

| Caso | Estrategia | Justificación |
|------|-----------|---------------|
| **NubeFact** (SaaS, 6 devs, varios despliegues al día) | **GitHub Flow** | Un solo producto, despliegue continuo y equipo pequeño. |
| **GeoLib** (mantiene 2.x y 3.x) | **Git Flow** o ramas de mantenimiento `release/2.x` y `release/3.x` | Necesita varias versiones vivas y parches en ambas. |
| **BancoAndino** (app móvil mensual con certificación) | **GitHub Flow + feature flags**, o ramas de release cortas si la certificación lo exige | Permite corregir urgencias sin publicar funciones a medio terminar. Caso debatible. |

## Reto 5 · Leer una ejecución fallida de Actions

- El log muestra `FAILED tests/test_core.py::test_agregar_rechaza_titulo_vacio` con `Failed: DID NOT RAISE ValueError`: la prueba esperaba una excepción al agregar un título vacío y el código ya no la lanza, porque se eliminó la validación.
- El botón de merge queda bloqueado porque el ruleset exige los checks `test (3.11/3.12/3.13)`.
- **Sin CI** el bug habría llegado a `main` y al sitio publicado, subiendo la tasa de fallo de cambios (métrica DORA).

## Hito 2 (Aplica)

Resuelto en este repositorio: PRs #1–#5, `ci.yml` con matrix, `deploy.yml` a Pages, `eliminar()` con 3 pruebas, badge y release v0.2.0. La configuración de GitHub (squash-only, ruleset `proteger-main`, Pages) la aplica `scripts/01_publicar_en_github.sh`.
