from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/produit',methods=['GET','POST'])
def produit():
    titre="Machallah"
    produits = {'banane':'Fruit provenant de la Guinée','pomme': 'fruit provenant de l\'Espagne','orange': 'Fruit provenant du Maroc','poire': 'Fruit provenant de l\'Algérie','mandarine':'Fruit provenant de la Maroc','mangue':'Fruit provenant du Senegal'}
    return render_template('produit.html',titre=titre,mesproduits=produits)


@app.route('/profil/<username>/<token>',methods=['GET'])
def profil(username, token):
    return f"<h1>Welcome {username} - Token {token} </h1>"

@app.route('/accueil')
def accueil():
    host = request.headers.get('User-agent')
    print(type(request.headers))
    return f'''
    <h1>La page d'accueil</h1>
    {host}
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18000, debug=True)