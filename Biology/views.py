from django.shortcuts import render
from .models import BiologyQuestions
from django.contrib import messages
import datetime
# Create your views here.
a = datetime.datetime.now().replace(microsecond=0)
biology_question = BiologyQuestions.objects.all()
a1 = biology_question[0]
a2 = biology_question[1]
a3 = biology_question[2]
a4 = biology_question[3]
a5 = biology_question[4]
a6 = biology_question[5]
a7 = biology_question[6]
a8 = biology_question[7]
a9 = biology_question[8]
a10 = biology_question[9]


def biology(request):
    global a
    a = datetime.datetime.now().replace(microsecond=0)

    biology_question = BiologyQuestions.objects.all()
    a1 = biology_question[0]
    a2 = biology_question[1]
    a3 = biology_question[2]
    a4 = biology_question[3]
    a5 = biology_question[4]
    a6 = biology_question[5]
    a7 = biology_question[6]
    a8 = biology_question[7]
    a9 = biology_question[8]
    a10 = biology_question[9]



    return render(request,'biology.html',{'a1':a1 ,'a2':a2,'a3':a3 ,'a4':a4 ,'a5':a5 ,'a6':a6 ,'a7':a7 ,'a8':a8 ,'a9':a9 ,'a10':a10 })

# Create your views here.

def thank(request):
    b = datetime.datetime.now().replace(microsecond=0)


    answer = BiologyQuestions.objects.all()

    count = 0
    if request.method == "POST":
        q1 = request.POST['qno1']
        q2 = request.POST['qno2']
        q3 = request.POST['qno3']
        q4 = request.POST['qno4']
        q5 = request.POST['qno5']
        q6 = request.POST['qno6']
        q7 = request.POST['qno7']
        q8 = request.POST['qno8']
        q9 = request.POST['qno9']
        q10 = request.POST['qno10']

        if q1 == answer[0].Answer:
            count += 1
        else:
            messages.error(request, a1.Question+":"+a1.Answer)
        if q2 == answer[1].Answer:
            count += 1
        else:
            messages.error(request, a2.Question+":"+a2.Answer)

        if q3 == answer[2].Answer:
            count += 1
        else:
            messages.error(request, a3.Question+":"+a3.Answer)
        if q4 == answer[3].Answer:
            count += 1
        else:
            messages.error(request, a4.Question+":"+a4.Answer)
        if q5 == answer[4].Answer:
            count += 1
        else:
            messages.error(request, a5.Question+":"+a5.Answer)
        if q6 == answer[5].Answer:
            count += 1
        else:
            messages.error(request, a6.Question+":"+a6.Answer)
        if q7 == answer[6].Answer:
            count += 1
        else:
            messages.error(request, a7.Question+":"+a7.Answer)
        if q8 == answer[7].Answer:
            count += 1
        else:
            messages.error(request, a8.Question+":"+a8.Answer)
        if q9 == answer[8].Answer:
            count += 1
        else:
            messages.error(request, a9.Question+":"+a9.Answer)
        if q10 == answer[9].Answer:
            count += 1
        else:
            messages.error(request, a10.Question+":"+a10.Answer)

    messages.info(request, count)
    messages.success(request, b-a)
    count = 0
    return render(request,'thank.html')
