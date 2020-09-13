# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from restApi.models import Employees
from restApi.serializers import EmployeesSerializers


class EmployeeList(APIView):

    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeesSerializers(employees, many=True)
        return Response(serializer.data)

    def post(self):
        pass
