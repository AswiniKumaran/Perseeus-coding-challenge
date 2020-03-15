from rest_framework import serializers
from user_data import models

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhoneNumber
        fields = ['id','number']

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields=['id','mail']

class UserSerializer(serializers.ModelSerializer):
    email=EmailSerializer(many=True,source='user_email')
    phone=PhoneNumberSerializer(many=True,source='user_mobile')
    class Meta:
        model = models.User
        fields = ['id','firstName','lastName','email','phone']

    def create(self, validated_data):
        email_datas=validated_data.pop('email')
        phone_datas=validated_data.pop('phone')
        user=models.User.objects.create(**user_data)
        for data in email_datas:
            email=models.Email.objects.create(user=user,**data)
        for data in phone_datas:
            phone=models.PhoneNumber.objects.create(user=user,**data)
        return user

    def update(self, instance, validated_data):
        email_datas=validated_data.pop('email')
        phone_datas=validated_data.pop('phone')
        mails = (instance.email_datas).all()
        mails = list(mails)
        numbers = (instance.phone_datas).all()
        numbers = list(numbers)
        instance.id = validated_data.get('id', instance.id)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.save()

        for data in email_datas:
            mail = mails.pop(0)
            mail.id = data.get('id', mail.id)
            mail.mail = data.get('mail', mail.mail)
            mail.save()
        for data in phone_datas:
            number = numbers.pop(0)
            number.id = data.get('id', number.id)
            number.number = data.get('number', number.number)
            mail.save()
        return instance
