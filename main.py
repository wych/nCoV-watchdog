#!/usr/bin/env python3

import requests
import re
import time
import json

class SourceFormatError(Exception):
    pass

get_timeline_news_pattern = re.compile(r'<script\sid="getTimelineService">.+?getTimelineService\s=\s(\[.+?\])}catch\(e\){}<\/script>')

dxy_url = 'https://3g.dxy.cn/newh5/view/pneumonia'

last_id: int

time_interval = 60 # 1min

def get_timeline_stat():
    r = requests.get(dxy_url)
    r.encoding = 'utf-8'
    m = get_timeline_news_pattern.search(r.text)
    if m == None:
        raise SourceFormatError
    return json.loads(m.group(1))

def ensure_get_timeline_stat():
    '''Sometimes dxy returns incomplete data.
    '''
    while True:
        try:
            stat = get_timeline_stat()
        except:
            time.sleep(1)
            continue
        else:
            break
    return stat

def find_new_info():
    '''This function will return lastest news
    
    Returns:
        A dict structure, most used key for example:
        
        {'title': 'title content',
        'summary': 'summary content',
        'infoSource': 'information source',
        'sourceUrl': 'source url'}
    ''' 
    global last_id
    stat = ensure_get_timeline_stat()
    msg = []
    if stat[0]['id'] > last_id:
        for i in stat:
            if i['id'] > last_id:
                msg.append(i)
            else:
                break
        last_id = stat[0]['id']
    return msg

def main():
    print('Script starting')
    stat = ensure_get_timeline_stat()
    global last_id
    last_id = stat[0]['id']
    time.sleep(1)
    while True:
        msgs = find_new_info()
        if msgs != []:
            print('Fetched out some new information..')
            send(msgs)
        time.sleep(time_interval)

# Overwrite your send function HERE!
def send(msgs):
    for i in msgs:
        title = i['title']
        content = '%s\r\n%s\r\n%s' % (i['summary'], i['infoSource'], i['sourceUrl'])
        requests.post('https://sc.ftqq.com/[YOUR SERVER CHAN SECRET KEY].send',data = {'text': title,'desp': content})

if __name__ == '__main__':
    main()
