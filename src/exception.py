import sys

def error_message_detail(error,error_detail:sys):
    _,_,exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script name {file_name} on line number {exec_tb.tb_lineno} and error is {str(error)}"
    
    return error_message
    
class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message