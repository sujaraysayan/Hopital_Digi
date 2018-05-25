# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, \
                        HttpResponseRedirect
# Create your views here.

def Home(requset):
    return render(requset, "home.html")
