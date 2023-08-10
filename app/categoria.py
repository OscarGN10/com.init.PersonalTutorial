from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#instanciar la aplicacion, se agrega variable interna de pyhton name
app = Flask(__name__)

#cadena de conexion
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/bdpythonapi'
#para que nos esten saliendo alertas  o warnings d la conexion
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



#inicializar e instanciar
db = SQLAlchemy(app)
#
ma = Marshmallow(app)

#crear la clase que sera la tabla
class Categoria(db.Model):
    cat_id = db.Column(db.Integer,primary_key=True)
    cat_nom = db.Column(db.String(100))
    cat_desc = db.Column(db.String(100))

#declarar el constructor
    def __init__(self, cat_nom, cat_desc):
        self.cat_nom = cat_nom
        self.cat_desc = cat_desc

#Indicar que cree la tabla en la db
with app.app_context():
    db.create_all()


#Crear un esquema para la tabla categoria para que sea mas facil llamarlo
class CategoriasSchema(ma.Schema):
     class Meta:
        fields = ('cat_id','cat_nom','cat_desc')

#inicializar el esquema
#para cuando sea una sola respuesta
categoria_schema = CategoriasSchema()

#cuando sean muchas respuestas
categorias_schema = CategoriasSchema(many=True)



# metodo GET
@app.route('/categoria', methods=['GET'])
def get_categorias():
    all_categorias = Categoria.query.all()
    result = categorias_schema.dump(all_categorias)
    # convertir ese result a json (response)
    return jsonify(result)






#ventana de bienvenida para python de tipo get
@app.route('/',methods=['GET'])

#definir una funcion inicial
def index():
    my_set = {f'Mensaje : Bienvenido '}
    return jsonify('Mensaje : Bienvenido Oscar')

#inicializar la aplicacion
if __name__=="__main__":
    app.run(debug=True)

