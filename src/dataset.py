import pandas as pd


def load(csv_path):
    print('Loading data from {}...'.format(csv_path))
    df_all = pd.read_csv(csv_path, sep=';', decimal=',')
    df_all['DTTM'] = pd.to_datetime(dict(year=df_all['ANO'], month=df_all['MES'], day=1))
    print('Finished!')

    return df_all

def filter_popular_seats(df):
    return df.sort_values('ASSENTOS',ascending=False).drop_duplicates(['DTTM', 'ORIGEM', 'DESTINO'])

