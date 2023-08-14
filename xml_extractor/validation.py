import pandas as pd 
import re
from xml_extractor.reactant_list import ReactantList
from xml_extractor.spectator_list import SpectatorList

class Validation:
    """Class related to result validation.

    Methods:
    filterOut(self): Filter out every string on list.
    filterOutReactant(self, root, year, accessName): Filter out all data from reactant list.
    filterOutSpectator(self, root, year, accessName): Filter out all data from spectator list.
    getClasses(self): Comprise a list of polymer classes to analysis.
    separateClasses(self, df): Separate in diferent dataframes all classes in getClasses() function.
    separateCopolymers(self, df): Returns only possible copolymer data.
    separateHomopolymers(self, df): Returns only possible homopolymer data.
    checkName(self, accessName, df): Filter out from a df all results from filterOut() function.
    """

    def filterOut(self):
        """Filter out every string on list."""
        words = ['polymer', 'resultant polymer']

        return words

    def filterOutReactant(self, root, year, accessName):
        """Filter out all data from reactant list.

        Arguments:
        root(str): Root tag for the xml file. Root tag is by default "reaction list".
        year(int): Variable int defining the years. 
        accessName(str): Pattern given by user which will be used to search matches at the spectator list tag.
        """
        reactantList = ReactantList(root)
        reactant = reactantList.getProcedures(year, accessName)

        return reactant

    def filterOutSpectator(self, root, year, accessName):
        """Filter out all data from spectator list.

        Arguments:
        root(str): Root tag for the xml file. Root tag is by default "reaction list".
        year(int): Variable int defining the years. 
        accessName(str): Pattern given by user which will be used to search matches at the spectator list tag.
        """
        spectatorList = SpectatorList(root)
        spectator = spectatorList.getProcedures(year, accessName)
        
        return spectator

    def getClasses(self):
        """Comprise a list of polymer classes to analysis."""
        classes = ['polyacrylamide', 'polyacrylate', 'polyacrylonitrile', 'polyadipate',
                'polyalkene', 'polyamide', 'polyanhydride', 'polybutadiene', 'polybutenedioate', 
                'polycarbonate', 'cellulose', 'polychloroolefin', 'polycyanoacrylate',
                'polydiene', 'polydiglycidyl', 'diglycidyl ether', 'polyepoxide', 
                'polyester', 'polyether', 'ether cellulose', 'polyethersulfone', 'polyfumarate',
                'polyglycol', 'polyhalodiene', 'polyhaloolefin', 'polyhalostyrene', 'polyhydroxyether', 
                'polyhydroxymethacrylate', 'polyisocyanate', 'polyisophthalate', 'polyisoprene',
                'polyitaconate', 'polyketone', 'polylactam', 'polymethacrylamide', 'polymethacrylate',
                'polymethylenesuccinate', 'polymethylstyrene', 'polyolefin', 'polyoxyalkylene',
                'polynitrile', 'nylon', 'polyphenoxy', 'polyphenylene', 'polyphenylether',
                'polyphenylsulfone', 'polyphenylthioether', 'polypropenoate', 'polysebacate', 
                'polysiloxane', 'polystyrene', 'polysuccinate', 'polysulfone', 'polyterephthalate',
                'polythioether', 'polysulfide', 'polyurethane', 'polyvinylalcohol', 'polyvinylester', 
                'polyvinylether', 'polyvinylhalide', 'polyvinylketone', 'polyvinylsulfide', 'styrene']

        return classes

    def separateClasses(self, df):
        """Separate in diferent dataframes all classes in getClasses() function.

        Arguments:
        df(dataframe): Dataframe of interest.
        """

        for i in self.getClasses():
            dataClasses = []
            for row in df.itertuples():
                if bool(re.findall(i, str(row[0]), re.IGNORECASE)) == True: # access only one column (smiles)
                    dataClasses.append(row)
                else:
                    continue

            dfClasses = pd.DataFrame(dataClasses, columns=['compound name', 'smiles', 'experimental procedure'])
            if not dfClasses.empty:
                dfClasses.to_csv(f'class_{i}.csv', sep=';', index=False)
            else:
                continue

        return dfClasses

    def separateCopolymers(self, df):
        """Returns only possible copolymer data.

        Arguments:
        df(dataframe): Dataframe of interest.
        """
        copolymer = []
        for row in df.itertuples():
            if bool(re.findall('copolymer', str(row[0]), re.IGNORECASE)) == True:
                copolymer.append(row)
            elif bool(re.findall('\/', str(row[0]))) == True:
                copolymer.append(row)
            else:
                continue

            df_copolymer = pd.DataFrame(copolymer, columns=['compound name', 'smiles', 'experimental procedure'])
            if not df_copolymer.empty:
                df_copolymer.to_csv(f'copolymer.csv', sep=';', index=False)
            else:
                continue

        return df_copolymer

    def separateHomopolymers(self, df):
        """Returns only possible homopolymer data.

        Arguments:
        df(dataframe): Dataframe of interest.
        """
        homopolymer = []
        for row in df.itertuples():
            if bool(re.findall('copolymer', str(row[0]), re.IGNORECASE)) == True:
                continue
            elif bool(re.findall('\/', str(row[0]))) == True:
                continue
            else:
                homopolymer.append(row)

            df_homopolymer = pd.DataFrame(homopolymer, columns=['compound name', 'smiles', 'experimental procedure'])
            if not df_homopolymer.empty:
                df_homopolymer.to_csv(f'homopolymer.csv', sep=';', index=False)
            else:
                continue

        return df_homopolymer

    def checkName(self, accessName, df):
        """Filter out from a df all results from filterOut() function.

        Arguments:
        df(dataframe): Dataframe of interest.
        accessName(str): Pattern given by user which will be used to search matches.
        """
        polymer = []
        for row in df.itertuples():
            if bool(re.findall(accessName, str(row[0]), re.IGNORECASE)) == True and accessName not in self.filterOut():
                polymer.append(row)
            else:
                continue

            df_polymer = pd.DataFrame(polymer, columns=['compound name', 'smiles', 'experimental procedure'])
            if not df_polymer.empty:
                df_polymer.to_csv(f'is_polymer.csv', sep=';', index=False)
                return df_polymer
            else:
                return

