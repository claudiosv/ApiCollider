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
    for page in range(716):
        raw_html = simple_get('https://www.programmableweb.com/category/all/apis?page={}'.format(page))
        #len(raw_html)
        client = MongoClient('mongodb://apicollider:apicollider123@ds125892.mlab.com:25892/apicollider')
 # r    aw_html = open('contrived.html').read()
        html = BeautifulSoup(raw_html, 'html.parser')
        table = html.find_all('tbody')[2].find_all('tr')
 #pr    int(table)
 #fo    r p in html.select('td'):
         #print(p['class'])
         #if 'views-field-title' in p['class']: #str.startswith
          #   print(p.text)
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
    # print('Getting the list of names....')
    # names = get_names()
    # print('... done.\n')

    # results = []

    # print('Getting stats for each name....')

    # for name in names:
    #     try:
    #         hits = get_hits_on_name(name)
    #         if hits is None:
    #             hits = -1
    #         results.append((hits, name))
    #     except:
    #         results.append((-1, name))
    #         log_error('error encountered while processing '
    #                   '{}, skipping'.format(name))

    # print('... done.\n')

    # results.sort()
    # results.reverse()

    # if len(results) > 5:
    #     top_marks = results[:5]
    # else:
    #     top_marks = results

    # print('\nThe most popular mathematicians are:\n')
    # for (mark, mathematician) in top_marks:
    #     print('{} with {} pageviews'.format(mathematician, mark))

    # no_results = len([res for res in results if res[0] == -1])
    # print('\nBut we did not find results for '
    #       '{} mathematicians on the list'.format(no_results))