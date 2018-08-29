function getTeacherByFirstName() {
        let first_name = document.getElementById("teacherfirstname").value;
        $.ajax({
            url: '/user',
            type: 'GET',
            data: {
                "first_name": first_name
            },
            success: function(response) {
                console.log("success")
            }
        });
        setWelcomeParagraph(first_name)
    }

function unhideDivComponent() {
    let div = document.getElementById("teacherdiv");
    let oldDiv = document.getElementById("start")
    div.style.visibility = "visible";
    oldDiv.style.visibility = "hidden";
}

function setWelcomeParagraph(name) {
	let paragraph = document.getElementById("welcome");
	name = name.charAt(0).toUpperCase() + name.slice(1);
	paragraph.innerHTML = "Welcome " + name;
}

function clockIn() {
	let button = document.getElementById("clockin");
	let clocktext = document.getElementById("clocktext");
	let clockInTimeVal = document.getElementById("clockintime");
	
	let clockInDate = new Date();
	let hours = clockInDate.getHours();
	let mins = clockInDate.getMinutes();
	let seconds = clockInDate.getSeconds();
	let time = hours + ":" + mins + ":" + seconds
	clocktext.innerHTML = "You clocked in at: " + time;
	clockInTime = clockInDate.getTime();
	clockInTimeVal.value = clockInTime;

	$.ajax({
            url: '/clock-in',
            type: 'POST',
            data: {
                "clock_in": clockInTime,
                "first_name": "Jane"
            },
            success: function(response) {
                console.log("success")
            }
        });
}

function clockOut() {
	let clocktext = document.getElementById("clocktext");
	let workText = document.getElementById("totalwork");
	let clockInTime = document.getElementById("clockintime").value;
	
	let clockOutDate = new Date();
	let hours = clockOutDate.getHours();
	let mins = clockOutDate.getMinutes();
	let seconds = clockOutDate.getSeconds();
	let time = hours + ":" + mins + ":" + seconds
	let clockOutTime = clockOutDate.getTime();
	let totalWorkText = getWorkTime(clockInTime, clockOutTime);
	clocktext.innerHTML = "You clocked out at: " + time + ". " + totalWorkText;

	$.ajax({
            url: '/clock-out',
            type: 'POST',
            data: {
                "clock_out": clockOutTime,
                "first_name": "Jane"
            },
            success: function(response) {
                console.log("success")
            }
        });
}

function getWorkTime(clockInTime, clockOutTime) {
	var seconds = (clockOutTime - clockInTime) / 1000; 
	var mins = Math.floor(seconds / 60);
	var hours = Math.floor(mins / 60);
	return "You worked for " + hours + " hours, " + mins + " minutes and " + seconds + " seconds today. Good work!";
}


$(document).ready(function() {
	$("#getteacher").submit(function (e) {
			e.preventDefault();
	        getTeacherByFirstName();
	        unhideDivComponent();
	    });

	document.getElementById("clockin").onclick = function() {
		clockIn();	
	}
	
	document.getElementById("clockout").onclick = function() {
		clockOut();
	}
});

