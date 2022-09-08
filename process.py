import re
import pandas as pd
import numpy as np


df_code = pd.read_csv('javascript_Sample_Dataset.csv')
#extract only the code and docstring columns
df_code_p = df_code[["code","docstring"]]
print (df_code_p["docstring"][0])
--------------------------- # console output#
Closes connection

@public
@memberOf ConnectionMachine.prototype
@returns {Promise} promise that is fulfilled after connection has been closed
---------------------------
#call clean_text function
processed_code= clean_text(df_code_p['code'])
processed_summary = clean_text(df_code_p['docstring'])
import spacy
from time import time
nlp = spacy.load('en', disable=['ner', 'parser'])
# Process the text as batches, you may should the batchsize when you use the complete dataset, empirically can be set to 5000 for > 1,00,000 records
code = [str(doc) for doc in nlp.pipe(processed_code, batch_size=50)]
#_START_ and _END_ tokens are markers to understand start and end of summaries
summary = [ str(doc) for doc in nlp.pipe(processed_summary, batch_size=50)]
