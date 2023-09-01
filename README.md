# XMLExtractor for Chemical reactions from US patents (1976-Sep2016)

Script developed to extract information from xml files including chemical reactions from US patents (1976-Sep2016) curated by Daniel M Lowe.

## Documentation

### **Installation**

* Download the code file to your desired directory and unzip it

### **Running the script**

* The [main.py](.main.py) file has all the steps needed to run the code.

To run the code, type at your terminal:

```
python main.py [start year] [end year] [keyword search]
```

The data extraction can be performed by extracting the following information:

procedure= extract information that contains the keyword on the procedure tag.
all_procedure= extract all procedures in the data input.
product= extract information that contains the keyword on the product tag.
reactant= extract information that contains the keyword on the reactant tag.
reaction_action_procedure_synthesize= extract information that contains the keyword on the reaction action attribute synthesize
spectator= extract information that contains the keyword on the spectator tag.

These analysis may be performed by adding the arguments on the Analysis.analysis() method.

**More information about the functions can be found at the xml_extractor directory**

---
## Authorship

* Author: **Brenda Ferrari** ([bferrari])
