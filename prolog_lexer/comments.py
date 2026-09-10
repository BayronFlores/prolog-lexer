"""Escaneo de comentarios: '% ...' (línea) y '/* ... */' (bloque).

Corresponde a la categoría léxica "Comentarios de línea ... y comentarios
de bloque" del enunciado. Los comentarios no generan tokens; solo se
descartan del flujo, salvo el caso de error "comentario sin cierre".
"""

from __future__ import annotations


class CommentScanning:
    """Mixin que asume un ``Cursor`` (_peek/_advance/_add_error)."""

    def _scan_line_comment(self) -> None:
        while self._peek() and self._peek() != "\n":
            self._advance()

    def _scan_block_comment(self) -> None:
        start_line, start_column, start_i = self.line, self.column, self.i
        depth = 0

        while self._peek():
            if self._peek() == "/" and self._peek(1) == "*":
                depth += 1
                self._advance()
                self._advance()
                continue

            if self._peek() == "*" and self._peek(1) == "/":
                depth -= 1
                self._advance()
                self._advance()
                if depth == 0:
                    return
                continue

            self._advance()

        fragment = self.source[start_i:self.i]
        self._add_error(
            "COMENTARIO_SIN_CIERRE",
            fragment,
            start_line,
            start_column,
            "Comentario de bloque sin cierre '*/'.",
        )
