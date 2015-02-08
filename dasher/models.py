from dasher import db

interest_identifier = db.Table(
    'interest_identifier',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('interest_id', db.Integer, db.ForeignKey('interest.id')),
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    image_url = db.Column(db.String(200), unique=False)
    age = db.Column(db.Integer, unique=False)
    state = db.Column(db.String(10), unique=False)
    gender = db.Column(db.String(10), unique=False)
    language = db.Column(db.String(120), unique=False)
    description = db.Column(db.String(120), unique=False)
    interests = db.relationship("Interest", secondary=interest_identifier)

    def __init__(self, name, image_url, age, state, gender, language, description):
        self.name = name
        self.image_url = image_url
        self.age = age
        self.state = state
        self.gender = gender
        self.language = language
        self.description = description

    def __repr__(self):
        return 'User(name:%s, description:%s)' % (self.name, self.description)

    __str__ = __repr__

class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    image_url = db.Column(db.String(200), unique=False)
    description = db.Column(db.String(120), unique=False)

    def __init__(self, name, image_url, description):
        self.name = name
        self.image_url = image_url
        self.description = description

    def __repr__(self):
        return 'Interest(name:%s, description:%s)' % (self.name, self.description)

    __str__ = __repr__

db.drop_all()
db.create_all()

prepopulated_users = [
    User('Tala Huhe', '', 24, 'CA', 'male', 'English', 'I like potatoes'),
    User('Kenji Endo', '', 18, 'DE', 'male', 'English', 'I like kayaking'),
    User('Michael Markell', '', 19, 'DE', 'male', 'English', 'I like underwater basket weaving ;))'),
    User('Miranda Chao', '', 19, 'NY', 'female', 'English', 'I sleep a lot'),
    User('Elbert Wang', '', 19, 'CA', 'male', 'English', 'I like binge eating'),
    User('Molly Long', '', 21, 'CA', 'female', 'English', 'I like bunnies'),
    User('Mackenzie Clark', '', 22, 'OR', 'female', 'English', 'I like long naps on the beach')
]

prepopulated_interests = [
    Interest('Sleeping', '', 'Really really really fun outdoor activity underwater that\'s quite fun'),
    Interest('Underwater Basket Weaving', '', 'Really fun outdoor activity underwater that\'s quite fun'),
    Interest('Reindeer Watching', '', 'Like bird watching, but reindeer'),
    Interest('Kayaking', '', 'Like underwater basket weaving, but more adventurous'),
    Interest('Knitting', '', 'Really fun indoor activity without water that\'s quite fun'),
    Interest('Drooling', '', 'Like underwater basket weaving, but your face, and no baskets'),
    Interest('Sliding', '', 'By land or by sea'),
    Interest('Candle Making', '', 'Let there be light')
]

[db.session.add(model) for model in prepopulated_users]
[db.session.add(model) for model in prepopulated_interests]

prepopulated_users_to_interests_map = {
    1: [6, 1, 4],
    2: [5, 2, 1],
    3: [4, 5, 6],
    4: [7, 4],
    5: [4, 7],
    6: [6, 2]
}

for user_id, interest_ids in prepopulated_users_to_interests_map.iteritems():
    [prepopulated_users[user_id].interests.append(prepopulated_interests[id]) for id in interest_ids]

db.session.commit()
