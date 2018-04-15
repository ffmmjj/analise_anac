import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches


def plot_pivot_table(pivot_df, company_id, plot_file_name):
    plt.rcParams["figure.figsize"] = (16, 8)
    fig, ax = plt.subplots()
    ax.set_xticks(pivot_df.index)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax.set_title('Medianas das tarifas populares de Jan 2012 a Out 2017 ({})'.format(company_id))
    ax.set_ylabel('Tarifa popular em R$')
    fig.autofmt_xdate(rotation=45)
    fig.tight_layout()

    plt.plot_date(x=pivot_df.index, y=pivot_df, ls='-')
    plt.savefig(plot_file_name)
    plt.gcf().clear()


def plot_pivot_table_with_inflation(pivot_df, company_id, plot_file_name):
    plt.rcParams["figure.figsize"] = (16, 8)
    fig, ax = plt.subplots()
    ax.set_xticks(pivot_df.index)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax.set_title('Medianas das tarifas populares corrigidas pela inflação de Jan 2012 a Out 2017 ({})'.format(company_id))
    ax.set_ylabel('Tarifa popular em R$')
    fig.autofmt_xdate(rotation=45)
    fig.tight_layout()

    tarifa, = plt.plot_date(x=pivot_df.index, y=pivot_df['TARIFA'], ls='-', label='Tarifa bruta')
    tarifa_corrigida, = plt.plot_date(x=pivot_df.index, y=pivot_df['TARIFA_CORRIGIDA'], ls='-', label='Tarifa corrigida')
    plt.legend(handles=[tarifa, tarifa_corrigida])
    plt.savefig(plot_file_name)
    plt.gcf().clear()


def plot_price_increases(prices_increases_series, company_id, plot_file_name):
    prior_median_value  = prices_increases_series[:-1].median()
    prices_increases_series.plot(color='b');
    prior_median_handle = plt.axhline(prior_median_value, color='r', label='Mediana até 2016')
    prices_handle = mpatches.Patch(color='b', label='Crescimento')

    plt.title('Crescimento das tarifas corrigidas entre Junho e Setembro ({})'.format(company_id))
    plt.legend(handles=[prices_handle, prior_median_handle])

    plt.savefig(plot_file_name)
    plt.gcf().clear()

