class tbuser(db.Model):
fullname = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(15), unique=True)
password = db.Column(db.String(128), unique=True)
email =db.Column(db.String(30), unique=True)
iddpt = db.Column(db.Integer, db.ForeignKey('tbdpt.iddpt'))
idrole = db.Column(db.Integer, db.ForeignKey('tbrole.idrole'))
def __init__(self, fullname, username, password, email, iddpt, idrole):
self.fullname = fullname
self.username = username
self.password = password
self.email = email
self.iddpt = iddpt #departamento
    def __repr__(self):
        return '<User %r>' % self.username
    
class tbdpt(db.Model):
iddpt= db.Column(db.Integer, primary_key=True)
namedpt= db.Column(db.String(50), unique=True)
user_dpt = db.relationship('tbuser', backref='tbdpt', lazy='dynamic')
def __init__(self, iddpt, namedpt):
self.iddpt = iddpt #departamento
self.namedpt = namedpt

class tbrole(db.Model):
idrole= db.Column(db.Integer, db.primary_key=True)
namerole= db.Column(db.String(50), unique=True)
user_role = db.relationship('tbuser', backref='tbrole', lazy='dynamic')
def __init__(self, idrole, namerole):
self.idrole = idrole #departamento
self.namerole = namerole