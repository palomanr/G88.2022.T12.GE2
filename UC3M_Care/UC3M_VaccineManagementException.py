"""THIS IS THE VACCINE MANAGER EXCEPTION MODULE WHERE WE HANDLE EXCEPTIONS RELATED TO THE VACCINE MANAGER MODULE"""

class VACCINEMANAGEMENTEXCEPTION(Exception):
    """THIS IS THE CLASS WHERE WE HANDLE THE EXCEPTIONS MESSAGES"""
    def __init__(self, message):
        self.messageContent = message
        super().__init__(self.message)

    @property
    def message(self):
        """This is the method used to send the messages shown for the exceptions"""
        return self.messageContent

    @message.setter
    def message(self,value):
        self.messageContent = value
VACCINEMANAGEMENTEXCEPTION("message")
