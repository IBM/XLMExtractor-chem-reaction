from xml_extractor.parameter import Parameter
from xml_extractor.dataframe import Dataframe
import re

class ReactantList:
    """Class related to reactant list extraction.

    Methods:
    getProcedures(self, year, accessName): Return name, smiles and procedures of reactions with "accessName" pattern in the reactant list tag.
    """

    def __init__(self, root):
        """Initialize the instance of a class.

        Arguments:
        root(str): Root tag for the xml file. Root tag is by default "reaction list".
        """
        self.root = root

    def getProcedures(self, year, accessName):
        """Main function. It will get the name, smiles and procedures of reactions with "accessName" pattern in the reactant list tag.

        Arguments:
        year(int): Variable int defining the years. 
        accessName(str): Pattern given by user which will be used to search matches at the reactant list tag.
        """
        count = 0
        countlen = []
        smiles = []
        name = []
        reactant = []
        procedure = []
        for child in self.root:
                reaction = child
                for i in range(len(reaction[3])):
                    if len(reaction[3][i][0]) == 1:
                        molName = reaction[3][i][0][0].text
                    else:
                        molName = reaction[3][i][0][1].text

                    if bool(re.findall(accessName, str(molName))) == True:
                        count+=1
                        parameters = Parameter(reaction)
                        reactionSmiles = parameters.ReactionSmiles()
                        iupacName = parameters.IUPACName()
                        expProc = parameters.getExp()
                                    
                        countlen.append(f'Reaction {count}')
                        smiles.append(reactionSmiles)
                        reactant.append(molName)
                        name.append(iupacName)
                        procedure.append(expProc)
                                    
                    else:
                        count+=0

        variables = zip(reactant, name, smiles, procedure)
        patternProcedure = dict(zip(countlen, variables))

        df = Dataframe()
        data = df.createDataFrame(data=patternProcedure, columns=('reactant name', 'compound name', 'smiles', 'experimental procedure'), year=year)
        return data