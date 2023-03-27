from flask import Flask, render_template,request
from publish import PubMqtt

app=Flask(__name__)


@app.route('/datos')
def datos():
	print(request.args)
	status=request.args.get('accion')
	enviar=PubMqtt()
	enviar.respuesta('control',status)	
	return 'la bomba se debe: {}'.format(status)


if __name__ =="__main__":
	#app.add_url_rule('/',view_func=index)
	app.run(debug=True)