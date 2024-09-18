import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    # sid - идентификатор пользователя
    # environ - информация о подключении
    print(f'Клиент {sid} подключен')
    print(f'Environ {environ}')


@sio.event
def disconnect(sid):
    print(f'Клиент {sid} отключен')


@sio.on('message')
def incoming_message(sid, data):
    print(f'message {data} от клиента {sid}')


@sio.on('*')
def catch_all(event, sid, data):
    sio.emit('error', {'message': f'No handler for event {event}'})


eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
