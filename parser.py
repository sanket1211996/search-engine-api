
import pandas as pd
#
#
# #
# # df.to_pickle(file_name)
# #
# # df = pd.read_pickle(file_name)
#
# df = pd.read_csv('./data/securities.csv', dtype=str)
# print(df.dtypes)
# df.fillna("_", inplace=True)
# print(df.head(1))
# df['text'] = df['security_id'] + ' ' + df['cusip']+ ' ' + df['sedol']+ ' ' + df['isin']+ ' ' + df['ric']+ ' ' + df['bloomberg']+ ' ' + df['bbg']+ ' ' + df['symbol']+ ' ' + df['root_symbol']+ ' ' + df['bb_yellow']+ ' ' + df['spn']
# df['priority'] = 9999
# print(df.shape)
# # store = pd.HDFStore('store.h5')
# # store['securities'] = df
# df.to_pickle("securities_pickle")
# df = pd.read_pickle('./data/securities_pickle')
# print(df.head(1))