from flask import Flask, render_template,request
from publish import PubMqtt

app=Flask(__name__)
@app.route('/')
def index():
	data={'titulo':'Bienvenido','encabezado':'Controla tu bomba'}
	return render_template('base.html',data=data)

@app.route('/datos')
def datos():
	print(request.args)
	status=request.args.get('accion')
	enviar=PubMqtt()
	enviar.respuesta('control',status)
	data={'titulo':'Bienvenido','encabezado':'Controla tu bomba'}
	estado={'actual':status}	
	return render_template('index.html',data=data,estado=estado)


if __name__ =="__main__":
	#app.add_url_rule('/',view_func=index)
	app.run(debug=True)