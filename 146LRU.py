class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = []
        self.dic = {}

    def get(self, key: int) -> int:
        if self.q.__contains__(key):
            self.q.remove(key)
            self.q.append(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.q:
            self.q.remove(key)
            self.q.append(key)
            self.dic[key] = value

        elif len(self.q) < self.capacity:
            self.q.append(key)
            self.dic[key] = value
        else:
            self.q.pop(0)
            self.q.append(key)
            self.dic[key] = value


if __name__ == "__main__":
    '''
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    print(lRUCache.get(1))
    lRUCache.put(3, 3)
    print(lRUCache.get(2))
    lRUCache.put(4, 4)
    print(lRUCache.get(1))
    print(lRUCache.get(3))
    print(lRUCache.get(4))
    '''

    lRUCache = LRUCache(2)
    print(lRUCache.get(2))
    lRUCache.put(2, 6)
    print(lRUCache.get(1))
    lRUCache.put(1, 5)
    lRUCache.put(1, 2)
    print(lRUCache.get(1))
    print(lRUCache.get(2))
