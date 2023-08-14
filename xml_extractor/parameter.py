class Parameter:
    """Class related to defining parameters that support main functions
    
    Methods:
    IUPACName(self): Function built to support main functions. It will get the IUPAC name from compounds in the xml files.
    ReactionSmiles(self): Function built to support main functions. It will get the reaction smiles from compounds in the xml files.
    getExp(self): Function built to support main functions. It will get the experimental procedure from compounds in the xml files.
    """

    def __init__(self, reaction):
        self.reaction = reaction

    def IUPACName(self):
        """Function built to support main functions. It will get the IUPAC name from compounds in the xml files.
        """
        if len(self.reaction[2][0][0]) == 1:
            name = self.reaction[2][0][0][0].text
        else:
            name = self.reaction[2][0][0][1].text
        return name

    def ReactionSmiles(self):
        """Function built to support main functions. It will get the reaction smiles from compounds in the xml files.
        """
        smiles = self.reaction[1].text
        return smiles

    def getExp(self):
        """Function built to support main functions. It will get the experimental procedure from compounds in the xml files.
        """
        if len(self.reaction[0]) == 2:
            expProc = {self.reaction[0][1].text}
        if len(self.reaction[0]) == 3:
            expProc = {self.reaction[0][2].text}
        if len(self.reaction[0]) == 4:
            expProc = {self.reaction[0][3].text}
        return expProc