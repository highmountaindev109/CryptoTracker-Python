from constants import *

def __init__(self, sizeOfArray, arrayType = int):
    self.sizeOfArray = len(list(map(arrayType, range(sizeOfArray))))
    self.arrayItems =[arrayType(0)] * sizeOfArray    # initialize array with zeroes
    self.arrayType = arrayType

def __str__(self):
    return ' '.join([str(i) for i in self.arrayItems])

def __len__(self):
    return len(self.arrayItems)

# magic methods to enable indexing
def __setitem__(self, index, data):
    self.arrayItems[index] = data

def __getitem__(self, index):
    return self.arrayItems[index]

# function for search
def search(self, keyToSearch):
    for i in range(self.sizeOfArray):
        if (self.arrayItems[i] == keyToSearch):      # brute-forcing
            return i                                 # index at which element/ key was found

    return -1                                        # if key not found, return -1
# any array init
def init_array():
    arr = []
    arr.append(CRV)
    arr.append(CVC)
    arr.append(CELO)
    arr.append(AR)
    arr.append(FIXED)
    return arr
    
# function for inserting an element
def insert(self, keyToInsert, position):
    if(self.sizeOfArray > position):
        for i in range(self.sizeOfArray - 2, position - 1, -1):
            self.arrayItems[i + 1] = self.arrayItems[i]
        self.arrayItems[position] = keyToInsert
    else:
        print('Array size is:', self.sizeOfArray)

# function to delete an element
def delete(self, keyToDelete, position):
    if(self.sizeOfArray > position):
        for i in range(position, self.sizeOfArray - 1):
            self.arrayItems[i] = self.arrayItems[i + 1]
        self.arrayItems[i + 1] = self.arrayType(0)
    else:
        print('Array size is:', self.sizeOfArray)


