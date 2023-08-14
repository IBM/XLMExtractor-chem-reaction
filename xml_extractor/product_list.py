from xml_extractor.parameter import Parameter
from xml_extractor.dataframe import Dataframe
from xml_extractor.validation import Validation
import re

class ProductList:
    """Class related to product list extraction.

    Methods:
    getProcedures(self, year): Return the name, smiles and procedures of all reactions in the xml files.
    """

    def __init__(self, root):
        """Initialize the instance of a class.

        Arguments:
        root(str): Root tag for the xml file. Root tag is by default "reaction list".
        """
        self.root = root

    def getProcedures(self, year, accessName):
        """Main function. It will get the name, smiles and procedures of reactions with "accessName" pattern in the product list tag.

        Arguments:
        year(int): Variable int defining the years. 
        accessName(str): Pattern given by user which will be used to search matches at the product list tag.
        """
        count = 0
        countlen = []
        smiles = []
        name = []
        procedure = []
        for child in self.root:
                reaction = child
                if len(reaction[2][0][0]) == 1:
                    molName = reaction[2][0][0][0].text
                else: 
                    molName = reaction[2][0][0][1].text

                validation = Validation()
                if bool(re.findall(accessName, str(molName))) == True and molName not in validation.filterOut():
                    count+=1
                    parameters = Parameter(reaction)
                    reactionSmiles = parameters.ReactionSmiles()
                    iupacName = parameters.IUPACName()
                    expProc = parameters.getExp()
                            
                    countlen.append(f'Reaction {count}')
                    smiles.append(reactionSmiles)
                    name.append(iupacName)
                    procedure.append(expProc)
                            
                else:
                    count+=0

        variables = zip(name, smiles, procedure)
        patternProcedure = dict(zip(countlen, variables))

        df = Dataframe()
        data = df.createDataFrame(data=patternProcedure, columns=('compound name', 'smiles', 'experimental procedure'), year=year)
        return data