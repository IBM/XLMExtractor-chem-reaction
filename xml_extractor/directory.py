import os
import time
from art import *

class Directory:
    """Class related to directory manipulation.

    Methods:
    starting(self, disable=False): Function related to greeting user.
    getDirectory(self): It will get the current working directory and change to 
        directory in which can be found the xml files to analyze.
    changeDirectory(self, year):It will change the directory to defined year.
    createOutputDir(self, year, folder_name): It will create the directory in which would be created outputfiles.
        Directory is by default named "outputDirectory"
    """

    def __init__(self, input_dir):
        """Initiate an instance of a class.
        
        Arguments:
        input_dir(str): Directory in which can be found the xml files to analysis. Directory is by default "grants".
        """
        self.input_dir = input_dir

    def starting(self, disable=False):
        """Function related to greeting user.
        
        Arguments:
        disable=False(boolean): The user may disable this method using this argument."""

        if disable==False:
            logo=text2art("XMLExtractor")
            print(logo)
            time.sleep(1)
            print("-------------------------------------------------")
            print("Extraction is starting...")
            time.sleep(1)        

        return

    def getDirectory(self):
        """Function related to directory manipulation. It will get the current working directory and change to 
        directory in which can be found the xml files to analyze.
        """
        os.chdir(f'{self.input_dir}')
        path = os.getcwd()
        return path

    def changeDirectory(self, year):
        """Function related to directory manipulation. It will change the directory to defined year

        Arguments:
        year(int): Variable int defining the years. 
        """
        print(f'Changing to directory {year}. The program will start the analysis at year {year}')
        os.chdir(f'..\{year}')
        path = os.getcwd()
        return path

    def createOutputDir(self, year, folder_name):
        """Function related to directory manipulation. It will create the directory in which would be created outputfiles.
        Directory is by default named "outputDirectory"

        Arguments:
        year(int): Variable int defining the years. 
        folder_name(str): Name of the output directory
        """
        cwd = os.getcwd()
        if os.path.exists(folder_name):
            print(f'Output is going to be written in {cwd}\{folder_name}')
            os.chdir(f'{year}')
        else:
            print(f'Creating output directory at {self.input_dir} in {cwd}')
            os.mkdir(folder_name)
            os.chdir(f'{year}')
        return 