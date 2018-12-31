# encoding in this modules makes use of the ceasar cipher with n as 1
# i.e a is encoded as b and z encoded as a

class encode_decode:
    '''
    Class that holds the functionality of encoding and decoding a 
    string a given string
    '''

    # class attributes 
    string_with_all_alphabets = 'abcdefghijklmnopqrstuvwxyz'

    # Initializer / Instance Attributes
    def __init__(self,string_to_encode_or_decode):
        self.string_to_encode_or_decode = string_to_encode_or_decode
        
    def encode_letter(self,letter_to_encode):
        '''
        function that encodes an alphabetical
        letter with ROT(n) where n == 1
        '''
        if(letter_to_encode not in self.string_with_all_alphabets ):
            # this ensures that alphabetical characters are handled correctly eg. spaces
            return letter_to_encode
        elif(letter_to_encode != 'z'):
            letter_alphabetical_index = self.string_with_all_alphabets.find(letter_to_encode)
            return self.string_with_all_alphabets[letter_alphabetical_index + 1]
        else:
            return 'a'

    def decode_letter(self,letter_to_decode):
        '''
        function that dencodes an alphabetical
        letter with ROT(n) where n == 1
        '''
        if(letter_to_decode not in self.string_with_all_alphabets ):
            # this ensures that alphabetical characters are handled correctly eg spaces
            return letter_to_decode
        elif(letter_to_decode != 'a'):
            letter_alphabetical_index = self.string_with_all_alphabets.find(letter_to_decode)
            return self.string_with_all_alphabets[letter_alphabetical_index - 1]
        else:
            return 'z'

    def encode_string(self):
        '''
        function that encodes a string with ROT(n) where n == 1
        '''
        return_string = ''
        for x in self.string_to_encode_or_decode:
            return_string += self.encode_letter(x) 
        return return_string

    def decode_string(self):
        '''
        function that decodes a string with ROT(n) where n == 1
        '''
        return_string = ''
        for x in self.string_to_encode_or_decode:
            return_string += self.decode_letter(x)
        return return_string