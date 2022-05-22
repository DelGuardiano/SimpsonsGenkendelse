from pymongo import MongoClient
import datetime

cluster = MongoClient("mongodb+srv://Admin:admin@cluster0.nrum9.mongodb.net/4SemesterProjekt?retryWrites=true&w=majority")
db = cluster["4SemesterProjekt"]

class Karakterer():  
    def get_all(self):
        data = list(db.Karakterer.find({}))
        return data

    def get_name(self):
        data = list(db.Karakterer.find({}, {'_id': False, 'total': False, 'train': False, 'test': False, 'bounding_box': False}).sort("name", +1))
        return data

    def get_total(self):
        data = list(db.Karakterer.find({}, {'_id': False, 'total': False, 'train': False, 'test': False, 'bounding_box': False}))
        return data
    
    def get_train(self):
        data = list(db.Karakterer.find({}, {'_id': False, 'test': False, 'bounding_box': False}))
        return data

    def get_test(self):
        data = list(db.Karakterer.find({}, {'_id': False, 'total': False, 'train': False, 'bounding_box': False}))
        return data
    
labels = Karakterer().get_name() 

class Bruger():
    def get_user(self, user):
        user = list(db.Brugere.find({'brugernavn': user}))
        return user
    
    def create_user(self, user, password):
        db.Brugere.insert_one({'Brugernavn': user, 'Password': password})

save_new_user = Bruger().create_user

date = datetime.datetime.now() 
dt = date.strftime("%d-%m-%Y %H:%M:%S")
author = "admin"

class Gem():
    def add_to_database(self, img, name, author, date):
        db.Forudsigelse.insert_one({"Navn": name, "Billed": img, "Forfatter": author, "Oprettelsesdato": dt})


add_to_database = Gem().add_to_database

class Forudsigelse():
    def get_all(self):
        data = list(db.Forudsigelse.find({}, {'_id':False}))
        return data
    
    def get_name(self):
        data = list(db.Forudsigelse.find({}, {'_id': False, 'img': False, 'author': False, 'date': False}).sort("name", +1))
        return data
    
    def get_author(self):
        data = list(db.Forudsigelse.find({}, {'_id': False, 'img': False, 'name': False, 'date': False}).sort("author", +1))
        return data
    
    def get_time(self):
        data = list(db.Forudsigelse.find({}, {'_id': False, 'img': False, 'name': False, 'author': False}).sort("date", +1))
        return data

former_prediction = Forudsigelse().get_all()

