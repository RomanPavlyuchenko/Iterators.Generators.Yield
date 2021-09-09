import hashlib


def generator(path_to_file):
    with open(path_to_file) as data:
        string = data.readline()
        while string != '':
            yield hashlib.md5(string.rstrip('\n').encode()).hexdigest()
            string = data.readline()


if __name__ == '__main__':
    for i in generator('countries_wiki_url.txt'):
        print(i)
