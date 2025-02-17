from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self._bag: dict[T, int] = {}
        if items is not None: 
            for i in items:
                self.add(i) aaaa

    def add(self, item: T) -> None:
        if item is not None:
            if item in self._bag:
                self._bag[item] += 1
            else:
                self._bag[item] = 1
        else:
            raise TypeError

    def remove(self, item: T) -> None:
        if item is not None:
            if item in self._bag:
                count=self._bag[item]
                if count==0:
                    raise ValueError
                else:
                    self._bag[item]=count-1
            else:
                raise ValueError
        else:
            raise ValueError

    def count(self, item: T) -> int:
        if item is not None:
            if item in self._bag:
                return self._bag[item]
            else:
                return 0
        else:
            raise TypeError
        


    def __len__(self) -> int:
        totalItems=0
        for items in self._bag:
            totalItems+=self._bag[items]
        return totalItems

    def distinct_items(self) -> Iterable[T]:
        itemsList=[]
        for key in self._bag:
            itemsList.append(key)
        return itemsList

    def __contains__(self, item) -> bool:
        if item in self._bag:
            return True
        else:
            return False

    def clear(self) -> None:
        self._bag = {}