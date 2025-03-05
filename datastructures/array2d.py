from __future__ import annotations
import os
from typing import Iterator, List, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type: type) -> None:
            self.row_index = row_index
            self._array = array
            self.num_columns = num_columns
            self.data_type = data_type

        def map_index(self, row_index: int, column_index) -> int:
            return row_index * self.num_columns + column_index

        def __getitem__(self, column_index: int) -> T:
            print("calling row getitem")
            index: int = self.map_index(self.row_index, column_index)
            print(index)
            if column_index >= self.num_columns:
                raise IndexError
            return self._array[index]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            print("calling set item")
            index: int = self.map_index(self.row_index, column_index)
            print(index)
            print(value)
            if column_index >= self.num_columns:
                raise IndexError

            self._array[index] = value
        
        def __iter__(self) -> Iterator[T]:
            for column_index in range(self.num_columns):
                yield self[column_index]
        
        def __reversed__(self) -> Iterator[T]:
            for column_index in reversed(range(self.num_columns)):
                yield self[column_index]

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        self.data_type = data_type
        if not isinstance(starting_sequence, Sequence):
            raise  ValueError
        if not isinstance(data_type,type):
            raise TypeError
        #if starting_sequence is not a sequence, raise ValueError
        #if all of the rows are not sequences, then raise ValueError
        #check that the types are all the same
        #check that all the lengths are the same as starting_sequence[0]

        self.rows_len = len(starting_sequence)
        self.cols_len = len(starting_sequence[0])

        py_list = []
        for row in range(self.rows_len):
            if len(starting_sequence[row]) == self.cols_len:
                for col in range (self.cols_len):
                    if isinstance (starting_sequence[row][col], self.data_type):
                        py_list.append(starting_sequence[row][col])
                    else:
                        raise ValueError
            else:
                raise ValueError


        self.elements2d = Array(py_list,self.data_type)

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:

        pylist2D: List[List[T]] = []
        data_type()

        for row in range(rows):
            pylist2D.append([])
            for col in range(cols):
                pylist2D[row].append(data_type())

        return Array2D(starting_sequence=pylist2D, data_type=data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        print("Calling getitem")
        if row_index >= self.rows_len:
            raise IndexError
        return Array2D.Row(row_index, self.elements2d, self.cols_len, self.data_type)
        
    def __iter__(self) -> Iterator[Sequence[T]]: 
        for column_index in range(self.cols_len):
            yield self[column_index]
    
    def __reversed__(self):
        for column_index in reversed(range(self.cols_len)):
            yield self[column_index]
    
    def __len__(self): 
        return self.rows_len
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.rows_len} Rows x {self.cols_len} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')