import json

import wikipedia


class CountryIterator:

    def __init__(self, data):
        self.data = data
        self.cursor = None

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        country_name = self.data[self.cursor]['name']['common']

        if self.cursor == len(self.data) - 1:
            raise StopIteration

        try:
            country_url = wikipedia.page(country_name, auto_suggest=False).url
        except wikipedia.DisambiguationError:
            country_name = wikipedia.search(country_name, results=2)[1]
            country_url = wikipedia.page(country_name, auto_suggest=False).url

        return f"{country_name} - {country_url}"


if __name__ == '__main__':
    with open('countries.json') as data:
        countries = json.load(data)

        with open('countries_wiki_url.txt', 'w') as write_file:
            for country in CountryIterator(countries):
                write_file.write(country + '\n')
                print(country)
