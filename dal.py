from pymongo import MongoClient

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
print(labels)

