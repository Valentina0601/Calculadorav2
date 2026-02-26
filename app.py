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






if __name__ == '__main__':
    app.run(debug=True)