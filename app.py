import web
from controller import Index

urls = ('/', 'Index')

app = web.application(urls, globals())

if __name__ == '__main__':
	app.run()