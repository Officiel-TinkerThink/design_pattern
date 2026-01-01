from __future__ import annotations
from collections.abc import Iterator, Iterable
from typing import Any


class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False
    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._sorted_items = None
        self._position = 0

    def __next__(self) -> Any:
        if self._sorted_items is None:
            self._sorted_items = sorted(self._collection._collection)
            if self._reverse:
                self._sorted_items = list(reversed(self._sorted_items))

        if self._position >= len(self._sorted_items):
            raise StopIteration()
        value = self._sorted_items[self._position]
        self._position += 1
        return value
    
class WordsCollection(Iterable):
    def __init__(self, collection: list[Any] = None) -> None:
        self._collection = collection or []

    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self, True)
    
    def add_item(self, item: str) -> None:
        self._collection.append(item)

if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("A")
    collection.add_item("B")
    collection.add_item("C")

    print("Straight traversal:")
    print("\n".join(collection))

    print("\nReverse traversal:")
    for item in collection.get_reverse_iterator():
        print(item)