import pandas as pd

emp_df = pd.read_csv("Employee_data.csv")
print(emp_df.duplicated())

# To check duplicates only on emp_id

print(emp_df.emp_id.duplicated())

# To get total count of duplicate rows

print(emp_df.duplicated().sum())

# To get only those rows which are duplicates

print(emp_df[emp_df.duplicated()])

# To get records which are not duplicates

print(emp_df[~emp_df.duplicated()])


# To drop duplicates

print(emp_df.drop_duplicates())

# To drop duplicates on the basis of column

print(emp_df.drop_duplicates(subset='dept_id'))