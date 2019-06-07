from Block import Block;


initialTransactions = {"This is initial Transaction","And My details"};
initialBlock = Block(0, initialTransactions);

block2Transactions = {"This is my second transaction", "My transaction details"};
block2 = Block(initialBlock.getBlockHash(), block2Transactions);


print("block 1", initialBlock.getBlockHash())
print("block 2", block2.getBlockHash())

