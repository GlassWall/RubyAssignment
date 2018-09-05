from flask import Blueprint, request
from flask.json import jsonify
from werkzeug.utils import redirect
from flask import make_response
from service import shorten_url, fetch_original, fetch_list, delete_url
import io
import csv

bp = Blueprint('api', __name__, url_prefix='/shortner')

def transform(text_file_contents):
    return text_file_contents.replace("=", ",")

@bp.route('/shorten', methods=['POST'])
def shorten_url_():
    url = request.form.get('url')
    # url= request.get_json()
    short_url = shorten_url(url)
    return jsonify({'status': 'success', 'short_url': short_url}), 201

@bp.route('/shortencsv', methods=['POST'])
def shorten_csv():
    f = request.files['data_file']
    if not f:
        return "No file"

    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    # print("file contents: ", file_contents)
    # print(type(file_contents))
    print(csv_input)
    for row in csv_input:
        print(row)

    stream.seek(0)
    result = transform(stream.read())

    response = make_response(result)
    response.headers["Content-Disposition"] = "attachment; filename=result.csv"
    return response
   # return jsonify({'status': file.read()}), 201

@bp.route('/shorten', methods=['GET'])
def return_all_urls():
    return jsonify(fetch_list()), 200


@bp.route('/original/<shortened>', methods=['GET'])
def original_url(shortened):
    return jsonify({'original_url': fetch_original(shortened)}), 200


@bp.route('/delete/<hash>', methods=['DELETE'])
def delete(hash):
    delete_url(hash)
    return '', 204


@bp.route('/redirect/<hash>', methods=['GET'])
def redirect(hash):
    return redirect(fetch_original(hash), 302)
