import pandas as pd
import glob
import os

class Dataframe:
    """Class related to dataframe manipulation
    
    Methods:
    createDataFrame(self, data, columns, year): It will create a dataframe with the all the information acquired from the xml files.
    concatDataFrame(self, folder_name): It will concatenate all the dataframes created with the information acquired form the xml files.
    removeDuplicates(self): It will remove all the duplicates obtained in the information acquired form the xml files.   
    """

    def createDataFrame(self, data, columns, year):
        """
        Function built to support main functions. It will create a dataframe with the all the information acquired from the xml files.

        Arguments:
        df(dataframe): Input dataframe.
        columns(list): Variable related to all the information acquired from the xml files.
        year(int): Variable int defining the years.
        """ 
        result = pd.DataFrame.from_dict(data, orient='index', columns=columns)
        result.index.names = [year]
        return result

    def concatDataFrame(self, folder_name):
        """Function built to support main functions. It will concatenate all the dataframes created with the information acquired form the xml files.

        Arguments:
        folder_name(str): Name of the folder that contains the output data.
        """

        path = "..\\" + folder_name
        os.chdir(path)
        files = glob.glob("smiles_[0-9]*.csv")

        dataList = []

        for file in files:
            df = pd.read_csv(file, index_col=None, header=0)
            dataList.append(df)

        frame = pd.concat(dataList, axis=0, ignore_index=True)
        return frame

    def removeDuplicates(self):
        """Function built to support main functions. It will remove all the duplicates obtained in the information acquired form the xml files."""
        
        frame = pd.read_csv('smiles_all.csv', sep=',', index_col=0)
        frame = frame.drop_duplicates(subset=['smiles'])
        frame.to_csv('smiles_all_notdup.csv')
        return frame