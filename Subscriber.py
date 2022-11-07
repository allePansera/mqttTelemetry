from Auth.MQTTSub import MQTTSub

subscriber = MQTTSub()
subscriberSession = subscriber.creaSessione()
subscriberSession.loop_forever()