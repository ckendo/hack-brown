from dasher import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    description = db.Column(db.String(120), unique=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<User %r>' % self.name

db.drop_all()
db.create_all()

prepopulated_models = [
    User('Kenji Endo', 'I like kayaking'),
    User('Test Endo', 'I like kayaking'),
    User('Kenji Test', 'I like kayaking')
]

[db.session.add(model) for model in prepopulated_models]
db.session.commit()
