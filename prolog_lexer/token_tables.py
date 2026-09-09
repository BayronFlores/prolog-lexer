"""Tablas de operadores y delimitadores del subconjunto de Prolog.

Estas constantes son puros datos (sin lógica de escaneo) y corresponden
directamente a las categorías léxicas "Operadores de cláusulas y consultas",
"Operadores de unificación y comparación", "Operadores aritméticos",
"Operadores de control" y "Delimitadores" del enunciado.
"""

from __future__ import annotations

# Operadores de dos o más caracteres. El orden importa: se evalúan de
# arriba hacia abajo y deben quedar antes que cualquier prefijo suyo para
# garantizar máxima coincidencia (p. ej. "==" antes que "=").
MULTI_CHAR_OPERATORS: list[tuple[str, str]] = [
    (r"\==", "OP_DIF_IDENTICO"),
    ("=..", "OP_UNIV"),
    ("-->", "OP_DCG"),
    (":-", "OP_REGLA"),
    ("?-", "OP_CONSULTA"),
    (r"\=", "OP_NO_UNIFICA"),
    ("==", "OP_IDENTICO"),
    ("=<", "OP_MENOR_IGUAL"),
    (">=", "OP_MAYOR_IGUAL"),
    ("//", "OP_DIV_ENTERA"),
    ("**", "OP_POTENCIA"),
    (r"\+", "OP_NEGACION"),
]

# Operadores de un solo carácter.
SINGLE_CHAR_OPERATORS: dict[str, str] = {
    "=": "OP_UNIFICA",
    "<": "OP_MENOR",
    ">": "OP_MAYOR",
    "+": "OP_SUMA",
    "-": "OP_RESTA",
    "*": "OP_MULTIPLICA",
    "/": "OP_DIVIDE",
    "!": "OP_CORTE",
    ";": "PUNTO_Y_COMA",
    ":": "DOS_PUNTOS",
}

# Delimitadores de agrupación, listas y punto final de cláusula.
DELIMITERS: dict[str, str] = {
    "(": "PARENTESIS_IZQ",
    ")": "PARENTESIS_DER",
    "[": "CORCHETE_IZQ",
    "]": "CORCHETE_DER",
    "{": "LLAVE_IZQ",
    "}": "LLAVE_DER",
    "|": "BARRA_VERTICAL",
    ",": "COMA",
    ".": "PUNTO",
}

# Átomos-operador reservados (palabras, no símbolos).
WORD_OPERATORS: dict[str, str] = {
    "is": "OP_IS",
    "mod": "OP_MOD",
}

# Categorías cuyo lexema se registra en la tabla de lexemas (sección 6 del
# enunciado): átomos, variables y literales.
INTERNED_CATEGORIES = {
    "ATOMO",
    "ATOMO_CITADO",
    "VARIABLE",
    "NUMERO_ENTERO",
    "NUMERO_REAL",
    "CADENA",
}
