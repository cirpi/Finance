import requests
import json
from flask import (
    Blueprint, request, flash, session, render_template, redirect, url_for
)

blueprint = Blueprint('page', __name__, url_prefix='/page')


@blueprint.route('/news', methods=['GET', 'POST'])
def news():
    from . import api_url
    res = requests.get(api_url.get_endpoint('news'), params=api_url.auth_param())
    news_dict = json.loads(res.text)
    return render_template('news.html', news = news_dict)

@blueprint.route('/profiles', methods=['GET', 'POST'])
def profiles():
    if request.method == 'POST':
        ticker = request.form['ticker']
        from . import api_url
        res = requests.get(api_url.get_profile_endpoint(ticker), params=api_url.auth_param())
        profile_dict = json.loads(res.text)
        return render_template('profile.html', pro=profile_dict)
    return render_template('profiles.html')

@blueprint.route('profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')
