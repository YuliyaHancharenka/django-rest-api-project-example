from rest_framework import serializers

from restApi.models import Employees


class EmployeesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Employees
        fields = '__all__'
