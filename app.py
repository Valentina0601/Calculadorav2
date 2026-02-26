from flask import Flask, render_template, request
# aplicación de calculadora


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("inicio.html")




@app.route("/suma", methods=["GET", "POST"])
def sumar():
    if request.method == "POST":
        if not request.form.get("numero1") or not request.form.get("numero2"):
            return render_template("suma.html", error="Por favor, ingresa ambos números.")
        numero1 = float(request.form.get("numero1"))
        numero2 = float(request.form.get("numero2"))
        resultado = numero1 + numero2
        return render_template("suma.html", resultado=resultado)
    
    return render_template("suma.html")


@app.route("/division", methods=["GET", "POST"])
def dividir():
    if request.method == "POST":
        if not request.form.get("numero1") or not request.form.get("numero2"):
            return render_template("división.html", error="Por favor, ingresa ambos números.")
        numero1 = float(request.form.get("numero1"))
        numero2 = float(request.form.get("numero2"))
        if numero2 == 0:
            return render_template("división.html", error="No se puede dividir entre cero.")
        resultado = numero1 / numero2
        return render_template("división.html", resultado=resultado)
    
    # al mostrar la página por primera vez no hay resultado ni error
    return render_template("división.html", resultado=None)


if __name__ == '__main__':
    app.run(debug=True)