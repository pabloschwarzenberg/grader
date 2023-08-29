import time
import logging
import json
import urllib.request as urllib2
import urllib.parse as urlparse
from multiprocessing import *
import sqlite3

import pika

import project_urls
import settings
import xqueue_util as util


log = logging.getLogger(__name__)

QUEUE_NAME = settings.QUEUE_NAME

conexion_db=None
cursor=None
conexion_qm=None
channel=None

def each_cycle():
    session = util.xqueue_login()
    print(".",end="")
    success_length, queue_length = get_queue_length(QUEUE_NAME, session)
    if success_length and queue_length > 0:
        success_get, queue_item = get_from_queue(QUEUE_NAME, session)
        success_parse, content = util.parse_xobject(queue_item, QUEUE_NAME)
        if success_get and success_parse:
            content_header = json.loads(content['xqueue_header'])
            submission_id=content_header['submission_id']
            submission_key=content_header['submission_key']
            dispatch(session,content,submission_id,submission_key)

def dispatch(session,content,submission_id,submission_key):
    global conexion_db
    global cursor
    global conexion_qm
    global channel

    body = json.loads(content['xqueue_body'])
    student_info = json.loads(body.get('student_info', '{}'))
    anonymous_student_id=student_info.get("anonymous_student_id")
    grader_payload=json.loads(body.get("grader_payload","{}"))
    ejercicio=grader_payload.get("ejercicio")
    puntos=grader_payload.get("puntos")
    student_response=body.get("student_response")

    files = json.loads(content['xqueue_files'])
    for (filename, fileurl) in files.items():
        response = urllib2.urlopen(fileurl)
        with open(filename, 'w') as f:
            f.write(response.read())
        f.close()
        response.close()

    try:
        #cursor.execute("select username from idmap where id=?",(anonymous_student_id,))
        #username=cursor.fetchone()
        #if username is None:
        username=anonymous_student_id
        #else:
        #   username=username[0]

        archivo=ejercicio+"_"+username
        respuesta=open(ejercicio+"/"+archivo+".py","w")
        student_response=student_response.replace("\r","")
        respuesta.write(student_response)
        respuesta.close()

        mensaje=[ejercicio,puntos,str(submission_id),submission_key,archivo]
        mensaje=",".join(mensaje)

        channel.basic_publish(exchange='',routing_key='iic1103_dev',body=mensaje,
                              properties=pika.BasicProperties(delivery_mode = 2,))

    except BaseException as e:
        mensaje="Grader: {0}: Por favor intenta nuevamente".format(str(e))
        xqueue_header, xqueue_body = util.create_xqueue_header_and_body(submission_id, submission_key, False, 0, mensaje, 'iic1103_2015_s2_puc')
        (success, msg) = util.post_results_to_xqueue(session, json.dumps(xqueue_header), json.dumps(xqueue_body),)
        if success:
            logging.info(submission_id,submission_key,"posted back to xqueue by evaluador error")

def get_from_queue(queue_name,xqueue_session):
    """
        Get a single submission from xqueue
        """
    try:
        success, response = util._http_get(xqueue_session,
                                           urlparse.urljoin(settings.XQUEUE_INTERFACE['url'], project_urls.XqueueURLs.get_submission),
                                           {'queue_name': queue_name})
    except Exception as err:
        return False, "Error getting response: {0}".format(err)
    
    return success, response

def get_queue_length(queue_name,xqueue_session):
    """
        Returns the length of the queue
        """
    try:
        success, response = util._http_get(xqueue_session,
                                           urlparse.urljoin(settings.XQUEUE_INTERFACE['url'], project_urls.XqueueURLs.get_queuelen),
                                           {'queue_name': queue_name})
        
        if not success:
            return False,"Invalid return code in reply"
    
    except Exception as e:
        log.critical("Unable to get queue length: {0}".format(e))
        return False, "Unable to get queue length."
    
    return True, response

def connect():
    global conexion_db
    global cursor
    global conexion_qm
    global channel

    conexion_db=sqlite3.connect("grader.db")
    cursor=conexion_db.cursor()

    credentials = pika.PlainCredentials('edx', 'edx')
    parameters = pika.ConnectionParameters('localhost',5672,'/',credentials)
    conexion_qm = pika.BlockingConnection(parameters)
    channel = conexion_qm.channel()

def disconnect():
    global conexion_db
    global cursor
    global conexion_qm
    global channel

    conexion_db.close()
    channel.close()
    conexion_qm.close()

if __name__ == '__main__':
    freeze_support()
    try:
        logging.basicConfig(level=logging.ERROR)

        while True:
            connect()
            each_cycle()
            disconnect()
            time.sleep(2)

    except KeyboardInterrupt:
        logging.info('^C received, shutting down')
        disconnect()

    except BaseException as e:
        logging.error("SCHEDULER: Error {0}".format(str(e)))
    finally:
        if conexion_db is not None:
            conexion_db.close()
        if channel is not None:
            channel.close()
        if conexion_qm is not None:
            conexion_qm.close()
