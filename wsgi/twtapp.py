#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import uuid
import bottle
import pymongo
import time
import netifaces
import logging
from threading import Timer

bottle.debug(True)

#try this again

connString = os.environ['OPENSHIFT_MONGODB_HA_DB_HOST1'] + ":" + os.environ['OPENSHIFT_MONGODB_HA_DB_PORT1'] + "," + \
             os.environ['OPENSHIFT_MONGODB_HA_DB_HOST2'] + ":" + os.environ['OPENSHIFT_MONGODB_HA_DB_PORT2'] + "," + \
             os.environ['OPENSHIFT_MONGODB_HA_DB_HOST3'] + ":" + os.environ['OPENSHIFT_MONGODB_HA_DB_PORT3']
mongo_client = pymongo.MongoReplicaSetClient(connString, replicaSet='rs0') 


mongo_db = mongo_client [os.environ['OPENSHIFT_APP_NAME']]
mongo_db.authenticate(os.environ['OPENSHIFT_MONGODB_HA_DB_USERNAME'],
                      os.environ['OPENSHIFT_MONGODB_HA_DB_PASSWORD'])

count = 0
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler(os.environ['OPENSHIFT_PYTHON_LOG_DIR']+ '/myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)
logger.info('connection ')
if(mongo_db != 0 ):
	logger.info('connected')

count=0
ipaddr=netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

def log_list():
  l = []
  for u in mongo_db.logs.find().sort([('timestamp', -1)]).limit(30):
    l.append(u)
  #l.sort()
  return l

def logfunction(count):
  #logger.info('Start logging')
  mongo_db.logs.save({"id" : count, "tag" : "heartbeat", "timestamp" : time.time(), "host": ipaddr})
  count+=1
  #time.sleep(5)

bottle.TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'],
                                         'wsgi', 'views'))


@bottle.route('/')
def home():
  #for post_id in loglist['timeline']:
   # post = post_find_by_id(post_id)
   # if post:
    #  postlist.insert(0, post)

  # bottle.TEMPLATES.clear()
  logger.info('in Home')
  #logfunction()
  logger.info('Start logging')
  count = 0
  Timer(2, logfunction(count), ()).start()
  return bottle.template('timeline',
                         loglist=log_list(),
                         page='timeline')

application = bottle.default_app()

