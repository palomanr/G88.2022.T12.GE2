"""THIS IS THE VACCINE MANAGER MODULE WHERE WE READ THE ACCESS REQUEST FROM JSON FILE"""
import json
import uuid
import re

from .UC3M_VaccineManagementException import VACCINEMANAGEMENTEXCEPTION
from .UC3M_VaccineRequest import VACCINEREQUEST

class VACCINEMANAGER:
    """THIS IS THE CLASS WHERE WE CHECK BOTH FOR THE GUID AND FOR THE ACCESS REQUEST IN THE JSON FILE"""
    def __init__(self):
        pass

    @staticmethod
    def validateGuid(guid):
        """In this method, we are trying to validate the GUID with the v4 format"""

        try:
            uuid.UUID(guid)
            myregex = re.compile(r'^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-'
                                 r'[0-9A-F]{12}$'
                                 , re.IGNORECASE)
            x_var = myregex.fullmatch(guid)
            if not x_var:
                raise VACCINEMANAGEMENTEXCEPTION("Invalid UUID v4 format")
        except ValueError as e_var:
            raise VACCINEMANAGEMENTEXCEPTION("Id receive is not a UUID") from e_var
        return True

    def readAccessRequestFromJson(self, fileContent):
        """In this method, we are checking for possible errors when opening the JSON file"""

        try:
            with open(fileContent, encoding="utf-8") as file_cont:
                data_cont = json.load(file_cont)
        except FileNotFoundError as e_var:
            raise VACCINEMANAGEMENTEXCEPTION("Wrong file or file path") from e_var
        except json.JSONDecodeError as e_var:
            raise VACCINEMANAGEMENTEXCEPTION("JSON Decode Error - Wrong JSON Format") from e_var


        try:
            guid_profile = data_cont["id"]
            zip_cont = data_cont["phoneNumber"]
            req = VACCINEREQUEST(guid_profile, zip_cont)
        except KeyError as e_var:
            raise VACCINEMANAGEMENTEXCEPTION("JSON Decode Error - Invalid JSON Key") from e_var
        if not self.validateGuid(guid_profile):
            raise VACCINEMANAGEMENTEXCEPTION("Invalid GUID")

        # Close the file
        return req
VACCINEMANAGER()
