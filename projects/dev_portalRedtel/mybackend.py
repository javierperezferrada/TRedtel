from django.contrib.auth.models import User
from portal.models import Usuario,Us
import md5
 
class RedtelBackend(object): 
    """ 
    Autentificacion contra la configuracion de usuarios del sistema 
    redtel.
    """ 
    def authenticate(self, username=None, password=None): 
        'metodo que realizara la autentificacion contra la tabla usuarios' 
        'de redtel.'
        usuario = Us.objects.get(username=username)
        m= md5.new()
        m.update(password)
        encript = m.hexdigest()
        if encript == usuario.password: 
            try: 
               user = User.objects.get(username=username) 
            except User.DoesNotExist: 
                # Crea un nuevo usuario. Nota que podemos fijar un password 
                # para cualquiera, porque este no sera comprobado; el password 
                # de settings.py lo hara. 
                user = User(username=username, password=usuario.password)
                user.save() 
            return user 
        return None 
 
    def get_user(self, user_id): 
        try: 
           return User.objects.get(pk=user_id) 
        except User.DoesNotExist: 
            return None