from flask import Flask, jsonify

#instanciar la aplicacion, se agrega variable interna de pyhton name
app = Flask(__name__)


#ventana de bienvenida para python de tipo get
@app.route('/',methods=['GET'])

#definir una funcion inicial
def index():
    my_set = {f'Mensaje : Bienvenido '}
    return jsonify('Mensaje : Bienvenido Oscar')

#inicializar la aplicacion
if __name__=="__main__":
    app.run(debug=True)

