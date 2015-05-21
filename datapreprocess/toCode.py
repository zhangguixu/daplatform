#coding=utf8
import web
import datetime
web.config.debug = False

db=web.database(dbn='mysql', db='daplatform', user='root', pw='123')

#案件类型数字化
def casetypetocode():
    total = 0
    typelist = []
    print '开始转换'
    starttime=datetime.datetime.now()
    while (total <= 10000):
        results = db.select("originText", order='ID DESC', limit=100, offset=total)
        for record in results:
            if typelist.count(record.type) == 0:
                db.insert("caseTypeToCode", name=record.type)
                typelist.append(record.type)
        total = total + 100
    endtime=datetime.datetime.now()
    print '耗时：', (endtime-starttime).seconds, '秒'

#地点 邮编
def placetocode():
    print '开始转换'
    start = datetime.datetime.now()
    results = db.select("type_translate", where='code>99999', order='code DESC')
    for record in results:
        db.insert("placetocode", code=record.code, name=record.type)
    end = datetime.datetime.now()
    print '耗时： ', (end-start).seconds, '秒'

#接下来需要做聚类，将文本聚类

if __name__ == '__main__':
    placetocode()
