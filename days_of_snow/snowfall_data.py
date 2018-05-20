import sys
import pandas as pd

def fix_snowfall(csv_path):
    '''snowfall data from NWS rows are
    from Jul of a year to Jun the NWS
    temp data is from Jan to Dec of year
    in each row. Let's make them match'''
    new_csv_name = csv_path + "_clean"
    snowfall_data = pd.read_csv(csv_path)
    cols = snowfall_data.columns.tolist()
    #make a list of lists, then create a df
    new_rows = []
    for index, row in snowfall_data.iterrows():
        row_list = []
        try:
            test = index+1
            row_list.append(row[0])
            row_list.extend(row[cols[7:-1]])
            row_list.extend(snowfall_data.loc[index+1][cols[1:7]])
            new_rows.append(row_list)
        except KeyError:
            break  
    new_cols = [cols[0]]
    new_cols.extend(cols[7:-1])
    new_cols.extend(cols[1:7])
    final_snowfall = pd.DataFrame(new_rows, columns = new_cols)
    print (final_snowfall.head())
    return final_snowfall.to_csv(new_csv_name)


if __name__ == '__main__':
    path = sys.argv[1]
    #f = open(new_csv_name, 'w')
    #sys.stdout = f
    fix_snowfall(path)


