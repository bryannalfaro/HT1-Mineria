# Referencia forma > https://towardsdatascience.com/splitting-the-text-column-and-getting-unique-values-in-python-367a9548d085
from collections import Counter
import pandas as pd
def clean_data(list_data):
    list_splitted = list_data.str.cat(sep='|')
    list_final = list_splitted.split("|")
    list_split_empty = [x.strip("") for x in list_final]
    count = Counter(list_split_empty)
    return pd.DataFrame(count.most_common(10000), columns=['Item', "Count"])
