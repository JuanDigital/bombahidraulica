from flask import Flask, render_template,request
from multi import multiplica

app=Flask(__name__)

#@app.route('/')

def index():
	data={'titulo':'Bienvenido','encabezado':'paz mundial'}
	return render_template('index.html',data=data)

def Hi():
	return"Hola Mundo"

@app.route('/contacto')
def contacto():
	data={'titulo':'contacto','encabezado':'directorio'}
	return render_template('contacto.html',data=data)

@app.route('/saludo/<names>')
def saludo(names):
	nombre=names
	data={'titulo':'saludo','encabezado':'saludo'}
	return 'Hola {}'.format(nombre) #render_template('contacto.html',data=data)

@app.route('/suma/<int:val1>/<int:val2>')
def suma(val1,val2):
	return 'la suma es: {} '.format(val1+val2)

@app.route('/multiplica/<int:val1>/<int:val2>')
def multi(val1,val2):
	multi=multiplica(val1,val2)
	return "el resultado de la multi es {}".format(multi.resultado())
@app.route('/datos')
def datos():
	print(request.args)
	a=request.args.get('dat1')
	b=request.args.get('dat2')
	return 'los datos son:{},{}'.format(a,b)


if __name__ =="__main__":
	app.add_url_rule('/',view_func=index)
	app.run(debug=True)