from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Token:
    tipo: str
    lexema: str
    linea: int
    columna: int
    atributo: Optional[int] = None

    def format(self, include_attribute: bool = False) -> str:
        escaped = self.lexema.replace("\\", "\\\\").replace("'", "\\'")
        base = f"<{self.tipo}, '{escaped}', {self.linea}, {self.columna}"
        if include_attribute and self.atributo is not None:
            base += f", idx={self.atributo}"
        return base + ">"


@dataclass(frozen=True)
class LexicalError:
    tipo: str
    fragmento: str
    linea: int
    columna: int
    mensaje: str

    def format(self) -> str:
        frag = self.fragmento.replace("\n", "\\n")
        return f"[{self.tipo}] línea {self.linea}, columna {self.columna}: {self.mensaje} Fragmento: {frag!r}"


class LexemeTable:
    """Tabla sin duplicados innecesarios.

    La clave es (categoría, lexema). El índice comienza en 1 y se conserva
    durante toda una ejecución del lexer.
    """

    def __init__(self) -> None:
        self._index: dict[tuple[str, str], int] = {}
        self._entries: list[tuple[int, str, str]] = []

    def intern(self, categoria: str, lexema: str) -> int:
        key = (categoria, lexema)
        if key not in self._index:
            idx = len(self._entries) + 1
            self._index[key] = idx
            self._entries.append((idx, categoria, lexema))
        return self._index[key]

    @property
    def entries(self) -> list[tuple[int, str, str]]:
        return list(self._entries)
