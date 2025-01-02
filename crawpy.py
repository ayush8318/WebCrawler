import requests
from bs4 import BeautifulSoup
import csv

'''Storing data to a CSV file'''
def store(fname,links,mode):
    try:
        with open(fname,mode,encoding='utf-8') as csvfile:
            csvwriter =csv.writer(csvfile)
            csvwriter.writerows(links)
    except:
        print('Error file already in use')
def checkstatus(url):
    try:
        sc=requests.get(url)
        return sc
    except:
        return 0
    
'''Extracting links of a given url'''
def trade_spider(url):
    l1=[]
    source_code=checkstatus(url)
    if source_code==0:
        return []
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.find_all('a'):
        s=str(link.get('href'))
        if s.startswith('http://') or s.startswith('https://'):
            l1.append(link.get('href'))
    l1=list(set(l1))#remove redundancy
    l1.sort()
    return l1

'''Indexing the Seed URL''' 
def add_index(l1,l2):#l1 seed to b added, l2 old seed urls
    #l3=[]
    if len(l2)== 0:
        c=1
    else:
        c=len(l2)+1
    for lnk in l1:
        l4=[]
        l4.append(c)
        l4.append(lnk)
        l2.append(l4)# now l2 is updated
        c=c+1
    return l2

'''Finding the index of url from seed URL'''
def searchnest(nestlist,ele):
    temp=0
    while temp<len(nestlist):
            if nestlist[temp][1] == ele:
                break
            temp+=1
    return temp+1

'''Storing and updating edgelist of extracted url from Seed URLs '''
def edgelist(url,allseed,urlseed,el):
    c2=searchnest(allseed, url)
    for lnk in urlseed:
        c1=searchnest(allseed, lnk)
        l1=[]
        l1.append(c2)
        l1.append(c1)
        el.append(l1)
    return el
def starter(url,lim):
    url_exp=url.split(';')
    print(url_exp)
    if '"'in url_exp:
        url_exp.remove('"')
    for u in url_exp:
        if u.startswith('http://') or u.startswith('https://'):
            continue
        else:
            k=url_exp.index(u)
            url_exp[k]='https://'+url_exp[k]
    url_exp1=url_exp
    for u in url_exp1:
        if checkstatus(u)==0:
            url_exp.remove(u)
    url_exp1=url_exp
    if len(url_exp1)==0:
        return 0
    url=url_exp1[0]
    if url.count('.')>1:
        fname=url[url.find('.')+1:url.rfind('.')]
    else:
        fname=url[url.find(':')+3:url.find('.')]
    url_front=url_exp1
    i=0
    while i<len(url_front):
        if url_front[i].endswith('/')==False:
            url_front[i]+='/'
        i=i+1
    print(url_front)
    seed_url=add_index(url_front,[])
    c=0
    elist=[]
    temp_seed=(url_front)
    #print(url_front)

    while c<len(url_front):
        newlinks=set(trade_spider(url_front[c]))
        print(url_front[c])
        if newlinks:
            '''if a non null value is present in new links'''
            nwseed=newlinks-set(temp_seed)
            #(len(newlinks),'-',len(temp_seed),'=',len(nwseed))
            url_front=url_front+list(nwseed-set(url_front))
            surl=(set(nwseed)-set(temp_seed))
            temp_seed=temp_seed+list(surl)
            seed_url=add_index(surl,seed_url)
            
            elist=edgelist(url_front[c], seed_url,list(newlinks), elist)
            store((fname+"_seeds.csv"),seed_url,"w")
        else:
            print('null')
            url_front.pop(c)
            if len(url_front)==0:
                break
            continue
        if len(seed_url)>lim:
            break
        print(len(seed_url),url_front[c],url_front)
        c=c+1
    store((fname+"_edgelist.csv"), elist, "w")
 
    if len(seed_url)==1:
        return 0
    else:
        return len(seed_url)

