#!/usr/bin/env python3
"""Genera un Game Design Document (GDD) en markdown a partir de template.md.

Uso interactivo:
    python3 generate.py

Uso por argumentos:
    python3 generate.py --titulo "Mi Juego" --genero "Roguelite" ...
"""

import argparse
import datetime
import re
import sys
import unicodedata
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent / "template.md"

CAMPOS = [
    ("TITULO", "titulo", "Título del juego"),
    ("GENERO", "genero", "Género (ej. Roguelite de acción)"),
    ("PLATAFORMA", "plataforma", "Plataforma objetivo (PC/Consola/Móvil/Web)"),
    ("MOTOR", "motor", "Motor (Unity/Unreal/Godot/Custom)"),
    ("ESTILO_VISUAL", "estilo", "Estilo visual (Pixel art/3D low-poly/...)"),
    ("DURACION", "duracion", "Duración estimada (ej. 25 horas)"),
    ("AUDIENCIA", "audiencia", "Audiencia objetivo (Casual/Hardcore/Nicho)"),
    ("INSPIRACIONES", "inspiraciones", "Inspiraciones (juegos separados por comas)"),
    ("AUTOR", "autor", "Autor/a o equipo"),
    ("ELEVATOR_PITCH", "pitch", "Elevator pitch (2-3 frases, opcional)"),
]


def slug(texto: str) -> str:
    sin_acentos = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "_", sin_acentos).strip("_") or "GDD"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for _, arg, ayuda in CAMPOS:
        parser.add_argument(f"--{arg}", help=ayuda)
    parser.add_argument("--salida", help="Ruta del archivo de salida (por defecto GDD_<Titulo>.md)")
    args = parser.parse_args()

    if not TEMPLATE_PATH.exists():
        print(f"error: no se encuentra la plantilla en {TEMPLATE_PATH}", file=sys.stderr)
        return 1

    valores = {}
    for marcador, arg, ayuda in CAMPOS:
        valor = getattr(args, arg)
        if valor is None and sys.stdin.isatty():
            valor = input(f"{ayuda}: ").strip()
        valores[marcador] = valor or f"[{ayuda}]"

    valores["FECHA"] = datetime.date.today().isoformat()

    contenido = TEMPLATE_PATH.read_text(encoding="utf-8")
    for marcador, valor in valores.items():
        contenido = contenido.replace("{{" + marcador + "}}", valor)

    pendientes = sorted(set(re.findall(r"\{\{(\w+)\}\}", contenido)))
    if pendientes:
        print(f"aviso: marcadores sin rellenar: {', '.join(pendientes)}", file=sys.stderr)

    salida = Path(args.salida) if args.salida else Path(f"GDD_{slug(valores['TITULO'])}.md")
    salida.write_text(contenido, encoding="utf-8")
    print(f"GDD generado en {salida}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
