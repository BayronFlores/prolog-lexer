"""Escaneo de átomos sin comillas, variables y la variable anónima.

Corresponde a las categorías "Átomos no entrecomillados ..." y
"Variables, iniciadas con letra mayúscula o guion bajo ... y la variable
anónima _" del enunciado. También resuelve aquí los átomos-operador
reservados (is, mod), ya que léxicamente son idénticos a un átomo hasta
que se compara el lexema contra ``WORD_OPERATORS``.
"""

from __future__ import annotations

from .cursor import ASCII_LETTERS, is_ascii_alnum
from .token_tables import WORD_OPERATORS


class IdentifierScanning:
    """Mixin que asume un ``Cursor`` (_peek/_advance/_emit)."""

    def _scan_identifier(self) -> None:
        start_line, start_column, start_i = self.line, self.column, self.i

        while self._peek() and (
            is_ascii_alnum(self._peek()) or self._peek() == "_"
        ):
            self._advance()

        lexeme = self.source[start_i:self.i]

        if lexeme[0] in ASCII_LETTERS and lexeme[0].islower():
            self._emit(
                WORD_OPERATORS.get(lexeme, "ATOMO"),
                lexeme,
                start_line,
                start_column,
            )
            return

        token_type = "VARIABLE_ANONIMA" if lexeme == "_" else "VARIABLE"
        self._emit(token_type, lexeme, start_line, start_column)
