from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime

from jinja2 import Environment, FileSystemLoader, select_autoescape
from file_loader import get_load, directory

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape('[html]')
)
template = env.get_template('template.html')

now = datetime.datetime.now()
company_age = now.year - 1920
wines = get_load(directory)

html_page = template.render(
    wines=wines,
    company_age=company_age
)

with open('index.html', 'w', encoding='utf8') as file:
    file.write(html_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
