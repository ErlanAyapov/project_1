while (run) {
	question_id = getRandomInt(questions.length);
	if (!last_questions.includes(question_id)) {
		last_questions.push(question_id);
		run = false;
	}
}

var fake_answer_1 = getRandomInt(answers.length);
var fake_answer_2 = getRandomInt(answers.length);
var fake_answer_3 = getRandomInt(answers.length);
var cs = getRandomInt(3);
	
if (cs == 1){
	document.getElementById('block_1').innerHTML = answers[fake_answer_1];
	document.getElementById('block_2').innerHTML = answers[fake_answer_2];
	document.getElementById('block_3').innerHTML = answers[fake_answer_3];
	document.getElementById('answer_4').value = answers[question_id];
	document.getElementById('block_4').innerHTML = answers[question_id];

} else if (cs == 2) {
	document.getElementById('block_1').innerHTML = answers[fake_answer_1];
	document.getElementById('block_2').innerHTML = answers[fake_answer_2];
	document.getElementById('block_4').innerHTML = answers[fake_answer_3];
	document.getElementById('answer_3').value = answers[question_id];
	document.getElementById('block_3').innerHTML = answers[question_id];
} else if (cs == 3) {
	document.getElementById('block_1').innerHTML = answers[fake_answer_1];
	document.getElementById('block_3').innerHTML = answers[fake_answer_2];
	document.getElementById('block_4').innerHTML = answers[fake_answer_3];
	document.getElementById('answer_2').value = answers[question_id];
	document.getElementById('block_2').innerHTML = answers[question_id];
} else {
	document.getElementById('block_3').innerHTML = answers[fake_answer_1];
	document.getElementById('block_2').innerHTML = answers[fake_answer_2];
	document.getElementById('block_4').innerHTML = answers[fake_answer_3];
	document.getElementById('answer_1').value = answers[question_id];
	document.getElementById('block_1').innerHTML = answers[question_id];
}
	

var question_el = document.getElementById('question');
question_el.innerHTML = (questions[question_id]) + ' ?';
document.getElementById('true_questions').innerHTML = 'Дұрыс: ' + (true_qestions.length)
document.getElementById('all_questions').innerHTML =  'Барлығы: '  + 0
document.getElementById('false_questions').innerHTML = 'Қате: ' + false_questions.length

	run = true
	function getRandomInt(max) {
		return Math.floor(Math.random() * max);
	}
	function make_question() {
	while (run) {
		question_id = getRandomInt(questions.length);
		if (!last_questions.includes(question_id)) {
			last_questions.push(question_id);
			run = false;
		}
	}

	var fake_answer_1 = getRandomInt(answers.length);
	var fake_answer_2 = getRandomInt(answers.length);
	var fake_answer_3 = getRandomInt(answers.length);
	var cs = getRandomInt(3);
	
	if (cs == 1){
		document.getElementById('block_1').innerHTML = answers[fake_answer_1];
		document.getElementById('block_2').innerHTML = answers[fake_answer_2];
		document.getElementById('block_3').innerHTML = answers[fake_answer_3];
		document.getElementById('answer_4').value = answers[question_id];
		document.getElementById('block_4').innerHTML = answers[question_id];

	} else if (cs == 2) {
		document.getElementById('block_1').innerHTML = answers[fake_answer_1];
		document.getElementById('block_2').innerHTML = answers[fake_answer_2];
		document.getElementById('block_4').innerHTML = answers[fake_answer_3];
		document.getElementById('answer_3').value = answers[question_id];
		document.getElementById('block_3').innerHTML = answers[question_id];
	} else if (cs == 3) {
		document.getElementById('block_1').innerHTML = answers[fake_answer_1];
		document.getElementById('block_3').innerHTML = answers[fake_answer_2];
		document.getElementById('block_4').innerHTML = answers[fake_answer_3];
		document.getElementById('answer_2').value = answers[question_id];
		document.getElementById('block_2').innerHTML = answers[question_id];
	} else {
		document.getElementById('block_3').innerHTML = answers[fake_answer_1];
		document.getElementById('block_2').innerHTML = answers[fake_answer_2];
		document.getElementById('block_4').innerHTML = answers[fake_answer_3];
		document.getElementById('answer_1').value = answers[question_id];
		document.getElementById('block_1').innerHTML = answers[question_id];
	}
	
	var question_el = document.getElementById('question');
	question_el.innerHTML = (questions[question_id]) + ' ?';
	document.getElementById('true_questions').innerHTML = 'Дұрыс: ' + true_qestions.length
	if (last_questions.length == 1){
		document.getElementById('all_questions').innerHTML = 'Барлығы: 1'  

	}else {
		document.getElementById('all_questions').innerHTML = 'Барлығы: ' + (last_questions.length - 1)

	}
	document.getElementById('false_questions').innerHTML = 'Қате: ' + false_questions.length

	run = true
	};		

	function check_1() {
		if (document.getElementById('answer_1').value == answers[question_id]) {
			alert('Дұрыс!');
			true_qestions.push(question_id)	
			make_question();
			}
		else {
			false_questions.push(question_id)
			alert('Дұрыс емес :(')
			make_question();
			}
					 
		}
	function check_2() { 
		if (document.getElementById('answer_2').value == answers[question_id]) {
			true_qestions.push(question_id)	
			alert('Дұрыс!');	
			make_question();
			}
		else {
			false_questions.push(question_id)	
			alert('Дұрыс емес :(')
			make_question();
			}
		}
	function check_3() { 
		if (document.getElementById('answer_3').value == answers[question_id]) {
			true_qestions.push(question_id)	
			alert('Дұрыс!');	
			make_question();
		}
		else {
			false_questions.push(question_id)	
			alert('Дұрыс емес :(')
			make_question();
		}
	}
	function check_4() { 
		if (document.getElementById('answer_4').value == answers[question_id]) {
			true_qestions.push(question_id)	
			alert('Дұрыс!');	
			make_question();
		}
		else {
			false_questions.push(question_id)	
			alert('Дұрыс емес :(')
			make_question();
		}
	}