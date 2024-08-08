import numpy as np, pandas as pd

# Create a serie with panda, not numpy
s = pd.Series([1, 3, 5, np.nan, 6, 8])


# Create a random DF with pandas
dates = pd.date_range("20240101", periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list("ABCD"))
df
df['A']
df.iloc[0]
df.loc['2024-01-06']
df.size
df.ndim
df.info
df.index
df.columns
df.dtypes
df.describe()
df.head(2)
df.tail(2)
df.to_numpy() # When you call DataFrame.to_numpy(), pandas will find the NumPy dtype that can hold all of the dtypes in the DataFrame
df.T # transposing
df.sort_index(ascending=False)
df.sort_values(by="B")
df.loc[dates[0]] # equals to df.loc['2024-01-01']
df.loc[:, ["A", "B"]]
df.loc["2024-01-01":"2024-01-03", ["A", "B"]]
df.iloc[[1, 2, 4], [0, 2]]
df[df["A"] > 1.14] # when A's values > 1,14
df[df > -1.0] # all positive cells in a df; otherwise -> NaN
df["Z"] = ["one", "one", "two", "three", "four", "three"] # adds a new col at the end

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("2024-01-01", periods=6))
df["W"] = s1


# Group
rows = pd.Series(list("ab"))
df = pd.DataFrame(np.random.randn(2,2), index=rows, columns=list("XY"))
df
df['2024-01-03'] = '2024-01-01'
df.groupby("A")["B"].sum() # groups by col=A and sum(B)
df.groupby('2024-01-03')["B"].sum() # groups by col='2024-01-03' and sum(B)
df.groupby("A")[["C", "D"]].sum() # groups by col=A and sum(C , D)

# Count
s = pd.Series(np.random.randint(0, 10, size=4))
s.value_counts()

pd.Series(['a','b','c','a','a','c']).value_counts()


# Merge (Join, enables SQL style join types along specific columns)
left = pd.DataFrame({"key": ["foo", "fo.o"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["fo.o", "foo"], "rval": [4, 5]})
pd.merge(left, right, on="key")





# manually-created complex df (for sample purposes only... BS!)
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
df2["E"] = ["one", "two", "three", "four"] # adds or replaces values in col
df2[df2["E"].isin(["two", "four"])] # filters values in col
df2.dropna(how="any") # drops any rows that have missing data
df1.fillna(value=5) # fills missing data with number 5