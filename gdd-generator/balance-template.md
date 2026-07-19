# Informe de Ajuste de Balance — {{SISTEMA}}

> **Juego:** {{JUEGO}} · **Fecha:** {{FECHA}} · **Autor/a:** {{AUTOR}} · **Iteración:** {{ITERACION}}

## Contexto

### Comportamiento actual

<!-- Describir exactamente qué pasa ahora, sin interpretar todavía. -->
{{COMPORTAMIENTO_ACTUAL}}

### Datos de playtesting

<!-- Métricas crudas: tiempo promedio, tasa de éxito, feedback de testers. Citar tamaño de muestra. -->
{{DATOS_PLAYTESTING}}

### Comportamiento deseado

<!-- Cómo debería sentirse. Traducir la sensación a métricas objetivo cuando sea posible. -->
{{COMPORTAMIENTO_DESEADO}}

### Referencia del GDD

<!-- Pegar la sección de economía/progresión afectada, con sus fórmulas. -->
{{REFERENCIA_GDD}}

### Restricciones

- Mantener la curva de dificultad definida en el GDD.
- No romper sistemas dependientes: {{SISTEMAS_DEPENDIENTES}}
- Ajustes incrementales: **±20 % máximo por parámetro y por iteración.**

---

## 1. Análisis de la raíz del problema

<!--
Separar síntoma de causa. Preguntas guía:
- ¿El problema es de números (valores) o de estructura (fórmula/diseño)?
- ¿Qué parámetro explica la mayor parte de la desviación entre métrica actual y objetivo?
- ¿El feedback de los testers coincide con lo que dicen los datos? Si no, ¿por qué?
-->

## 2. Valores actuales vs. propuestos

| Parámetro | Valor actual | Valor propuesto | Δ % | Justificación |
|-----------|--------------|-----------------|-----|---------------|
| | | | | |
| | | | | |

<!-- Ningún Δ % puede superar ±20. Si un solo parámetro no basta, repartir el ajuste entre varios. -->

## 3. Fórmula de balanceo ajustada

```
Antes:   <fórmula actual>
Después: <fórmula propuesta>
```

<!-- Tabla de proyección: evaluar ambas fórmulas en 4-5 puntos de la curva (inicio, medio, final). -->

| Punto de la curva | Antes | Después | Δ % |
|-------------------|-------|---------|-----|
| | | | |

## 4. Impacto en sistemas dependientes

| Sistema dependiente | Impacto esperado | ¿Riesgo de romperlo? | Mitigación |
|---------------------|------------------|----------------------|------------|
| | | | |

## 5. Plan de validación

- **Hipótesis medible:** <!-- "Tras el cambio, la métrica X pasará de A a B" -->
- **Métricas a vigilar:** <!-- primarias (las del problema) y secundarias (las que podrían romperse) -->
- **Método:** <!-- playtest dirigido / telemetría / A-B con build paralela -->
- **Tamaño de muestra y duración:** <!-- nº de testers o de runs, días -->
- **Criterio de éxito:** <!-- umbral concreto para dar el cambio por bueno -->
- **Criterio de rollback:** <!-- qué lectura obliga a revertir y volver a iterar -->
