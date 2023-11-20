#factory pattern
class NOSFactory:
    @staticmethod
    def create_nos(nos_type):
        if nos_type == "Resonac":
            return "Resonac NOS"
        elif nos_type == "Sema":
            return "Sema NOS"
        else:
            return "Unknown NOS"