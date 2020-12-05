import csv
import requests
# import pandas as pd
import bs4

session = requests.session()

# f = open('./res.html', 'w+')
# f.write(res.text)
# f.close()

def login():
    print('login....')
    datas = {
        'username': 'user',
        'password': 'user12345'
    }
    res = session.post('http://localhost:5000/login', data=datas)
    # THIS IS FOR CHECK THE LOGIN IS SUCCESFULL OR NOT
    # f = open('./res2.html', 'w+')
    # f.write(res.text)
    # f.close()
    return (res)

def after_login(resp):
    print('proses....')
    soup = bs4.BeautifulSoup(resp.text, "html.parser")
    paginations = soup.find_all('li', attrs={'class': 'page-item'})
    total_pages = len(paginations) - 2
    dict_data2 = []
    for page in range(total_pages):
        # print(page+1)
        params = {
            'page': page+1
        }
        resp = session.get('http://localhost:5000/', params=params)
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        titles = soup.find_all('h4', attrs={'class': 'card-title'})
        i=1
        for title in titles:
            title_url = title.find('a')['href']
            # print(title_url)
            dict_data2.append(detail(i, title_url))
            i+=1
    # print(dict_data2)
    return dict_data2

def detail(j, url):
    res = session.get('http://localhost:5000'+url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    title = soup.find('title').text.strip()
    price = soup.find('h4', attrs={'class': 'card-price'}).text.strip()
    stock = soup.find('span', attrs={'class': 'card-stock'}).text.strip().replace('stock: ', '')
    category = soup.find('span', attrs={'class': 'card-category'}).text.strip().replace('category: ', '')
    description = soup.find('p', attrs={'class': 'card-text'}).text.strip().replace('Desription: ', '')

    dict_data = {
        'no': j,
        'title': title,
        'price': price,
        'stock': stock,
        'category': category,
        'description': description
    }
    print(dict_data)
    return dict_data

def create_csv(dict_data4):
    print('create csv....')
    with open('hasil.csv', 'w') as csvfile:
        field_names = ['no','title','price','stock','category','description']
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(dict_data4)
#     with open('hasil.csv', 'w') as f:
#         for key in dict_data.keys():
#             f.write("%s,%s\n" % (key, dict_data[key]))

if __name__ == '__main__':
    resp = login()
    # dict_data3 = []
    dict_data3 = after_login(resp)
    # print(dict_data3)
    create_csv(dict_data3)
