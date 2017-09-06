import pandas as pd
import datetime
import csv

df = pd.read_excel("Data extracted from sniffer logs.xlsx", sheetname = "Sheet1")
input_file = "time.csv"

def data_extract(date):
    global df
    end_date = pd.to_datetime(date)
    start_date = end_date - datetime.timedelta(minutes=5)
    #start_date = "30.8.2017  17:44:41"
    
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    # df.loc[mask,["Source","Temperature"]]
    
    df1 = df.loc[mask,"Source":"Temperature"]
    df1 = df1.sort_values("Source")
    df1 = df1.drop_duplicates(subset='Source', keep="last")
    
    # list = df2['Source'].tolist()
    
    return df1


def main():
    global input_file
    list_dfs = []
    writer = pd.ExcelWriter('output.xlsx')
    
    with open(input_file, 'r') as file:
        in_data = csv.reader(file, delimiter=';')
        for i, row in enumerate(in_data):
            data = data_extract(row[0])
            
            # upisati addr time temp pojednacno
            # data2 = data["Chamber_Temp"] = row[1]
            data2 = data.set_index('Source')
            data2.to_excel(writer,row[1])
            
            data = data.loc[:,["Source","Temperature"]]
            data = data.set_index('Source')
            
            data = data.rename(index=str, columns={"Temperature": row[1]})
            data = data.transpose()
            
            print(data)
            
            list_dfs.append(data)
            
            
        i=0
        for n, df in enumerate(list_dfs):
            df.to_excel(writer, 'Final', startcol=0, startrow = i, header=True, index = True)
            i+=2
        writer.save()

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    