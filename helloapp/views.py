from django.shortcuts import render


from helloapp.models import Email
from .serializers import EmailSendSerializer
from rest_framework.response import Response
from rest_framework import generics, status
# Create your views here.
class EmailSendAPIView(generics.ListCreateAPIView):
    serializer_class = EmailSendSerializer
    queryset = Email.objects.all()

    def get(self, request):
        emails = Email.objects.all()
        serializer = self.serializer_class(instance=emails, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data 
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            email = serializer.data['email']
            print(email)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        