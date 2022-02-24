"""FILE CREATED TO STORE THE CLASS RELATED TO THE VACCINE'S REQUESTS"""

import json
from datetime import datetime

class VACCINEREQUEST:
    """CLASS IN CHARGED OF HAVING ALL FUNCTIONS CONCERNED WITH THE REQUESTING APPOINTMENTS TO GET THE VACCINE"""
    def __init__( self, idcode, phoneNumber ):
        self.phoneNumber = phoneNumber
        self.idCode = idcode
        justnow = datetime.utcnow()
        self.timeStamp = datetime.timestamp(justnow)

    def __str__(self):
        return "VaccineRequest:" + json.dumps(self.__dict__)

    @property
    def phoneVariable(self):
        """TO MAKE A VARIABLE PRIVATE"""
        return self.phoneNumber
    @phoneVariable.setter
    def phoneVariable(self, value):
        self.phoneNumber = value

    @property
    def idDocument(self):
        """TO MAKE A VARIABLE PRIVATE"""
        return self.idCode
    @idDocument.setter
    def idDocument(self,value):
        self.idCode = value
