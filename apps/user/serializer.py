from rest_framework import serializers

from apps.user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_login', 'username', 'date_joined', 'age', 'phone', 'direction', 'coin')


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 255,
        write_only = True
    )
    confirm_password = serializers.CharField(
        max_length = 255,
        write_only = True
    )
    
    class Meta:
        model = User
        fields = ('id', 'username', 'age', 'phone', 'email', 'direction', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        if '+996' not in attrs['phone']:
            raise serializers.ValidationError({'phone':'Указанный вами код не соответствует к стандартам КР(+996)'})
        if len(attrs['password']) < 4 and len(attrs['confirm_password']) < 4 :
            raise serializers.ValidationError({'password':'Пароль слишком короткий!'})
        if '@gmail.com' not in attrs['email']:
            raise serializers.ValidationError({'email':'Введите корректный email (@gmail.com)'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            phone=validated_data['phone'],
            age=validated_data['age'],
            email=validated_data['email'],
            direction=validated_data['direction'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user 
    

class UserDetileSerializer(serializers.DjangoModelField):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'age', 'direction', 'coin', 'password', 'confirm_password')
