#!/usr/bin/env python3
"""Genera documentos de diseño en markdown a partir de una plantilla con marcadores {{...}}.

Uso interactivo (GDD por defecto):
    python3 generate.py

Uso por argumentos:
    python3 generate.py --titulo "Mi Juego" --genero "Roguelite" ...

Otras plantillas (los marcadores se descubren automáticamente):
    python3 generate.py --template balance-template.md \\
        --set SISTEMA="Economía de Sedimento" --set JUEGO="Cronomarea"
"""

import argparse
import datetime
import re
import sys
import unicodedata
from pathlib import Path

PLANTILLA_GDD = Path(__file__).parent / "template.md"

# Argumentos con nombre para la plantilla de GDD; en otras plantillas solo
# aplican si el marcador existe.
CAMPOS_GDD = [
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

AYUDAS = {marcador: ayuda for marcador, _, ayuda in CAMPOS_GDD}


def slug(texto: str) -> str:
    sin_acentos = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "_", sin_acentos).strip("_") or "documento"


def marcadores_de(contenido: str) -> list[str]:
    vistos = []
    for m in re.findall(r"\{\{(\w+)\}\}", contenido):
        if m not in vistos:
            vistos.append(m)
    return vistos


def nombre_salida(valores: dict, plantilla: Path) -> Path:
    if valores.get("TITULO"):
        return Path(f"GDD_{slug(valores['TITULO'])}.md")
    if valores.get("SISTEMA"):
        return Path(f"Balance_{slug(valores['SISTEMA'])}.md")
    return Path(f"{plantilla.stem}_relleno.md")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    for _, arg, ayuda in CAMPOS_GDD:
        parser.add_argument(f"--{arg}", help=ayuda)
    parser.add_argument(
        "--template",
        help=f"Ruta de la plantilla a rellenar (por defecto {PLANTILLA_GDD.name})",
    )
    parser.add_argument(
        "--set",
        action="append",
        default=[],
        metavar="MARCADOR=VALOR",
        help="Rellena cualquier marcador de la plantilla; repetible",
    )
    parser.add_argument("--salida", help="Ruta del archivo de salida")
    args = parser.parse_args()

    plantilla = Path(args.template) if args.template else PLANTILLA_GDD
    if not plantilla.exists():
        print(f"error: no se encuentra la plantilla en {plantilla}", file=sys.stderr)
        return 1
    contenido = plantilla.read_text(encoding="utf-8")

    valores = {}
    for marcador, arg, _ in CAMPOS_GDD:
        valor = getattr(args, arg)
        if valor:
            valores[marcador] = valor
    for par in args.set:
        if "=" not in par:
            print(f"error: --set espera MARCADOR=VALOR, no {par!r}", file=sys.stderr)
            return 1
        clave, valor = par.split("=", 1)
        valores[clave.strip()] = valor

    valores.setdefault("FECHA", datetime.date.today().isoformat())

    for marcador in marcadores_de(contenido):
        if marcador in valores:
            continue
        ayuda = AYUDAS.get(marcador, marcador.replace("_", " ").capitalize())
        valor = input(f"{ayuda}: ").strip() if sys.stdin.isatty() else ""
        valores[marcador] = valor or f"[{ayuda}]"

    for marcador, valor in valores.items():
        contenido = contenido.replace("{{" + marcador + "}}", valor)

    pendientes = marcadores_de(contenido)
    if pendientes:
        print(f"aviso: marcadores sin rellenar: {', '.join(pendientes)}", file=sys.stderr)

    salida = Path(args.salida) if args.salida else nombre_salida(valores, plantilla)
    salida.write_text(contenido, encoding="utf-8")
    print(f"Documento generado en {salida}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
