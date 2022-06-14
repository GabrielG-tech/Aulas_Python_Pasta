import pandas as pd

# print(pd.__version__)

drivers_df = pd.read_csv('07-Pandas\\00drivers.csv') #, index_col=0)
results_df = pd.read_csv('07-Pandas\\03results.csv')
races_df = pd.read_csv('07-Pandas\\02races.csv')

# print(drivers_df)
# print(drivers_df.head(10))
# print(drivers_df.tail())
# print(drivers_df.columns)
# drivers_df = drivers_df.sort_index(axis=1, ascending=True)
# axis=0 (ordena por linhas) ou axis=1 (ordena por colunas)
# ascending=True (Ordena de maneira crescente) ou ascending=False (Ordena de maneira decrescente)
# drivers_df = drivers_df.sort_values(by=["surname", "forename"])
#   print(drivers_df([["forename", "surname"]]).head(10))
# print(drivers_df[10:20])

#  print(drivers_df.iloc[0, :])
# print(drivers_df.loc[drivers_df['driverId']])

drivers_results_df = results_df.merge(drivers_df, indicator=True)
print(drivers_results_df[['year', 'forname', 'name', 'surname', 'points', '_merge']])
