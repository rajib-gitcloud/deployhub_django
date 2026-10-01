from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import sys
import django

class HealthCheckView(APIView):
    def get(self, request):
        return Response({
            "status": "healthy",
            "service": "deployhub_django",
            "framework": f"Django {django.get_version()}",
            "python_version": sys.version.split()[0]
        }, status=status.HTTP_200_OK)

class InfoView(APIView):
    def get(self, request):
        return Response({
            "app_name": "DeployHub Django Backend",
            "version": "1.0.0",
            "description": "Production-ready Django backend template with REST framework support.",
            "endpoints": [
                {"path": "/", "method": "GET", "desc": "Root health check"},
                {"path": "/api/health/", "method": "GET", "desc": "Detailed service health status"},
                {"path": "/api/info/", "method": "GET", "desc": "Service information"},
                {"path": "/api/items/", "method": "GET", "desc": "Sample item data"}
            ]
        })

class ItemListView(APIView):
    def get(self, request):
        items = [
            {"id": 1, "title": "Setup Django Project", "status": "Completed"},
            {"id": 2, "title": "Configure DeployHub Manifest", "status": "Completed"},
            {"id": 3, "title": "Deploy to Production Cloud", "status": "Ready"}
        ]
        return Response({"items": items, "count": len(items)})
