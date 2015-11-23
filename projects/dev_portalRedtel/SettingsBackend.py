from django.conf import settings 
from django.contrib.auth.models import User, check_password 
 
class SettingsBackend(object): 
    """ 
    Autentificación contra la configuración ADMIN_LOGIN y ADMIN_PASSWORD. 
    Usa el nombre de login, y el hash del password. Por ejemplo: 
    ADMIN_LOGIN = ’admin’ 
    ADMIN_PASSWORD =     
        ’sha1$4e987$afbcf42e21bd417fb71db8c66b321e9fc33051de’ 
    """ 
    def authenticate(self, username=None, password=None): 
        login_valid = (settings.ADMIN_LOGIN == username) 
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD) 
        if login_valid and pwd_valid: 
            try: 
               user = User.objects.get(username=username) 
            except User.DoesNotExist: 
                # Crea un nuevo usuario. Nota que podemos fijar un password 
                # para cualquiera, porque este no será comprobado; el password 
                # de settings.py lo hará. 
                user = User(username=username, password=’get from settings.py’) 
                user.is_staff = True 
                user.is_superuser = True 
                user.save() 
 
            return user 
        return None 
 
    def get_user(self, user_id): 
        try: 
           return User.objects.get(pk=user_id) 
        except User.DoesNotExist: 
            return None
