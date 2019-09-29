from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement
from cassandra.query import BatchStatement
import datetime
cluster = Cluster()

session = cluster.connect('consultation')

insertStudent = [('kate99',83.6, 4), ('oros97', 65.7, 6), ('kuper99', 76.8, 4)]
insertBooking = [('01kuper99', 'kuper99', 'cons1', datetime.datetime.now(), 3, 36), ('02kuper99', 'kuper99', 'cons2', datetime.datetime.now(), 5, 12), ('01oros97', 'oros97', 'cons3', datetime.datetime.now(), 1, 15)]

queryStudent = SimpleStatement(
    "insert into consultation.student (student_id, succes, course) VALUES (%s, %s, %s)",
        consistency_level=ConsistencyLevel.LOCAL_ONE)

for i in insertStudent:
    session.execute(queryStudent, i)

queryBooking = SimpleStatement(
    "insert into consultation.booking (booking_id, student_id, consultation_id, time_of_booking, number_of_questions, number_of_students) VALUES (%s, %s, %s, %s, %s, %s)",
            consistency_level=ConsistencyLevel.LOCAL_ONE)

for i in insertBooking:
    session.execute(queryBooking, i)

batch = BatchStatement(consistency_level=ConsistencyLevel.ONE)
for i in insertBooking:
    batch.add(queryBooking, i)

for i in insertStudent:
    batch.add(queryStudent, i)

session.execute(batch)