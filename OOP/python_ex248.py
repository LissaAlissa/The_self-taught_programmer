class PublicPrivateExample:
    def __init__(self):
        self.ulic = "безопасно"
        self._unsafe = "опасно"

    def pulic_method(self):
        # клиенты могут это использовать
        pass
    def _unsafe_method(self):
        # клиенты недолжны это использовать
        pass
        self.ulic = "безопасно"
        self._unsafe = "опасно"