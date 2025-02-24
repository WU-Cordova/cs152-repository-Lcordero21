from __future__ import annotations
import os
from typing import Iterator, List, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int) -> None:
            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns

        def map_index(self, row_index: int, column_index) -> int:
            return row_index * self.num_columns + column_index

        def __getitem__(self, column_index: int) -> T:
            #if row and column are out of bounds, raise IndexError
            index: int=self.map_index(self.row_index, column_index)

            return self.array[index]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            index: int=self.map_index(self.row_index, column_index)

            self.array[index] = value
        
        def __iter__(self) -> Iterator[T]:
            raise NotImplementedError('Row.__iter__ not implemented.')
        
        def __reversed__(self) -> Iterator[T]:
            raise NotImplementedError('Row.__reversed__ not implemented.')

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        self.data_type = data_type

        #if starting_sequence is not a sequence, raise ValueError
        #if all of the rows are not sequences, then raise ValueError
        #check that the types are all the same
        #check that all the lengths are the same as starting_sequence[0]

        self.rows_len = len(starting_sequence)
        self.cols_len = len(starting_sequence[0])

        py_list = []
        for row in range(self.rows_len):
            for col in range (self.cols_len):
                py_list.append(starting_sequence[row][col])


        self.elements2d = Array(data_type=data_type)

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
        return Array2D.Row(row_index, self.elements2d, self.cols_len)
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        raise NotImplementedError('Array2D.__iter__ not implemented.')
    
    def __reversed__(self):
        raise NotImplementedError('Array2D.__reversed__ not implemented.')
    
    def __len__(self): 
        raise NotImplementedError('Array2D.__len__ not implemented')
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__num_rows} Rows x {self.__num_columns} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')