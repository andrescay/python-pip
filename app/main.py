import utils
import read_csv
import charts


def run():
    # names = {'Nicolas', 'Miguel', 'Juan', 'Nicolas'}
    # print(names)
    country = input('Selecciona un pais =>').title()
    data = read_csv.read_csv('data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data))
    country_data = utils.population_by_country(data, country)
    lables, values = utils.get_population(country_data[0])
    # print(lables, values)
    charts.generate_bar_chart(country,lables, values)

    lables, values = utils.get_population_percentage(data)
    charts.generate_pie_chart(lables, values)


if __name__ == '__main__':
    run()
