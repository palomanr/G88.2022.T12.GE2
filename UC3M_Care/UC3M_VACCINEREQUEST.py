"""FILE FOR CREATING A CLASS TO MANAGE THE REQUESTED VACCINES"""

import json
from datetime import datetime


class VACCINEREQUEST:
    """INSIDE VACCINE_REQUEST CLASS WE CAN APPRECIATE ALL FUNCTIONS WHICH ARE NECESSARY TO REQUEST AN APPOINTMENT TO
    HAVE A VACCINE """

    def __init__(self, idcode, phoneNumber):
        self.phoneNumber = phoneNumber
        self.idcode = idcode
        just_now = datetime.utcnow()
        self.timeStamp = datetime.timestamp(just_now)

    def __str__(self):
        return "VaccineRequest:" + json.dumps(self.__dict__)

    @property
    def phoneVariable(self):
        """TO MAKE ATTRIBUTE PRIVATE"""
        return self.phoneNumber

    @phoneVariable.setter
    def phoneVariable(self, value):
        self.phoneNumber = value

    @property
    def idDocument(self):
        """TO MAKE ATTRIBUTE PRIVATE"""
        return self.idcode

    @idDocument.setter
    def idDocument(self, value):
        self.idcode = value
