from datetime import datetime

import timestamp as timestamp
import unix as unix

TIME = datetime.now()

LOGGIN = {
    "action": "authenticate",
    "time": <unix timestamp>
    "user": {
    "account_name": "C0deMaver1ck",
    "password": "CorrectHorseBatterStaple"
     }
}

RESPONSE = {
    "response": None,
    "time": str(TIME),
    "alert": None,
    "contacts": None
}

MESSAGE = {
    "action": "msg",
    "time": str(TIME),
    "to": "#all",
    "from": "account_name",
    "message": "Hello Everything",
}


MESSAGE_FROM_SERVR = {
    "response": 200,
    "alert":"Необязательное сообщение/уведомление"
}

NOT_VALID_PASSWORD = {
    "response": 402,
    "error": "This could be "wrong password" or "no account with that name""
}


CONFLICT =  {
    "response": 409,
    "error": "Someone is already connected with the given user name"
}

EXIT = {
    "action": "quit"
}

LISTEN = {
         "action": "presence",
            "time": < unix timestamp >,
            "type": "status",
                "user": {
                    "account_name": "C0deMaver1ck",
                     "status": "Yep, I am here!"
                        }
}

ONLINE_USER = {
        "action": "probe",
        "time": <unix timestamp>,
}