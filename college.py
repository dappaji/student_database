class college():
    name = "PESCE"
    place = "Mandya"
    code = "4PS"

    @classmethod
    def get_info(cls):
        print(cls.name, cls.place, cls.code)