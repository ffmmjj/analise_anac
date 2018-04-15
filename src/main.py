import sys
import numpy as np
import pandas as pd

import dataset
import inflacao
import reports


def median_pivot_table_by_dttm(df):
    return pd.pivot_table(df, index=['DTTM'], values=['TARIFA'], aggfunc=np.median)


def adjust_for_inflation(df, df_inflacao):
    df['TARIFA_CORRIGIDA'] = df['TARIFA'] / df_inflacao['Inflacao_acumulada']
    return df


def calculate_price_increase_percentage(pivot_df, starting_month, final_month):
    starting_month_values = pivot_df[pivot_df.index.month == starting_month]['TARIFA_CORRIGIDA'].values
    final_month_values = pivot_df[pivot_df.index.month == final_month]['TARIFA_CORRIGIDA'].values

    years_list = list(range(2012, 2018)) # TODO extract form pivot_df
    price_increases = (final_month_values - starting_month_values) / starting_month_values

    return pd.Series(index=years_list, data=price_increases)


def analyze_popular_seats_from_company(df_all, df_inflacao, company_identifier):
    df_company = df_all[df_all['EMPRESA'] == company_identifier]
    df_popular_seats = dataset.filter_popular_seats(df_company)
    df_pivot = median_pivot_table_by_dttm(df_popular_seats)
    reports.plot_pivot_table(df_pivot, company_identifier, '../reports/medianas_{}.png'.format(company_identifier))

    df_adjusted = adjust_for_inflation(df_pivot, df_inflacao)
    reports.plot_pivot_table_with_inflation(df_adjusted, company_identifier,
            '../reports/medianas_ajustadas_{}.png'.format(company_identifier))

    prices_adjustments = calculate_price_increase_percentage(df_adjusted, 6, 9)
    reports.plot_price_increases(prices_adjustments, company_identifier,
            '../reports/crescimentos_{}.png'.format(company_identifier))



if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python main.py <path_do_csv> <identificador_da_companhia>')
        sys.exit(0)

    df_all = dataset.load(sys.argv[1])
    df_inflacao = inflacao.load_dataset(sys.argv[2])
    analyze_popular_seats_from_company(df_all, df_inflacao, sys.argv[3])

