import pandas as pd
import numpy as np


xl = pd.read_excel("Data extracted from sniffer logs.xlsx", sheetname = "Sheet1")
# print(xlsx)

# s = xlsx["Source"]
# d = xlsx["Date"]
# t = xlsx["Temperature"]
# print()
# # print(s[0])
# # print(t[50185])

# # print(len(s))
# # print(len(d))
# # print(len(t))

# # snif_row = []
# # snif_col = []

# snif_matrix = [[0 for w in range(0)] for h in range(10)] 

# for i in range(len(snif_matrix)):
        # snif_matrix[i].append(s[i])
        # snif_matrix[i].append(d[i])
        # snif_matrix[i].append(t[i])

# for i in range(len(snif_matrix)):
    # for j in range(len(snif_matrix[i])):
        # print(snif_matrix[i][j], end=' ')
    # print()

# print()    
# print(len(snif_matrix))
# print(snif_matrix[0][0])
# print(snif_matrix[0][1])
# print(snif_matrix[0][2])

# print(snif_matrix[9][0])
# print(snif_matrix[9][1])
# print(snif_matrix[9][2])

# strat_date = "30.8.2017  17:44:41"
# end_date =  "30.8.2017  17:45:44"
# mask = (xl['Date'] >= strat_date) & (xl['Date'] <= end_date)
# print(xl.loc[mask,"Source":"Temperature"])

import datetime
end_date = "30.8.2017  17:45:44"
#start_date = "30.8.2017  17:44:41"

end_date = pd.to_datetime(end_date)

start_date = end_date - datetime.timedelta(minutes=5)

print(start_date)
print(end_date)

#xl['Date'] = pd.to_datetime(xl.Date)
mask = (xl['Date'] >= start_date) & (xl['Date'] <= end_date)
print(xl.loc[mask,"Source":"Temperature"])


