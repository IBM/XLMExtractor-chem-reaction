from xml_extractor.parameter import Parameter
from xml_extractor.dataframe import Dataframe
from xml_extractor.validation import Validation
import re

class Procedure:
    """Class related to procedure extraction.

    Methods:
    getAllProcedures(self, year): Return the name, smiles and procedures of all reactions in the xml files.
    getDefinedProcedure(self, year, accessName, filterOut=False): Return the name, smiles and procedures of reactions with "accessName" pattern in the experimental procedure string.
    """

    def __init__(self, root):
        """Initialize the instance of a class.

        Arguments:
        root(str): Root tag for the xml file. Root tag is by default "reaction list".
        """
        self.root = root
    
    def getAllProcedures(self, year):
        """Main function. It will get the name, smiles and procedures of all reactions in the xml files.

        Arguments:
        year(int): Variable int defining the years. 
        """
        count = 0
        countlen = []
        smiles = []
        name = []
        procedure = []
        for child in self.root:
            reaction = child
            count+=1
            parameter = Parameter(reaction)
            expProc = parameter.getExp()
            reactionSmiles = parameter.ReactionSmiles()
            iupacName = parameter.IUPACName()

            countlen.append(f'Reaction {count}')
            procedure.append(expProc)
            smiles.append(reactionSmiles)
            name.append(iupacName)

        variables = zip(name, smiles, procedure)
        patternProcedure = dict(zip(countlen, variables))

        dataframe = Dataframe()
        data = dataframe.createDataFrame(df=patternProcedure, columns=('compound name', 'smiles', 'experimental procedure'), year=year)
        
        return data

    def getDefinedProcedure(self, year, accessName, filterOut=False):
        """Main function. It will get the name, smiles and procedures of reactions with "accessName" pattern in the experimental procedure string.

        Arguments:
        year(int): Variable int defining the years. 
        accessName(str): Pattern given by user which will be used to search matches at the experimental procedure string.
        filterOut(boolean): If True, it will filter out reactants and spectators with the same keyword search. Default False.
        """
        count = 0
        pattern = []
        countlen = []
        smiles = []
        name = []
        for child in self.root:
            reaction = child
            parameter = Parameter(reaction)
            expProc = parameter.getExp()
            validation = Validation()
            if filterOut == True:
                if bool(re.findall(accessName, str(expProc))) == True and accessName not in validation.filterOutReactant(self.root, year, accessName) and accessName not in validation.filterOutSpectator(self.root, year, accessName):
                    count+=1
                    reactionSmiles = parameter.ReactionSmiles()
                    iupacName = parameter.IUPACName()
                        
                    countlen.append(f'Reaction {count}')
                    pattern.append(expProc)
                    smiles.append(reactionSmiles)
                    name.append(iupacName)
                
                else:
                    count+=0
            elif filterOut == False:
                if bool(re.findall(accessName, str(expProc))) == True:
                    count+=1
                    reactionSmiles = parameter.ReactionSmiles()
                    iupacName = parameter.IUPACName()
                        
                    countlen.append(f'Reaction {count}')
                    pattern.append(expProc)
                    smiles.append(reactionSmiles)
                    name.append(iupacName)
                
                else:
                    count+=0

        variables = zip(name, smiles, pattern)
        patternProcedure = dict(zip(countlen, variables))

        dataframe = Dataframe()
        data = dataframe.createDataFrame(data=patternProcedure, columns=('compound name', 'smiles', 'experimental procedure'), year=year)

        return data