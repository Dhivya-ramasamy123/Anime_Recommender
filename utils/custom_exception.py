import sys 

#creating a class for handling exception
class CustomException(Exception):
    def __init__(self,message: str, error_detail: Exception = None): # type: ignore
        self.error_message = self.get_detailed_error_message(message,error_detail) # type: ignore
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message,error_detail):
         _, _, exc_tb= sys.exc_info()   #Exception info
         #extract file name
         file_name=exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown file"
         line_number=exc_tb.tb_lineno if exc_tb else "Unknown Line"
         return f"{message} | Error : {error_detail} | File : {file_name} | Line: {line_number}"

    def __str__(self):
         return self.error_message




