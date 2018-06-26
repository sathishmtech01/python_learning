import logging

def activity_log(log_dirpath, log_format,log_activity):
    """
    This module gives the activity log, having two functionalities which stores in helpdesk folder and stream in the python terminal

    :param log_dirpath: log directory path
    :param log_format: log storage format
    :param log_activity: log activity purpose
    :return: logger object with is used in all modules
    """

    logging.basicConfig(filename=log_dirpath, level=logging.DEBUG,format=log_format)

    # create logger
    logger = logging.getLogger(log_activity)
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(log_format)

    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)

    return logger

def activity_log_message(user=None,role=None,ip_address=None,rest_method=None,module=None,start_time=None,end_time=None,time_taken=None):
    """

    :param user:
    :param role:
    :param ip_address:
    :param rest_method:
    :param module:
    :param start_time:
    :param end_time:
    :param time_taken:
    :return:
    """

    message = "{} | {} | {} | {} | {} | {} | {} | {}".format(user,role,ip_address,rest_method,module,start_time,end_time,time_taken)

    return message


if __name__ == "__main__":
    import datetime
    now = datetime.datetime.now()
    log_file_name = "activity_{}-{}-{}.log".format(now.date(), now.hour, now.minute)
    log_directory = "activity_log"
    log_dirpath = log_directory + "/" + log_file_name
    log_format = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    log_activity = "activity_log"

    # log data
    logger = activity_log(log_dirpath, log_format,log_activity)

    # "application" code
    logger.debug("debug message")
    logger.info(activity_log_message())
    logger.warn("warn message")
    logger.error("error message")
    logger.critical("critical message")