from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from .models import Userprofile, LoanApplication
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from .serializers import LoanApplicationSerializer


@api_view(['GET'])
def check_auth(request):
    return Response({
        'status': True,
    })


@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def signup(request):
    user = Userprofile.objects.create_user(email="admin@email.com", password="password")
    user.save()
    return Response({
        "status": True,
        "data": {},
        'message': 'User Account Successfully Created'
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def signin(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        Userprofile.objects.get(email=email)
        user = authenticate(email=email, password=password)
        if not user:
            return Response({
                "status": False,
                "data": {},
                'message': 'Invalid Credentials'
            }, status=status.HTTP_400_BAD_REQUEST)
        if user.is_active:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            response = Response({
                "status": True,
                "data": {
                    "user": {
                        "id": user.id,
                        "email": user.email,
                    },
                    "token": token.key
                },
                'message': 'User Account Successfully Logged In'
            }, status=status.HTTP_200_OK)
            response.set_cookie(key='jwt', value=token.key, httponly=True)
            return response

        else:
            return Response({
                "status": False,
                "data": {},
                'message': 'User Account is not active, reach out to admin'
            }, status=status.HTTP_400_BAD_REQUEST)

    except Userprofile.DoesNotExist:
        return Response({
            "status": False,
            "data": {},
            'message': 'User does not exist'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
@parser_classes([MultiPartParser])
def create_loan_application(request):
    print(request.data)
    print(request.data.loan_type)
    serializer = LoanApplicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": True,
            "data": serializer.data,
            'message': 'Loan Application Successfully Created'
        }, status=status.HTTP_201_CREATED)
    return Response({
        "status": False,
        'message': 'Loan Application Creation Failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_loan_applications(request):
    loan_applications = LoanApplication.objects.all()
    serializer = LoanApplicationSerializer(loan_applications, many=True)
    return Response({
        "status": True,
        "data": serializer.data,
        'message': 'Loan Applications Successfully Retrieved'
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_loan_application(request, pk):
    try:
        loan_application = LoanApplication.objects.get(loan_id=pk)
        serializer = LoanApplicationSerializer(loan_application)
        return Response({
            "status": True,
            "data": serializer.data,
            'message': 'Loan Application Successfully Retrieved'
        }, status=status.HTTP_200_OK)
    except LoanApplication.DoesNotExist:
        return Response({
            "status": False,
            "data": {},
            'message': 'Loan Application Does Not Exist'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def update_loan_application(request, pk):
    try:
        loan_application = LoanApplication.objects.get(loan_id=pk)
        serializer = LoanApplicationSerializer(loan_application, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            app_status = serializer.data.get('status')
            if app_status == "Approved":
                return Response({
                    "status": True,
                    "data": serializer.data,
                    'message': 'Loan Application Approved'
                }, status=status.HTTP_200_OK)
            elif app_status == "Declined":
                return Response({
                    "status": True,
                    "data": serializer.data,
                    'message': 'Loan Application Declined'
                }, status=status.HTTP_200_OK)
        return Response({
            "status": False,
            "data": serializer.errors,
            'message': 'Loan Application Update Failed'
        }, status=status.HTTP_400_BAD_REQUEST)
    except LoanApplication.DoesNotExist:
        return Response({
            "status": False,
            "data": {},
            'message': 'Loan Application Does Not Exist'
        }, status=status.HTTP_400_BAD_REQUEST)
