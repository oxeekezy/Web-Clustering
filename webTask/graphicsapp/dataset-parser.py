import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd


def arr_del(string, start, end):
    return str(string).split('>')[start].split('<')[end]


def parse(c):
    main_link = "https://www.myshiptracking.com"
    links = []
    vessels = []

    for i in range(c):
        response = requests.get(main_link + "/vessels?&page=" + str(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        data = soup.findAll('tr')

        del data[0]
        for d in data:
            tds = str(d.find('span', {'class': 'table_title table_vessel_title'})).split('"')
            links.append(main_link + tds[5])
            link = main_link + tds[5]

            try:
                response = requests.get(link)
                soup = BeautifulSoup(response.content, 'html.parser')
                data = soup.findAll('tr')
                tds = str(data).split('td')

                name = arr_del(tds[3], 2, 0)
                country = tds[7].split('"')

                if '---' in country[0]:
                    print('(SKIP) ' + link)
                    continue
                else:
                    country = country[5]
                mmsi = arr_del(tds[11], 1, 0)
                type = arr_del(tds[23], 1, 0)
                size = arr_del(tds[27], 1, 0).split(' ')

                if '---' in size[0]:
                    print('(SKIP) ' + link)
                    continue
                else:
                    size = int(size[0]) * int(size[2])

                dwt = tds[43].split('>')[1].split(' ')[0].replace(',', '')
                if '---' in dwt:
                    print('(SKIP) ' + link)
                    continue

                year = tds[51].split('>')[1].split(' ')[0]
                area = arr_del(tds[75], 1, 0)

                if '---' in area:
                    print('(SKIP) ' + link)
                    continue

                vessels.append([name, country, mmsi, type, size, dwt, year, area])
                print('(DONE) '+link)

            except:
                print('(ERROR) '+link)
                continue

    columns = ['Name', 'Country', 'MMSI', 'Type', 'Size', 'DWT', 'Year', 'Area']
    df = pd.DataFrame(vessels, columns=columns)
    df.to_csv(sys.path[0]+'/s.csv')

    print((1-len(vessels)/len(links))*100)

    return vessels


parse(100)