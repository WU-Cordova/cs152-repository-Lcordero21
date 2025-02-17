# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray
from copy import copy


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        if not isinstance(starting_sequence, Sequence):
            raise  ValueError
        if not isinstance(data_type,type):
            raise TypeError
        self.__logical_size: int = len(starting_sequence)
        self.__physical_size: int = self.__logical_size
        self.__data_type: type = data_type
        self.__items: NDArray = np.empty(self.__logical_size, dtype = self.__data_type)

        for index in self.__logical_size:
            NDArray[index]=copy.deepcopy(starting_sequence[index])

    @overload
    def __getitem__(self, index: int) -> T:...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance (index,int):
            arrayRange = len(self.__items)
            if (index > (-len(self.__items)) and (index < len(self.__items))):
                item = self.__items[index]
                return item.item() if isinstance(item,np.generic) else item
            else:
                raise IndexError
        if isinstance (index,slice):
            start = (index.start if index.start is not None else 0)
            stop = (index.stop if index.stop is not None else (len(self.__items)))
            step = (index.step if index.step is not None else 1) 
            if start in range(-arrayRange,arrayRange) and stop in range(-arrayRange,arrayRange) and step in range(-arrayRange,arrayRange):
                sliced_items= self.__items[start:stop:step]
                return Array(starting_sequence=sliced_items.tolist(), data_type=self.__data_type)
            else:
                raise IndexError
        else:
            raise TypeError

    
    def __setitem__(self, index: int, item: T) -> None:
        raise NotImplementedError('Indexing not implemented.')

    def append(self, data: T) -> None:
        raise NotImplementedError('Append not implemented.')

    def append_front(self, data: T) -> None:
        raise NotImplementedError('Append front not implemented.')

    def pop(self) -> None:
        raise NotImplementedError('Pop not implemented.')
    
    def pop_front(self) -> None:
        raise NotImplementedError('Pop front not implemented.')

    def __len__(self) -> int: 
        raise NotImplementedError('Length not implemented.')

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError('Equality not implemented.')
    
    def __iter__(self) -> Iterator[T]:
        raise NotImplementedError('Iteration not implemented.')

    def __reversed__(self) -> Iterator[T]:
        raise

    def __delitem__(self, index: int) -> None:
       raise NotImplementedError('Delete not implemented.')

    def __contains__(self, item: Any) -> bool:
        raise NotImplementedError('Contains not implemented.')

    def clear(self) -> None:
        raise NotImplementedError('Clear not implemented.')

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')