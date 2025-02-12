class RandomizedSet:

    #My Attempt

    # def __init__(self):
    #     self.data = set()


    # def insert(self, val: int) -> bool:
    #     if val in self.data:
    #         return False
    #     self.data.add(val)
    #     return True


    # def remove(self, val: int) -> bool:
    #     if val not in self.data:
    #         return False
    #     self.data.remove(val)
    #     return True


    # def getRandom(self) -> int:


    def __init__(self):
        # The HashMap key: value value: index
        self.numMap = {}
        # The List will keep track of the values
        self.numList = []


    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            # add at the end
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res


    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            # get the index of what we are removing
            idx = self.numMap[val]
            # we want to swap with the last value
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            # then remove the lat value in the List itself
            self.numList.pop()
            # update the index
            self.numMap[lastVal] = idx
            # this is O(1) in HashMap
            del self.numMap[val]
        return res


    def getRandom(self) -> int:
        # This is O(1) I just didn't know
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()