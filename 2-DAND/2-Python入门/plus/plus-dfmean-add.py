import numpy as np
import pandas as pd

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3, 
    'str': 'string'
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

print('\n---df---\n', example_df)
print('\n---mean(column)---\n',example_df.mean())
print('\n---mean(row)---\n',example_df.mean(axis = 1))
print('\n---add(bool)---\n',example_df + 1)