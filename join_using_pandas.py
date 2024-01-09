import pandas as pd
from openpyxl.workbook import Workbook

emp_df = pd.read_csv("Employee_data.csv")
print(emp_df.head(10))

dept_df = pd.read_csv("Dept_Data.csv")
print(dept_df.head())

df_inner_join = pd.merge(left=emp_df, right=dept_df, how="inner", on='dept_id')
df_outer_join = pd.merge(left=emp_df, right=dept_df, how="outer", on='dept_id')
df_right_join = pd.merge(left=emp_df, right=dept_df, how='right', on='dept_id')
df_left_join = pd.merge(left=emp_df, right=dept_df, how='left', on='dept_id')
#print(df_inner_join.head())

with pd.ExcelWriter('Output.xlsx') as writer:
    df_inner_join.to_excel(writer, sheet_name='inner_join')
    df_outer_join.to_excel(writer, sheet_name='outer_join')
    df_right_join.to_excel(writer, sheet_name='right_join')
    df_left_join.to_excel(writer, sheet_name='left_join')
