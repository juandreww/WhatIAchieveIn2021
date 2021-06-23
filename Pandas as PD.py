import pandas as pd 
 
Developer = pd.DataFrame({'Name': ['Isyana Saraswati', 'Nicholas Saputra', 'Raisa Andriana'], 
        'Age':[30, 36, 32]}) 
print("Machine Learning Developer di Indonesia :\n", Developer) 
 
Developer[['First','Last']] = Developer.Name.str.split(expand=True) 
print("\n Split kolom 'Name', lalu tambahkan kedua kolom : \n", Developer)