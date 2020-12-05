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
    after_login(res)

def after_login(resp):
    soup = bs4.BeautifulSoup(resp.text, "html.parser")
    paginations = soup.find_all('li', attrs={'class': 'page-item'})
    total_pages = len(paginations) - 2
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
            print(i)
            i+=1
            # detail(title)

# def detail(soup2):
#     title = soup2.find('title').text.strip()
#     price = soup2.find('h4', attrs={'class': 'card-price'}).text.strip()
#     stock = soup2.find('span', attrs={'class': 'card-stock'}).text.strip().replace('stock: ', '')
#     category = soup2.find('span', attrs={'class': 'card-category'}).text.strip().replace('category: ', '')
#     description = soup2.find('p', attrs={'class': 'card-text'}).text.strip().replace('Desription: ', '')
#
#     dict_data = {
#         'title': title,
#         'price': price,
#         'stock': stock,
#         'category': category,
#         'description': description
#     }
#     print(dict_data)

if __name__ == '__main__':
    login()
