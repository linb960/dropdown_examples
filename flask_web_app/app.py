from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:GoBrewers12@localhost:5432/WTA"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class players(db.Model):
    __tablename__ = 'player_ranking'

    ranking = db.Column(db.Integer)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    country = db.Column(db.String())
    date = db.Column(db.Integer())
    id = db.Column(db.Integer(), primary_key=True)
    full_name = db.Column(db.String())

    def __init__(self, ranking, first_name, last_name, country, date, id, full_name):
        self.ranking = ranking
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.date = date
        self.id = id
        self.full_name = full_name

    def __repr__(self):
        return f"<Player {self.name}>"

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/input")
def input():
      return render_template("input.html", players = players.query.with_entities(players.full_name, players.last_name).distinct().where(players.ranking < 150).order_by(players.last_name))

@app.route('/playerone', methods=['GET', 'POST'])
def playerone():
    if request.method == "POST":
        player_1 = request.form.get("playerone", None)
        if player_1!=None:
            return render_template("index.html", player_1 = player_1)
    
@app.route('/playertwo', methods=['GET', 'POST'])
def playertwo():
    if request.method == "POST":
        player_2 = request.form.get("playertwo", None)
        if player_2!=None:
            return render_template("index.html", player_2 = player_2)


@app.route('/reset')
def reset():
    return render_template("index.html")

# @app.route('/cars', methods=['POST', 'GET'])
# def handle_cars():
#     if request.method == 'POST':
#         if request.is_json:
#             data = request.get_json()
#             new_car = CarsModel(name=data['name'], model=data['model'], doors=data['doors'])
#             db.session.add(new_car)
#             db.session.commit()
#             return {"message": f"car {new_car.name} has been created successfully."}
#         else:
#             return {"error": "The request payload is not in JSON format"}

#     elif request.method == 'GET':
#         cars = CarsModel.query.all()
#         results = [
#             {
#                 "name": car.name,
#                 "model": car.model,
#                 "doors": car.doors
#             } for car in cars]

#         return {"count": len(results), "cars": results}

# @app.route('/cars/<car_id>', methods=['GET', 'PUT', 'DELETE'])
# def handle_car(car_id):
#     car = CarsModel.query.get_or_404(car_id)

#     if request.method == 'GET':
#         response = {
#             "name": car.name,
#             "model": car.model,
#             "doors": car.doors
#         }
#         return {"message": "success", "car": response}

#     elif request.method == 'PUT':
#         data = request.get_json()
#         car.name = data['name']
#         car.model = data['model']
#         car.doors = data['doors']
#         db.session.add(car)
#         db.session.commit()
#         return {"message": f"car {car.name} successfully updated"}

#     elif request.method == 'DELETE':
#         db.session.delete(car)
#         db.session.commit()
#         return {"message": f"Car {car.name} successfully deleted."}

if __name__ == '__main__':
    app.run(debug=True)