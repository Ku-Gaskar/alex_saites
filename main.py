
from flask import Flask, render_template,request,redirect,url_for
from psycopg2 import Error


from DB_SQL_Alchemy import Games,db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgress@localhost/alex_100'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)



@app.route("/selectJson/<id>",methods=['GET', 'POST'])
def selectJson(id):
    data:Games=Games.query.filter(Games.id_game_group == id.split('.')[0]).all()
    res=';'.join(f"{game.id_game}':'{game.name_game} {game.name_game_ext if game.name_game_ext else ''} " for game in data)
    # a=jsonify(data)
    # for game in data:
    #     res[game.id_game] = game.name
    # res=jsonify(res)
    return res

@app.route("/searchGame", methods=['GET'])
def searchGame():    
    content={}
    content['title'] = '100/100'
    if request.args.get('search'):
        textSearch = request.args.get('search')
        content['info'] = ''
        try:
            content['info'] = Games.query.filter(Games.name_game.ilike(f"%{textSearch}%")).order_by(Games.id_game).all()
        except (Exception,Error) as error:
            print(f"Ошибка чтения из БД:{error}")
        
        return render_template('index.html',content=content)
    else:
        return redirect('/')


@app.route('/',methods=['GET', 'POST'])
@app.route('/index',methods=['GET', 'POST'])
def index():
    
    if request.method== 'GET':
        print(request.url)

    content={}
    content['title'] = '100/100'
    content['info'] = ''
    try:
        content['info'] = Games.query.order_by(Games.id_game).all()
    except (Exception,Error) as error:
        print(f"Ошибка чтения из БД:{error}")

    return render_template('index.html',content=content)

if __name__ == '__main__':
    app.run(host='192.168.1.102', port=8000, debug=True)
 