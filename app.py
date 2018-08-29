from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
import models.teacher as Teacher
import controller

app = Flask(__name__)


@app.route("/")
def index():
    first_name = str(request.args.get("first_name"))
    return render_template('index.html', first_name=str(first_name))
    
    
@app.route("/user", methods=["GET", "POST"])
def getTeacher():
    first_name = request.args.get("first_name")
    teacher_first_name = ""
    teacher_last_name = ""
    teacher_id = None
    clock_type = None
    clock_time = None
    
    teacher = controller.getTeacherByFirstName(first_name)
    if teacher:
        teacher_first_name = teacher.getFirstName()
        teacher_last_name = teacher.getLastName()
        teacher_id = teacher.getTeacherId()
        clock_type = teacher.getClockType()
        clock_time = teacher.getClockTime()
    
    return redirect(url_for("index"))
    
    
@app.route("/clock-in", methods=["GET", "POST"])
def clockIn():
    clockInTime = request.form['clock_in']
    teacherFirstName = request.form['first_name']
    controller.clock_in(clockInTime, teacherFirstName)
    return redirect(url_for("index"))
    
    
@app.route("/clock-out", methods=["GET", "POST"])
def clockOut():
    clockOutTime = request.form['clock_out']
    teacherFirstName = request.form['first_name']
    controller.clock_out(clockOutTime, teacherFirstName)
    return redirect(url_for("index"))
    
    
if __name__ == "__main__":
    app.run()