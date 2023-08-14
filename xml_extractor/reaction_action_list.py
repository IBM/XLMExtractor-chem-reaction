from xml_extractor.parameter import Parameter
from xml_extractor.dataframe import Dataframe
from xml_extractor.validation import Validation
import re

class ReactionActionList:
    """Class related to reaction action list extraction.
    
     Methods:
    getProceduresFromSynthesize(self, year, accessName): Return name, smiles and procedures of reactions with "accessName" pattern in the reactant list tag.
    """

    def __init__(self, root):
        """Initialize the instance of a class.

        Arguments:
        root(str): Root tag for the xml file. Root tag is by default "reaction list".
        """
        self.root = root

    def getProceduresFromSynthesize(self, year, accessName):
        """Main function. It will get the name, smiles and procedures of reactions with "accessName" pattern in the 'reaction action attribute synthesize' string.

        Arguments:
        year(int): Variable int defining the years. 
        accessName(str): Pattern given by user which will be used to search matches at the 'reaction action attribute synthesize' string.
        """
        count = 0
        countlen = []
        smiles = []
        name = []
        procedure = []
        for child in self.root:
                reaction = child
                reactionActionList = reaction[5]
                for reactionAction in reactionActionList.findall('{http://bitbucket.org/dan2097}reactionAction'):
                    if reactionAction.attrib == {'action': 'Synthesize'}:
                        reactionType = reactionAction.find('{http://bitbucket.org/dan2097}phraseText').text
                        
                        validation = Validation()
                        if bool(re.findall(accessName, str(reactionType ))) == True and reactionType  not in validation.filterOut():
                            count+=1
                            parameter = Parameter(reaction)
                            reactionSmiles = parameter.ReactionSmiles()
                            iupacName = parameter.IUPACName()
                            expProc = parameter.getExp()
                            
                            countlen.append(f'Reaction {count}')
                            smiles.append(reactionSmiles)
                            name.append(iupacName)
                            procedure.append(expProc)
                            
                        else:
                            count+=0

        variables = zip(name, smiles, procedure)
        patternProcedure = dict(zip(countlen, variables))

        dataframe = Dataframe()
        data = dataframe.createDataFrame(data=patternProcedure, columns=('compound name', 'smiles', 'experimental procedure'), year=year)

        return data