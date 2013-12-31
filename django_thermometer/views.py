from django.http import HttpResponseBadRequest, HttpResponse
import simplejson
from temperature import read_temperatures, get_thermometers, ThermometerNotFound


def list_thermometers(request):
    if request.method != "GET":
        response = HttpResponseBadRequest(
            content=simplejson.dumps({"errors": ["Only GET method allowed", ]}),
            content_type="application/json")
        response["Cache-Control"] = 'no-cache'
        return response

    temperatures = None
    if "temperatures" in request.GET and request.GET["temperatures"] not in (None, ""):
        temperatures = request.GET["temperatures"]

    if temperatures is None:
        response = HttpResponse(
            content=simplejson.dumps([x.name for x in get_thermometers()]),
            content_type="application/json")
    else:
        response = HttpResponse(
            content=simplejson.dumps(read_temperatures()),
            content_type="application/json",
        )
    response['Cache-Control'] = 'no-cache'
    return response


def thermometer(request, thermometer):
    if request.method != "GET":
        response = HttpResponseBadRequest(
            content=simplejson.dumps({"errors": ["Only GET method allowed", ]}),
            content_type="application/json")
        response["Cache-Control"] = 'no-cache'
        return response
    try:

        response = HttpResponse(
            content=simplejson.dumps(read_temperatures(thermometer)),
            content_type="application/json",
        )
        response["Cache-Control"] = "no-cache"
        return response

    except ThermometerNotFound:
        response = HttpResponseBadRequest(
            content=simplejson.dumps({"errors": ["Themometer %s not found" % thermometer, ]}),
            content_type="application/json")
        response["Cache-Control"] = 'no-cache'
        return response

