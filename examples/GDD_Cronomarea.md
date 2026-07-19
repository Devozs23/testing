# Game Design Document — Cronomarea

> **Versión:** 0.1 (borrador) · **Fecha:** 2026-07-19 · **Autor/a:** Equipo de diseño
>
> **Plataforma objetivo:** PC (Steam), port posterior a Switch 2 · **Motor:** Godot 4 · **Estilo visual:** Pixel art HD (sprites 48×48, resolución base 640×360)
> **Duración estimada:** 25 horas (historia) / 80+ horas (completista) · **Audiencia objetivo:** Hardcore / entusiastas de roguelites
> **Inspiraciones:** Hades, Dead Cells, Outer Wilds

---

## 1. Elevator Pitch

**Cronomarea** es un roguelite de acción donde cada run ocurre dentro de una marea temporal de 12 minutos que rebobina el mundo al terminar — pero el conocimiento y las "anclas" que colocas persisten entre ciclos. Combate rápido tipo Hades con una capa de puzzle temporal: aprender *cuándo* ocurre cada cosa en la isla es tan importante como pegar fuerte. Para jugadores hardcore que quieren que su habilidad **y** su conocimiento del mundo progresen a la vez.

## 2. Género y Tags

- **Género principal:** Roguelite de acción (top-down, combate en tiempo real)
- **Subgéneros:** Bucle temporal, exploración basada en conocimiento, acción-puzzle
- **Tags de tienda:** Roguelite, Acción, Pixel Art, Bucle Temporal, Difícil, Historia Rica, Un Jugador, Rejugabilidad Alta, Indie, Combate Rápido

## 3. Core Gameplay Loop

### Core Loop (30–90 segundos)

```
[Explorar sala] → [Combate/peligro temporal] → [Botín: Fragmentos + reliquia]
      ↑                                                    ↓
[Elegir ruta según fase de la marea] ← [Decisión: avanzar, anclar o arriesgar]
```

### Meta Loop (una run = 12 minutos; sesión = 3–5 runs)

```
[Fin de run (muerte o marea)] → [Conservas: Sedimento + conocimiento del cronograma]
        ↑                                          ↓
[Nueva run con mejor build inicial] ← [Gastar Sedimento en el Faro (mejoras permanentes)]
```

### Social Loop

```
[Semilla diaria compartida] → [Tabla de líderes por tiempo/estilo] → [Clips de "rutas perfectas" en comunidad]
        ↑                                                                      ↓
[Retos asíncronos entre amigos ("supera mi ancla")] ← [Compartir código de ruta]
```

## 4. Mecánicas Principales

Las tres primeras son las mecánicas únicas diferenciadoras; las dos últimas son el sustrato de género.

| Nombre | Descripción | Input | Output | Riesgos |
|--------|-------------|-------|--------|---------|
| **Marea Temporal** | Toda la isla vive un ciclo fijo de 12 min: mareas que abren/cierran zonas, patrullas con horarios, eventos programados (erupción al minuto 8, eclipse al 10). El cronograma es idéntico entre runs; el jugador progresa memorizándolo. | Reloj de marea siempre visible (HUD); sin input directo | Rutas óptimas emergentes; el mapa "cambia" sin ser procedural | Frustración si el ciclo se siente como espera; mitigar con atajos que doblan el tiempo útil |
| **Anclas de Cronos** | 3 anclas por run que fijan un objeto/estado fuera del rebobinado (una puerta abierta, un puente reparado, un cofre marcado). Persisten entre runs hasta ser reclamadas. | Mantener `E` 1,5 s sobre objeto anclable | Progresión espacial permanente elegida por el jugador; cada run "esculpe" la isla | Softlocks si se ancla algo inútil; permitir des-anclar en el Faro |
| **Eco de Combate** | Al morir, los últimos 20 s de tu combate quedan grabados como un "eco" fantasma que lucha junto a ti la próxima vez que entres a esa sala (una vez por run). | Automático al morir; `Q` para invocar el eco al entrar en la sala | La muerte alimenta el poder futuro; enseña al jugador a "morir bien" | Puede trivializar salas si el eco es muy fuerte; el eco hace 40 % del DPS original y no recibe curación |
| Combate direccional | Ataque ligero/pesado, dash con i-frames (0,25 s), parry con ventana de 0,15 s que devuelve proyectiles | `LMB`/`RMB`, `Space`, `F` | Combate expresivo skill-based | Curva de entrada alta; tutorial con parry asistido opcional |
| Reliquias sinérgicas | 90 reliquias pasivas con tags (fuego, marea, eco) que combean entre sí, al estilo boons de Hades | Elección en altares (3 opciones) | Variedad de builds por run | Balanceo combinatorio; cap de 1 sinergia legendaria por run |

## 5. Sistema de Progresión

