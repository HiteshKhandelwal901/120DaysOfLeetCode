class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counter = 0
        self.lrumap = dict()



    def get(self, key: int) -> int:
        if key in self.lrumap.keys():
            #print("key found")
            val = self.lrumap[key]
            self.move(key)
            return val
        else:
            return -1



    def put(self, key: int, value: int) -> None:

        self.counter = self.counter+1
        if len(self.lrumap) < self.capacity:
            self.add(key, value)
            self.move(key)

        else:
            if key in self.lrumap.keys():

                self.add(key, value)
                self.move(key)
            else:

                self.evict(key)
                self.add(key, value)


    def add(self, key: int, value: int) -> None:
        self.lrumap[key] = value



    def move(self, key) -> None:
        val = self.lrumap[key]
        self.remove(key)
        self.add(key, val)




    def remove(self, key) -> None:
        del self.lrumap[key]



    def evict(self, key) -> None:
        key = list(self.lrumap.keys())[0]
        self.remove(key)






# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
