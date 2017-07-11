#coding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from send_message.models import User, Message_details
from django import forms
import re
from send_message.task import send
# Create your views here.
def send_message(request):
    if(request.method == 'POST'):
        b = str(request.POST)
        mode = re.compile(r"\'.*?\'")
        strs = mode.findall(b)
        if strs:
            if strs is not None:
                print(strs)
                mode = re.compile(r"/TITLE:.*?\:TITLE/")
                r = mode.findall(strs[1])[0]
                title = r[7:-7]

                mode = re.compile(r"/CONTENTS:.*?\:CONTENTS/")
                r = mode.findall(strs[1])[0]
                contents = r[10:-10]

                mode = re.compile(r"/FILE:.*?\:FILE/")
                r = mode.findall(strs[1])[0]
                file = r[6:-6]

                mode = re.compile(r"/UUID:.*?\:UUID/")
                r = mode.findall(str(strs[1]))[0]
                uuid = r[6:-6]
                title_contents = "//" + uuid + "//" + title + "//" + contents
                if(file):
                    f = open(file, 'r')
                    try:
                        message = f.readlines()
                        tempstr = ""
                        for line in message:
                            tempstr = tempstr + "," + line
                    finally:
                        send_a = "//" + tempstr + title_contents
                        print(send_a)
                        f.close()
                        # send.delay(send_a)
                Message_details.objects.create(message_uuid=uuid, message_title=title, message_content=contents, number_of_receivers="1", number_of_devices="1", number_of_arrival="1")
                print("create done!")
    return render(request, 'send_message/send_message.html')

def about(request):
    return render(request, 'send_message/about.html', {})
def history(request):
    uuid_message = str(request.GET)
    mode = re.compile(r"\'.*?\'")
    r = mode.findall(uuid_message)
    if r:
        result = eval(r[1])
        print(result)
        exist = Message_details.objects.filter(message_uuid=result)
        if exist:
            print("Find! " + Message_details.objects.get(message_uuid=result).message_content)
            b_con = Message_details.objects.get(message_uuid=result).message_content
            b_n_r = Message_details.objects.get(message_uuid=result).number_of_receivers
            b_n_d = Message_details.objects.get(message_uuid=result).number_of_devices
            b_n_a = Message_details.objects.get(message_uuid=result).number_of_arrival
            hr = b_con+"//"+b_n_r+"//"+b_n_d+"//"+b_n_a
            return HttpResponse(hr)
        else:
            print("Not Find!")
            return ()
    return render(request, 'send_message/history.html', {})

#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='UserName ', max_length=100)
    password = forms.CharField(label='PassWord ', widget=forms.PasswordInput())

def login(request):
    if request.method == 'POST':
        # 获取表单用户密码
        a_username = str(request.POST['username'])
        a_password = str(request.POST['password'])
        # 获取的表单数据与数据库进行比较
        user = User.objects.filter(username__exact=a_username, password__exact=a_password)
        if user:
            return HttpResponseRedirect('/send_message.html/')
        else:
            return HttpResponseRedirect('/')
    return render_to_response('send_message/login.html')

#注册
def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        print(str(request.POST))
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username=username, password=password)
            return HttpResponseRedirect('../')
    else:
        uf = UserForm()
    return render_to_response('send_message/register.html', {'uf': uf})
