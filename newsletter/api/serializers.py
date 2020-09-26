from rest_framework import serializers

from newsletter.models import Join


class JoinSerializer(serializers.ModelSerializer):
    """
    Serializer for newsletter is added to use AJAX method with subscription 
    Instead of refreshing page.
    """
    class Meta:
        model = Join
        fields = ['email']
    
    def validate_email(self, value):
        email = value
        qs = Join.objects.filter(email__iexact=email)
        if qs.exists():
            raise serializers.ValidationError("This email already exists")
        return email