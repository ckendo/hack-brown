def populate_db(db):
    # make our people

    # 1
    db.execute('INSERT INTO users (name, image_url, age, state, gender, language, description) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     ['Kenji Endo', '', 18, 'DE', 'male', 'English', 'I like kayaking'])

    # 2
    db.execute('INSERT INTO users (name, image_url, age, state, gender, language, description) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     ['Michael Markell', '', 19, 'DE', 'male', 'English', 'I like underwater basket weaving ;))'])
    # 3
    db.execute('INSERT INTO users (name, image_url, age, state, gender, language, description) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     ['Miranda Chao', '', 19, 'NY', 'female', 'English', 'I sleep a lot'])

    # 4
    db.execute('INSERT INTO users (name, image_url, age, state, gender, language, description) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     ['Elbert Wang', '', 19, 'CA', 'male', 'English', 'I like binge eating'])

    # 5
    db.execute('INSERT INTO users (name, image_url, age, state, gender, language, description) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     ['Molly Long', '', 21, 'CA', 'female', 'English', 'I like bunnies'])

    # 6
    db.execute('INSERT INTO users (name, image_url, age, state, gender, language, description) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     ['Mackenzie Clark', '', 22, 'OR', 'female', 'English', 'I like long naps on the beach'])

    # make our interests
    # 1
    db.execute('INSERT INTO interests (name, image_url, description) VALUES (?, ?, ?)',
                     ['Underwater Basket Weaving', '', 'Really fun outdoor activity underwater that\'s quite fun'])

    # 2
    db.execute('INSERT INTO interests (name, image_url, description) VALUES (?, ?, ?)',
                     ['Reindeer Watching', '', 'Like bird watching, but reindeer'])

    # 3
    db.execute('INSERT INTO interests (name, image_url, description) VALUES (?, ?, ?)',
                     ['Kayaking', '', 'Like underwater basket weaving, but more adventurous'])

    # 4
    db.execute('INSERT INTO interests (name, image_url, description) VALUES (?, ?, ?)',
                     ['Knitting', '', 'Really fun indoor activity without water that\'s quite fun'])

    # 5
    db.execute('INSERT INTO interests (name, image_url, description) VALUES (?, ?, ?)',
                     ['Drooling', '', 'Like underwater basket weaving, but your face, and no baskets'])

    # 6
    db.execute('INSERT INTO interests (name, image_url, description) VALUES (?, ?, ?)',
                     ['Sliding', '', 'By land or by sea'])

    # 7
    db.execute('INSERT INTO interests (name, image_url, description) VALUES (?, ?, ?)',
                     ['Candle Making', '', 'Let there be light'])

    # make our peoples' interests

    # 1
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [1, 6])

    # 2
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [1, 1])

    # 3
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [1, 4])

    # 4
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [2, 5])
    # 5
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [2, 2])
    # 6
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [2, 1])

    # 7
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [3, 4])

    # 8
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [3, 5])

    # 9
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [3, 6])

    # 10
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [4, 7])
    # 11
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [4, 4])

    # 12
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [5, 4])

    # 13
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [5, 7])

    # 14
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [6, 6])

    # 15
    db.execute('INSERT INTO user_interests (user_id, interest_id) VALUES (?, ?)',
                     [6, 2])

    db.commit()
