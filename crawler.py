#coding=utf8
import web
import datetime
web.config.debug = False

def crawler():
	proj=web.database(host='222.201.131.208',port=3306,dbn='mysql',db='proj',user='myadmin',pw='scutensave')
	daplatform=web.database(dbn='mysql',db='daplatform',user='root',pw='123')
	starttime=datetime.datetime.now()
	print 'start crawler...'
	total=0
	while (total<=10000):
		results=proj.select("text", order='id DESC', limit=100, offset=total)
		for record in results:
			daplatform.insert('originText',id=record.id,title=record.title,type=record.type,date=record.date,accuser=record.accuser,defendant=record.defendant,publicProsecutionOrgan=record.publicProsecutionOrgan,authorizedAgent=record.authorizedAgent,issue=record.issue,crime=record.crime,law=record.law,judgement=record.judgement,content=record.content,place=record.place)
		total=total+100
	endtime=datetime.datetime.now()
	print 'cost time ',(endtime-starttime).seconds,' s'

def codecrawler():
	proj=web.database(host='222.201.131.208', port=3306, dbn='mysql', db='proj', user='myadmin', pw='scutensave')
	daplatform=web.database(dbn='mysql', db='daplatform', user='root', pw='123')
	starttime=datetime.datetime.now()
	print '开始收集数据'
	results=proj.select("type_translate", order='code DESC')
	for record in results:
		daplatform.insert("type_translate", code=record.code, type=record.type)
	endtime=datetime.datetime.now()
	print '耗时 ：', (endtime-starttime).seconds ,' s'

if __name__=="__main__":
	codecrawler()

