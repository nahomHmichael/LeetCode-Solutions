class MyHashMap:

    def __init__(self):
        self.set = [-1]*1000001

    def put(self, key: int, value: int) -> None:
        self.set[key] = value

    def get(self, key: int) -> int:
        return self.set[key] 

    def remove(self, key: int) -> None:
        try:
            self.set[key] = -1
        except:
            pass

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)