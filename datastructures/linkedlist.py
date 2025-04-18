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
        for item in sequence:
            if not isinstance(item, data_type):
                raise TypeError
        if sequence is None:
            raise TypeError
    
        linked_list: LinkedList[T] = LinkedList(data_type) 
        for item in sequence:
            linked_list.append(item)
        return linked_list


    def append(self, item: T) -> None:
        # Check that item's type is of type data_type
        # Instantiate a new node witht the data
        # Append the item at the end
        # Check if empty 
        if not isinstance (item, self._data_type):
            raise TypeError
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
        if not isinstance (item, self._data_type):
            raise TypeError
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
        if not isinstance (target, self._data_type):
            raise TypeError
        if not isinstance (item, self._data_type):
            raise TypeError

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
        
        new_node: LinkedList.Node = LinkedList.Node(data=item)
        # Create a new_ode with "item"
        travel.previous.next = new_node
        # Set travel.previous.next to new_node
        new_node.previous = travel.previous
        # Set new_node.prev to travel.prev
        new_node.next = travel
        # Set new_node.next to travel
        # Set travel.prev to new_node
        travel.previous = new_node
        # Increase Count
        self.count += 1

        # What if target is the head? (Check first and just prepend)

    def insert_after(self, target: T, item: T) -> None:
                # raise a TypeError if target or item are not the correct types
        if not isinstance (target,self._data_type):
            raise TypeError
        if not isinstance (item, self._data_type):
            raise TypeError
        # raise a ValueError if target is not in the list

        if self.tail and self.tail.data == target:
            self.append(item)
            return

        travel = self.head

        while travel is not None:
            if travel.data == target:
                break
            
            travel = travel.next

        if travel is None:
            raise ValueError (f"The target item {target} is not in the linked list")
        
        new_node: LinkedList.Node = LinkedList.Node(data=item)
        new_node.next = travel.next
        new_node.previous = travel
        travel.next.previous = new_node
        travel.next = new_node
        self.count += 1

    def remove(self, item: T) -> None: #COMPLETE THIS
        #iterate to find item
        if not isinstance (item, self._data_type):
            raise TypeError
        travel_node= self.head
        while travel_node is not None:
            if travel_node.data == item:
                travel_node.previous.next = travel_node.next
                travel_node.next.previous = travel_node.previous
                self.count-=1
                return
            travel_node = travel_node.next
        raise ValueError

    def remove_all(self, item: T) -> None: #COMPLETE THIS?
                #iterate to find item
        if not isinstance (item, self._data_type):
            raise TypeError
        travel_node= self.head
        while travel_node:
            if travel_node.data == item:
                if travel_node.next is not None:
                    travel_node.next.previous = travel_node.previous 
                if travel_node.previous is not None:
                    travel_node.previous.next = travel_node.next
                self.count-=1
            travel_node = travel_node.next
        return

    def pop(self) -> T:
        if self.count == 0:
            raise IndexError #DOUBLE CHECK
        data = self.tail.data
        if self.tail != self.head:
            self.tail = self.tail.previous
            self.tail.next = None
            self.count -= 1
            return data
        else:
            self.head = None
            self.tail = None
            self.count -= 1
            return data

    def pop_front(self) -> T:
        if self.count == 0:
            raise IndexError #DOUBLE CHECK
        data = self.head.data
        if self.tail != self.head:
            self.head = self.head.next
            self.head.previous = None
        elif self.tail == self.head:
            self.head = self.tail = None
        self.count -= 1
        return data

    @property
    def front(self) -> T:
        if not self.head or self.count == 0:
            raise IndexError ("The Linked List is Empty")
        return self.head.data

    @property
    def back(self) -> T:
        if not self.tail or self.count == 0:
            raise IndexError ("The Linked List is Empty")
        return self.tail.data
        

    @property
    def empty(self) -> bool:
        return self.head is None and self.tail is None and self.count == 0
        #can also check the count 

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.count = 0

    def __contains__(self, item: T) -> bool:
        if not isinstance (item,self._data_type):
            raise TypeError
        travel_node= self.head
        while travel_node:
            if item == travel_node.data:
                return True
            travel_node = travel_node.next
        return False


    def __iter__(self) -> ILinkedList[T]:
        self.travel_node = self.head
        return self

    def __next__(self) -> T:
        if self.travel_node is None:
            raise StopIteration
        data = self.travel_node.data
        self.travel_node = self.travel_node.next
        return data
        
    
    def __reversed__(self) -> ILinkedList[T]: #FINISH
        if self.travel_node is None:
            raise StopIteration
        data = self.travel_node.data
        self.travel_node = self.travel_node.previous
        yield data
    
    def __eq__(self, other: object) -> bool:
        if self._data_type != other._data_type:
            raise TypeError
        if self.count != other.count:
            return False
        travel_node_self= self.head
        travel_node_other = other.head

        while travel_node_self:
            if travel_node_self.data != travel_node_other.data:
                return False
            travel_node_other = travel_node_other.next
            travel_node_self = travel_node_self.next
        return True

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
