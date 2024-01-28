from dataclasses import dataclass, field
import typing as t

class LRU:
    def __init__(self):
        self.head: CacheObject = None
        self.tail: CacheObject = None

    def exists(self, obj):
        if obj._prev or obj._next:
            return True
        return False

    def hit(self, obj):
        """Hits (used) gets sent to head"""
        if not self.head:
            self.head = obj
            self.tail = obj
            return

        if not self.exists(obj):
            self.head._prev = obj
            obj._next = self.head  
            self.head = obj  
            return   
        else:
            if obj == self.head:
                return
            
            if obj == self.tail:
                self.tail = obj._prev
            

            if obj._prev:
                obj._prev._next = obj._next
            if obj._next:
                obj._next._prev = obj._prev   

            obj._next = self.head
            obj._prev = None  
            self.head._prev = obj
            self.head = obj


    def get_lru_and_remove(self):
        if not self.head:
            return
        
        
        h = self.tail

        new_tail = self.tail._prev


        self.tail = new_tail
        self.tail._next = None

        return h

    def __repr__(self):
        result = []
        current = self.head
        while current:
            #result.append(f'({"" if current._prev is None else str(current._prev.key) }, {str(current.key)}, {"" if current._next is None else str(current._next.key)})')
            result.append(str(current.key))
            current = current._next
        return " -> ".join(result)
        
@dataclass
class CacheObject:
    key: any
    value: any
    hits: int = field(init=False, default=0) # automatically starts at 0 hits
    _next: 'CacheObject' = None
    _prev: 'CacheObject' = None

    def hit(self, lru: LRU):
        self.hits += 1
        lru.hit(self)

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity:int = capacity
        self.cache: t.Dict[any, CacheObject] = {}
        self.size:int = 0
        self.LRU: LRU = LRU()


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache.keys():
            self.cache[key].hit(lru = self.LRU)
            return self.cache[key].value
        
        return -1

    def set(self, key, value):
        if key is None:
            raise Exception('Key cannot be None')
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache.keys():
            self.cache[key].hit(lru=self.LRU) # if key exists then just hit and return
            return self.cache[key].value
        else:
            # otherwise check if we have capacity, if yes just add and hit. Otherwise remove least used and add
            new = CacheObject(key, value)

            if not self.LRU:
                self.LRU = new

            #print(self.size, self.capacity)
            if self.size >= self.capacity: 
                obj_to_remove = self.LRU.get_lru_and_remove()
                del self.cache[obj_to_remove.key]
            
            new.hit(lru = self.LRU)
            self.cache[key] = new
            self.size += 1
            return new.value
            
            
            


            
our_cache = LRU_Cache(5)

# LRU tests
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

# assert our_cache.LRU.__repr__() == '4 -> 3 -> 2 -> 1', 'LRU linked list is not correct'
our_cache.get(0)

# Get from tail
t1 = our_cache.get(1)       # returns 1
assert t1 == 1, 'get() method does not return the right value'
assert our_cache.LRU.__repr__() == '1 -> 4 -> 3 -> 2', 'LRU linked list is not correct'

# Get from head
t2 = our_cache.get(1)
assert t2 == 1, 'get() method does not return the right value'
assert our_cache.LRU.__repr__() == '1 -> 4 -> 3 -> 2', 'LRU linked list is not correct'

# Get from middle
t3 = our_cache.get(3)
assert t3 == 3, 'get() method does not return the right value'
assert our_cache.LRU.__repr__() == '3 -> 1 -> 4 -> 2', 'LRU linked list is not correct'

t4 = our_cache.get(0)
assert t4 == -1, 'get() method does not return the right value'
assert our_cache.LRU.__repr__() == '3 -> 1 -> 4 -> 2', 'LRU linked list is not correct'

our_cache.set(5, 5) # reaches limit
assert our_cache.LRU.__repr__() == '5 -> 3 -> 1 -> 4 -> 2', 'LRU linked list is not correct'

our_cache.set(10, 10) # its limit. 2 should be removed
assert our_cache.LRU.__repr__() == '10 -> 5 -> 3 -> 1 -> 4', 'LRU linked list is not correct'


t = our_cache.get(2) # return -1 because its been removed as it was least recently used
assert t == -1, 'get() method does not return the right value'
assert our_cache.LRU.__repr__() == '10 -> 5 -> 3 -> 1 -> 4', 'LRU linked list is not correct'

# check get None should return -1
t = our_cache.get(None)
assert t == -1, 'get() method does not return the right value'
assert our_cache.LRU.__repr__() == '10 -> 5 -> 3 -> 1 -> 4', 'LRU linked list is not correct'

# check set None
try:
    our_cache.set(None, 1)
    print('NOT PASSED')
except Exception as e:
    if str(e) == 'Key cannot be None':
        pass
