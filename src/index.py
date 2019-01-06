from flask import Flask #Importo Flask desde flask para porder usarlo
from flask import render_template #Funcion que me permite regresar archivos

app = Flask(__name__) #Variable que almacena el objeto Flask con el que trabajaremos en el proyecto.

@app.route('/') #Indica al navegador el nombre de la ruta de un archivo
def home(): #Funcion que retorna algo al cliente
    return render_template('home.html') # render_template regresa el archivo que coincida dentro de la carpeta templates

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True) #Al asignar el valor True le indico al metodo que quiero que el objeto se reinicie automaticamente cuando realice un cambio en el archivo
    #Nota: Si realizo un cambio y este no se refleja en el navegador es debido al cache del mismo, para reiniciar sin memoria cache usaremos ctr + shift + r