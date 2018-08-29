import sys
# sys.path.append('/models')
import time
import datetime
from pymongo import MongoClient
from bson.dbref import DBRef
from bson import ObjectId
from models.teacher import Teacher

## Initialize Database
mongo_uri = "mongodb://berk:berk123@ds133632.mlab.com:33632/himama-dev"
client = MongoClient(mongo_uri)

db = client['himama-dev']


## Initialize Teacher Object
jane = Teacher()


def test():
    
    jane.setFirstName("ali")
    a = jane.getFirstName()
    return a


def getTeacherById(teacherId):
    '''
    Get Teacher object from database using their Teacher ID
    '''
    teacher_object = None
    teacher = Teacher()
    
    try:
        teacher_object = db.teachers.find_one({'teacherId': teacherId})
    except:
        print "There was a problem with the database operation"
        
    if teacher_object:
        if "firstName" in teacher_object:
            teacher.setFirstName(teacher_object["firstName"])
            
        if "lastName" in teacher_object:    
            teacher.setLastName(teacher_object["lastName"])
            
        if "teacherId" in teacher_object:
            teacher.setTeacherId(teacher_object["teacherId"])
    else:
        print "Could not find teacher with ID: ", teacherId
        return  
        
        
    return teacher
    

def getTeacherByFirstName(firstName):
    '''
    Get Teacher object from database using their first Name
    '''
    teacher_object = None
    teacher = Teacher()
    
    try:
        teacher_object = db.teachers.find_one({'firstName': firstName})
    except:
        print "There was a problem with the database operation"
        
    if teacher_object:
        if "firstName" in teacher_object:
            teacher.setFirstName(teacher_object["firstName"])
            
        if "lastName" in teacher_object:    
            teacher.setLastName(teacher_object["lastName"])
            
        if "teacherId" in teacher_object:
            teacher.setTeacherId(teacher_object["teacherId"])
    else:
        print "Could not find teacher with first Name: ", firstName
        return  
        
        
    return teacher
    
    
def getTeacherByLastName(lastName):
    '''
    Get Teacher object from database using their Family Name
    '''
    teacher_object = None
    teacher = Teacher()
    
    try:
        teacher_object = db.teachers.find_one({'lastName': lastName})
    except:
        print "There was a problem with the database operation"
        
    if teacher_object:
        if "firstName" in teacher_object:
            teacher.setFirstName(teacher_object["firstName"])
            
        if "lastName" in teacher_object:    
            teacher.setLastName(teacher_object["lastName"])
            
        if "teacherId" in teacher_object:
            teacher.setTeacherId(teacher_object["teacherId"])
    else:
        print "Could not find teacher with family Name: ", lastName
        return  
        
        
    return teacher
    

def clock_in(clockInTime, teacherFirstName):
    '''
    Starts the clock when teacher arrives to work
    '''
    teacher_object = None
    now = datetime.datetime.now()
    
    try:
        teacher_object = db.teachers.find_one({'firstName': teacherFirstName})
    except:
        print "There was a problem with the database operation"
        
    if teacher_object:
        #update db with new clock_out value
        db.teachers.update(
        {
            '_id': teacher_object['_id']
        },
        {
            "$set": {"clockInTime": now, "clockType": "In"}
        })
        
    else:
        print "Could not find teacher with first Name: ", teacherFirstName
        return  
        
    
    
    
    
def clock_out(clockOutTime, teacherFirstName):
    '''
    Stops the clock when teacher leaves
    '''
    teacher_object = None
    now = today = datetime.datetime.now()
    
    try:
        teacher_object = db.teachers.find_one({'firstName': teacherFirstName})
    except:
        print "There was a problem with the database operation"
        
    if teacher_object:
        #update db with new clock_out value
        db.teachers.update(
        {
            '_id': teacher_object['_id']
        },
        {
            "$set": {"clockOutTime": now, "clockType": "Out"}
        })
        
    else:
        print "Could not find teacher with first Name: ", teacherFirstName
        return  
        

def teacher_database_insert(first_name):
    '''
    Create new teacher object
    '''
    try:
        db.teachers.insert({
            "firstName": first_name
        })
    except:
        print "Invalid Operation"
    
