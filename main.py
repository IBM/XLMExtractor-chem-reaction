import sys
from tqdm import tqdm

from xml_extractor.directory import Directory
from xml_extractor.validation import Validation
from xml_extractor.analysis import Analysis
from xml_extractor.dataframe import Dataframe

dir = Directory('grants')
dir.starting(disable=False)

if len(sys.argv) <= 3:
    print("Some parameters are missing. Please follow the structure main.py [start year] [end year] [keyword search]")
    sys.exit()

year_start = int(sys.argv[1])
year_end = int(sys.argv[2])
access_name = str(sys.argv[3])
folder_name="output"
input_dir = "grants"

print(f"Current working directory: {dir.getDirectory()}")

dir.createOutputDir(year_start, folder_name=folder_name)

analysis = Analysis()
analysis.analysis(year_start, year_end, access_name, folder_name, input_dir, procedure=True)

df = Dataframe()
allDataframes = df.concatDataFrame(folder_name)
allDataframes.to_csv('smiles_all.csv', index=False)
print(f'All results with {access_name} were saved at outputDirectory')

notDuplicates = df.removeDuplicates()
print(f'All non duplicated results with {access_name} were saved at outputDirectory')

validation = Validation()
isPolymer = validation.checkName(access_name, notDuplicates)
print("All polymers were saved at outputDirectory")

separateClasses = validation.separateClasses(notDuplicates)
print("All classes were saved at outputDirectory")

copolymers = validation.separateCopolymers(notDuplicates)
print("All copolymers were saved at outputDirectory")

homopolymers = validation.separateHomopolymers(notDuplicates)
print("All homopolymers were saved at outputDirectory")