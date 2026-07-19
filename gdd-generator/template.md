# Game Design Document — {{TITULO}}

> **Versión:** 0.1 (borrador) · **Fecha:** {{FECHA}} · **Autor/a:** {{AUTOR}}
>
> **Plataforma objetivo:** {{PLATAFORMA}} · **Motor:** {{MOTOR}} · **Estilo visual:** {{ESTILO_VISUAL}}
> **Duración estimada:** {{DURACION}} · **Audiencia objetivo:** {{AUDIENCIA}}
> **Inspiraciones:** {{INSPIRACIONES}}

---

## 1. Elevator Pitch

<!-- 2-3 frases. Qué es el juego, por qué es distinto y para quién. -->
{{ELEVATOR_PITCH}}

## 2. Género y Tags

- **Género principal:** {{GENERO}}
- **Subgéneros:** <!-- ej. roguelite, deckbuilder, metroidvania -->
- **Tags de tienda (Steam / stores):** <!-- 5-10 tags que usaría la página de tienda -->

## 3. Core Gameplay Loop

<!-- Diagrama en texto. Indicar duración objetivo de cada ciclo. -->

### Core Loop (segundos → minutos)

```
[Acción base] → [Feedback inmediato] → [Recompensa corta] → [Decisión] → (vuelta al inicio)
```

### Meta Loop (sesión → días)

```
[Fin de sesión/run] → [Moneda meta] → [Mejora permanente] → [Nueva sesión más profunda]
```

### Social Loop (si aplica)

```
[Logro compartible] → [Comparación/cooperación] → [Retención por comunidad]
```

## 4. Mecánicas Principales

<!-- Mínimo 3 mecánicas ÚNICAS que diferencien el juego, además de las estándar del género. -->

| Nombre | Descripción | Input | Output | Riesgos |
|--------|-------------|-------|--------|---------|
| | | | | |
| | | | | |
| | | | | |

## 5. Sistema de Progresión

<!-- Progresión intra-sesión y meta-progresión. Incluir curvas numéricas. -->

- **Progresión intra-run/nivel:**
- **Meta-progresión (permanente):**
- **Curva de XP / desbloqueos:** <!-- fórmula o tabla, ej. XP_nivel(n) = base * n^1.5 -->
- **Recompensas por hito:** <!-- qué recibe el jugador y cada cuánto (regla de los 5 minutos) -->

### Métricas de balanceo

| Métrica | Valor inicial | Valor final | Curva |
|---------|---------------|-------------|-------|
| DPS del jugador | | | |
| HP de enemigos base | | | |
| Tiempo por nivel/run | | | |

## 6. Economía del Juego

| Recurso | Fuente (faucet) | Sumidero (sink) | Ritmo de ganancia | Tope/Cap |
|---------|-----------------|-----------------|-------------------|----------|
| | | | | |
| | | | | |

<!-- Reglas anti-inflación: ¿qué evita que el jugador acumule sin gastar? -->

## 7. Niveles / Worlds / Biomas

<!-- Lista de zonas con tema, mecánica exclusiva, rango de dificultad y duración. -->

| Zona/Bioma | Tema | Mecánica exclusiva | Dificultad | Duración |
|------------|------|--------------------|------------|----------|
| | | | | |

## 8. Personajes / Enemigos / NPCs

- **Protagonista(s):**
- **Arquetipos de enemigos:** <!-- tabla con rol, comportamiento, contramedida del jugador -->
- **Jefes:**
- **NPCs / vendedores / narrativa:**

## 9. Estética y Dirección de Arte

- **Referencias visuales:**
- **Paleta:**
- **Resolución / pipeline:** <!-- ej. 640x360 pixel-perfect, sprites 32x32 -->
- **UI/UX:** <!-- diegética o no, legibilidad, accesibilidad -->

## 10. Audio y Música

- **Dirección musical:** <!-- género, capas adaptativas, referencias -->
- **SFX:** <!-- prioridades de feedback: golpe, recogida, peligro -->
- **Implementación:** <!-- middleware (FMOD/Wwise) o nativo del motor -->

## 11. Monetización

<!-- Premium, F2P, DLC, cosméticos. Si es premium puro, indicarlo y justificar precio. -->

## 12. Roadmap de Desarrollo

| Fase | Alcance | Criterio de salida | Duración estimada |
|------|---------|--------------------|-------------------|
| MVP | Core loop jugable con arte placeholder | "¿Es divertido 10 minutos?" | |
| Alpha | Todas las mecánicas y 1 bioma completo | Feature-complete, contenido parcial | |
| Beta | Todo el contenido, balanceo y pulido | Content-complete, sin bugs bloqueantes | |
| Gold | Certificación, localización, marketing | Build de lanzamiento aprobada | |

## 13. Métricas de Éxito (KPIs)

| KPI | Objetivo | Cómo se mide |
|-----|----------|--------------|
| Retención D1 / D7 / D30 | | Analítica in-game |
| Duración media de sesión | | Analítica in-game |
| Tasa de finalización del tutorial | | Funnel de eventos |
| Wishlists pre-lanzamiento | | Steamworks |
| Reseñas positivas | | Página de tienda |
