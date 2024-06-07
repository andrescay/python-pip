import utils
import read_csv
import charts
import pandas as pd


# def run():
#     country = input('Selecciona un pais =>').title()
#     data = read_csv.read_csv('data.csv')
#     data = list(filter(lambda item: item['Continent'] == 'South America', data))
#     country_data = utils.population_by_country(data, country)
#     lables, values = utils.get_population(country_data[0])
#     charts.generate_bar_chart(country,lables, values)

#     lables, values = utils.get_population_percentage(data)
#     charts.generate_pie_chart(lables, values)

# Con pandas
def run():
    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'Africa']

    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentages)

if __name__ == '__main__':
    run()
