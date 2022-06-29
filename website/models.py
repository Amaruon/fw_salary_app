from . import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    acronym = db.Column(db.String(4), unique=True)
    password = db.Column(db.String(150))


class Worker(db.Model):
    __tablename__ = 'worker'
    __table_args__ = dict(schema='salary')

    id = db.Column(db.Integer, primary_key=True, unique=True)
    ru_name = db.Column(db.String(50), unique=True, nullable=False)
    eng_name = db.Column(db.String(50), unique=True, nullable=False)
    pms = db.relationship('Pms', backref='worker')
    wage = db.relationship('Wage', backref='worker')


class Projects(db.Model):
    __tablename__ = 'project'
    __table_args__ = dict(schema='salary')

    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(6), unique=True, nullable=False)
    pms = db.relationship('Pms', backref='project')


class Pms(db.Model):
    __tablename__ = 'pms'
    __table_args__ = dict(schema='salary')

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    week = db.Column(db.Integer, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('salary.project.id'))
    worker_id = db.Column(db.Integer, db.ForeignKey('salary.worker.id'))
    func_addon = db.Column(db.String(2))
    work_start = db.Column(db.Time)
    work_end = db.Column(db.Time)
    total_with_lunch = db.Column(db.Float)
    total = db.Column(db.Float)
    work_on_site = db.Column(db.Float)
    lunch = db.Column(db.Float)
    travelling = db.Column(db.Float)
    transport = db.Column(db.Float)
    overhr_2 = db.Column(db.Float)
    overhr_15 = db.Column(db.Float)
    holiday = db.Column(db.Float)
    course = db.Column(db.Float)
    paper_work = db.Column(db.Float)
    site_sup = db.Column(db.Float)
    safety_sup = db.Column(db.Float)
    without_diet = db.Column(db.Float)
    meal_1 = db.Column(db.Float)
    meal_2 = db.Column(db.Float)
    meal_3 = db.Column(db.Float)
    full_diet = db.Column(db.Float)
    sick_leave_paid = db.Column(db.Float)
    standby_weather_wo_work = db.Column(db.Float)
    standby_weather_as_work = db.Column(db.Float)
    standby_other_wo_work = db.Column(db.Float)
    standby_other_as_work = db.Column(db.Float)
    used_in_calc = db.Column(db.Boolean, nullable=False, default=False)
    pms_salary = db.relationship('PmsSalary', backref='pms')

    db.UniqueConstraint(date, project_id, worker_id)


class PmsSalary(db.Model):
    __tablename__ = 'pms_salary'
    __table_args__ = dict(schema='salary')

    id = db.Column(db.Integer, primary_key=True)
    pms_id = db.Column(db.Integer, db.ForeignKey('salary.pms.id'))
    amount = db.Column(db.Float, nullable=False)


class Entity(db.Model):
    __tablename__ = 'entity'
    __table_args__ = dict(schema='salary')

    id = db.Column(db.Integer, primary_key=True)
    entity_name = db.Column(db.String(50), unique=True)
    wage = db.relationship('Wages', backref='entity')


class Wage(db.Model):
    __tablename__ = 'wage'
    __table_args__ = dict(schema='salary')

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    worker_id = db.Column(db.Integer, db.ForeignKey('salary.worker.id'))
    entity_id = db.Column(db.Integer, db.ForeignKey('salary.entity.id'))
    accrual_type = db.Column(db.String(60))
    value = db.Column(db.Float, nullable=False)

    db.UniqueConstraint(date, worker_id, entity_id, accrual_type)
