import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime

from jinja2 import Environment, FileSystemLoader, select_autoescape
from file_loader import loader

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape('[html]')
)
template = env.get_template('template.html')

now = datetime.datetime.now()
company_age = str(now.year - 1920)
wines = loader()

data_on_page = template.render(
    wines=wines,
    company_age=company_age
)

with open('index.html', 'w', encoding='utf8') as file:
    file.write(data_on_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
