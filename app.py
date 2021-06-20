from flask import Flask,render_template,request
import requests

api_key = "b604ad3855e14aff0aea598deae2ef85"

url ="http://data.fixer.io/api/latest?access_key="+api_key

app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():
    
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency")
        secondCurrency = request.form.get("secondCurrency")
        amount = request.form.get("amount")
        response = requests.get(url)
        app.logger.info(response)

        infos = response.json()

        firstValue = infos["rates"][firstCurrency]
        seconValue = infos["rates"][secondCurrency]
        result = (seconValue/firstValue)*float(amount)
        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result
        return render_template("index.html",info = currencyInfo)
    else:
        return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)