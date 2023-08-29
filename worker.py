import logging
import json
import urllib.parse as urlparse
from multiprocessing import *
import pika
import xqueue_util as util
import grading
import project_urls
import settings

import hito3_ej1.grader
import hito3_ej2.grader
import hito3_ej3.grader
import hito0_ej0.grader
import hito1_ej1.grader
import hito1_ej2.grader
import hito1_ej3.grader
import hito1_ej4.grader
import hito1_ej5.grader
import hito1_ej6.grader
import hito1_ej7.grader
import hito1_ej8.grader
import hito1_ej9.grader
import hito1_ej10.grader
import hito1_ej11.grader
import hito1_ej12.grader
import hito1_ej13.grader
import hito2_ej1.grader
import hito2_ej2.grader
import hito2_ej3.grader
import hito2_ej4.grader
import tema1_ej1.grader
import tema2_ej1.grader
import tema2_ej2.grader
import tema2_ej3.grader
import tema2_p1.grader
import tema3_ej1.grader
import tema3_ej2.grader
import tema3_ej3.grader
import tema3_ej4.grader
import tema3_ej5.grader
import tema4_ej1.grader
import tema4_ej2.grader
import tema4_ej3.grader
import tema8_ej1.grader
import tema8_ej2.grader
import tema8_ej3.grader
import tema8_ej4.grader
import tema8_ej5.grader
import tema9_ej1.grader
import tema9_ej2.grader
import tema9_ej3.grader
import tema9_ej4.grader
import tema9_ej5.grader
import tema10_ej2.grader
import tema10_ej3.grader
import tema10_ej1.grader
import tema11_ej1.grader
import tema11_ej2.grader
import tema11_ej3.grader
import tema12_ej1.grader
import lab1a.grader
import lab1b.grader
import lab2a.grader
import lab2b.grader
import lab3a.grader
import lab3b.grader
import lab5.grader

log = logging.getLogger(__name__)

QUEUE_NAME = settings.QUEUE_NAME

def consume(channel, method, properties, body):
    session = util.xqueue_login()

    mensaje=body.decode(encoding="utf-8")
    mensaje=mensaje.split(',')
    ejercicio=mensaje[0]
    puntos=mensaje[1]
    submission_id=mensaje[2]
    submission_key=mensaje[3]
    archivo=mensaje[4]

    if ejercicio=="hito0_ej0":
        resultado=grading.GradingResult()
        resultado.generar_exito(1)
    else:
        resultado=grade(ejercicio,puntos,archivo)

    xqueue_header, xqueue_body = util.create_xqueue_header_and_body(submission_id, submission_key, resultado.estado, resultado.puntaje, resultado.mensaje, 'iic1103_2015_s2_puc')
    (success, msg) = util.post_results_to_xqueue(session, json.dumps(xqueue_header), json.dumps(xqueue_body),)
    if success:
        channel.basic_ack(delivery_tag = method.delivery_tag)
        logging.info(resultado.mensaje)
        logging.info(submission_id,submission_key,"succesfully posted back to xqueue")

def grade(ejercicio,puntos,archivo):
    try:
        grader= grading.Grader()
        funcion_revision=eval(ejercicio+"."+"grader.Analizador().revisar")
        resultado=grader.iniciar_revision(ejercicio,float(puntos),archivo,funcion_revision)

    except BaseException as e:
        resultado= grading.GradingResult()
        resultado.generar_error("WORKER: {0}: Por favor intenta nuevamente.".format(str(e)),0)

    return resultado

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

if __name__ == '__main__':
    freeze_support()
    try:
        logging.basicConfig(level=logging.ERROR)
        credentials = pika.PlainCredentials('edx', 'edx')
        parameters = pika.ConnectionParameters('localhost',5672,'/',credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(consume,queue='iic1103_dev')
        channel.start_consuming()

    except BaseException as e:
        logging.error("WORKER: {0}: Por favor intenta nuevamente.".format(str(e)))
