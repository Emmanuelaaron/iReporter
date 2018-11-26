class Validating_string:

    @staticmethod
    def is_string(string):
        return type(string) == str
    
    @staticmethod
    def is_space(string):
        return string.isspace()

    @staticmethod
    def characters(string):
        return len(string) > 0