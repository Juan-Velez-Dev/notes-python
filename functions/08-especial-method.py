""" Metodos especiales """


class CD:
    def __init__(self, auth, title, songs):
        self.auth = auth
        self.title = title
        self.songs = songs

    def __str__(self):
        return f"Album: {self.title}, de {self.auth}"

    def __len__(self):
        return self.songs
