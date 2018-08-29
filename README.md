# HiMama-Coding-Challenge

## Run the app
Run the app by typing the following command from the project root directory:

python app.py

(You might need to install Flask & PyMongo -- type: pip install flask and pip install pymongo to download the dependencies)

Then go to localhost:5000 in Google Chrome to view the app.

(Refresh the page to start again)

## Use Case
Enter "Jane" (test teacher object that I created on mLab) as first name. If it cannot find a teacher with first name "Jane" it will insert a new one to the database. 

After entering first name - you will see the buttons to either "Clock In" or "Clock Out". When you click "Clock In" you will see a message that will show the arrival time of the teacher to work. When you click "Clock Out" button you will again see the time with the amount of time that the teacher worked for that day (in hours - minutes - seconds).


## Database
Created a database using mLab. There is a test teacher object with first name: Jane - last name: Doe. I used this test object throughout the project.

## Technologies
I used Python Flask for back end and Javascript / JQuery / HTML for front end. 

## CRUD Operations
There are couple of database operations in controller.py. After typing the first name, there is a function call (db.teachers.find_one()) to get the teacher with the given first name (Read) (I was going to use teacherId or mongo object ID (to make it unique) but it says use first name in the handout so I just used first name instead). if there is no such teacher object, then I create one using db.teachers.insert() (Create)/

Also upon clicking "Clock In" or "Clock Out" buttons, teacher object gets updated with the new clockInTime and clockOutTime respectively (Update).






