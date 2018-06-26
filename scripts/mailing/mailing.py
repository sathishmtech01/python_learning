###Importing all the necessary libraries
from flask import Flask, jsonify,abort,request
import os
import pandas as pd
import random
import pymongo
from pymongo import MongoClient
import datetime
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys

def get_connection(uri,db,collection):
    """
    This module uses the uri, db and collection for the mongodb connection establishment
    :param uri: the mongodb server uri example mongodb://localhost:27017
    :param db: database example: HelpDeskCRM
    :param collection: collection example client_users
    :return: try : db_connection mongodb object
            except : None in case of timeout error
    """
    try:
        client = MongoClient(uri)
        client.server_info()
        db_connection = client[db][collection]
        return db_connection
    except (pymongo.errors.ServerSelectionTimeoutError) as err:
        logging.info("Connection not established!!")
        return None

def send_mail(fromaddr, password, toaddr, ccaddr,bccaddr,subject,body,attachments):
    """
    This module is to send mail with to,cc,bcc,subject,body and list of attachments.
    :param fromaddr:
    :param password:
    :param toaddr:
    :param ccaddr:
    :param bccaddr:
    :param subject:
    :param body:
    :param attachments:
    :return:
    """
    #
    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = ",".join(toaddr)
    msg["Cc"] = ",".join(ccaddr)
    msg["Bcc"] = ",".join(bccaddr)
    msg["Subject"] = subject

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, "rb") as fp:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(fp.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", "attachment", filename=os.path.basename(file))
            msg.attach(part)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            pass
            #raise

    msg.attach(MIMEText(body, "plain"))
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    #
    server.close()


if __name__ == "__main__":
    fromaddr = "csk@gmail.com"
    password = "csk"
    toaddr = ["csk@gmail.com"]
    ccaddr = ["csk@gmail.com"]
    bccaddr = ["csk@gmail.com"]
    subject = "Request"
    body = "Hello"
    attachments = ["README.md"]
    send_mail(fromaddr, password, toaddr, ccaddr,bccaddr,subject,body,attachments)
    print("Hello Testing Mail function")