# encoding in this modules makes use of the ceasar cipher with n as 1
# i.e a is encoded as b and z encoded as a
from manipulate_csv import appending_new_rows


class controllers:
    '''
    Class that holds the functionality of cheking that the
    values entered to the form are entered correctly
    '''

    # class attributes 
   

    # Initializer / Instance Attributes
    def __init__(self):
        pass
        
    def not_empty(self,field_to_check,collected_value):
        '''
        Function that ensures that the given field is
        not empty
        '''
        pass

    def check_date_format(self,field_to_check,collected_value):
        '''
        function that checks that a given date field is 
        given in the correct format
        '''
        pass


class save_customer_details:
    '''
    Class that save the given customer details
    '''

    def __init__(self,given_data,file_to_write):
        self.given_data = given_data
        self.file_to_write = file_to_write

    def save_current_details(self):
        '''
        Function that save the given data details to a 
        specific file
        '''
        appending_new_rows(self.file_to_write,self.given_data)