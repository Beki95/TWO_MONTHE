import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("ORM")

connection = sqlite3.connect("sql.sqlite3")
cursor = connection.cursor()


class ORM:

    def __init__(self, id, name, course_id):
        self.id = id
        self.name = name
        self.course_id = course_id

    @classmethod
    def create_table(cls):
        global table
        table = cls.__name__.lower()
        if table != "course":
            sql = f"CREATE TABLE IF NOT EXISTS {table} (id INTEGER PRIMARY KEY, name VARCHAR(150), course_id INTEGER)"
        else:
            sql = f"CREATE TABLE IF NOT EXISTS {table} (id INTEGER PRIMARY KEY, name VARCHAR(150))"

        logger.info(f"Создана таблица {table}")
        return cursor.execute(sql)

    @classmethod
    def delete_table(cls):
        table = cls.__name__.lower()
        sql = f"""
            DROP TABLE {table}
        """
        logger.info(f"удалена таблица {table}")
        return cursor.execute(sql)

    def update(self):
        table = self.__class__.__name__.lower()
        try:
            if self.__class__.__name__.lower() == "student":
                sql = f"""
                    INSERT INTO {table} VALUES ({self.id}, '{self.name}', '{self.course_id}')
                """
                cursor.execute(sql)
                connection.commit()
            else:
                sql = f"""
                        INSERT INTO {table} VALUES ({self.id}, '{self.name}')
                        """
                cursor.execute(sql)
                connection.commit()
            logger.info("Ваш sql запрос выполнен!!!")
        except sqlite3.IntegrityError:
            logger.info("ОШИБКА такой id уже есть")

    @classmethod
    def delete(cls, id):
        table = cls.__name__.lower()
        sql = f"""
            DELETE FROM {table} WHERE id = {id}
        """
        cursor.execute(sql)
        connection.commit()
        logger.info(f"User с id {id} удален!!!")

    @classmethod
    def m2m_relationship(cls, other_cls, other_cls2):
        table = cls.__name__.upper()
        student = other_cls.__class__.__name__.lower()
        course = other_cls2.__class__.__name__.lower()
        sql = f"""
            CREATE TABLE IF NOT EXISTS {table}(student_id, course_id, FOREIGN KEY (student_id) REFERENCES {student}(id), FOREIGN KEY (course_id) REFERENCES {course}(id))
        """
        return cursor.execute(sql)

    @classmethod
    def foreign_key(cls, other_cls):
        cursor.execute(f"DROP TABLE {cls.__name__.lower()}")
        sql = f"" \
              f"CREATE TABLE IF NOT EXISTS {cls.__name__.lower()}" \
              f" (id INTEGER PRIMARY KEY," \
              f" name VARCHAR(150)," \
              f" course_id INTEGER," \
              f" FOREIGN KEY (course_id) REFERENCES {other_cls.__name__.lower()} (id))"

        return cursor.execute(sql)

    @classmethod
    def update_m2m(cls):
        table = cls.__name__.lower()
        sql = f"""
            INSERT INTO {table} VALUES (1, 1),(2, 2), (2, 1)
        """
        cursor.execute(sql)
        connection.commit()

    @classmethod
    def get_data_from_m2m(cls, rel):
        table = cls.__name__.upper()
        sql = f"""
            SELECT student.id, student.name, course.name FROM student, course, {table} WHERE {table}.student_id == {rel} and student.course_id == {rel} and course.id == {rel}
        """
        return cursor.execute(sql)

    @classmethod
    def get_data_from_foreing(cls, other_cls, rel):
        o_cls = other_cls.__class__.__name__.lower()
        sql = f"""
            SELECT course.id, course.name, student.id, student.name from {cls.__name__.lower()}, {o_cls} WHERE course.id = {rel} AND student.course_id == {rel}
        """
        return cursor.execute(sql)


class Student(ORM):
    pass


class Course(ORM):
    pass


class M2M(ORM):
    pass


student = Student(2, "Beki", 1)
# student.update()
#
course = Course(2, "java", "")
# course.update()
# print(*student.get_data_from_foreing(course, 1))
# print(student.m2m_relationship(course))
m2m = M2M(id=None, name=None, course_id=None)
# print(m2m.update_m2m())
print(*m2m.get_data_from_m2m(1))

connection.close()
