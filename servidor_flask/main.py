from flask import Flask, request

app = Flask(__name__)
contador = 0


@app.route("/")
def helloworld():
    global contador
    contador += 1

    return f"Hello World! numero de visitas: {contador}"


@app.route("/patata")
def hello_poteito():
    def sanitize(arg):
        cantidad = 0
        try:
            cantidad = int(request.args.get(arg))
        except TypeError:
            pass
        except ValueError:
            pass

        return cantidad

    respuesta = f"Hello POTEIGOO! Nº {contador}"

    cantidad = sanitize('cantidad')
    respuesta += f"cantidad: {cantidad}"
    respuesta += "<ul>"
    for i in range(cantidad):
        respuesta += f"<li>{i}</li>"
    respuesta += "</ul>"

    return respuesta


if __name__ == "__main__":
    app.run()
