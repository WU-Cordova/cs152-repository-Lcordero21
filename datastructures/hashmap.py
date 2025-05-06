import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib
 
from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets: Array[LinkedList[Tuple[KT,VT]]] = \
            Array(starting_sequence=[LinkedList(data_type=tuple) for _ in range(number_of_buckets)],
                  data_type=LinkedList)
        self._count: int = 0
        self._load_factor: float = load_factor
        self._hash_function = custom_hash_function or self._default_hash_function

    def _get_bucket_index (self, key:KT, bucket_size: int) -> int:
        bucket_index = self._hash_function(key)
        return bucket_index % bucket_size

    def __getitem__(self, key: KT) -> VT:
        for (k,v) in self._buckets[self._get_bucket_index(key, len(self._buckets))]:
            if k == key:
                return v
        raise KeyError
    
    def _resize(self):
        next_size = self._next_prime(len(self._buckets)*2)
        new_array: Array[LinkedList[Tuple[KT,VT]]] = \
            Array(starting_sequence=[LinkedList(data_type=tuple) for _ in range(next_size)],
                  data_type=LinkedList) 
        for bucket in self._buckets:
            for (k,v) in bucket:
                index = self._get_bucket_index(k,next_size)
                new_array[index].append((k,v))
        self._buckets = new_array
        

        #create new array instead with new size instead of using number_of_buckets
        #use next_prime() to find next size
        

    def _next_prime (self, n: int) -> int:

        def is_prime(num:int) -> bool:
            #check if num is less than 2 (return False), check all values between 2 and num to the power of 1/2 plus 1,
            #if num mod i == 0 then return False, because it's not a prime number. Return True after the for loop.
            if num < 2:
                return False
            for i in range (2, int(num**.5)+1):
                if num % i == 0:
                    return False
            return True

        while not is_prime(n):
            n+=1
        return n

    def __setitem__(self, key: KT, value: VT) -> None:        
        if self._count / len(self._buckets) >= self._load_factor:
            self._resize()
        hash_bucket = self._buckets[self._get_bucket_index(key, len(self._buckets))]
        for (k,v) in hash_bucket:
            if k == key:
                hash_bucket.remove((k,v))
                self._count -= 1
        hash_bucket.append((key,value))
        self._count += 1
            


    def keys(self) -> Iterator[KT]:
        #for loop to go through each bucket (use k,_) and a second for loop to go through linked list, and
        #  yield the first part of the tuple (key, value)
        for bucket in self._buckets:
            for (k,_) in bucket:
                yield k
    
    def values(self) -> Iterator[VT]:
        #same as keys() but with other half of tuple
        for bucket in self._buckets:
            for (_,v) in bucket:
                yield v

    def items(self) -> Iterator[Tuple[KT, VT]]:
        #yield the tuple (k,v)
        for bucket in self._buckets:
            for (k,v) in bucket:
                yield (k,v)
            
    def __delitem__(self, key: KT) -> None:
        #be sure to find the value (using get_item) before properly removing the item, can use get bucket 
        # using the key, then use .remove on the key value pair
        hash_bucket = self._buckets[self._get_bucket_index(key, len(self._buckets))]
        for (k,v) in hash_bucket:
            if k == key:
                hash_bucket.remove((k,v))
                self._count -= 1
                return
        raise KeyError
    
    def __contains__(self, key: KT) -> bool:
        bucket_index: int = self._get_bucket_index(key, len(self._buckets))
        bucket_chain: LinkedList = self._buckets[bucket_index]
        for (k,v) in bucket_chain:
            if k == key:
                return True
        return False
    
    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        #exact same as the keys function, just yield the keys
        for bucket in self._buckets:
            for (k,_) in bucket:
                yield k
    
    def __eq__(self, other: object) -> bool:
        #start with checking length and type, and if the key in one is in the other (using the contains function; "in")
        if not isinstance (other, HashMap):
            return False
        if self._count != other._count:
            return False
        if len(self._buckets) != len(other._buckets):
            return False
        
        for bucket in self._buckets:
            for (k,v) in bucket:
                if k not in other:
                    return False
                if v != other[k]:
                    return False
        return True

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)