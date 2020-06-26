import datetime
import pandas as pd
from dateutil import parser


MONTHS = {'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4,  'mai': 5,  'jun': 6,
          'jul': 7, 'ago': 8, 'set': 9, 'out': 10, 'nov': 11, 'dez': 12}
FULL_MONTHS = {'janeiro': 1,  'fevereiro': 2, u'março': 3,    'abril': 4,
               'maio': 5,     'junho': 6,     'julho': 7,     'agosto': 8,
               'setembro': 9, 'outubro': 10,  'novembro': 11, 'dezembro': 12}

def parse_pt_date(date_string):
    '''Parses a date-time string and return datetime object
       The format is like this:
       'Seg, 21 Out 2013 22:14:36 -0200'
    '''
    try:
        date_info = date_string.lower().split()
        if date_info.count('de') == 2 or len(date_info) == 3:
            if ',' in date_info[0]:
                date_string = date_string.split(',')[1]
            date_info = date_string.lower().replace('de ', '').split()
            day, month_pt, year = date_info
            if len(month_pt) == 3:
                month = MONTHS[month_pt]
            else:
                month = FULL_MONTHS[month_pt]
            return f"{day}/{month}/{year}"
            date_iso = '{:02d}-{:02d}-{}'.format(int(day), int(month), year)
            date_object = datetime.datetime.strptime(date_iso, '%d-%m-%Y')
            return date_object
        else:
            _, day, month_pt, year, hour_minute_second, offset = date_info

            if offset.lower() == 'gmt':
                offset = '+0000'
            offset_signal = int(offset[0] + '1')
            offset_hours = int(offset[1:3])
            offset_minutes = int(offset[3:5])
            total_offset_seconds = offset_signal * (offset_hours * 3600 +
                                                    offset_minutes * 60)
            offset_in_days = total_offset_seconds / (3600.0 * 24)

            month = MONTHS[month_pt]
            datetime_iso = '{}-{:02d}-{:02d}T'.format(int(day), month, year)
            datetime_object = datetime.datetime.strptime(datetime_iso,
                    '%d/%m/%Y')
    except:
        date = date_string.split(" ")
        if len(date) > 1:
            if len(date[0]) < 1:
                dates = date[1].split("/")
                return f"{dates[2]}/{dates[1]}/{dates[0]}"
            return date[0]
        else:
            dates = date[0].split("/")
            return f"{dates[2]}/{dates[1]}/{dates[0]}"
    return datetime_object - datetime.timedelta(offset_in_days)


def get_dataframes() -> list:
    df_true = pd.read_csv("../../data_csv/true-meta.csv")
    df_fake = pd.read_csv("../../data_csv/fake-meta.csv")
    return [df_true, df_fake]    

df_true, df_fake = get_dataframes()

for i, row in df_fake.iterrows():
    date = parser.parse(row["Date"])
    df_fake.loc[i, "Date"] = date
    
for i, row in df_true.iterrows():
    date = parser.parse(row["Date"])
    df_true.loc[i, "Date"] = date
    

def download_dataframe_as_csv(df, name:str, path:str="../../data_csv/") -> None:
    df.to_csv(f"{path}/{name}.csv", index=True)
    
download_dataframe_as_csv(df_true, "true-meta")
download_dataframe_as_csv(df_fake, "fake-meta")