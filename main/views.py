from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Main
from accounts.models import Profile
from django.views.decorators.csrf import csrf_exempt
from firebase import firebase
import json
from django.contrib.auth.models import User

def main_sourcing(request):
    return render(request, 'main/main_view.html')
def readme(request):
    return render(request, 'main/readme.html')
@csrf_exempt # csrf 보안을 사용 하기 않겠다는 의미
def practice_sourcing(request):
    #index =[]
    #indexs = Main.objects.values_list('index')
    #for i in indexs:
    #    index.append(i[0]) # 인덱스만 들어가게
    index = Profile.objects.get(user=request.user)
    index = index.index
    index = int(index)
    qs_links = Main.objects.values_list('direct_links')
    qs_sentences = Main.objects.values_list('before_sentences')
    qs_links = qs_links[index:index+5]## [index:index+5]유저의 index 변수를 받아서 거기서 부터 일을 할 수 있게끔 하장
    qs_sentences = qs_sentences[index:index+5]
    qs_link =[]
    qs_sentence=[]
    for i in qs_links:
        #print(i[0])
        qs_link.append(i[0])
    for i in qs_sentences:
        #print(i[0])
        qs_sentence.append(i[0])
    ##qs_link 가 너무 길어서 ;;;
    short_qs_link =[]
    for i in qs_link:
        i = i[:58]
        #print(i)
        short_qs_link.append(i)

    context = {
        #'links' : qs_link,
        'links' : short_qs_link,
        'sentences' : qs_sentence,
        'indexs' : index
    }
    #print(context)
    return render(request, 'main/practice_sourcing.html',context)
    #return render(request, 'main/practice_sourcing.html',{
    #   'main_list' : qs
    #})

@csrf_exempt # csrf 보안을 사용 하기 않겠다는 의미
def next_sentence(request):
    if request.method =='POST':
        sended = int(request.POST['sended'])#5가 전달## data[index:index+5]한데 부터 다섯개를 보여준다
        #print(sended)
        qs_links = Main.objects.values_list('direct_links')
        qs_sentences = Main.objects.values_list('before_sentences')
        qs_links = qs_links[sended+1:sended+6]
        qs_sentences = qs_sentences[sended+1:sended+6]#@@@@@ 마지막 하나 안되는 거 고치기!
        qs_link =[]
        qs_sentence=[]
        
        for j in qs_links:
            #print(j[0])
            qs_link.append(j[0])
        for j in qs_sentences:
            #print(j[0])
            qs_sentence.append(j[0])
        #context ={}
        #for i in range(len(qs_links)):
        #    context[qs_link[i]] = context[qs_sentence[i]]
        context = {
            'links2' : qs_link,
            'sentences2' : qs_sentence
        }
        #print(context)
    #return redirect({'main_list' : qs})
    #return render(request, 'main/practice_sourcing.html',context)
    return JsonResponse(context)
    #return render(request, 'main/practice_sourcing.html',{
    # 'main_list1' : qs
    #})
    



firebase = firebase.FirebaseApplication('https://lionsourcing-35ea5.firebaseio.com/', None)

@csrf_exempt # csrf 보안을 사용 하기 않겠다는 의미
def send_fb(request):
     if request.method =='POST':
        sended = request.POST['sended_sentence']
        indexing = request.POST['indexing'] # 0,1,2 ~11886 까지 int 값들이 들어옴 -> FB에서 인덱스 문제 발생

        firebase.put('/After_Sentence/',repr(indexing),sended) #파이어베이스에 쏘기// indexing

    
     return HttpResponse()

@csrf_exempt # csrf 보안을 사용 하기 않겠다는 의미
def index_save(request):
     if request.method =='POST':
        #user = super()  #유저 값  얻기
        sended = request.POST['sended']## 어디까지 했느지의 index가 들어옴
        #user = User.objects.get(id=user_id)
        '''
        index = Profile.objects.create( 유저 정보 생성
           user = request.user,
           phone_number = '0202020',
           email = 'fsdf@sdf.com',
           index = sended,
           allocated ='만칠천문장')
        
        index.save()
        '''
        index = Profile.objects.get(user=request.user)
        index.index = sended # title 수정
        index.save()
        context ={
            'data':sended
        }
     return JsonResponse(context)
     #return redirect('main:practice')

