from flask import Flask, request, render_template
import codecs

app = Flask(__name__, template_folder='templates')


@app.route('/<file>')
@app.route('/')
def content(file='file1.txt'):
    start = request.args.get('start', 0)
    end = request.args.get('end', 100)

    with codecs.open(file, encoding='cp1251', errors='replace') as fn:
        lines = fn.readlines()[int(start): int(end)]
        return render_template('content.html',
                               data=' '.join(map(str, lines)))


if __name__ == "__main__":
    app.run(port=5000, debug=True)
