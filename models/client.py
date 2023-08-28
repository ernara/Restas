from app import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.String(40), unique=True, nullable=False)
    client_secret = db.Column(db.String(55), nullable=False)
    redirect_uris = db.Column(db.Text)
    
    def get_redirect_uris(self):
        return self.redirect_uris

    def get_default_redirect_uri(self):
        return self.redirect_uris[0] if self.redirect_uris else None

    def check_redirect_uri(self, redirect_uri):
        return redirect_uri in self.redirect_uris if self.redirect_uris else False
