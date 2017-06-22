from flask import Flask, Response, render_template, request
import json

app = Flask(__name__)

NAMES=["abc","abcd","abcde","abcdef"]

@app.route('/autocomplete',methods=['GET'])
def autocomplete():
    search = request.args.get('autocomplete')
    app.logger.debug(search)
    return Response(json.dumps(NAMES), mimetype='application/json')

@app.route('/',methods=['GET','POST'])
def index():
    form = request.form.get("autocomp")
    return render_template("index.html",form=form)

if __name__ == '__main__':
    app.run(debug=True)
