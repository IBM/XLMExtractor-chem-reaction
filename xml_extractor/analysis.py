from xml_extractor.directory import Directory
from xml_extractor.product_list import ProductList
from xml_extractor.reactant_list import ReactantList
from xml_extractor.spectator_list import SpectatorList
from xml_extractor.procedures import Procedure
from xml_extractor.reaction_action_list import ReactionActionList
import xml.etree.ElementTree as ET
import glob
import pandas as pd
from tqdm import tqdm

class Analysis:
    """Class related to analysis
    
    Methods:
    analysis(self, year_start, year_end, access_name, 
        folder_name, input_dir, procedure=True, all_procedure=False,
        product=False, reactant=False, 
        reaction_action_reaction_synthesize=False, 
        reaction_action_procedure_synthesize=False,
        spectator=False): It will perform the analysis of the data. It comprises all 
        the possible analysis implemented on this extraction algorithm.
    """

    def analysis(self, year_start, year_end, access_name, 
        folder_name, input_dir, procedure=False, all_procedure=False,
        product=False, reactant=False,
        reaction_action_procedure_synthesize=False,
        spectator=False):
        """It will perform the analysis of the data. It comprises all 
        the possible analysis implemented on this extraction algorithm.
        
        Arguments:
        year_start(int): sys.argv[1], start year.
        year_end(int): sys.argv[2], end year.
        access_name(str): sys.argv[3], desired pattern.
        folder_name(str): Name of the folder that contains the output data.
        input_dir(str): Name of the folder that contains the input data."""

        year = year_start
        while year <= year_end:

            dir = Directory(input_dir)
            changedPath = dir.changeDirectory(year)
            print(f"Current working directory: {changedPath}")

            polymerReactionsData = []
            for file in tqdm(glob.glob("*.xml"), total=len(glob.glob("*.xml"))):
                tree = ET.parse(file)
                root = tree.getroot()

                if procedure == True:
                    pro = Procedure(root)
                    procedures = pro.getDefinedProcedure(year, access_name, filterOut=False)
                    if procedures is not None:
                        polymerReactionsData.append(procedures)
                    else:
                        continue

                if all_procedure == True:
                    pro = Procedure(root)
                    Allprocedures = pro.getAllProcedures(year, filterOut=False)
                    if Allprocedures is not None:
                        polymerReactionsData.append(Allprocedures)
                    else:
                        continue

                if product == True:
                    pro = ProductList(root)
                    products = pro.getProcedures(year, access_name)
                    if products is not None:
                        polymerReactionsData.append(products)
                    else:
                        continue

                if reactant == True:
                    react = ReactantList(root)
                    reactants = react.getProcedures(year, access_name)
                    if reactants is not None:
                        polymerReactionsData.append(reactants)
                    else:
                        continue

                if reaction_action_procedure_synthesize == True:
                    react = ReactionActionList(root)
                    procedure = react.getProceduresFromSynthesize(year, access_name)
                    if procedure is not None:
                        polymerReactionsData.append(procedure)
                    else:
                        continue

                if spectator == True:
                    react = SpectatorList(root)
                    reactants = react.getProcedures(year, access_name)
                    if reactants is not None:
                        polymerReactionsData.append(reactants)
                    else:
                        continue

            polymerReactionsData = pd.concat(polymerReactionsData, ignore_index=True)
            polymerReactionsData.to_csv(f'..\{folder_name}\smiles_{year}.csv', index=False)
            year+=1
        
        return