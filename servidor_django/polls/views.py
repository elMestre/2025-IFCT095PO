from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))


def patata(request):
    return HttpResponse("Hey, hola patata")


def detail(request, question_id):
    return HttpResponse("Estas mirando la pregunta nº: %s." % question_id)


def results(request, question_id):
    response = "Resultados de la pregunta %s."

    response += "<ol>"
    for i in range(question_id):
        response += f"<li>{i + question_id}</li>"
    response += "</ol>"

    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Vas a votar la pregunta %s." % question_id)