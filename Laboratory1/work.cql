
insert into consultation.student (student_id, succes, course)
values ('kuper99', 76.8, 4 );
insert into consultation.student (student_id, succes, course)
values ('oros97', 65.7, 6 );
insert into consultation.student (student_id, succes, course)
values ('kate99', 83.6, 4 );
select * from consultation.student;

insert into consultation.teacher (teacher_id, age, start_of_consultation, disciplines, university)
values ('igorOT', 32, ['2017-04-01T16:10', '2017-04-02T16:10', '2017-04-03T16:10'], {'python':['dictionary','flask','data analysis'], 'db':['Oracle', 'noSQL', 'transactions'], 'data science':['big data', 'machine learning']}, 'KPI' );
insert into consultation.teacher (teacher_id, age, start_of_consultation, disciplines, university)
values ('volodymyrVM', 44, ['2017-04-01T16:10', '2017-04-02T16:10', '2017-04-03T16:10'], {'math analysis':['limits','Riemann integrals'], 'QA':['manual', 'automation'], 'differential equations':['homogeneous', 'systems of differential equations', 'phase portraits']}, 'KPI' );
insert into consultation.teacher (teacher_id, age, start_of_consultation, disciplines, university)
values ('tatyanaSL', 50, ['2017-04-01T16:10', '2017-04-02T16:10', '2017-04-03T16:10'], {'optimization methods':['Vengerian method','Simplex method', 'Travelling salesman problem'], 'Operations Research':['simlex method', 'golden ratio method']}, 'KPI' );
select * from consultation.teacher;


insert into consultation.consultation (cons_id, teacher_id, time_of_consultation, topic, discipline)
values ('cons1', 'igorOT', {start_of_consultation:'2017-04-01T16:10',end_of_consultation:'2017-04-01T17:30'}, 'flask', 'python');
insert into consultation.consultation (cons_id, teacher_id, time_of_consultation, topic, discipline)
values ('cons2', 'volodymyrVM', {start_of_consultation:'2017-04-01T16:10',end_of_consultation:'2017-04-01T17:30'}, 'Riemann integrals', 'math analysis');
insert into consultation.consultation (cons_id, teacher_id, time_of_consultation, topic, discipline)
values ('cons3', 'volodymyrVM', {start_of_consultation:'2017-04-02T16:10',end_of_consultation:'2017-04-02T17:30'}, 'limits', 'math analysis');
select * from consultation.consultation;


insert into consultation.booking (booking_id, student_id, consultation_id, time_of_booking, number_of_questions, number_of_students)
values ('01kuper99', 'kuper99', 'cons1', dateof(now()), 3, 36);
insert into consultation.booking (booking_id, student_id, consultation_id, time_of_booking, number_of_questions, number_of_students)
values ('02kuper99', 'kuper99', 'cons2', dateof(now()), 5, 12);
insert into consultation.booking (booking_id, student_id, consultation_id, time_of_booking, number_of_questions, number_of_students)
values ('01oros97', 'oros97', 'cons3', dateof(now()), 1, 15);
select * from consultation.booking;

update consultation.consultation set time_of_consultation = {start_of_consultation:'2017-04-01T16:30',end_of_consultation:'2017-04-01T17:50'} where cons_id = 'cons1' and teacher_id = 'igorOT';
select time_of_consultation from consultation.consultation where cons_id = 'cons1';

update consultation.booking set number_of_questions = 6 where booking_id = '01oros97' and student_id = 'oros97' and consultation_id = 'cons3';
select consultation_id from consultation.booking where booking_id = '01oros97';

update consultation.teacher set university = 'KNU' where teacher_id = 'tatyanaSL';
select university from consultation.teacher where teacher_id = 'tatyanaSL';

select * from consultation.consultation;
select * from consultation.booking where student_id = 'kuper99' allow filtering;
select * from consultation.consultation where teacher_id = 'igorOT' allow filtering;
select * from consultation.student where student_id = 'kuper99';


delete number_of_questions from consultation.booking where booking_id = '02kuper99';
select * from consultation.booking where booking_id = '02kuper99';

delete university from consultation.teacher where teacher_id = 'tatyanaSL';
select * from consultation.teacher where teacher_id = 'tatyanaSL';


delete time_of_consultation from consultation.consultation where cons_id = 'cons1';
select * from consultation.consultation where cons_id = 'cons1';



