"""Escaneo de literales entre comillas: átomos citados y cadenas.

Corresponde a las categorías "Átomos entre comillas simples ... incluyendo
espacios o caracteres especiales" y "Cadenas delimitadas por comillas
dobles ... con una convención documentada para secuencias de escape" del
enunciado. Ambas comparten la misma lógica de escaneo (escape con barra
invertida, sin saltos de línea crudos), por lo que un único método
parametrizado atiende las dos categorías.
"""

from __future__ import annotations


class QuotedScanning:
    """Mixin que asume un ``Cursor`` (_peek/_advance/_emit/_add_error)."""

    def _scan_quoted(
        self,
        quote: str,
        token_type: str,
        error_type: str,
        human_name: str,
    ) -> None:
        start_line, start_column, start_i = self.line, self.column, self.i
        self._advance()  # comilla de apertura
        escaped = False

        while self._peek():
            ch = self._peek()

            if ch == "\n" and not escaped:
                fragment = self.source[start_i:self.i]
                self._add_error(
                    error_type,
                    fragment,
                    start_line,
                    start_column,
                    f"{human_name} sin cierre antes del fin de línea.",
                )
                return

            if escaped:
                self._advance()
                escaped = False
                continue

            if ch == "\\":
                self._advance()
                escaped = True
                continue

            if ch == quote:
                self._advance()
                self._emit(
                    token_type,
                    self.source[start_i:self.i],
                    start_line,
                    start_column,
                )
                return

            self._advance()

        fragment = self.source[start_i:self.i]
        self._add_error(
            error_type,
            fragment,
            start_line,
            start_column,
            f"{human_name} sin cierre al final del archivo.",
        )
