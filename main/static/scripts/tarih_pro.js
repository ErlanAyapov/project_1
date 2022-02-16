var false_answers_textarea, false_answers_number = 0;
rendering_questions();

function rendering_questions() {
	var false_answers_textarea, false_answers_number = 0;
	while (run) {
		question_id = getRandomInt(questions.length);
		if (!last_questions.includes(question_id)) {
			last_questions.push(question_id);
			run = false;
		}
	}
	var cs = getRandomInt(3);
	if (cs == 1){
		document.getElementById('block_1').innerHTML = answers_4[question_id];
		document.getElementById('block_2').innerHTML = answers_2[question_id];
		document.getElementById('block_3').innerHTML = answers_3[question_id];
		document.getElementById('answer_4').value = answers_1[question_id];
		document.getElementById('block_4').innerHTML = answers_1[question_id];
	} else if (cs == 2) {
		document.getElementById('block_1').innerHTML = answers_2[question_id];
		document.getElementById('block_2').innerHTML = answers_3[question_id];
		document.getElementById('block_4').innerHTML = answers_4[question_id];
		document.getElementById('answer_3').value = answers_1[question_id];
		document.getElementById('block_3').innerHTML = answers_1[question_id];
	} else if (cs == 3) {
		document.getElementById('block_1').innerHTML = answers_2[question_id];
		document.getElementById('block_3').innerHTML = answers_3[question_id];
		document.getElementById('block_4').innerHTML = answers_4[question_id];
		document.getElementById('answer_2').value = answers_1[question_id];
		document.getElementById('block_2').innerHTML = answers_1[question_id];
	} else {
		document.getElementById('block_3').innerHTML = answers_2[question_id];
		document.getElementById('block_2').innerHTML = answers_3[question_id];
		document.getElementById('block_4').innerHTML = answers_4[question_id];
		document.getElementById('answer_1').value = answers_1[question_id];
		document.getElementById('block_1').innerHTML = answers_1[question_id];
	}	
	var question_el = document.getElementById('question');
	question_el.innerHTML = (questions[question_id]) + ' ?';
	document.getElementById('true_questions').innerHTML = 'Дұрыс: ' + true_qestions.length
	document.getElementById('id_result_true').value = true_qestions.length;
	if (last_questions.length == 1){
		document.getElementById('all_questions').innerHTML = 'Барлығы: 0'
		document.getElementById('id_result_true').value = '1'
	}else {
		document.getElementById('all_questions').innerHTML = 'Барлығы: ' + (last_questions.length - 1)
		document.getElementById('id_result_all').value = (last_questions.length - 1)
	}
	document.getElementById('id_result_false').value = false_questions.length
	document.getElementById('false_questions').innerHTML = 'Қате: ' + false_questions.length

	run = true
	if (questions.length == last_questions.length) {
		alert('Сұрақтар бітті, басынан бастайсыз')
		last_questions = []
		true_questions = []
		false_questions = []
	}
	};
	jQuery('#block_1').on('click', function() {
		if (document.getElementById('answer_1').value == answers_1[question_id]) {
			alert('Дұрыс!');
			true_qestions.push(question_id)	
			rendering_questions();
			}
		else {
			false_questions.push(question_id)
			alert('Дұрыс емес :(')
			rendering_questions();
			false_answers_number++
			false_answers_textarea += '<li>' + false_answers_number + ') ' + questions[question_id] + '? </li>';
			}
			document.getElementById('id_false_answers').value = false_answers_textarea;				 
		})
	jQuery('#block_2').on('click', function() { 
		if (document.getElementById('answer_2').value == answers_1[question_id]) {
			true_qestions.push(question_id)	
			alert('Дұрыс!');	
			rendering_questions();
			}
		else {
			false_questions.push(question_id)	
			alert('Дұрыс емес :(')
			rendering_questions();
			false_answers_number++
			false_answers_textarea += '<li>' + false_answers_number + ') ' + questions[question_id] + '? </li>';

			}
			document.getElementById('id_false_answers').value = false_answers_textarea;
		})
	jQuery('#block_3').on('click', function() { 
		if (document.getElementById('answer_3').value == answers_1[question_id]) {
			true_qestions.push(question_id)	
			alert('Дұрыс!');	
			rendering_questions();
		}
		else {
			false_questions.push(question_id)	
			alert('Дұрыс емес :(')
			rendering_questions();
			false_answers_number++
			false_answers_textarea += '<li>' + false_answers_number + ') ' + questions[question_id] + '? </li>';

		}
			document.getElementById('id_false_answers').value = false_answers_textarea;
	})
	jQuery('#block_4').on('click', function() { 
		if (document.getElementById('answer_4').value == answers_1[question_id]) {
			true_qestions.push(question_id)	
			alert('Дұрыс!');	
			rendering_questions();
			
		}
		else {
			false_questions.push(question_id)	
			alert('Дұрыс емес :(')
			rendering_questions();
			false_answers_number++
			false_answers_textarea += '<li>' + false_answers_number + ') ' + questions[question_id] + '? </li>';

		}
			document.getElementById('id_false_answers').value = false_answers_textarea;

	}); 


