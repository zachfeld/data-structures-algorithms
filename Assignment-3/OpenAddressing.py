class openAddress:
    def __init__(self, size):
        self.size = size
        self.table = {}
        for i in range(size):
            self.table[i] = None

    def __repr__(self):
        return str(self.table)

    #inserts value into table
    #returns true on success, false on failure
    def insert(self, value):
        #if table is x amount full, double it
        self.checkDouble()

        #make hash of value
        trial = 0
        
        #trials for the entirety of the hash 
        while trial <= len(self.table):
            hashValue = self.hashWithTrial(value, trial)
            #TODO: fix another value being in the slot, maybe != None
            if self.table[hashValue] is None or self.table[hashValue] == value:
                self.table[hashValue] = value
                return True

            trial = trial + 1
        
        print('hash overflow, can not insert')
        return False
    
    #searches for value in table
    #returns an int with the index of the value
    def search(self, value):
        trial = 0

        #not appropriate to search for none
        if value is None:
            return None
        
        #probably need a check for none in this while loop
        while trial <= len(self.table):
            hashValue = self.hashWithTrial(value, trial)
            if self.table[hashValue] == value:
                return hashValue
            trial = trial + 1

        return None

    #deletes value from table
    #returns true if deleted, false if not
    def delete(self, value):

        deleteIndex = self.search(value)

        #TODO: value could also already be 'DELETED'
        if deleteIndex is not None:
            self.table[deleteIndex] = 'DELETED'    
        else:
            print('value not deleted')

        self.checkHalve()

    #hashes a value and with its trial value
    #returns an int with the hash value mapped to the size of the table
    def hashWithTrial(self, value, trial):
        #returns the hash value of an object, ensure it is within length of dictionary
        return hash(str(value) + str(trial)) % len(self.table)

    #decides if table needs to be doubled or halved
    def checkDouble(self):

        #gather how many not-null values in dictionary
        numFull = 0
        for index in self.table:
            if self.table[index] is not None:
                numFull = numFull + 1

        #if the table is half full, double it's size
        if numFull > (len(self.table) / 2):
            self.doubleTable()
       
    
    def checkHalve(self):
        #gather how many deleted values in dictionary
        numDeleted = 0
        for index in self.table:
            if self.table[index] == 'DELETED':
                numDeleted = numDeleted + 1

        #if the deleted values are greater than 1/4 of the table size
        #halve the table
        if numDeleted > (len(self.table) / 4):
            self.halveTable()

    def doubleTable(self):
        tempTable = {}

        #copy current values to table
        for i in range(len(self.table)):
            tempTable[i] = self.table[i]

        #double the size of the table and reset all spaces to None
        for i in range(len(tempTable) * 2):
            self.table[i] = None
        
        #iterate through table, and rehash all new values to the new size of table
        for i in range(len(tempTable)):
            if tempTable[i] != None and tempTable[i] != 'DELETED':
                self.insert(tempTable[i])

        return

    def halveTable(self):
        tempTable = {}

        size = len(self.table)
        halfSize = int(size // 2)

        #copy values from original to temp
        for index in self.table:
            tempTable[index] = self.table[index]

        #set first half of table to None
        for i in range(halfSize + 1):
            self.table[i] = None

        #remove values from the second half of the table
        for i in range(halfSize + 1, halfSize * 2):
            del self.table[i]

        #rehash all non-null and non deleted values to new smaller table size
        for i in range(0, len(tempTable)):
            if tempTable[i] is not None and tempTable[i] != 'DELETED':
                self.insert(tempTable[i])




table = openAddress(5)

print(table)

table.insert(3402)
print(table)
table.insert(40141)
print(table)
table.insert(42984)
print(table)
table.insert('bob')
print(table)
table.insert(41824)
print(table)
table.insert(32)
print(table)
table.insert(441)
print(table)

table.delete(3402)
print(table)
table.delete(40141)
print(table)
table.delete(42984)
print(table)
table.delete('bob')
print(table)
table.delete(41824)
print(table)
table.delete(32)
print(table)
table.insert(441)
print(table)