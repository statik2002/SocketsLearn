import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print(f'Клиент {sid} подключен')
    print(f'Environ {environ}')


@sio.event
def disconnect(sid):
    print(f'Клиент {sid} отключен')


eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
