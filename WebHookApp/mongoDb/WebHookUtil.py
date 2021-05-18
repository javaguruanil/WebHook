from datetime import datetime

def getCurrentDateTime():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


