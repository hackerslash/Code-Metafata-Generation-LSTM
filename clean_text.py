import re
import pandas as pd
import numpy as np
def clean_text(column):
    for row in column:
# Split CamelCase Characters like ConcatenationOperator to Concatenation Operator
        row = re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1',  str(row))).split()
        row = ' '.join(row)
# Replace tabs and newlines with a single space
        row = re.sub("(\\t)", " ", str(row)).lower()
        row = re.sub("(\\r)", " ", str(row)).lower()
        row = re.sub("(\\n)", " ", str(row)).lower()
# Remove the special characters and numbers 
        row = re.sub(r"[<>()|&©ø\[\]\'\",.\}`$\{;@?~*!+=_\//1234567890]", " ", str(row)).lower()
# Remove Repeated words
        row = re.sub(r"\\b(\\w+)(?:\\W+\\1\\b)+", "", str(row)).lower()
# Remove punctuation at the end of a word
        row = re.sub("(\.\s+)", " ", str(row)).lower()
        row = re.sub("(\-\s+)", " ", str(row)).lower()
        row = re.sub("(\:\s+)", " ", str(row)).lower()
# Remove multiple spaces
        row = re.sub("(\s+)", " ", str(row)).lower()
# Remove the single character (any character) between any two spaces
        row = re.sub("(\s+.\s+)", " ", str(row)).lower()
        yield row

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


max_code_len = 100
max_summary_len =25
# Extract the codes and summaries within the maximum length
import numpy as np
cleaned_code = np.array(df_code_p['code'])
cleaned_summary= np.array(df_code_p['docstring'])
short_text = []
short_summary = []
for i in range(len(cleaned_code)):
if len(cleaned_summary[i].split()) <= max_summary_len and len(cleaned_code[i].split()) <= max_code_len:
short_text.append(cleaned_code[i])
short_summary.append(cleaned_summary[i])
post_code = pd.DataFrame({'code': short_text,'summary': short_summary})
post_code.head(100)
#apply start and end markers
post_code['summary'] = post_code['summary'].apply(lambda x: 'sostok ' + x \
+ ' eostok')
post_code.head(2)
