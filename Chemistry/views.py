from django.shortcuts import render
from .models import ChemistryQuestions
from django.contrib import messages
import datetime
# Create your views here.
a = datetime.datetime.now().replace(microsecond=0)
def chemistry(request):
    global a
    a = datetime.datetime.now().replace(microsecond=0)

    chemistry_question = ChemistryQuestions.objects.all()
    a1 = chemistry_question[0]
    a2 = chemistry_question[1]
    a3 = chemistry_question[2]
    a4 = chemistry_question[3]
    a5 = chemistry_question[4]
    a6 = chemistry_question[5]
    a7 = chemistry_question[6]
    a8 = chemistry_question[7]
    a9 = chemistry_question[8]
    a10 = chemistry_question[9]



    return render(request,'chemistry.html',{'a1':a1 ,'a2':a2,'a3':a3 ,'a4':a4 ,'a5':a5 ,'a6':a6 ,'a7':a7 ,'a8':a8 ,'a9':a9 ,'a10':a10 ,})

def thank(request):
    b = datetime.datetime.now().replace(microsecond=0)
    answer = ChemistryQuestions.objects.all()
    print(answer[0].Answer)

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
        l1=[]
        if q1 == answer[0].Answer:
            count += 1
        else:
            messages.error(request,answer[0].Question+"  Answer:  "+answer[0].Answer )
        if q2 == answer[1].Answer:
            count += 1
        else:
            messages.error(request,answer[1].Question+"  Answer:  "+answer[1].Answer )
        if q3 == answer[2].Answer:
            count += 1
        else:
            messages.error(request,answer[2].Question+"  Answer:  "+answer[2].Answer )

        if q4 == answer[3].Answer:
            count += 1
        else:
            messages.error(request,answer[3].Question+"  Answer:  "+answer[3].Answer )
        if q5 == answer[4].Answer:
            count += 1
        else:
            messages.error(request,answer[4].Question+"  Answer:  "+answer[4].Answer )
        if q6 == answer[5].Answer:
            count += 1
        else:
            messages.error(request,answer[5].Question+"  Answer:  "+answer[5].Answer )
        if q7 == answer[6].Answer:
            count += 1
        else:
            messages.error(request,answer[6].Question+"  Answer:  "+answer[6].Answer )
        if q8 == answer[7].Answer:
            count += 1
        else:
            messages.error(request,answer[7].Question+"  Answer:  "+answer[7].Answer )
        if q9 == answer[8].Answer:
            count += 1
        else:
            messages.error(request,answer[8].Question+"  Answer:  "+answer[8].Answer )
        if q10 == answer[9].Answer:
            count += 1
        else:
            messages.error(request,answer[9].Question+"  Answer:  "+answer[9].Answer )

    messages.info(request, count)
    messages.success(request, b - a)
    count = 0
    return render(request, 'thank.html')