class SearchBinTree:
    def __init__(self, valeur):
        self.v = valeur
        self.fg = None
        self.fd = None

    def CreateChild(self,valeur):
        if valeur > self.v:
            if self.fd == None:
                self.fd = SearchBinTree(valeur)
            else:
                return SearchBinTree.CreateChild(self.fd, valeur)
        if valeur < self.v:
            if self.fg == None:
                self.fg = SearchBinTree(valeur)
            else:
                return SearchBinTree.CreateChild(self.fg, valeur)

    def get_v(self):
        return self.v

    def get_LeftChild(self):
        return self.fg

    def get_RightChild(self):
        return self.fd

    def size(self):
        if self == None:
            return 0
        else:
            return(1+SearchBinTree.size(self.fg)+SearchBinTree.size(self.fd))

    def height(self):
        if self == None:
            return 0
        else:
            return(1+max(SearchBinTree.height(self.fg),SearchBinTree.height(self.fd)))

    def affiche(self):
        """permet d'afficher un arbre"""
        if self==None:
            return None
        else :
            return [self.v,SearchBinTree.affiche(self.fg),SearchBinTree.affiche(self.fd)]
    
    # Method allowing to check the existence of a value in the tree
    
    def searchValue(self, valeur): 
        if self == None: # Return False when the value doesn't exist
            return False
        elif valeur == self.v: # Return True when the value is found
            return True
        elif valeur > self.v:
            return SearchBinTree.searchValue(self.fd, valeur)
        elif valeur < self.v:
            return SearchBinTree.searchValue(self.fg, valeur)




rc = SearchBinTree(6) # New Instance ( = Root value )

rc.CreateChild(8)
rc.CreateChild(2)
rc.CreateChild(1)
rc.CreateChild(5)

""" Tests """

print(rc.affiche())
print(rc.size())

print(rc.searchValue(8)) # Presente in this tree
print(rc.searchValue(1165)) # Not presente in this tree

