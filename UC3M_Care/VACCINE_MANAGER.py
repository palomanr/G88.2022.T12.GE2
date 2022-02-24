import json
import uuid

from .VACCINE_MANAGEMENT_EXCEPTION import VACCINE_MANAGEMENT_EXCEPTION
from .UC3M_VACCINEREQUEST import VACCINEREQUEST

class VACCINE_MANAGER:
    def __init__(self):
        pass

    @staticmethod
    def ValidateGUID( GUID ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        try:
            myUUID = uuid.UUID(GUID)
            import re
            myregex = re.compile(r'^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-'
                                 r'[0-9A-F]{12}$'
                                 , re.IGNORECASE)
            x = myregex.fullmatch(GUID)
            if not x:
                raise VACCINE_MANAGEMENT_EXCEPTION("Invalid UUID v4 format")
        except ValueError as e:
            raise VACCINE_MANAGEMENT_EXCEPTION("Id receive is not a UUID") from e
        return True

    def ReadaccessrequestfromJSON(self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise VACCINE_MANAGEMENT_EXCEPTION("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise VACCINE_MANAGEMENT_EXCEPTION("JSON Decode Error - Wrong JSON Format") from e


        try:
            Guid = DATA["id"]
            Zip = DATA["phoneNumber"]
            req = VACCINEREQUEST(Guid, Zip)
        except KeyError as e:
            raise VACCINE_MANAGEMENT_EXCEPTION("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateGUID(Guid):
            raise VACCINE_MANAGEMENT_EXCEPTION("Invalid GUID")

        # Close the file
        return req