from flask import Blueprint, request, redirect, render_template, url_for
from models import Zip
import json

home = Blueprint('home', __name__, template_folder='templates')


@home.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home/index.html')

@home.route('/next', methods=['GET', 'POST'])
def next():
    if request.args.get('zip') != '':
        zip = Zip.query.filter_by(zip=request.args.get('zip').zfill(5)).first()
        if zip:
            dti_conv = _dti_to_json(zip.dti_info(1))
            dti_fha = _dti_to_json(zip.dti_info(2))
            return render_template('home/next.html', zip=zip, dti_conv=dti_conv, dti_fha=dti_fha)
        else:
            return render_template('home/index.html', invalid_zip=True)
    else:
        return redirect('/')


def _dti_to_json(dti):
    if dti:
        return json.dumps(dti._asdict())
    else:
        return None