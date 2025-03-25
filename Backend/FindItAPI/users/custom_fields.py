from rest_framework import serializers
from phonenumbers import NumberParseException
import phonenumbers


class PhoneNumberField(serializers.CharField):
    def to_internal_value(self, data):
        try:
            parsed_number = phonenumbers.parse(data)
        except:
            raise serializers.ValidationError('Invalid Phone Number.')
        
        return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

    def to_representation(self, value):
        try:
            parsed_number = phonenumbers.parse(value)
        except NumberParseException:
            return value
        
        return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        