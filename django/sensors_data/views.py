from django.shortcuts import render
from django.http import HttpResponse

# from .models import DataType
from .models import Unit

from datetime import datetime as dt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def index(request):
    # list_unixtimes_values = sorted([(data.measure.unixtime, data.value) for data in DataType.objects.all()[0].data_set.all()])
    list_unixtimes_values = sorted([(data.measure.unixtime, data.value)
                                    # for measure in Unit.objects.filter(name='temp1')[0].measure_set.all()
                                    for measure in Unit.objects.filter(name='y4k_temp1_noised')[0].measure_set.all()
                                    for data in measure.data_set.all()])
    list_unixtimes, list_values = zip(*list_unixtimes_values)
    list_datetimes = list(map(dt.fromtimestamp, list_unixtimes))

    # return HttpResponse(str([list_unixtimes, list_values]))

    fig = Figure(facecolor='white')
    ax = fig.add_subplot(1, 1, 1)
    # ax.plot(list_unixtimes, list_values)
    ax.plot(list_datetimes, list_values)
    ax.grid()
    fig.autofmt_xdate()

    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
