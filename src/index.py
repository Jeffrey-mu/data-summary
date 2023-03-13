import pandas as pd
def gather_data(path, column):
  df = pd.read_csv(path)
  gather = df[column].sum()
  # 输出结果
  print('汇总：',gather)


gather_data('./data/topfun-2023-03-12:20:47:08-2023-03-06~2023-03-07 copy.csv', 'Column.AD_EXCHANGE_LINE_ITEM_LEVEL_REVENUE')
141432193353
3007611005
