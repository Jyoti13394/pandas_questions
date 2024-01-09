# Get employees with 2nd highest salary for each department

import pandas as pd

emp_df = pd.read_csv("Employee_data.csv")
print(emp_df)

emp_df['rnk'] = emp_df.sort_values('salary', ascending=False).groupby('dept_id').cumcount()+1

final_df = emp_df[emp_df['rnk'] == 3]
print(final_df.head())

