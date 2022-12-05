class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key):
        if not self.contains(key):
            self.set.append(key)

    def remove(self, key):
        try:
            self.set.remove(key)
        except:
            pass

    def contains(self, key):
        return key in self.set
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)