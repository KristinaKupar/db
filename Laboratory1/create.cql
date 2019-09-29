create keyspace if not exists consultation
with replication = {'class': 'SimpleStrategy', 'replication_factor': '3'};

use consultation;

create type period_of_time(
	start_of_consultation timestamp,
	end_of_consultation timestamp
);

create table student(
	student_id varchar,
	succes float,
	course int,
	primary key(student_id)
);

create table consultation(
	cons_id varchar,
	teacher_id varchar,
	time_of_consultation frozen<period_of_time>,
	topic varchar,
	discipline varchar,
	primary key(cons_id)
);

create table booking(
	booking_id varchar,
	student_id varchar,
	consultation_id varchar,
	time_of_booking timestamp,
	number_of_questions int,
	number_of_students int,
	primary key(booking_id)
);

create table teacher(
	teacher_id varchar,
	start_of_consultation list<timestamp>,
	disciplines map<varchar,frozen<list<varchar>>>,
	primary key(teacher_id)
);
