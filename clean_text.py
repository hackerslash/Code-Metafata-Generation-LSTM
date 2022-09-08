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
