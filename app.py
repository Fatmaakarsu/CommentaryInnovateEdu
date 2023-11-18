from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_bcrypt import Bcrypt
from flask_bcrypt import Bcrypt  # Add this import if you are using Flask-Bcrypt
# from sinkaf import Sinkaf
# sinkaf_model = Sinkaf()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# def is_comment_bad(comment_text):
#     result = sinkaf_model.tahmin([comment_text])[0]
#     return result

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(200), nullable=False)
    likes = db.Column(db.Integer, default=0)
    parent_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    children = db.relationship('Comment', backref=db.backref('parent', remote_side=id), lazy='dynamic')

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False)
    __table_args__ = (db.UniqueConstraint('person_id', 'comment_id', name='_person_comment_uc'),)

@app.route('/comments', methods=['GET'])
def get_comments():
    # get all comments
    comments = Comment.query.all()

    if not comments:
        # return empty list if no comments
        return jsonify([])
    # return all comments with person username and likes count
    all_comments = []
    for comment in comments:
        person = Person.query.get(comment.person_id)
        username = person.username

        # get likes count
        likes = Like.query.filter_by(comment_id=comment.id).all()
        comment.likes = len(likes)

        # get comment children
        children = []
        for child in comment.children:
            # get likes count
            likes = Like.query.filter_by(comment_id=child.id).all()
            child.likes = len(likes)

            children.append({
                'id': child.id,
                'text': child.comment,
                'username': child.username,
                'likes': child.likes,
                'parent_id': child.parent_id if child.parent_id else 'null'
            })

        # sort children by likes
        children.sort(key=lambda x: x['likes'], reverse=True)

        all_comments.append({
            'id': comment.id,
            'text': comment.comment,
            'username': username,
            'likes': comment.likes,
            'children': children,
            'parent_id': comment.parent_id if comment.parent_id else 'null'
        })

        # sort comments by likes
        all_comments.sort(key=lambda x: x['likes'], reverse=True)



    return jsonify(all_comments)

# /comments/${commentId}/like client will send username
@app.route('/comments/<int:comment_id>/like', methods=['POST'])
def like_comment(comment_id):
    username = request.json.get('username')
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({'error': 'Comment not found.'}), 404

    person = Person.query.filter_by(username=username).first()

    if not person:
        return jsonify({'error': 'Person not found.'}), 404

    like = Like.query.filter_by(person_id=person.id, comment_id=comment_id).first()

    if like:
        return jsonify({'error': 'Person already liked this comment.'}), 400

    like = Like(person_id=person.id, comment_id=comment_id)
    db.session.add(like)
    db.session.commit()

    # return success true
    return jsonify({'success': True}), 200

# /comments/${commentId} also client will send username
@app.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    username = request.json.get('username')
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({'error': 'Comment not found.'}), 404

    person = Person.query.filter_by(username=username).first()

    if not person:
        return jsonify({'error': 'Person not found.'}), 404

    if comment.person_id != person.id:
        return jsonify({'error': 'Comment does not belong to person.'}), 400
    
    # delete all children of comment
    for child in comment.children:
        db.session.delete(child)

    db.session.delete(comment)
    db.session.commit()

    return jsonify({'success': True}), 200


# /comments/${commentId} also client will send username and text of comment
@app.route('/comments/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    username = request.json.get('username')
    text = request.json.get('text')
    comment = Comment.query.get(comment_id)
    # get person by username
    person = Person.query.filter_by(username=username).first()

    if not person:
        return jsonify({'error': 'Person not found.'}), 404
    
    # check if comment belongs to person
    if comment.person_id != person.id:
        return jsonify({'error': 'Comment does not belong to person.'}), 400



    if not comment:
        return jsonify({'error': 'Comment not found.'}), 404

    comment.comment = text
    db.session.commit()

    return jsonify({'success': True}), 200

@app.route('/comments', methods=['POST'])
def add_comment():
    username = request.json.get('username')
    text = request.json.get('text')

    person = Person.query.filter_by(username=username).first()

    if not person:
        return jsonify({'success': False}), 404

    # if is_comment_bad(text):
    #    return jsonify({'success': False, 'message': 'hakaret'})

    
    # check for parent id
    parent_id = request.json.get('parent_id')

    comment = Comment(comment=text, person_id=person.id, username=username, likes=0, parent_id=parent_id)

    db.session.add(comment)
    db.session.commit()

    return jsonify({'success': True}), 200


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        req_email = request.form.get('email')
        req_password = request.form.get('password')

        user = Person.query.filter_by(email=req_email).first()

        if user and req_password == user.password:
            # create session for user
            left_image_url = "https://github.com/Fatmaakarsu/project-task/blob/main/Senaryo.png?raw=true"
            right_image_url = "https://github.com/Fatmaakarsu/project-task/blob/main/editor.png?raw=true"
            
            return render_template('home.html', left_image_url=left_image_url, right_image_url=right_image_url, user_id = user.id, username=user.username, email=user.email, full_name=user.full_name)

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
