#!/usr/bin/python

import datetime
import string
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, DateTime, Integer, String

DB_USER = 'mitctf'
DB_PASS = 'p@ssw0rd1ss3cur3'
DB_HOST = 'localhost'
DB_NAME = 'mitctf2014'

DB_STRING = "mysql+mysqldb://%s:%s@%s/%s" % (DB_USER, DB_PASS, DB_HOST, DB_NAME)

engine = sqlalchemy.create_engine(DB_STRING)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=True)
    flag = Column(String(256), unique=True)
    points = Column(Integer, default=100)


class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=True)
    username = Column(String(256), unique=True)
    password = Column(String(256))


class Submission(Base):
    __tablename__ = 'submissions'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    team_id = Column(Integer)
    flag = Column(String(256))
    service_id = Column(Integer, nullable=True, default=None)


def db_create():
    Base.metadata.create_all(engine)


def db_commit(obj):
    session = Session()
    session.add(obj)
    session.commit()


def canon(s):
    s = s.replace("tesseract2014", "")
    return ''.join(l.lower() for l in s if l in string.ascii_letters)


def add_service(name, pts, flag):
    s = Service()
    s.name = name
    s.flag = canon(flag)
    s.points = pts
    db_commit(s)


def create_team(name, username, password):
    session = Session()
    exists = session.query(Team).filter(Team.username == username).count()
    if exists:
        return "ERROR: Team already exists."
    t = Team()
    t.name = name
    t.username = username
    t.password = password
    db_commit(t)


def submit_flag(username, password, flag):
    session = Session()
    teams = session.query(Team).filter(Team.username == username, Team.password == password).all()
    if len(teams) != 1:
        return "ERROR: Invalid Login Information."
    team = teams[0]
    flag = canon(flag)
    flags = session.query(Submission).filter(Submission.team_id == team.id, Submission.flag == flag).count()

    if flags:
        return "ERROR: Flag Already Submitted."
    
    service = session.query(Service).filter(Service.flag == flag).all()

    s = Submission()
    s.timestamp = datetime.datetime.utcnow()
    s.team_id = team.id
    s.flag = flag
    if service and len(service) == 1:
        s.service_id = service[0].id

    db_commit(s)

    if service and len(service) == 1:
        return "Flag Submitted for '%s'" % (service[0].name)
    return "INVALID FLAG"
