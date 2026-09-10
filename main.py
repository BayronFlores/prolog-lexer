from __future__ import annotations

import argparse
from pathlib import Path

from prolog_lexer import PrologLexer


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Analizador léxico del subconjunto Prolog de INFO1148."
    )
    parser.add_argument("archivo", type=Path, help="Archivo .pl a analizar")
    parser.add_argument(
        "--atributos",
        action="store_true",
        help="Incluye el índice de la tabla de lexemas en la salida.",
    )
    parser.add_argument(
        "--tabla",
        action="store_true",
        help="Muestra la tabla de lexemas al final.",
    )
    args = parser.parse_args()

    try:
        source = args.archivo.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"No se pudo leer {args.archivo}: {exc}")
        return 2

    lexer = PrologLexer(source)
    tokens, errors = lexer.tokenize()

    print("TOKENS")
    for token in tokens:
        print(token.format(include_attribute=args.atributos))

    if args.tabla:
        print("\nTABLA DE LEXEMAS")
        print("idx | categoría       | lexema")
        print("----+-----------------+-------------------------")
        for idx, category, lexeme in lexer.lexemes.entries:
            print(f"{idx:>3} | {category:<15} | {lexeme}")

    if errors:
        print("\nERRORES LÉXICOS")
        for error in errors:
            print(error.format())
        return 1

    print("\nAnálisis finalizado sin errores léxicos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
