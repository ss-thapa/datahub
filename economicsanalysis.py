# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import plotly.express as px 
# plt.style.use('fivethirtyeight')
# pd.set_option('display.max_column', None)
# color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
# from fredapi import Fred




# ## fred_key = 'ef55a9d824dc16895aeea8163307203b'

# ## create the fred object

# fred = Fred(api_key='ef55a9d824dc16895aeea8163307203b')

# ##search for econimic data

# # sp_search =fred.search('S&P', order_by='popularity')

# ##pull raw data and plot

# # sp500 = fred.get_series(series_id='SP500')

# # sp500.plot(figsize=(10,5), title='S&P500', lw=2)
# # plt.show()

# ##pull and join multiple data series

# # uemp_data = fred.search('unemployment')
# # unrate = fred.get_series('UNRATE')
# # unrate.plot()
# # plt.show()


# unemp_df = fred.search('unemployment rate state',filter=('frequency', 'Monthly'))
# unemp_df= unemp_df.query('seasonal_adjustment == "Seasonally Adjusted" and units == "Percent"')
# unemp_df = unemp_df.loc[unemp_df['title'].str.contains('Unemployment Rate')]

# all_results = []
# for myid in unemp_df.index:
#     results = fred.get_series(myid)
#     results = results.to_frame(name = myid)
#     all_results.append(results)

# unemp_results = pd.concat(all_results, axis=1).drop(['M0892AUSM156SNBR'], axis=1)

# unemp_states = unemp_results.drop('UNRATE', axis=1)

# unemp_states = unemp_states.dropna()
# #plot states unemployment rate 
# px.line(unemp_states)
# plt.show()