from django.shortcuts import render
from django.template import loader

from .models import Bb, Rubric


def index(requests):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(requests, 'bboard/index.html', context)

def by_rubric(requests, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(requests, 'bboard/by_rubric.html', context)
