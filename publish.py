import paho.mqtt.publish as publish

class PubMqtt:
	def __init__(self,hostname='localhost'):
		self.hostname=hostname

	def respuesta(self,topic,mensaje):		
		publish.single(topic,mensaje, hostname=self.hostname)		
		
if __name__ == "__main__":
	enviar=PubMqtt()
	enviar.respuesta('control',"apagar")

