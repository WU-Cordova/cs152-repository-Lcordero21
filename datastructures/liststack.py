import os
from datastructures.istack import IStack
from typing import Generic

from datastructures.linkedlist import LinkedList, T

class ListStack[T](Generic[T], IStack[T]): #might be able to write it as "ListStack(IStack[T])"
    """
    ListStack (LinkedList-based Stack)

    """

    def __init__(self, data_type:object) -> None:
        """
        Initializes the ListStack.

        Args:
            data_type (type): The type of data the stack will hold.

        """

        self.count = 0
        self.data_type= data_type
        self._list = LinkedList(self.data_type)

    def push(self, item: T):
        """
        Pushes an item onto the stack.

        Args:
            item (T): The item to push onto the stack.
        
        Raises:
            TypeError: If the item is not of the correct type.

        """
        if not isinstance (item, self.data_type):
            raise TypeError
        
        self._list.append(item) 
        self.count+=1

    def pop(self) -> T:
        """
        Removes and returns the top item from the stack.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.count == 0:
            raise IndexError
        self.count-=1
        return self._list.pop()
        

    def peek(self) -> T:
        """
        Returns the top item from the stack without removing it.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.count == 0:
            return IndexError
        return self._list.front

    @property
    def empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.count == 0

    def clear(self):
        """
        Clears all items from the stack.
        """
        self.count = 0
        self._list.clear()

    def __contains__(self, item: T) -> bool:
        """
        Checks if an item exists in the stack.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item exists in the stack, False otherwise.

        """
        return self._list.__contains__(item)

    def __eq__(self, other) -> bool:
        """
        Compares two stacks for equality.

        Args:
            other (ListStack): The stack to compare with.

        Returns:
            bool: True if the stacks are equal, False otherwise.

        """
        if not isinstance (other, list):
            return self._list.__eq__(other._list)
        else:
            return False

    def __len__(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return self.count

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        return self._list.__str__()

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the stack.

        Returns:
            str: A detailed string representation of the stack.

        """
        return self._list.__repr__()
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
