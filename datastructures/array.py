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
import copy


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        if not isinstance(starting_sequence, Sequence):
            raise  ValueError
        if not isinstance(data_type,type):
            raise TypeError
        self.__elements = starting_sequence
        self.__logical_size = len(starting_sequence)
        self.__physical_size =  self.__logical_size
        self.__data_type = data_type
        self.__items = np.empty(self.__physical_size, dtype = self.__data_type)
        if not isinstance(self.__elements[0], self.__data_type):
            raise TypeError 

        for index in range(self.__logical_size):
            self.__items[index]=copy.deepcopy(self.__elements[index])


    @overload
    def __getitem__(self, index: int) -> T:...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        arrayRange = len(self.__items)        
        if isinstance (index,int):
            if (index > (-arrayRange) and (index < arrayRange)):
                item = self.__items[index]
                return item.item() if isinstance(item,np.generic) else item
            else:
                raise IndexError
        elif isinstance (index,slice):
            start = (index.start if index.start is not None else 0)
            stop = (index.stop if index.stop is not None else (len(self.__items)-1))
            step = (index.step if index.step is not None else 1) 
            if start in range(-arrayRange,arrayRange-1) and stop in range(-arrayRange,arrayRange) and step in range(-arrayRange,arrayRange-1):
                sliced_items= self.__items[start:stop:step]
                return Array(starting_sequence=sliced_items.tolist(), data_type=self.__data_type)
            else:
                raise IndexError
        else:
            raise TypeError

    
    def __setitem__(self, index: int, item: T) -> None:
        arrayRange= len(self.__items)
        if index not in range(-arrayRange,arrayRange):
            raise IndexError
        #if type(item) != self.__data_type:
           # raise TypeError
        self.__items[index] = item
        
    def __grow(self,newSize: int):
        if newSize > self.__physical_size:
            self.__physical_size = self.__physical_size * 2
            newArray = np.empty(self.__physical_size, dtype=self.__data_type)
            for index in range(len(self.__items)):
                newArray[index]=copy.deepcopy(self.__items[index])
            self.__items = newArray
        else:
            pass    

    def append(self, data: T) -> None:
        self.__grow(self.__logical_size+1)
        self.__logical_size += 1
        self.__items[self.__logical_size+1]=copy.deepcopy(data)

    def append_front(self, data: T) -> None:
        self.__grow(self.__logical_size+1)
        self.__logical_size += 1
        newArrayFr = np.empty(self.__physical_size, dtype=self.__data_type)
        i=0
        newArrayFr[i]=copy.deepcopy(data)
        for index in range(i+1,len(self.__items)):
            newArrayFr[index]=copy.deepcopy(self.__items[index])
            i=index        
        self.__items= newArrayFr

    def decreaseSize(self,newSize):
        if newSize <= (self.__physical_size//4):
            return (self.__physical_size//2)
        else:
            return (self.__physical_size)
        
    def __delitem__(self, index: int) -> None:
        size = self.decreaseSize(self.__logical_size-1)       
        newArray = copy.deepcopy(self.__items)
        newArray = np.concatenate([newArray[:index], newArray [index+1:self.__logical_size]])
        print(newArray)
        self.__items=newArray
        print(self.__items)
        self.__logical_size-=1 


            
    def pop(self) -> None:
        self.__delitem__(len(self.__logical_size)-1)
    
    def pop_front(self) -> None:
        self.__delitem__(0)

    def __len__(self) -> int: 
        return self.__logical_size

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Array):
            return False
        if self.__logical_size != other.__logical_size:
            return False
        else:
            for index in range(self.__logical_size):
                if other.__elements[index] != self.__elements[index]:
                    return False
        return True
    
    def __iter__(self) -> Iterator[T]:
        return iter(self.__items)

    def __reversed__(self) -> Iterator[T]:
        newArray = []
        for i in range(len(self.__elements)-1,-1,-1):
            newArray.append(self.__elements[i])
        return iter(newArray)

    def __contains__(self, item: Any) -> bool:
        for index in range(self.__logical_size):
            if item == self.__elements[index]:
                return True
        return False

    def clear(self) -> None:
        self.__logical_size=0
        self.__physical_size=0
        self.__items = np.empty(self.__physical_size, dtype = self.__data_type)
        self.__elements = []


    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__logical_size}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')