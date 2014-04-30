
class Encoder(object):
    def get_input(self,feed):
        return True
    def get_value(self):
        return (int(self.get_input(1))*2) + int(self.get_input(2))

