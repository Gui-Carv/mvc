from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/t2')
def teste1():
    return render_template('index.html')

@app.route('/gravar', methods=['POST'])
def teste2():
    nomerec = request.form['nome']
    print(nomerec)
    emailrec = request.form['email']
    print(emailrec)
    senharec = request.form['senha']
    print(senharec)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)