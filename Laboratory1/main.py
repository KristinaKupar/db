from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement
import datetime

cluster = Cluster()

session = cluster.connect('consultation')

class period_of_time(object):
    def __init__(self, start_of_consultation, end_of_consultation):
        self.start_of_consultation = start_of_consultation
        self.end_of_consultation = end_of_consultation

cluster.register_user_type('consultation', 'period_of_time', period_of_time)

insertStudent = [('kate99',83.6, 4), ('oros97', 65.7, 6), ('kuper99', 76.8, 4)]
insertTeacher = [('igorOT', 32, ['2017-04-01T16:10', '2017-04-02T16:10', '2017-04-03T16:10'], {'python':['dictionary','flask','data analysis'], 'db':['Oracle', 'noSQL', 'transactions'], 'data science':['big data', 'machine learning']}, 'KPI' ), ('volodymyrVM', 44, ['2017-04-01T16:10', '2017-04-02T16:10', '2017-04-03T16:10'], {'math analysis':['limits','Riemann integrals'], 'QA':['manual', 'automation'], 'differential equations':['homogeneous', 'systems of differential equations', 'phase portraits']}, 'KPI' ), ('tatyanaSL', 50, ['2017-04-01T16:10', '2017-04-02T16:10', '2017-04-03T16:10'], {'optimization methods':['Vengerian method','Simplex method', 'Travelling salesman problem'], 'Operations Research':['simlex method', 'golden ratio method']}, 'KPI' )]
insertConsultation = [('cons1', 'igorOT', period_of_time('2017-04-01T16:10','2017-04-01T17:30'), 'flask', 'python'), ('cons2', 'volodymyrVM', period_of_time('2017-04-01T16:10','2017-04-01T17:30'), 'Riemann integrals', 'math analysis'), ('cons3', 'volodymyrVM', period_of_time('2017-04-02T16:10','2017-04-02T17:30'), 'limits', 'math analysis')]
insertBooking = [('01kuper99', 'kuper99', 'cons1', datetime.datetime.now(), 3, 36), ('02kuper99', 'kuper99', 'cons2', datetime.datetime.now(), 5, 12), ('01oros97', 'oros97', 'cons3', datetime.datetime.now(), 1, 15)]

queryStudent = SimpleStatement(
    "insert into consultation.student (student_id, succes, course) VALUES (%s, %s, %s)",
        consistency_level=ConsistencyLevel.LOCAL_ONE)

for i in insertStudent:
    session.execute(queryStudent, i)

studentSelect = session.execute('SELECT * FROM consultation.student')
for i in studentSelect:
    print i

queryTeacher = SimpleStatement(
    "insert into consultation.teacher (teacher_id, age, start_of_consultation, disciplines, university) VALUES (%s, %s,%s,%s,%s)",
            consistency_level=ConsistencyLevel.LOCAL_ONE)

for i in insertTeacher:
    session.execute(queryTeacher, i)

teacherSelect = session.execute('SELECT * FROM consultation.teacher')
for i in teacherSelect:
    print i


queryConsultation = SimpleStatement(
    "insert into consultation.consultation (cons_id, teacher_id, time_of_consultation, topic, discipline) VALUES (%s, %s,%s,%s,%s)",
            consistency_level=ConsistencyLevel.LOCAL_ONE)

for i in insertConsultation:
    session.execute(queryConsultation, i)

consultationSelect = session.execute('SELECT * FROM consultation.consultation')
for i in consultationSelect:
    print i

queryBooking = SimpleStatement(
    "insert into consultation.booking (booking_id, student_id, consultation_id, time_of_booking, number_of_questions, number_of_students) VALUES (%s, %s, %s, %s, %s, %s)",
            consistency_level=ConsistencyLevel.LOCAL_ONE)

for i in insertBooking:
    session.execute(queryBooking, i)

bookingSelect = session.execute('SELECT * FROM consultation.booking')
for i in bookingSelect:
    print i