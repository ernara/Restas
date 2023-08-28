from app import app, db, oauth

@app.route('/oauth/authorize', methods=['GET', 'POST'])
@oauth.authorize_handler
def authorize():
    return True

@app.route('/oauth/token', methods=['POST'])
@oauth.token_handler
def access_token():
    return None