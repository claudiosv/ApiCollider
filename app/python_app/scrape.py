from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from pymongo import MongoClient

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

if __name__ == '__main__':
    page_num = 161
    for page in range(page_num,716):
        print(page_num)
        raw_html = simple_get('https://www.programmableweb.com/category/all/apis?page={}'.format(page))
        client = MongoClient('mongodb://apicollider:apicollider123@ds125892.mlab.com:25892/apicollider')
        html = BeautifulSoup(raw_html, 'html.parser')
        table = html.find_all('tbody')[2].find_all('tr')
        db = client.apicollider
        apic = db.apis
        pairs = []
        for i, td in enumerate(table):
            title = td.select('.views-field-title')[0].a.text.strip()
            description = td.select('.views-field-search-api-excerpt')[0].text.strip()
            if not description.startswith('[This API is no longer available.'):
                pairs.append({ 'title': title, 'description': description})
                print(title, description)

        new_result = apic.insert_many(pairs)
        page_num += 1