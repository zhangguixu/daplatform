#coding=utf8
#控制器，处理页面的跳转
import web

render = web.template.render('templates', base='base')

class Index:
    def GET(self):
        return render.index()
