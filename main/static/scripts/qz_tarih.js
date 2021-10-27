//  |=======================================================|
//	| Сұрақтар парағына кірген кезде make_question() 		|
//  | функциясының бір бөлігі орындалуы керек болғандықтан  |
//  | сол бөлікті көшіріп қойдым, бұл қателік емес!!!       |
//	|=======================================================|

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
// Жұмыс жасау принціпі
// Djinja шаблонизаторының циклімен деректер қорынан
// сұрақтарды алып 'questions' массивіне жинақтайды

// ---------- Функцияның 1-ші бөлігі ----------
// Шексіз цикл ішінде 'questions' массивінің идентификаторы болатын санды генрациялайды
// егер генерацияланған сан 'last_questions' массивінде болмаса, онда генерацияланған 
// сан 'last_questions' массивіне түседі және question_id айнымалсында сақталады

// ---------- Функцияның 2-ші бөлігі ----------
// fake_answer_n айнымалысына 3 жалған жауаптың 'anwers' массивінің идентификаторы болатын
// сандар генерацияланады, радомды ретпен 'block_1' элементінің ішіне орналастырылады

// ---------- Функцияның 3-ші бөлігі ----------
// Барша қойылған сұрақтардың идентификаторы 'last_questions' массивіне жазылып отырғандықтан
// массив ұзындығы == қойылған сұрақтар санына, 

// ---------- Функцияның 4-ші бөлігі ----------
// Сұрақтар тексеріледі егер жауап дұрыс болса сұрақ идентификаторы 'true_answers' массивіне 
// жазылады, кері жағдайда 'false_answers' массивіне  жазылады

function make_question() {
	
	// Функцияның 1-ші бөлігі
	while (run) {
		question_id = getRandomInt(questions.length);
		if (!last_questions.includes(question_id)) {
			last_questions.push(question_id);
			run = false;
		}
	}

	// Функцияның 2-ші бөлігі
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

	// Функцияның 3-ші бөлігі	
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
	if (questions.length == last_questions.length) {
		alert('Сұрақтар бітті, басынан бастайсыз')
		last_questions = []
		true_questions = []
		false_questions = []
	}
	};	

	// Функцияның 4-ші бөлігі
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