import pandas as pd

# print(pd.__version__)

drivers_df = pd.read_csv('07-Pandas\\00drivers.csv') # , index_col=0)
results_df = pd.read_csv('07-Pandas\\03results.csv') # , index_col=0)
races_df = pd.read_csv('07-Pandas\\02races.csv') # , index_col=0)
# print(drivers_df)
# print(drivers_df.head(10))
# print(drivers_df.tail())
# print(drivers_df.columns)
# drivers_df = drivers_df.sort_index(axis=1, ascending=False)
#   axis=0 (ordena por linhas) ou axis=1 (ordena por colunas)
#   ascending=True (Ordena de maneira crescente) ou ascending=False (Ordena de maneira decrescente)
# drivers_df = drivers_df.sort_values(by=["surname", "forename"])
# print(drivers_df[["forename","surname"]].head(10))
# print(drivers_df[10:20])
# print(drivers_df.iloc[0, :])
# print(drivers_df.loc[drivers_df['driverId'] == 1])
# print(drivers_df.columns)
# print(results_df.columns)

results_drivers_df = results_df.merge(drivers_df)
results_drivers_df = results_drivers_df[['resultId', 'raceId', 'driverId',
       'position','points', 'forename', 'surname']]
# print(results_drivers_df.columns)
# print(races_df.columns)
results_drivers_races_df = results_drivers_df.merge(races_df)

filtered_df = results_drivers_races_df.loc[results_drivers_races_df['year'] == 2019]
print(filtered_df[['year', 'forename', 'surname','points']])
