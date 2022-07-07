from binance.client import Client
import pandas as pd
import time

perf = time.perf_counter()
client = Client("", "")
columns = {'symbol': str(), 'price': float()}

api_data = client.get_all_tickers()
df = pd.DataFrame(api_data, columns=columns)
df.to_csv('api_data.csv', index=False)


alarm_data_columns = {'symbol': str(), 'alarm1': float, 'alarm2': float, 'alarm3': float, 'alarm4': float,
                      'alarm5': float, 'alarm6': float, 'alarm7': float, 'alarm8': float, 'alarm9': float,
                      'alarm10': float}
alarm_data = pd.DataFrame(df['symbol'], columns=alarm_data_columns)
alarm_data.fillna({'alarm1': 0, 'alarm2': 0, 'alarm3': 0, 'alarm4': 0, 'alarm5': 0, 'alarm6': 0,
                   'alarm7': 0, 'alarm8': 0, 'alarm9': 0, 'alarm10': 0}, inplace=True)
alarm_data.to_csv('alarm_data.csv', index=False)
alarm_list = ['alarm1', 'alarm2', 'alarm3', 'alarm4', 'alarm5', 'alarm6', 'alarm7', 'alarm8', 'alarm9', 'alarm10']


def add_alarm_data(self, alarm):
    find = pd.read_csv('alarm_data.csv')
    pair = find.loc[find['symbol'] == self, ['symbol']]
    if find.at[pair.index[0], 'symbol'] == self:
        for i in alarm_list:
            # could be there is a faster way to do this
            if find[find['symbol'] == self].to_dict('records')[0][i] == alarm:
                return print("Alarm is already in alarm_data")

            # TODO:if all alarms are full? check this

            if find[find['symbol'] == self].to_dict('records')[0][i] == 0:
                find.at[pair.index[0], i] = alarm
                find.to_csv('alarm_data.csv', index=False)
                return print(f"{self}: {alarm} added")
            if find[find['symbol'] == self].to_dict('records')[0][i] != 0:
                # TODO:sort alarms in db?
                continue


def remove_alarm_data(self: str, alarm: float):
    find = pd.read_csv('alarm_data.csv')
    pair = find.loc[find['symbol'] == self, ['symbol']]
    for i in alarm_list:
        if find[find['symbol'] == self].to_dict('records')[0][i] == alarm:
            find.at[pair.index[0], i] = 0
            find.to_csv('alarm_data.csv', index=False)
            print(f"{self}: {alarm} removed")
            break

#TESTING
add_alarm_data('BTCUSDT', 1000)
add_alarm_data('ETHBTC', 1000)
add_alarm_data('ETHBTC', 2000)
# remove_alarm_data('ETHBTC', 2000)
# remove_alarm_data('BTCUSDT', 1000)