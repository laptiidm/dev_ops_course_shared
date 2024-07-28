import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)

# Установка базової директорії як директорії, що знаходиться на рівень вище project
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Вказати шлях до бази даних у папці instance на рівень вище project
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'database.db')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
api = Api(app)

# Request parser and fields for marshalling
user_args = reqparse.RequestParser()
user_args.add_argument('user_name', type=str, help='"user_name" field is required, check passed fields')
user_args.add_argument('user_lastname', type=str, help='"user_lastname" field is required, check passed fields')
user_args.add_argument('user_age', type=str, help='"user_age" field is required, check passed fields')

userFields = {
    'id': fields.Integer,
    'user_name': fields.String,
    'user_lastname': fields.String,
    'user_age': fields.String
}

# Define SQLAlchemy model
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(80), nullable=False)
    user_lastname = db.Column(db.String(80), nullable=False)
    user_age = db.Column(db.String(), nullable=False)

    def __repr__(self) -> str:
        return f'User (name = {self.user_name})'

# Define your resources
class User(Resource):
    @marshal_with(userFields)
    def get(self, id=None, lastname=None):
        if id:
            user = UserModel.query.filter_by(id=id).first()
            if not user:
                abort(404, message="User not found")
            return user

        if lastname:
            users = UserModel.query.filter_by(user_lastname=lastname).all()
            if not users:
                abort(404, message="Users not found")
            return users

        users = UserModel.query.all()
        return users

    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        provided_args = {key: value for key, value in args.items() if value is not None}
        missing_fields = [key for key, value in args.items() if value is None]

        # Custom validation for all fields
        if not provided_args:
            abort(400, message="All fields are missing")

        if missing_fields:
            abort(400, message=f"The following field(s) are missing: {', '.join(missing_fields)}")

        # Check for any extra fields
        allowed_fields = {'user_name', 'user_lastname', 'user_age'}
        extra_fields = set(request.json.keys()) - allowed_fields
        if extra_fields:
            abort(400, message=f"Field(s) {', '.join(extra_fields)} are not allowed")

        new_user = UserModel(user_name=args['user_name'],
                             user_lastname=args['user_lastname'],
                             user_age=args['user_age'])

        db.session.add(new_user)
        db.session.commit()

        return new_user, 201
    
    @marshal_with(userFields)
    def put(self, id):
        args = user_args.parse_args()

        # Initialize dictionaries for provided arguments and list for missing fields
        provided_args = {}
        missing_fields = []

        # Iterate over the arguments to filter provided ones and identify missing ones
        for key, value in args.items():
            if value is not None:
                provided_args[key] = value
            else:
                missing_fields.append(key)

        # Check if no fields are passed
        if not provided_args:
            abort(400, message="No fields provided to update")

        # Check for any extra fields
        allowed_fields = {'user_name', 'user_lastname', 'user_age'}
        if len(allowed_fields) != len(provided_args):
            abort(400, message="Partial replacement is not allowed for PUT method, there must be all required fields")

        extra_fields = set(request.json.keys()) - allowed_fields
        if extra_fields:
            abort(400, message=f"Field(s) {', '.join(extra_fields)} are not allowed")

        # Find the user by ID
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")

        # Update the user fields
        if 'user_name' in provided_args:
            user.user_name = provided_args['user_name']
        if 'user_lastname' in provided_args:
            user.user_lastname = provided_args['user_lastname']
        if 'user_age' in provided_args:
            user.user_age = provided_args['user_age']

        db.session.commit()

        return user, 200
    
    @marshal_with(userFields)
    def patch(self, id):
        args = user_args.parse_args()
        if not args['user_age']:
            abort(400, message="The 'user_age' field is required in the request body for PATCH request.")

        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")

        user.user_age = args['user_age']

        db.session.commit()

        return user, 200
    
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")

        db.session.delete(user)
        db.session.commit()

        return {'message': 'User deleted successfully'}, 200

# add resources to the API
api.add_resource(User, '/api/users/', '/api/users/<int:id>', '/api/users/lastname/<string:lastname>')

if __name__ == "__main__":
    app.run(debug=True)