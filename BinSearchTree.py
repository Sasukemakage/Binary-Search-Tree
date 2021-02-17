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

    def taille(self):
        if self == None:
            return 0
        else:
            return(1+SearchBinTree.taille(self.fg)+SearchBinTree.taille(self.fd))

    def hauteur(self):
        if self == None:
            return 0
        else:
            return(1+max(SearchBinTree.hauteur(self.fg),SearchBinTree.hauteur(self.fd)))

    def affiche(self):
        """permet d'afficher un arbre"""
        if self==None:
            return None
        else :
            return [self.v,SearchBinTree.affiche(self.fg),SearchBinTree.affiche(self.fd)]
    # Méthode permettant de vérifier l'existence d'une valeur dans l'arbre
    def searchValue(self, valeur): 
        if self == None: # Renvoie False si la valeur n'existe pas
            return False
        elif valeur == self.v: # Renvoie True lorsque l'on trouve la valeur
            return True
        elif valeur > self.v:
            return SearchBinTree.searchValue(self.fd, valeur)
        elif valeur < self.v:
            return SearchBinTree.searchValue(self.fg, valeur)




rc = SearchBinTree(6) # Valeur de la racine

rc.CreateChild(8)
rc.CreateChild(2)
rc.CreateChild(1)
rc.CreateChild(5)

""" Tests """

print(rc.affiche())
print(rc.taille())

print(rc.searchValue(8)) # Présent dans l'arbre
print(rc.searchValue(1165)) # Non présent dans l'arbre

