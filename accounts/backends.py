from django.contrib.auth.models import user

class EmailAuth:
    """Authenticate a user by an email"""
    
    def authenticate(self, username=None, password=None):
        """Get and instance of user based off the email and verify the password"""
        
        
        try:
            user = User.objects.get(email=username)
            
            if user.check_password(password)
                return user
            return None
        except User.DoesNotExist:
            return None
            
    def get_user(self, user_id)
        """Used by the django authentication system to retrieve a user"""
        
        try:
            user = User.objects.get(pk=user_id)
            
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
        
        