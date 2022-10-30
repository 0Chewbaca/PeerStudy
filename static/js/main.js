//console.log('hello')


function fetchData() {
    $.ajax({
        type: 'GET',
        url: '/values',
        success:function(response) {
            var theGod = document.getElementById('erenn');
            theGod.innerHTML = ""

            var select = document.getElementById('grade');
            var grade = select.options[select.selectedIndex].value;
            
            var select1 = document.getElementById('lessons');
            var lesson = select1.options[select1.selectedIndex].value;
            
            console.log("Grade: " + grade + " Lesson: " + lesson)

            const data = response.data
            data.map(tutor => {
                //console.log("Hello")
                
                //console.log("Tutors: " + tutor.lesson)
                //console.log("Selected lesson: "  + lesson)
                if (tutor.grade == grade && tutor.lesson == lesson){
                    
                    text = "Name: " + tutor.fname + " " + tutor.lname + " Email: " + tutor.email + " Lesson: " + tutor.lesson + "<br>"
                    theGod.innerHTML += text
                    text = ""
                }

            })

        },
        error: function(error){
            console.log(error)
        }
    });
}

