# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:23:11 2017

@author: Luo
"""
import urllib
import re
#import MySQLdb
# http://www.quanshuwang.com/list/3_1.html

#class Qql(object):
#    conn = MyQSLdb.connect(
#            host = 'mysql.luojiahong.com',
#            prot =7150,
#            usrt = 'noveltest',
#            password = '123456',
#            db = 'noveltest',
#            charset = 'utf8'
#            )
#    def addnovel(self, sort, sortname, name, imgurl, description, status, author):
#        cur = self.conn.cursor()
#        cur.execute()
#        lastrowid = cur.lastrowid
#        cur.close()
#        self.conn.commit("insert into novel(sort, sortname, name, imgurl,description, status, author) valuse(%s_,_'%s'_,_'%s'_,_'%s'_,_'%s'_,_'%s'_,_'%s'_,)" %(sort, sortname, name, imgurl, description, status, author))
#        return lastrowid
#    del addchapter(self, novelid, title,content):
        
sort_dist = {
        1:'玄幻魔法',
        2:'武侠修真',
        3:'纯爱耽美',
        4:'都市言情',
        5:'职场校园',
        6:'穿越重生',
        7:'历史军事',
        8:'网游动漫',
        9:'恐怖灵异',
        10:'科幻小说',
        11:'美文名著'
        }
def getNovel(url):
    #print(url)
    html = urllib.request.urlopen(url).read().decode().encode()
    # name
    #reg = r'<meta property="og:novel:book_name" content="(.*?)"/>'
    #bookname = re.findall(reg,html)[0]
    
    #reg = r'<meta property="og.novel.description" content=".*?"/>'
    #description = re.findall(reg,html,re.S)[0]
    
    # 
    #print(bookname)
    

def getList(sort_id, sort_name):
    html = urllib.request.urlopen('http://www.quanshuwang.com/list/%s_1.html'
                                  %sort_id).read().decode('gbk').encode('utf-8')
#    reg = r '<a href="_blank" href="(*.?)" class="readTo">马上阅读</a>'
    #print(html)
    getNovel(html)
    
for sort_id, sort_name in sort_dist.items():
    print(sort_id, sort_name)
    #getList(sort_id, sort_name)
    #break