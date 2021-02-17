class SearchBinTree:
    def __init__(self, value):
        self.v = value
        self.LeftChild = None
        self.RightChild = None

    def CreateChild(self,value):
        if value > self.v:
            if self.RightChild == None:
                self.RightChild = SearchBinTree(value)
            else:
                return SearchBinTree.CreateChild(self.RightChild, value)
        if value < self.v:
            if self.LeftChild == None:
                self.LeftChild = SearchBinTree(value)
            else:
                return SearchBinTree.CreateChild(self.LeftChild, value)

    def get_v(self):
        return self.v

    def get_LeftChild(self):
        return self.LeftChild

    def get_RightChild(self):
        return self.RightChild

    def size(self):
        if self == None:
            return 0
        else:
            return(1+SearchBinTree.size(self.LeftChild)+SearchBinTree.size(self.RightChild))

    def height(self):
        if self == None:
            return 0
        else:
            return(1+max(SearchBinTree.height(self.LeftChild),SearchBinTree.height(self.RightChild)))

    def display(self):
        """ Allow to display the tree in the form of lists """
        if self==None:
            return None
        else :
            return [self.v,SearchBinTree.display(self.LeftChild),SearchBinTree.display(self.RightChild)]
    
    # Method allowing to check the existence of a value in the tree
    
    def searchValue(self, value): 
        if self == None: # Return False when the value doesn't exist
            return False
        elif value == self.v: # Return True when the value is found
            return True
        elif value > self.v:
            return SearchBinTree.searchValue(self.RightChild, value)
        elif value < self.v:
            return SearchBinTree.searchValue(self.LeftChild, value)


""" Tests """ 
          
rc = SearchBinTree(6) # New Instance ( = Root value )

rc.CreateChild(8)
rc.CreateChild(2)
rc.CreateChild(1)
rc.CreateChild(5)

print(rc.display())
print(rc.size())

print(rc.searchValue(8)) # Presente in this tree
print(rc.searchValue(1165)) # Not presente in this tree
