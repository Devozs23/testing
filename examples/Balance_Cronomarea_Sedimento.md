# Informe de Ajuste de Balance — Economía de Sedimento y curva de primera victoria

> **Juego:** Cronomarea · **Fecha:** 2026-07-19 · **Autor/a:** Equipo de diseño · **Iteración:** 1

## Contexto

### Comportamiento actual

Los jugadores tardan demasiado en lograr su primera victoria y sienten que el árbol del Faro "se seca" a mitad de partida: entre los nodos 12 y 20 pasan varias runs sin poder comprar nada, justo cuando el juego más lo necesita para sostener la motivación.

### Datos de playtesting

Playtest cerrado, 42 testers, 2 semanas, telemetría opt-in (1 870 runs registradas):

- **Mediana de runs hasta primera victoria: 52** (objetivo del GDD: 25–35).
- **Runs entre compras de nodo en la franja 12–20 del Faro: 6,1** (al inicio: 1,4).
- **Sedimento medio por run: 27** (rango del GDD: 25–40; estamos en el suelo del rango).
- Tasa de abandono del playtest entre las runs 20 y 30: 31 % de los testers.
- Feedback cualitativo (encuesta): "el combate es justo, pero siento que no avanzo" (23/42); nadie señala al parry ni a los jefes como injustos.

### Comportamiento deseado

La primera victoria debe llegar en 25–35 runs y el jugador debería poder comprar un nodo del Faro al menos cada 3 runs durante toda la partida (regla de ritmo del GDD: algo permanente cada ≤ 3 runs). La dificultad *percibida* del combate debe mantenerse: el problema es de ritmo de progresión, no de habilidad exigida.

### Referencia del GDD

De `GDD_Cronomarea.md`, secciones 5 y 6:

- Curva de coste del Faro: `coste(n) = 15 × 1.35^n` Sedimento por nodo.
- Fuentes de Sedimento: 1 por sala superada + 10 por jefe + 5 por página del diario.
- DPS del jugador sin reliquias: 35 → 110 (Faro completo), +2,5 DPS por nodo de Filo.
- HP de enemigo base: `HP = 40 × 1.6^bioma`.
- KPI: mediana de runs hasta primera victoria 25–35; si > 45, el juego está sobre-difícil.

### Restricciones

- Mantener la curva de dificultad definida en el GDD.
- No romper sistemas dependientes: reliquias sinérgicas (multiplican DPS base), tienda del Contrabandista (precios en Fragmentos), Eco de Combate (hace el 40 % del DPS original), tabla de líderes de semilla diaria.
- Ajustes incrementales: **±20 % máximo por parámetro y por iteración.**

---

## 1. Análisis de la raíz del problema

El síntoma (52 runs hasta la primera victoria) tiene dos causas que se componen, y ninguna es el combate:

1. **Los faucets de Sedimento son planos pero los costes son exponenciales.** La ganancia por run (~27) apenas crece con la habilidad del jugador, mientras `15 × 1.35^n` dobla el coste cada ~2,3 nodos. El cruce de ambas curvas produce la sequía observada en los nodos 12–20 (6,1 runs por compra, el doble del máximo tolerable según la regla de ritmo).
2. **La ganancia real está en el suelo del rango previsto.** El GDD asumía 25–40 Sedimento por run, pero la mediana real es 27 porque las páginas del diario (5 c/u) se agotan pronto y los testers medios superan menos salas de las estimadas.

El feedback cualitativo confirma que la dificultad de combate percibida es correcta ("el combate es justo"), así que **no tocamos la fórmula de coste** (define la forma de la curva y el ritmo de final de juego) y actuamos sobre los faucets y, levemente, sobre el poder base — repartiendo el ajuste entre varios parámetros para respetar el tope de ±20 %.

## 2. Valores actuales vs. propuestos

| Parámetro | Valor actual | Valor propuesto | Δ % | Justificación |
|-----------|--------------|-----------------|-----|---------------|
| Sedimento por jefe derrotado | 10 | 12 | +20 % | Premia runs profundas, que son las que se secan |
| Sedimento por página del diario | 5 | 6 | +20 % | Refuerza la progresión por conocimiento, marca de identidad |
| Bonus nuevo: sala superada en biomas 3–4 | 1 | 1 + 20 % de prob. de +1 | +20 % esperado | Solo afecta al tramo medio-tardío, donde está la sequía |
| DPS base del jugador | 35 | 38 | +8,6 % | Acorta runs fallidas; no altera el techo (110 se mantiene) |
| Multiplicador de HP enemigo por bioma | 1,60 | 1,55 | −3,1 % (−12 % en bioma 4) | Suaviza el muro tardío sin tocar biomas 1–2 |
| Coste del Faro (`15 × 1.35^n`) | sin cambios | sin cambios | 0 % | La forma de la curva es correcta; el fallo está en los faucets |

