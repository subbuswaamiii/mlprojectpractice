import sys
import logging

def error_message_detail(error, error_detail:sys):
    
    exc_type, exc_value, exc_traceback = sys.exc_info()
    file_name = exc_traceback.tb_frame.f_code.co_filename
    error_message ="Error occured in Python Script name [{0}] line number [{1}] error message [{2}]"
    file_name,exc_traceback.tb_lineno,str(error)


    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super.__init__(error_message)
        self.error_message= error_messsage_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
     




if __name__== "__main__":

    try:
        a = 1/0

    except CustomException as e:

        ##logging.info("Logging has started")
        logging.info("Divide By Zero ")
        raise CustomException(e,sys)
    
    