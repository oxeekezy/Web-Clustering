import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd


def arr_del(string, start, end):
    return str(string).split('>')[start].split('<')[end]

def write_log(log:pd.DataFrame, result, link, i):
    log.loc[i] = list([result, link])
    log.to_csv(sys.path[0] + '/logs.csv')


def parse(c):
    main_link = "https://www.myshiptracking.com"
    links = []

    columns = ['Name', 'Country', 'MMSI', 'Type', 'Size', 'DWT', 'Year', 'Area']
    logColumns = ['Result', 'Link']

    log = pd.DataFrame(columns=logColumns)
    df = pd.DataFrame(columns=columns)

    iterator = 0
    logIterator = 0

    for i in range(c):
        try:
            response = requests.get(main_link + "/vessels?&page=" + str(i))
            soup = BeautifulSoup(response.content, 'html.parser')
            data = soup.findAll('tr')

            del data[0]
            for d in data:
                tds = str(d.find('span', {'class': 'table_title table_vessel_title'})).split('"')
                links.append(main_link + tds[5])
                link = main_link + tds[5]


                response = requests.get(link)
                soup = BeautifulSoup(response.content, 'html.parser')
                data = soup.findAll('tr')
                tds = str(data).split('td')

                name = arr_del(tds[3], 2, 0)
                country = tds[7].split('"')

                if '---' in country[0]:
                    print('(COUNTRY SKIP) ' + link)
                    write_log(log, '(COUNTRY SKIP)', link, logIterator)
                    logIterator+=1
                    continue
                else:
                    country = country[5]
                mmsi = arr_del(tds[11], 1, 0)
                type = arr_del(tds[23], 1, 0)
                size = arr_del(tds[27], 1, 0).split(' ')

                if '---' in size[0]:
                    print('(SIZE SKIP) ' + link)
                    write_log(log, '(SIZE SKIP)', link, logIterator)
                    logIterator += 1
                    continue
                else:
                    size = int(size[0]) * int(size[2])

                dwt = tds[43].split('>')[1].split(' ')[0].replace(',', '')
                if '---' in dwt:
                    print('(DWT SKIP) ' + link)
                    write_log(log, '(DWT SKIP)', link, logIterator)
                    logIterator += 1
                    continue

                year = tds[51].split('>')[1].split(' ')[0]
                area = arr_del(tds[75], 1, 0)

                if '---' in year:
                    print('(YEAR SKIP) ' + link)
                    write_log(log, '(YEAR SKIP)', link, logIterator)
                    logIterator += 1
                    continue

                if '---' in area:
                    area = "None"


                df.loc[iterator] = list([name, country, mmsi, type, size, dwt, year, area])
                df.to_csv(sys.path[0] + '/s.csv')
                iterator+=1


                print('(DONE) '+link)
        except:
            print('(ERROR IN PAGE)')
            continue

parse(10000)