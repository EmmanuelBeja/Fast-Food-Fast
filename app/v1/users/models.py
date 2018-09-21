"""app/v1/users/models.py"""
from flask import jsonify, session
import re


class User(object):
    def __init__(self):
        """ Initialize empty user list"""
        self.user_list = []
        self.notfound = None

    def create_user(self, username, userphone, password, userRole):
        """Create users"""
        self.users = {}
        if not self.valid_username(username):
            self.id = len(self.user_list)
            self.users['username'] = username
            self.users['userphone'] = userphone
            self.users['password'] = password
            self.users['userRole'] = userRole
            self.users['userid'] = self.id + 1
            self.user_list.append(self.users)
            return jsonify({"message": "Successful", "user": self.users}), 201
        return jsonify({"message": "Username is taken."}), 400

    def login(self, username, password):
        """login users"""
        if len(self.user_list) == 0:
            return jsonify({"message": "Please register first."})
        else:
            for user in self.user_list:
                if username == user['username']:
                    if password == user['password']:
                        session['userid'] = user['userid']
                        session['username'] = user['username']
                        return jsonify({
                            "message": "You are successfully logged in",
                            "user": user}), 201
                    else:
                        return jsonify({
                            "message": "Wrong username or password"}), 401
                else:
                    return jsonify({"message": "user does not exist"}), 200

    def get_specific_user(self, id):
        """get specific user """
        user = [user for user in self.user_list if user['userid'] == id]
        return jsonify({
            "message": "Successful.",
            "User": user}), 200

    def get_users(self):
        """get all user """
        return jsonify({
            "message": "Successful.",
            "Users": self.user_list}), 200

    def update_user(
            self,
            id,
            username,
            userphone,
            password,
            userRole):
        """ update User """
        for user in self.user_list:
            if user['userid'] == id:
                user['username'] = username
                user['userphone'] = userphone
                user['password'] = password
                user['userRole'] = userRole
                return jsonify({
                    "message": "Update Successful.",
                    "Users": self.user_list}), 201
            self.notfound = True
        if self.notfound is True:
            return jsonify({
                "message": "User doesn't exist.",
                "Users": self.user_list}), 400

    def delete_user(self, id):
        """ delete User """
        for user in self.user_list:
            if user['userid'] == id:
                self.user_list.remove(user)
                return jsonify({
                    "message": "Delete Successful.",
                    "Users": self.user_list}), 201
            self.notfound = True
        if self.notfound is True:
            return jsonify({
                "message": "user doesn't exist.",
                "Users": self.user_list}), 404

    def valid_username(self, username):
        """check if username exist"""
        if len(self.user_list):
            for user in self.user_list:
                if user['username'] == username:
                    return True
                else:
                    return False
        return False

    def valid_password(self, password):
        """check password length and special characters"""
        if len(password) < 3 or not re.match("^[a-zA-Z0-9_ ]*$", password):
            return False
        else:
            return True