- **Progresión intra-run:** reliquias (poder inmediato, se pierden al morir) + Fragmentos de Marea (moneda de run para altares y tienda del Contrabandista).
- **Meta-progresión permanente:** Sedimento gastado en el Faro — árbol de 40 nodos en 4 ramas: Vitalidad, Filo (daño), Cronos (utilidades temporales), Fortuna (economía/rareza).
- **Progresión por conocimiento:** el Diario de Mareas registra automáticamente cada evento del cronograma descubierto; completar una página desbloquea un atajo narrado. Es progresión sin números, al estilo Outer Wilds.
- **Curva de coste del Faro:** `coste(n) = 15 × 1.35^n` Sedimento por nodo (15, 20, 27, 37…). Una run media produce 25–40 Sedimento → 1 nodo por cada 1–2 runs al inicio, 1 por cada 4–5 al final.
- **Recompensas por hito:** cada jefe derrotado por primera vez otorga una Llave de Bruma (desbloquea arma nueva: 5 armas en total) + escena de historia. Regla de ritmo: algo permanente (nodo, arma, página del diario o atajo) cada ≤ 3 runs.

### Métricas de balanceo

| Métrica | Valor inicial | Valor final | Curva |
|---------|---------------|-------------|-------|
| DPS del jugador (sin reliquias) | 35 | 110 (Faro completo) | Lineal por nodos: +2,5 DPS/nodo de Filo |
| DPS del jugador (run con build media) | 60 | 320 | Multiplicativa: reliquias ×1,15–×1,4 c/u, cap ×3 sobre base |
| HP de enemigo base (Bruma Menor) | 40 | 260 (bioma 4) | `HP = 40 × 1.6^bioma` |
| DPS enemigo → TTK del jugador | 8 DPS (jugador sobrevive ~12 golpes) | 30 DPS (~7 golpes) | El TTK del jugador baja: la defensa se gana con parry/dash, no con stats |
| Tiempo por run | 6–8 min (muerte temprana) | 12 min (run completa, límite de la marea) | Fijo por diseño: la marea ES el timer |
| Runs hasta primera victoria | — | 25–35 runs (~5–6 h) | Referencia Hades: ajustar en beta con telemetría |

## 6. Economía del Juego

| Recurso | Fuente (faucet) | Sumidero (sink) | Ritmo de ganancia | Tope/Cap |
|---------|-----------------|-----------------|-------------------|----------|
| **Fragmentos de Marea** (run) | Enemigos (2–6), cofres (15–30), eventos del cronograma (25) | Altares de reliquias (30/50/80), tienda del Contrabandista, reintentos de sala (20) | ~180–250 por run completa | Se pierde todo al morir (presión de gasto) |
| **Sedimento** (meta) | Fin de run: 1 por sala superada + bonus por jefes (10) y páginas del diario (5) | Árbol del Faro (`15 × 1.35^n`), des-anclar (5), cosméticos del protagonista | 25–40 por run | Sin cap; sinks tardíos (cosméticos) absorben excedente |
| **Llaves de Bruma** | Primer kill de cada jefe (5 en total) | Desbloqueo de armas (1 llave = 1 arma) | 1 por jefe nuevo | 5 (finitas, no farmeables) |
| **Anclas de Cronos** | 3 al inicio de cada run | Anclar objetos en el mundo | 3/run, no acumulables | 3 activas simultáneas en la isla; +2 vía Faro |

**Regla anti-inflación:** los Fragmentos se pierden al morir (gasta o pierde) y el Sedimento tiene curva de coste exponencial + sinks cosméticos infinitos al final. Ningún recurso meta es comprable con dinero real.

## 7. Niveles / Worlds / Biomas

Isla fija (no procedural) dividida en 4 biomas + hub. La variedad entre runs viene del cronograma de la marea, las reliquias y las anclas — no de layouts aleatorios.

| Zona/Bioma | Tema | Mecánica exclusiva | Dificultad | Duración |
|------------|------|--------------------|------------|----------|
| **El Faro** (hub) | Refugio fuera del tiempo | Árbol de mejoras, Diario, gestión de anclas | — | 1–3 min entre runs |
| **Costa de Sal** | Playas y arrecifes; la marea inunda salas según el minuto | Salas que se abren/cierran con el agua (min 0–3 seco, 4–7 inundado…) | ★☆☆☆ | 3 min |
| **Bosque Detenido** | Selva con fauna congelada a medio movimiento | Enemigos "estatua" que despiertan en minutos concretos del ciclo | ★★☆☆ | 3 min |
| **Cámaras de Ceniza** | Volcán con erupción programada al minuto 8 | Rutas de lava que se solidifican tras la erupción (llegar tarde = camino nuevo) | ★★★☆ | 3 min |
| **El Ojo de la Marea** | Núcleo temporal, arquitectura imposible | El reloj corre al doble; parry devuelve el tiempo 2 s | ★★★★ | 3 min + jefe final |

## 8. Personajes / Enemigos / NPCs

- **Protagonista — Isla (sí, se llama como el lugar):** farera náufraga atrapada en el ciclo; muda durante el juego, expresiva por animación. Su historia se cuenta por las páginas del Diario.
- **Arquetipos de enemigos:**

