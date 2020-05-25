
import requests
from bs4 import BeautifulSoup
import multiprocessing as mp
try:
    cite = 'https://www.google.com/search?q=automation'
    key = 'testautomationday.com'
    results=[]
    # print("Number of processors: ", mp.cpu_count())
    # pool = mp.Pool(mp.cpu_count())
    for x in range (1,6):
        cite = cite+'&start='+str(x-1)+'0'
        soup = BeautifulSoup(requests.get(cite).content, 'lxml')
        p = soup.findAll('a', href=True)
        for i in p:
            i = (i['href'])
            # print(i)
            if '/url?q=' in i and 'https://accounts.google.com' not in i:
                i = i.lstrip('/url?q=')
                results.append(i)
                print(i)
            else:
                continue
    print(results)
    pos=0
    for i in results:
        if key in i:
            pos=results.index(i)
        else:
            continue
except Exception as exception:
    print(exception)
    print(exception.__class__.__name__)
finally:
    print('searched cite is on position:', pos)

