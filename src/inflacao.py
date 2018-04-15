import pandas as pd


def load_dataset(csv_path):
    df_inflacao = pd.read_csv(csv_path, sep=';', decimal=',')

    df_inflacao['DTTM'] = pd.to_datetime(df_inflacao['Data'], format='%m/%Y')
    df_inflacao.drop('Data', axis=1, inplace=True)
    df_inflacao.set_index('DTTM', inplace=True)

    df_inflacao['Variacao'] = (df_inflacao['Variacao'] / 100.0) + 1.0
    df_inflacao.loc['2012-01-01', 'Variacao'] = 1.0

    df_inflacao['Inflacao_acumulada'] = df_inflacao['Variacao'].cumprod()

    return df_inflacao
