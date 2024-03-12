

class User(object):
    def __init__(self,idd,name,email,type_user,username):
        self.idd=idd
        self.name=name
        self.email=email
        self.type_user=type_user
        self.username=username



class Listener(User):
    def __init__(self, idd, name, email, type_user,username,l_albums,l_songs,playlists): #l_albums y l_songs es una abreviatura para liked albums y liked songs
        super().__init__(idd,name, email, type_user,username)
        self.l_albums=l_albums
        self.l_songs=l_songs
        self.playlists=playlists
    
    def show_attr(self):
        print(f"""
              Nombre: {self.name}
              Email: {self.email}
              Liked Songs: {self.l_songs}
              Liked Albums: {self.l_albums}
              Playlists: {self.playlists}""")

class Artist(User):
    def __init__(self,idd, name, email, type_user,username,albums,top_songs,reproducciones): 
        super().__init__(idd,name, email, type_user,username)
        self.albums=albums
        self.top_songs=top_songs
        self.reproducciones=reproducciones

    def show_attr(self):
        print(f"""
              Nombre: {self.name}
              Email: {self.email}
              Top Songs: {self.top_songs}
              Albums:{self.albums}
              Total listens: {self.reproducciones}""")