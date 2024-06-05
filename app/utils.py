def get_population(country_data):
  years = ['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']
  data = {
      year: int(country_data.get(f'{year} Population', 0))
      for year in years
  }
  labels = list(data.keys())
  values = list(data.values())
  return labels, values


def get_population_percentage(countries_data):
  data = {
      item['Country/Territory']: item['World Population Percentage']
      for item in countries_data
  }
  labels = list(data.keys())
  values = list(data.values())
  return labels, values


def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country,
                       data))
  return result
