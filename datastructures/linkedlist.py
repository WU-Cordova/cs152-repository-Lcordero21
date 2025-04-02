from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self._data_type = data_type
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.count = 0


    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        linked_list: LinkedList[T] = LinkedList(data_type) 
        raise NotImplementedError("LinkedList.from_sequence is not implemented")
        #FINSIH!!

    def append(self, item: T) -> None:
        #Check that item's type is of type data_type
        # Instantiate a new node witht the data
        #Append the item at the end
        #Check if empty 
        new_node: LinkedList.Node = LinkedList.Node(data=item)
        if self.empty:
            #Set head and tail to new node
            self.head = self.tail = new_node
        else:
            if self.tail:
                self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.count+=1

    def prepend(self, item: T) -> None:
        new_node: LinkedList.Node = LinkedList.Node(data=item)
        if self.empty:
            self.head = self.tail = new_node
        else:
            if self.tail:
                self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.count+=1

    def insert_before(self, target: T, item: T) -> None:
        # raise a TypeError if target or item are not the correct types
        if type(target) != self._data_type:
            raise TypeError
        # raise a ValueError if target is not in the list

        if self.head and self.head.data == target:
            self.prepend(item)
            return

        travel = self.head

        while travel is not None:
            if travel.data == target:
                break
            
            travel = travel.next

        if travel is None:
            raise ValueError (f"The target item {target} is not in the linked list")
        
        # Create a new_ode with "item"
        # Set travel.previous.next to new_node
        # Set new_node.prev to travel.prev
        # Set new_node.next to travel
        # Set travel.prev to new_node
        # Increase Count

        # What if target is the head? (Check first and just prepend)
        
        


        raise NotImplementedError("LinkedList.insert_before is not implemented")

    def insert_after(self, target: T, item: T) -> None:
        raise NotImplementedError("LinkedList.insert_after is not implemented")

    def remove(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove is not implemented")

    def remove_all(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove_all is not implemented")

    def pop(self) -> T:
        raise NotImplementedError("LinkedList.pop is not implemented")

    def pop_front(self) -> T:
        raise NotImplementedError("LinkedList.pop_front is not implemented")

    @property
    def front(self) -> T:
        if not self.head or self.count == 0:
            raise ValueError ("The Linked List is Empty")
        return self.head.data

    @property
    def back(self) -> T:
        if not self.tail or self.count == 0:
            raise ValueError ("The Linked List is Empty")
        return self.tail.data
        

    @property
    def empty(self) -> bool:
        return self.head is None and self.tail is None and self.count == 0
        #can also check the count 

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        raise NotImplementedError("LinkedList.clear is not implemented")

    def __contains__(self, item: T) -> bool:
        raise NotImplementedError("LinkedList.__contains__ is not implemented")

    def __iter__(self) -> ILinkedList[T]:
        raise NotImplementedError("LinkedList.__iter__ is not implemented")

    def __next__(self) -> T:
        raise NotImplementedError("LinkedList.__next__ is not implemented")
    
    def __reversed__(self) -> ILinkedList[T]:
        raise NotImplementedError("LinkedList.__reversed__ is not implemented")
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("LinkedList.__eq__ is not implemented")

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
