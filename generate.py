from faker import Faker
from datetime import datetime
import random

Faker.seed(0)
fake = Faker()

fake.date(pattern='%Y-%m-%d %H:%M:%s')

ddl = open('init.d/DML.sql', 'w+', encoding='utf-8')


# date_time_between(start_date: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int] = '-30y', end_date: Union[datetime.date, datetime.datetime, datetime.timedelta, str, int] = 'now', tzinfo: Optional[datetime.tzinfo] = None) → datetime.datetime

start_date = datetime(2021, 1, 1)
middle_date = datetime(2022, 1, 1)
end_date = datetime(2023, 1, 1)
today = datetime(2023, 1, 2)

ddl.write(
    """INSERT INTO room (owner_id, room_type, status)
    VALUES
    """
)

for i in range(100):
    cr = fake.date_time_between(start_date = start_date, end_date = middle_date)
    up = fake.date_time_between(start_date = middle_date, end_date = end_date)

    print(
        "('%s', '%s')"%(str(cr), str(up))
    )

    ddl.write("\t\t('%s', '%s')"%(str(cr), str(up)))

    if i < 99:
        ddl.write(",\n")

ddl.write(
    ";\n"
)

mode = ['같이 모드', '따로 모드']
status = ['START' , 'END']
for _ in range(280):
    print(
        "(%d, '%s', '%s'),"
            %(
                random.randint(1, 100),
                mode[random.randint(0,1)],
                'END'
            )
    )
for _ in range(20):
    print(
        "(%d, '%s', '%s'),"
            %(
                random.randint(1, 100),
                mode[random.randint(0,1)],
                'START'
            )
    )


for i in range(280):
    cr = fake.date_time_between(start_date = start_date, end_date = middle_date)
    up = fake.date_time_between(start_date = middle_date, end_date = end_date)
    print(
        "(%d, %d, '%s', '%s', NULL, '%s'),"%(
            i+1,
            random.randint(1, 100),
            'OWNER',
            str(cr),
            str(up)
        )
    )

for i in range(20):
    cr = fake.date_time_between(start_date = start_date, end_date = middle_date)
    up = fake.date_time_between(start_date = middle_date, end_date = end_date)
    ee = fake.date_time_between(start_date = end_date, end_date = today)
    print(
        "(%d, %d, '%s', '%s', NULL, NULL),"%(
            i+281,
            random.randint(1, 100),
            'OWNER',
            str(up)
        )
    )

role = ['PARTICIPANT', 'WATCHER']
for _ in range(300):
    cr = fake.date_time_between(start_date = start_date, end_date = middle_date)
    up = fake.date_time_between(start_date = middle_date, end_date = end_date)
    ee = fake.date_time_between(start_date = end_date, end_date = today)
    print(
        "(%d, %d, '%s', '%s', '%s', '%s'),"%(
            random.randint(1, 300),
            random.randint(1, 100),
            role[random.randint(0,1)],
            str(cr),
            str(up),
            str(ee)
        )
    )