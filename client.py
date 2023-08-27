from app import db

class Client:
    def __init__(self, client_id, client_secret, redirect_uris):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uris = redirect_uris

    def get_redirect_uris(self):
        return self.redirect_uris

    def get_default_redirect_uri(self):
        return self.redirect_uris[0]

    def check_redirect_uri(self, redirect_uri):
        return redirect_uri in self.redirect_uris


# Sample client data
clients = {
    'sample-client': Client(
        'sample-client',
        'sample-secret',
        ['http://localhost:5000/authorized']
    )
}