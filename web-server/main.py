import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
	return [1,2,3]

@app.get('/contact')
def get_list():
	return {'name': 'hsk'}

@app.get('/page', response_class=HTMLResponse)
def get_list():
	return  """
		<h1>Hola, soy una página web</h1>
		<p>y una muy bonita</p>
	"""

def run():
	store.get_categories()

if __name__ == '__main__':
	run()