| Arquetipo | Rol | Comportamiento | Contramedida |
|-----------|-----|----------------|--------------|
| Bruma Menor | Carne de cañón | Melee lento en grupo | AoE, kiting |
| Anguila Vidente | Presión a distancia | Proyectil teledirigido lento | Parry (devuelve ×2 daño) |
| Centinela de Sal | Tanque de zona | Bloquea pasillos, escudo frontal | Dash a la espalda |
| Reflejo Roto | Élite | Imita los últimos 5 s de inputs del jugador | Cambiar de patrón, no repetirse |

- **Jefes (5):** uno por bioma + jefe final "La Mareante", cada uno ligado a un evento del cronograma (p. ej., el jefe del volcán solo es vulnerable durante la erupción).
- **NPCs:** el **Contrabandista** (tienda de run, aparece en salas distintas según el minuto), la **Cartógrafa** (vende pistas del cronograma por Sedimento), el **Eco del Farero anterior** (narrador y árbol de historia en el hub).

## 9. Estética y Dirección de Arte

- **Referencias visuales:** Hyper Light Drifter (paleta y atmósfera), Dead Cells (fluidez de animación), estampas japonesas de olas (motivo de la marea).
- **Paleta:** turquesas y arenas desaturadas de base; cada minuto del ciclo tiñe la luz global (amanecer → tormenta → eclipse), de modo que el jugador *lee la hora en el color de la pantalla*.
- **Resolución / pipeline:** 640×360 pixel-perfect escalado ×3; sprites de personaje 48×48 con 12–16 frames por acción; shaders de agua y rebobinado en Godot (canvas shaders, sin 3D).
- **UI/UX:** reloj de marea diegético (anillo alrededor del personaje, opción de HUD clásico); daltonismo: los eventos temporales siempre se señalan con forma + color + sonido.

## 10. Audio y Música

- **Dirección musical:** electrónica orgánica con instrumentación de cuerdas procesadas; **la banda sonora dura exactamente 12 minutos y está sincronizada con el cronograma** — el motivo de la erupción siempre suena al minuto 8, así la música es también interfaz.
- **Capas adaptativas:** intensidad de combate (2 capas), proximidad de evento (1 capa de anticipación 15 s antes de cada evento del ciclo).
- **SFX prioritarios:** parry (el sonido más satisfactorio del juego, prioridad de mezcla máxima), campana de ancla, "latido" de la marea en los últimos 60 s del ciclo.
- **Implementación:** FMOD integrado en Godot; mezcla por snapshots (exploración/combate/últimos 60 s).

## 11. Monetización

- **Premium puro: 19,99 USD.** Sin microtransacciones, sin cosméticos de pago — coherente con la audiencia hardcore y las inspiraciones (Hades, Dead Cells).
- **Post-lanzamiento:** 1 DLC de pago (nuevo bioma + jefe + 20 reliquias, ~7,99 USD) si se superan 150 000 unidades; actualizaciones de contenido menores gratuitas para sostener reseñas.
- **Demo:** primera zona completa (Costa de Sal) con marea de 6 minutos, para festivales de Steam.

## 12. Roadmap de Desarrollo

| Fase | Alcance | Criterio de salida | Duración estimada |
|------|---------|--------------------|-------------------|
| **MVP** | Combate base + marea de 6 min + 1 bioma greybox + muerte/rebobinado | "¿Repetir el mismo mapa con cronograma es divertido 10 min?" (playtest interno) | 3 meses |
| **Alpha** | Las 5 mecánicas, 2 biomas con arte final, Faro con 20 nodos, 40 reliquias, 2 jefes | Feature-complete; primera victoria posible de principio a fin | +6 meses |
| **Beta** | 4 biomas, 5 jefes, 90 reliquias, Diario completo, FMOD, semilla diaria | Content-complete; telemetría de balanceo activa; sin bugs bloqueantes; demo pública | +5 meses |
| **Gold** | Balanceo final con datos de la demo, localización (EN/ES/FR/DE/PT-BR/ZH/JA), certificación Steam Deck, prensa/keys | Build candidata aprobada; crash rate < 0,5 % | +2 meses |

Total: ~16 meses con un equipo de 5 personas (2 código, 1 arte, 1 diseño, 1 audio/prod parcial).

## 13. Métricas de Éxito (KPIs)

| KPI | Objetivo | Cómo se mide |
|-----|----------|--------------|
| Wishlists antes del lanzamiento | 75 000 (mínimo viable: 30 000) | Steamworks |
| Reseñas positivas | ≥ 90 % ("Muy positivas") | Página de Steam |
| Retención D1 / D7 / D30 | 60 % / 30 % / 15 % | Telemetría in-game (opt-in) |
| Mediana de runs hasta primera victoria | 25–35 (si > 45, el juego está sobre-difícil) | Telemetría de runs |
| Duración media de sesión | ≥ 45 min (3+ runs) | Telemetría |
| % de jugadores que usan las 3 anclas por run | ≥ 70 % (valida la mecánica estrella) | Telemetría de eventos |
| Tasa de finalización del tutorial | ≥ 85 % | Funnel de eventos |
| Unidades vendidas (año 1) | 100 000 | Backend de ventas |
