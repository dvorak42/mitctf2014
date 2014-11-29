#!/usr/bin/python

import cgi
import datetime
import json
import models
import time

SCOREBOARD_FILE = '/var/www/scoreboard.html'
SCOREBOARD_JSON_FILE = '/var/www/scoreboard.json'
TEMPLATE_HTML = open('template.html').read()
session = models.Session()
teams = session.query(models.Team).all()
services = session.query(models.Service).all()
FINAL_TIME = datetime.datetime.utcnow()

def get_scores():
    scores = {}
    point_dict = {}
    team_dict = {}
    for t in teams:
        team_dict[t.id] = t.name
        scores[t.name] = (0, None)
    for s in services:
        point_dict[s.id] = s.points

    submissions = session.query(models.Submission).all()
    for s in submissions:
        if s.service_id in point_dict:
            scores[team_dict[s.team_id]] = (scores[team_dict[s.team_id]][0] + point_dict[s.service_id], FINAL_TIME - s.timestamp)
    return scores

scores = get_scores()
sa = []
for t,v in scores.iteritems():
    (s,d) = v
    sa.append((s, d, t))
FINAL_TIME = datetime.datetime.now()
sa = sorted(sa)[::-1][:8]
for t in sa:
    print '%d Points (%s): %s' % (t[0], (FINAL_TIME - t[1]).strftime(format='%I:%M %p'), t[2])
