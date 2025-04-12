from django.shortcuts import render, HttpResponse
from django.utils.dateformat import format
from django.utils import timezone
# from .models import (TodoItem)
from .models import Calc
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pytz
import pyautogui

# Create your views here.

def home(request):
    return render(request, "home.html")

# def todos(request):
#     items = TodoItem.objects.all()
#     return render(request, "todos.html", {"todos": items})

@csrf_exempt
def add(request):
    if(request.method == "POST"):
        data = json.loads(request.body.decode("utf-8"))
        num1 = data.get("num1")
        num2 = data.get("num2")
        add_obj = Calc.objects.create(
                num1=num1,
                num2=num2,
                operation="add",
            )
        total = num1 + num2
        return JsonResponse({"ADD": total, "Operation": add_obj.operation, "Time": add_obj.time.strftime("%Y-%m-%d %H:%M:%S")})
    
@csrf_exempt
def sub(request):
    if(request.method == "POST"):
        data = json.loads(request.body.decode("utf-8"))
        num1 = data.get("num1")
        num2 = data.get("num2")
        add_obj = Calc.objects.create(
                num1=num1,
                num2=num2,
                operation="sub",
            )
        total = num1 - num2
        return JsonResponse({"SUB": total, "Operation": add_obj.operation, "Time": add_obj.time.strftime("%Y-%m-%d %H:%M:%S")})
    
@csrf_exempt
def cursorMovement(request):
    if(request.method == "POST"):
        data = json.loads(request.body.decode("utf-8"))
        x = data.get("x")
        y = data.get("y")
        pyautogui.moveTo(x, y, duration= 0)
        return JsonResponse({"status": "Cursor moved", "x": x, "y": y}, status=200)
    
def moveCursor(request):
    return render(request, 'cursor.html')


def history(request):
    data = list(Calc.objects.all().values())
    return JsonResponse({"history": data, "message": "successfully retreived"})