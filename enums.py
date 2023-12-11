from enum import Enum,unique

@unique
class ResponseCode(Enum):
    SUCCESS = 0, 'success'
    PARAMS_ERROR = 202, 'params error.'
    OPERATION_FAIL = 203, 'operation failure.'
    PLEASE_WAIT = 204, 'please wait'
    MEDIA_FILE_EXTENSIONS_ERROR = 205, 'file format error.'
    TASK_NOT_EXISTS = 206, 'task does not exist.'
    NO_MORE = 207, 'no more'
    MESSAGE_TOO_LONG = 208, 'The message is too long. Please clear page or refresh the webpage.'



