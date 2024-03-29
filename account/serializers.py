from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model






User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200,read_only=True)
    name = serializers.CharField(max_length=100, read_only=True)
    password = serializers.CharField(max_length=100, min_length=12,write_only=True)
    country = serializers.CharField(max_length=100, read_only=True)
    state = serializers.CharField(max_length=100, read_only=True)
    city = serializers.CharField(max_length=100, read_only=True)
    phone = serializers.CharField(read_only=True)
    profile_pic = serializers.ImageField(read_only=True)
    is_superuser = serializers.BooleanField(default=False)
    is_staff = serializers.BooleanField(default=False)
    
    
   

    class Meta:
        model = User
        fields = ['id','email','name','country', 'state', 'password','city', 'phone', 'is_superuser','is_staff','is_lawyer','is_lawstudent','is_lawfirm','is_client','profile_pic']

 

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    refresh_token = serializers.SerializerMethodField(read_only=True)
 

    
    class Meta:
        model = User
        fields = ['id','email','name','country', 'state', 'password','city', 'phone', 'is_superuser','is_staff', 'is_lawyer','is_lawstudent','is_lawfirm','is_client','profile_pic','token', 'refresh_token']


    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

    def get_refresh_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token)

   








# class SetNewPasswordSerializer(serializers.Serializer):
#     password = serializers.CharField(min_length=8, max_length=30, write_only=True)
#     token = serializers.CharField(min_length=1, write_only=True)
#     uidb64 = serializers.CharField(min_length=1, write_only=True)


#     class Meta:
#         fields = ['password','token', 'uidb64']
    
#     def validate(self,attrs):
#         try:
#             password= attrs.get('password')
#             token = attrs.get('token') 
#             uidb64 = attrs.get('uidb64') 
#             id = force_str(urlsafe_base64_decode(uidb64))  
#             user = User.objects.get(id=id)

#             if not PasswordResetTokenGenerator().check_token(user, token):
#                 raise AuthenticationFailed('The reset link is invalid', 401)

#             user.set_password(password)
#             user.save()    
#         except Exception as e:
#             raise AuthenticationFailed('The reset link is invalid', 401)
#         return super().validate(attrs)






    



