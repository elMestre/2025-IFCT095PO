from flask import Flask, request

# Ejemplo de peticion
# http://127.0.0.1:5000/patata?color=rojo&cantidad=12&tamanyo=grande

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
    cantidad = sanitize('cantidad')
    respuesta += f"cantidad: {cantidad}"
    respuesta += f"tamanyo: {request.args.get("tamanyo")[::-1]}"
    respuesta += "<ul>"
    for i in range(cantidad):
        respuesta += f"<li>{i}</li>"
    respuesta += "</ul>"

    return respuesta


@app.route("/html")
def html():
    str_que_contiene_html = """<!DOCTYPE html>
<html>
    <head>
        <title>er titulico de mi páhina</title>
        <style>
            body {
                background-color: blueviolet;
                color: white;
            }

            .codigo {
                background-color: darkslategray;
                color: pink;
            }
        </style>

    </head>
    <body>
        <h1>Texto to gordako</h1>
        <p>Texto a tamañao mas normal</p>
        <p class="codigo">Este es un ejemplo</p>
        <img src="https://repository-images.githubusercontent.com/256318667/1ff44700-8a79-11ea-961e-a6eae4e5c8fd" width="480" alt="esta es una imagen de prueba" >
        <h2> Texto no estructurado <h2>
        <div>
            Hello, World Wide Web!
            This is my first website.

            About me

            I'm a Python programmer and a bug collector.

            Random facts

            I don't just like emoji,
            I love emoji!

            My most-used emoji are:
                1. 🐞
                2. 🐍
                3. 👍

            Links

            My favorite websites are:
                * realpython.com
                * python.org
                * pypi.org
        </div>

        <h2> Texto estructurado <h2>
            <h1>Hello, World Wide Web!</h1>
            <p>This is my first website.</p>

            <h2>About me</h2>
            <p>I'm a Python programmer and a bug collector.</p>

            <h3>Random facts</h3>
            <p>I don't just <em>like</em> emoji,<br>
            I <strong>love</strong> emoji!</p>
            <p>My most-used emoji are:</p>
            <ol>
                <li>🐞</li>
                <li>🐍</li>
                <li>👍</li>
            </ol>

            <h2>Links</h2>
            <p>My favorite websites are:</p>
            <ul>
                <li>realpython.com</li>
                <li>python.org</li>
                <li>pypi.org</li>
            </ul>
        <div>
        </div>

        <script>
            alert("MENSAJE DESDE JavaScript");
        </script>

    </body>
    </html>
<p>Este es <strong>un ejemplo</p></strong>
"""

    return str_que_contiene_html



if __name__ == "__main__":
    app.run()
