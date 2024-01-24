from graphviz import Digraph
from typing import Tuple
import functools

wishes: list[Tuple[str, list[str]]] = [
    ("A", ["B", "C"]),
    ("B", ["C", "E"]),
    ("C", ["A", "D"]),
    ("D", ["B", "E"]),
    ("E", ["C", "B"]),
]

def wishToEdge(wish: Tuple[str, Tuple[str, str]]) -> list[Tuple[str, str]]:
    result: list[Tuple[str, str]] = []
    for wishy in wish[1]:
        result.append((wish[0], wishy))
    return result

def folder(acc: list[list[str]], choice: Tuple[str, Tuple[str, str]]) -> list[list[str]]:
    acc.extend(wishToEdge(choice))
    return acc

edges = functools.reduce(folder, wishes, [])

dot = Digraph()
dot.edges(edges)
dot.render(view=False)
