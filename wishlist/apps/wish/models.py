from __future__ import unicode_literals
from django.db import models
import bcrypt
import datetime
now = datetime.datetime.now()


class UserManager(models.Manager):
    def login(self, username_in, pwd_in):
        error = False
        if len(username_in) < 2:
            error = True  # END OF EMAIL VALIDATION

        if len(pwd_in) < 8:
            error = True  # END OF PASSWORD VALIDATION

        if error is True:
            return False
        else:
            print Users.UserManager.get(username=username_in).username
            passwordHash = Users.UserManager.filter(username=username_in).last().password.encode()
            if bcrypt.hashpw(pwd_in, passwordHash) == passwordHash:
                return True
            else:
                return False

    def register(self, name_up, username_up, pwd_up):
        error = []
        if len(username_up) < 2:
            error.append("Too short!! Username should be at least 2 characters")
        elif not username_up:
            error.append("Username field must be filled out")  # END OF FIRST NAME VALIDATION

        if len(name_up) < 2:
            error.append("Please enter your full name")  # END OF EMAIL VALIDATION

        if len(pwd_up) < 8:
            error.append('Password is too short')
        if len(error) > 0:
            return [False, error]
        else:
            hashedPW = bcrypt.hashpw(pwd_up, bcrypt.gensalt())
            Users.UserManager.create(name=name_up, username=username_up, password=hashedPW, created_at=now)
            return [True]

    def validuser(self, username_valid):
        if len(username_valid) < 3:
            return True
        else:
            return False


    def validpassword(self, pass_valid):
        if len(pass_valid) < 9:
            return True
        else:
            return False

    def matchpasswords(self, password, confirmpass):
        if password != confirmpass:
            return True
        else:
            return False


class Users(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    date = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    UserManager = UserManager()


class Items(models.Model):
    name = models.CharField(max_length=45)
    owned_by = models.ManyToManyField(Users, blank=True)
    added_by = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ItemManager = UserManager()
