def read_data():
    data = pd.read_csv('all_owm.csv')
    data["Dates"] = ""
    data["rise_set"] = 0.0

    for i in range(data.shape[0]):
        dt = datetime.fromtimestamp(data.iloc[i]['timestamp'] // 1000)
        data.at[i, 'Dates'] = dt

        m = (data.iloc[i]['sunset'] + data.iloc[i]['sunrise']) // 2

        if data.iloc[i]['timestamp'] < m:
            time_rs = (data.iloc[i]['timestamp'] - data.iloc[i]['sunrise']) / \
            (m - data.iloc[i]['sunrise'])
        else:
            time_rs = (data.iloc[i]['sunset'] - data.iloc[i]['timestamp']) / \
            (data.iloc[i]['sunset'] - m)

        data.at[i, 'rise_set'] = time_rs

    data = data.set_index('Dates')
    data = data.drop(['timestamp','sunrise','sunset'], axis=1) 

    cols = list(data.columns)
    a, b = cols.index('pwr'), cols.index('rise_set')
    cols[b], cols[a] = cols[a], cols[b]
    data = data[cols]
    
    return data
