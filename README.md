# GDD Template Generator

Generador de Game Design Documents (GDD) en formato markdown, pensado para equipos indie y AA que necesitan documentar un juego de forma completa y consistente desde el primer día.

## Contenido

| Ruta | Descripción |
|------|-------------|
| `gdd-generator/template.md` | Plantilla maestra del GDD con marcadores `{{...}}` y las 13 secciones estándar. |
| `gdd-generator/balance-template.md` | Plantilla de informe de ajuste de balance basado en datos de playtesting. |
| `gdd-generator/generate.py` | Script CLI que rellena cualquier plantilla (modo interactivo o por argumentos). |
| `examples/GDD_Cronomarea.md` | GDD de ejemplo completamente rellenado (roguelite de acción en pixel art). |
| `examples/Balance_Cronomarea_Sedimento.md` | Informe de balance de ejemplo sobre la economía de Cronomarea. |

## Uso rápido

### Modo interactivo

```bash
python3 gdd-generator/generate.py
```

El script pregunta título, género, plataforma, motor, estilo visual, duración, audiencia e inspiraciones, y escribe `GDD_<Titulo>.md` en el directorio actual.

### Modo por argumentos

```bash
python3 gdd-generator/generate.py \
  --titulo "Cronomarea" \
  --genero "Roguelite de acción" \
  --plataforma "PC" \
  --motor "Godot" \
  --estilo "Pixel art" \
  --duracion "25 horas" \
  --audiencia "Hardcore" \
  --inspiraciones "Hades, Dead Cells, Outer Wilds" \
  --salida GDD_Cronomarea.md
```

### Otras plantillas

Con `--template` el script rellena cualquier plantilla; los marcadores `{{...}}` se descubren automáticamente y se rellenan con `--set` o de forma interactiva:

```bash
python3 gdd-generator/generate.py \
  --template gdd-generator/balance-template.md \
  --set SISTEMA="Economía de Sedimento" \
  --set JUEGO="Cronomarea" \
  --set ITERACION="1" \
  --autor "Equipo de diseño"
```

La plantilla de balance produce un informe con: análisis de la raíz del problema, tabla de valores actuales vs. propuestos (con tope de ±20 % por parámetro), fórmula ajustada con proyección de curva, impacto en sistemas dependientes y plan de validación.

## Estructura del GDD generado

1. Elevator Pitch
2. Género y Tags
3. Core Gameplay Loop (con Meta Loop y Social Loop)
4. Mecánicas Principales (tabla: Nombre | Descripción | Input | Output | Riesgos)
5. Sistema de Progresión
6. Economía del Juego (tabla de recursos)
7. Niveles / Worlds / Biomas
8. Personajes / Enemigos / NPCs
9. Estética y Dirección de Arte
10. Audio y Música
11. Monetización
12. Roadmap de Desarrollo (MVP → Alpha → Beta → Gold)
13. Métricas de Éxito (KPIs)

La plantilla incluye secciones guiadas para métricas de balanceo (DPS, curvas de economía y progresión) y exige definir al menos 3 mecánicas únicas diferenciadoras.
