from django.shortcuts import render
from .models import MathsQuestions
from django.contrib import messages
import datetime
# Create your views here.
a = datetime.datetime.now().replace(microsecond=0)
def maths(request):
    global a
    a = datetime.datetime.now().replace(microsecond=0)

    maths_questions = MathsQuestions.objects.all()
    a1 = maths_questions[0]
    a2 = maths_questions[1]
    '''a3 = maths_questions[2]
    a4 = maths_questions[3]
    a5 = maths_questions[4]
    a6 = maths_questions[5]
    a7 = maths_questions[6]
    a8 = maths_questions[7]
    a9 = maths_questions[8]
    a10 = maths_questions[9]'''

    return render(request,'maths.html',{'a1': a1 , 'a2': a2})

def thank(request):
    b = datetime.datetime.now().replace(microsecond=0)

    answer = MathsQuestions.objects.all()
    print(answer[0].Answer)

    count=0
    if request.method == "POST":
        q1 = request.POST['qno1']
        q2 = request.POST['qno2']
        if q1 == answer[0].Answer:
            count+=1
        if q2 == answer[1].Answer:
            count+=1

    messages.info(request, count)
    messages.success(request, b - a)
    count = 0
    return render(request,'thank.html')