Ganancia proyectada por run: de ~27 a ~33 Sedimento (+22 % agregado, pero ningún parámetro individual supera +20 %).

## 3. Fórmula de balanceo ajustada

```
Antes:   sedimento_run = salas + 10·jefes + 5·paginas
         HP_enemigo(bioma) = 40 × 1.60^bioma          DPS_base = 35

Después: sedimento_run = salas + 0.2·salas_bioma_3_4 + 12·jefes + 6·paginas
         HP_enemigo(bioma) = 40 × 1.55^bioma          DPS_base = 38
```

Proyección del tiempo-para-matar (TTK) de un enemigo base, `HP / DPS_base`:

| Punto de la curva | Antes | Después | Δ % |
|-------------------|-------|---------|-----|
| Bioma 1 (Costa de Sal) | 64 / 35 = 1,83 s | 62 / 38 = 1,63 s | −11 % |
| Bioma 2 (Bosque Detenido) | 102 / 35 = 2,93 s | 96 / 38 = 2,53 s | −14 % |
| Bioma 3 (Cámaras de Ceniza) | 164 / 35 = 4,68 s | 149 / 38 = 3,92 s | −16 % |
| Bioma 4 (El Ojo de la Marea) | 262 / 35 = 7,49 s | 231 / 38 = 6,08 s | −19 % |

La curva conserva su forma (cada bioma sigue siendo ~55 % más duro que el anterior) y todos los deltas quedan dentro del ±20 %. Runs por compra de nodo en la franja 12–20: de 6,1 proyectadas a ~3,1 con la nueva ganancia media.

## 4. Impacto en sistemas dependientes

| Sistema dependiente | Impacto esperado | ¿Riesgo de romperlo? | Mitigación |
|---------------------|------------------|----------------------|------------|
| Reliquias sinérgicas (×1,15–×1,4, cap ×3) | El cap escala sobre DPS base: techo pasa de 105→114 en early | Bajo: +8,6 % uniforme, las sinergias relativas no cambian | Revisar solo las 3 reliquias de daño plano (no porcentual) |
| Tienda del Contrabandista (Fragmentos) | Ninguno: no tocamos la economía de Fragmentos | Nulo | — |
| Eco de Combate (40 % del DPS original) | El eco también pega +8,6 % | Medio: en salas de bioma 1 el combo jugador+eco puede trivializar | Vigilar tasa de salas limpiadas < 10 s en bioma 1; si sube del 15 %, bajar el eco al 37 % |
| Tabla de líderes / semilla diaria | Tiempos globales bajarán ~10-15 % | Bajo, pero rompe comparación histórica | Resetear la tabla al desplegar el parche (estándar del género) |
| Jefes ligados al cronograma | Ventanas de vulnerabilidad fijas: menos ciclos de espera por TTK menor | Bajo: es exactamente el efecto deseado | Confirmar que ningún jefe muere en 1 sola ventana en su primer encuentro |

## 5. Plan de validación

- **Hipótesis medible:** con estos valores, la mediana de runs hasta primera victoria baja de 52 a ≤ 38 en esta iteración (el objetivo 25–35 puede requerir una segunda pasada; no se fuerza en una sola por la regla del ±20 %).
- **Métricas a vigilar:** primarias — runs hasta primera victoria, runs entre compras de nodo (franja 12–20), Sedimento por run; secundarias (guardarraíles) — tasa de muerte por bioma (no debe caer > 20 % en biomas 1–2), duración de run completa (debe seguir ≈ 12 min, la marea lo fija), uso de las 3 anclas (≥ 70 %).
- **Método:** A/B con la cohorte existente: 21 testers en build ajustada, 21 en build actual como control, misma semilla diaria.
- **Tamaño de muestra y duración:** ≥ 400 runs por cohorte, 10 días.
- **Criterio de éxito:** mediana ≤ 38 runs hasta victoria en la cohorte ajustada **y** runs-por-nodo ≤ 3,5 en la franja 12–20, sin que las métricas guardarraíl salgan de rango.
- **Criterio de rollback:** si la tasa de muerte en biomas 1–2 cae más del 20 % o el feedback cualitativo reporta "demasiado fácil" en > 25 % de la cohorte, revertir el cambio de DPS base (38→35) y conservar solo los ajustes de faucets para la iteración 2.
