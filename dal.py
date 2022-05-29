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
    def find_user(self, user, password): 
        findes = db.Brugere.count_documents({"Brugernavn": user, "Password": password}) > 0
        return findes

    def create_user(self, user, password):
        db.Brugere.insert_one({'Brugernavn': user, 'Password': password})

save_new_user = Bruger().create_user

date = datetime.datetime.now() 
dt = date.strftime("%d-%m-%Y %H:%M:%S")

class Gem():
    def add_to_database_sandt(self, img, name, author, date, prediction):
        db.Forudsigelse.insert_one({"Navn": name, "Billed": img, "Forfatter": author, "Oprettelsesdato": dt, "Forudsigelse": "Korrekt"})
    
    def add_to_database_falsk(self, img, name, author, date, prediction):
        db.Forudsigelse.insert_one({"Navn": name, "Billed": img, "Forfatter": author, "Oprettelsesdato": dt, "Forudsigelse": "Ikke korrekt"})

add_to_database_sandt = Gem().add_to_database_sandt
add_to_database_falsk = Gem().add_to_database_falsk

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
    
    def get_data(self):
        data = list(db.Forudsigelse.find({}, {'_id': False, 'img': False, 'name': False, 'author': False}).sort("date", +1))
        return data
    
    def get_prediction(self):
        data = list(db.Forudsigelse.find({}, {'_id': False, 'img': False, 'name': False, 'author': False, 'date': False}).sort("prediction", +1))
        return data
    

former_prediction = Forudsigelse().get_all()

