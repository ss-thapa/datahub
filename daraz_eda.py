import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import numpy as np
import re
pd.set_option('display.max_column', None)
pd.set_option('display.max_colwidth', None)




df = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/daraz_data_all_pages.csv')


df['product_name'] = df['product_name'].str.strip()

df= df.drop_duplicates()

df['ratings'] = df['ratings'].str.replace('/5', ' ')


df['ratings'] = df['ratings'].str.replace('-May', ' ')


df['ratings'] = df['ratings'].astype(float)

df['no_of_ratings'] = df['no_of_ratings'].astype(str).str.replace('-', '')

df['no_of_ratings'] = df['no_of_ratings'].astype(int)

df['sold_num'] =df['sold_num'].str.replace(' Sold', '')

def convert_k_to_1000(value):
    if isinstance(value, str) and 'k' in value.lower():
        try:
            return int(float(value[:-1]) * 1000)
        except ValueError:
            return 0  # Handle the case where 'k' is not followed by a numeric value
    else:
        return int(value)

# Apply the function to the 'no_of_ratings' column
df['sold_num'] = df['sold_num'].apply(convert_k_to_1000)

df['original_price'] = df['original_price'].replace('Rs. ', '', regex=True).replace(',', '', regex=True).astype(int)

df['current_price'] = df['current_price'].replace('Rs.', '', regex=True).replace(',', '', regex=True).astype(int)

df = df[df['current_price'] > 50]

df['discount_amount'] = df['original_price']-df['current_price']


df['discount_amount'] = np.maximum(df['discount_amount'], 0)


### deleting 3 datas 
index_to_delete = [3472, 1632, 519]  # Specify the index of the row you want to delete

# Use drop to remove the row by index
df = df.drop(index_to_delete)





#### feature enginnering on product_name column about price

df['contains_keywords'] = df['product_name'].str.contains(r'\b(combo|pack|pcs)\b', case=False, regex=True)


# df1 = df[df['contains_keywords'] == True]


df['contains_numeric'] = df['product_name'].str.contains('\d', regex=True)


# df2 = df[df['contains_numeric'] == True]


df['extracted_numeric'] = df[df['contains_keywords'] & df['contains_numeric']]['product_name'].str.extract(r'(\b\d\b)')


pattern = r'\b(?:Five|Six|Seven|One|Two|Three|Four|Eight|Nine|Ten)\b'

# Create a new column indicating whether the product_name contains any of the specified words
df['contains_numeric_words'] = df['product_name'].str.contains(pattern, case=False, regex=True)

df =df[~(df['contains_numeric_words'] & df['contains_keywords'])]


# print(df[df['extracted_numeric']  'NaN'])

# # df['extracted_numeric']=df['extracted_numeric'].astype(int)

# # df['actual_current_price'] = df['current_price'] / df['extracted_numeric']

# # columns =['contains_keywords','contains_numeric_words', 'contains_numeric' ]






