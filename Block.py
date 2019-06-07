import hashlib;

#Created by LavaKumar T

class Block:
    previousHash=0;
    transactions=[];
    blockHash=0;

    def __init__(self, previousHash, transactions):
        self.previousHash = previousHash
        self.transactions = transactions
        result = hashlib.md5(repr(transactions).encode())
        contents = {result.digest(), previousHash}
        self.blockHash = hashlib.md5(repr(contents).encode()).digest()


    def getPreviousHash(self):
        return self.previousHash

    def getBlockHash(self):
        return self.blockHash

    def getTransactions(self):
        return self.transactions