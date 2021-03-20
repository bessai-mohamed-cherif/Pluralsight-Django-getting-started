from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return HttpResponse("Welcome to the meeting planner!")

def date(request):
    return HttpResponse("This page was served at" + str(datetime.now()))

def about(request):
    return HttpResponse("My name is Bachir Boulayoun and I am a software engineer")