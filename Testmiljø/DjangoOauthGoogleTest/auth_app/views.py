from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

def home(request):
    return render(request, 'auth_app/home.html')

@api_view(['GET'])
def get_jwt_token(request):
    if not request.user.is_authenticated:
        return Response({"error": "Sign in first"}, status=401)
    refresh = RefreshToken.for_user(request.user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    })
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def projects(request):
    data = {
        "message": "Welcome to project collab api",
        "user": request.user.email,
        "projects": ["sample project 1", "Sample project 2"]
    }
    return Response(data)