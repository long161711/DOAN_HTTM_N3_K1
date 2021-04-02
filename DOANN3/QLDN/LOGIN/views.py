from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
import requests, random
import xlrd
import smtplib
from datetime import datetime

import numpy as np
from . import cacham
from .form import contact_Form
from .models import Wdudoan, dulieudauvao, API, thingspeaks, theongay, dudoanngay
# Create your views here.
from django.views import View

class logins(View):
    def get(self, request):
        # cf =contact_Form
        # return render(request, 'LOGIN/login.html', {'cf': cf})
        return render(request, 'LOGIN/login.html')
    def post(self, request):
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            try:
                my_user = authenticate(username=User.objects.get(email=email), password=password)
            except:
                my_user = authenticate(username=email, password=password)

            if my_user is None:
                return render(request, 'LOGIN/login.html')
            login(request, my_user)
            return render(request, 'LOGIN/trangchu.html')
        #     cf = user.objects.all()
        #     for item in cf:
        #         if item.email == email:
        #             if item.password == password:
        #                 # return HttpResponse("hay qua")
        #                 return render(request, 'LOGIN/trangchu.html')
        #     return render(request, 'LOGIN/login.html')
        #     # cf = contact_Form(request.POST)
        #     # if cf.is_valid():
        #     #     # savecf=user(email = cf.cleaned_data['email'],
        #     #     #             password =cf.cleaned_data['password'])
        #     #     # savecf.save()
        #     #     cf.save()
        #     #     return HttpResponse("ngon")
        # else:
        #     return render(request, 'LOGIN/login.html')
# class login1(View):
#     def get(self, request):
#         cf = user.objects.all()
#         return render(request, 'LOGIN/HOME.html', {'cf': cf})

class trangchu(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'LOGIN/trangchu.html')

class table(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        cf = dulieudauvao.objects.all()

        contex = {"cf": cf}

        return render(request, 'LOGIN/table.html', contex)
class file(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'LOGIN/bieudo.html')
    def post(self, request):
        if request.method == "POST":
            file= request.POST['tenfile']
            dulieudauvao.objects.all().delete()
            # dulieu.thoigian = 100
            # dulieu.nhietdo = 4
            # dulieu.doam = 10
            # dulieu.luongnuoc =110
            # dulieu.save()
            # file_location = file
            diem1 = "2020-12-15 6:00:00"
            diem11 = datetime.strptime(diem1, "%Y-%m-%d %H:%M:%S")
            diem12 = 0

            diem2 = "2020-12-15 8:00:00"
            diem21 = datetime.strptime(diem2, "%Y-%m-%d %H:%M:%S")
            diem22 = 2

            diem3 = "2020-12-15 10:00:00"
            diem31 = datetime.strptime(diem3, "%Y-%m-%d %H:%M:%S")
            diem32 = 1

            diem4 = "2020-12-15 13:00:00"
            diem41 = datetime.strptime(diem4, "%Y-%m-%d %H:%M:%S")
            diem42 = 3

            diem5 = "2020-12-15 17:00:00"
            diem51 = datetime.strptime(diem5, "%Y-%m-%d %H:%M:%S")
            diem52 = 1

            diem6 = "2020-12-15 20:00:00"
            diem61 = datetime.strptime(diem6, "%Y-%m-%d %H:%M:%S")
            diem62 = 4

            diem7 = "2020-12-15 22:00:00"
            diem71 = datetime.strptime(diem7, "%Y-%m-%d %H:%M:%S")
            diem72 = 2

            diem82 = 1

            wb = xlrd.open_workbook(file)
            sheet = wb.sheet_by_index(0)
            n = sheet.nrows
            m = sheet.ncols - 2
            n1 = sheet.nrows
            m1 = sheet.ncols - 5
            lamda = 0.05
            # print(sheet.nrows)
            # print(sheet.ncols)
            # print(sheet.ncols)
            # return HttpResponse(sheet.cell_value(3, 1))
            matrixA = np.zeros((n, m))
            matrixB = np.zeros((n1, m1))
            for x in range(1, sheet.nrows, 1):
                # dulieu = dulieudauvao()
                # dulieu.thoigian = sheet.cell_value(x, 0)
                for y in range(2, sheet.ncols, 1):
                    if y == sheet.ncols-1:
                        # dulieu.luongnuoc = sheet.cell_value(x, y)
                        matrixB[x-1][0] = sheet.cell_value(x, y)
                    else:
                        # if y == 1:
                        #     dulieu.nhietdo = sheet.cell_value(x, y)
                        # if y == 2:
                        #     dulieu.doam = sheet.cell_value(x, y)
                        # if y == 3:
                        #     dulieu.songuoi = sheet.cell_value(x, y)
                        matrixA[x-1][y - 2] = sheet.cell_value(x, y)
                # dulieu.save()
            for x in range(1, sheet.nrows, 1):
                tg = sheet.cell_value(x, 0)
                td = ""
                for k in range(0, 19, 1):
                    # if x == 1:
                    #     tg1 += tg[k]
                    td += tg[k]
                td1 = datetime.strptime(td, "%Y-%m-%d %H:%M:%S")
                for qwe in range(1,2,1):
                    if td1.time() <= diem11.time() :
                        matrixA[x-1][3] = diem12
                        break
                    if td1.time()<= diem21.time():
                        matrixA[x-1][3] = diem22
                        break
                    if td1.time()<= diem31.time():
                        matrixA[x-1][3] = diem32
                        break
                    if td1.time()<= diem41.time():
                        matrixA[x-1][3] = diem42
                        break
                    if td1.time()<= diem51.time():
                        matrixA[x-1][3] = diem52
                        break
                    if td1.time()<= diem61.time():
                        matrixA[x-1][3] = diem62
                        break
                    if td1.time()<= diem71.time():
                        matrixA[x-1][3] = diem72
                        break
                    if td1.time() > diem71.time():
                        matrixA[x-1][3] = diem82
                        break

            matrixACV = np.zeros((m, n))
            cacham.chuyenvi(matrixA, n, m, matrixACV)

            matrixBCV = np.zeros((m1, n1))
            cacham.chuyenvi(matrixB, n1, m1, matrixBCV)

            matrixBCV_A = np.zeros((m1, m))
            cacham.nhan2matran(matrixBCV, matrixA, matrixBCV_A, m1, n1, m)

            matrixACV_A = np.zeros((m, m))
            cacham.nhan2matran(matrixACV, matrixA, matrixACV_A, m, n, m)

            for q in range(0, m, 1):
                matrixACV_A[q][q] = matrixACV_A[q][q] + lamda
            d = cacham.tinhdetmatran(matrixACV_A, m)

            cacham.matranphuhop(matrixACV_A, m)

            cacham.matrankhanghic(matrixACV_A, m, d)

            matrixW = np.zeros((m1, m))
            cacham.nhan2matran(matrixBCV_A, matrixACV_A, matrixW, m1, m, m)
            # return HttpResponse(matrixW)
            # for i in range(0, m1, 1):
            #     for j in range(0, n, 1):
            #         dulieuhm = dulieudauvao()
            #         sum = 0
            #         for k in range(0, m, 1):
            #             sum = (float(matrixW[i][k]) * float(matrixACV[k][j])) + sum
            #         dulieuhm.luongnuocdudoan = sum
            #         dulieuhm.save()
            q = 0
            # tg1 =""
            for x in range(1, sheet.nrows, 1):
                dulieu = dulieudauvao()
                tg = sheet.cell_value(x, 0)
                td = ""
                for k in range(0, 19, 1):
                    # if x == 1:
                    #     tg1 += tg[k]
                    td += tg[k]
                dulieu.thoigian = td
                td1 = datetime.strptime(td, "%Y-%m-%d %H:%M:%S")
                for qwe in range(1,2,1):
                    if td1.time() <= diem11.time():
                        dulieu.khoangtg = diem12
                        break
                    if td1.time()<= diem21.time():
                        dulieu.khoangtg = diem22
                        break
                    if td1.time()<= diem31.time():
                        dulieu.khoangtg = diem32
                        break
                    if td1.time()<= diem41.time():
                        dulieu.khoangtg = diem42
                        break
                    if td1.time()<= diem51.time():
                        dulieu.khoangtg = diem52
                        break
                    if td1.time()<= diem61.time():
                        dulieu.khoangtg = diem62
                        break
                    if td1.time()<= diem71.time():
                        dulieu.khoangtg = diem72
                        break
                    if td1.time() > diem71.time():
                        dulieu.khoangtg = diem82
                        break
                for y in range(2, sheet.ncols, 1):
                    if y == sheet.ncols - 1:
                        dulieu.luongnuoc = sheet.cell_value(x, y)
                    else:
                        if y == 2:
                            dulieu.nhietdo = sheet.cell_value(x, y)
                        if y == 3:
                            dulieu.doam = sheet.cell_value(x, y)
                        if y == 4:
                            dulieu.songuoi = sheet.cell_value(x, y)
                sum = 0
                for k in range(0, m, 1):
                    sum += (float(matrixW[0][k]) * float(matrixA[q][k]))
                dulieu.luongnuocdudoan = sum
                dulieu.save()
                q = q+1



            # tgthu = "2020-12-17 5:50:00"
            # tgthu1 = datetime.strptime(tgthu, "%Y-%m-%d %H:%M:%S")
            # dt_object1 = datetime.strptime(tg1, "%Y-%m-%d %H:%M:%S")
            # if tgthu1 < dt_object1:
            #     print(tg1)
            # print(tgthu)
            # print(tg1)
            p = Wdudoan.objects.all()
            for lon in p:
                if lon.email == request.user.email :
                    lon.delete()
            print(matrixW)
            wdudoan = Wdudoan()
            wdudoan.email = request.user.email
            print()
            for w in range(0, m, 1):
                if w == 0:
                    wdudoan.wnhietdo=matrixW[0][w]
                if w == 1:
                    wdudoan.wdoam = matrixW[0][w]
                if w == 2:
                    wdudoan.wsonguoi = matrixW[0][w]
                if w == 3:
                    wdudoan.wkhoangtg= matrixW[0][w]
            wdudoan.save()
            return render(request, 'LOGIN/bieudo.html')
        else:
            return HttpResponse("me may")



# def get_data(request, *args, **kwargs):
#     data = {
#         "sales": 100,
#         "customers": 10,
#     }
#     return JsonResponse(data)
class thingspeak(LoginRequiredMixin,View):
    login_url = '/login/'

    def get (self, request):
        # url1 = 'https://api.thingspeak.com/channels/1261095/feeds.json?units=metric&api_key=Z41XMSV1FZZOE5KU&start=2020-12-16'
        url ="https://api.thingspeak.com/channels/1261095/feeds.json?units=metric&api_key=Z41XMSV1FZZOE5KU&start=2020-12-16"
        json_data = requests.get(url).json()
        print("lolol")
        print(json_data)
        print("lolol")
        thingspeaks.objects.all().delete()
        diem1 = "2020-12-15 6:00:00"
        diem11 = datetime.strptime(diem1, "%Y-%m-%d %H:%M:%S")
        diem12 = 0

        diem2 = "2020-12-15 8:00:00"
        diem21 = datetime.strptime(diem2, "%Y-%m-%d %H:%M:%S")
        diem22 = 2

        diem3 = "2020-12-15 10:00:00"
        diem31 = datetime.strptime(diem3, "%Y-%m-%d %H:%M:%S")
        diem32 = 1

        diem4 = "2020-12-15 13:00:00"
        diem41 = datetime.strptime(diem4, "%Y-%m-%d %H:%M:%S")
        diem42 = 3

        diem5 = "2020-12-15 17:00:00"
        diem51 = datetime.strptime(diem5, "%Y-%m-%d %H:%M:%S")
        diem52 = 1

        diem6 = "2020-12-15 20:00:00"
        diem61 = datetime.strptime(diem6, "%Y-%m-%d %H:%M:%S")
        diem62 = 4

        diem7 = "2020-12-15 22:00:00"
        diem71 = datetime.strptime(diem7, "%Y-%m-%d %H:%M:%S")
        diem72 = 2

        diem82 = 1
        n = len(json_data['feeds'])
        n1 =len(json_data['feeds'])
        m = 4
        m1 = 1
        lamda = 0.8

        matrixA = np.zeros((n, m))
        matrixB = np.zeros((n1, m1))
        for x in range(0, n, 1):
            y=0
            matrixA[x][y]=json_data['feeds'][x]['field1']
            matrixB[x][y]=json_data['feeds'][x]['field4']
            y=y+1
            matrixA[x][y]=json_data['feeds'][x]['field2']
            y=y+1
            matrixA[x][y]=json_data['feeds'][x]['field3']

        for x in range(0, n, 1):
            tg = json_data['feeds'][x]['created_at']
            td = ""
            for k in range(0, 19, 1):
                if tg[k] == 'T':
                    td += ' '
                else:
                    td += tg[k]
            td1 = datetime.strptime(td, "%Y-%m-%d %H:%M:%S")
            for qwe in range(1, 2, 1):
                if td1.time() <= diem11.time():
                    matrixA[x][3] = diem12
                    break
                if td1.time() <= diem21.time():
                    matrixA[x][3] = diem22
                    break
                if td1.time() <= diem31.time():
                    matrixA[x][3] = diem32
                    break
                if td1.time() <= diem41.time():
                    matrixA[x][3] = diem42
                    break
                if td1.time() <= diem51.time():
                    matrixA[x][3] = diem52
                    break
                if td1.time() <= diem61.time():
                    matrixA[x][3] = diem62
                    break
                if td1.time() <= diem71.time():
                    matrixA[x][3] = diem72
                    break
                if td1.time() > diem71.time():
                    matrixA[x][3] = diem82
                    break

        matrixACV = np.zeros((m, n))
        cacham.chuyenvi(matrixA, n, m, matrixACV)

        matrixBCV = np.zeros((m1, n1))
        cacham.chuyenvi(matrixB, n1, m1, matrixBCV)

        matrixBCV_A = np.zeros((m1, m))
        cacham.nhan2matran(matrixBCV, matrixA, matrixBCV_A, m1, n1, m)

        matrixACV_A = np.zeros((m, m))
        cacham.nhan2matran(matrixACV, matrixA, matrixACV_A, m, n, m)

        for q in range(0, m, 1):
            matrixACV_A[q][q] = matrixACV_A[q][q] + lamda
        d = cacham.tinhdetmatran(matrixACV_A, m)

        cacham.matranphuhop(matrixACV_A, m)

        cacham.matrankhanghic(matrixACV_A, m, d)

        matrixW = np.zeros((m1, m))
        cacham.nhan2matran(matrixBCV_A, matrixACV_A, matrixW, m1, m, m)
        p = Wdudoan.objects.all()
        for lon in p:
            if lon.email == request.user.email:
                lon.delete()
        wdudoan = Wdudoan()
        wdudoan.email = request.user.email
        wdudoan.wnhietdo = matrixW[0][0]
        wdudoan.wdoam = matrixW[0][1]
        wdudoan.wsonguoi = matrixW[0][2]
        wdudoan.wkhoangtg = matrixW[0][3]
        wdudoan.save()
        print(matrixW)
        for n in range(0, len(json_data['feeds']), 1):
            nd = json_data['feeds'][n]['field1']

            da = json_data['feeds'][n]['field2']

            sn = json_data['feeds'][n]['field3']

            ln = json_data['feeds'][n]['field4']

            tg = json_data['feeds'][n]['created_at']
            b = ''
            for i in range(0, 19, 1):
                if tg[i] == 'T':
                    b += ' '
                else:
                    b += tg[i]
            format = '%Y-%m-%d %H:%M:%S'
            td1 = datetime.strptime(b, format)
            thingspeak1 = thingspeaks()
            thingspeak1.thoigian=b
            thingspeak1.nhietdo = nd
            thingspeak1.doam = da
            thingspeak1.songuoi = sn
            ktg = 0
            for qwe in range(1, 2, 1):
                if td1.time() <= diem11.time():
                    ktg = diem12
                    thingspeak1.khoangtg = diem12
                    break
                if td1.time() <= diem21.time():
                    ktg = diem22
                    thingspeak1.khoangtg = diem22
                    break
                if td1.time() <= diem31.time():
                    ktg = diem32
                    thingspeak1.khoangtg = diem32
                    break
                if td1.time() <= diem41.time():
                    ktg = diem42
                    thingspeak1.khoangtg = diem42
                    break
                if td1.time() <= diem51.time():
                    ktg = diem52
                    thingspeak1.khoangtg = diem52
                    break
                if td1.time() <= diem61.time():
                    ktg = diem62
                    thingspeak1.khoangtg = diem62
                    break
                if td1.time() <= diem71.time():
                    ktg = diem72
                    thingspeak1.khoangtg = diem72
                    break
                if td1.time() > diem71.time():
                    ktg = diem82
                    thingspeak1.khoangtg = diem82
                    break
            sum = float(matrixW[0][0])*float(nd)+float(matrixW[0][1])*float(da)+float(matrixW[0][2])*float(sn)+float(matrixW[0][3])*float(ktg)
            thingspeak1.luongnuoc = ln
            if sum < 0 :
                sum=0
            thingspeak1.luongnuocdudoan = sum
            # print(sum)
            thingspeak1.save()
        return redirect('usermember:hienthi')

class theongays(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        cf = thingspeaks.objects.all()
        n = len(cf)
        k =0
        date1 = '2020-12-16 00:00:00'
        date = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
        luongnuocdo = 0
        luongnuocdudoan =0
        theongay.objects.all().delete()
        for i in cf:
            k=k+1
            if i.thoigian.date() == date.date():
                luongnuocdo += i.luongnuoc
                luongnuocdudoan += i.luongnuocdudoan
            if i.thoigian.date() != date.date():
                theongay1 = theongay()
                theongay1.thoigian = date.date()
                theongay1.luongnuocdodac = luongnuocdo
                theongay1.luongnuocdudoan =luongnuocdudoan
                theongay1.save()
                date = i.thoigian
                luongnuocdo = 0
                luongnuocdudoan = 0
                print("ngu")
            if k==n:
                theongay1 = theongay()
                theongay1.thoigian = date.date()
                theongay1.luongnuocdodac = luongnuocdo
                theongay1.luongnuocdudoan = luongnuocdudoan
                theongay1.save()
            print(i.thoigian.date())
            data = theongay.objects.all()
            contex = {"data": data}
        return render(request, 'LOGIN/bangthingspeak.html',contex)


class dudoanAPI(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        url = "http://api.openweathermap.org/data/2.5/forecast?q=danang&mode=json&units=metric&appid=d21bd0f39d8b2f58200742118e238628"
        json_data = requests.get(url).json()
        dulieu = []
        wdudoan = Wdudoan.objects.all()
        wdd = []
        for w in wdudoan:
            if w.email == request.user.email:
                wdd.append(w.email)
                wdd.append(w.wnhietdo)
                wdd.append(w.wdoam)
                wdd.append(w.wsonguoi)
                wdd.append(w.wkhoangtg)
                break
        if wdd == []:
            return render(request, 'LOGIN/chuacodulieu.html')
        # print(wdd[3])

        diem1 = "2020-12-15 6:00:00"
        diem11 = datetime.strptime(diem1, "%Y-%m-%d %H:%M:%S")
        diem12 = 0

        diem2 = "2020-12-15 8:00:00"
        diem21 = datetime.strptime(diem2, "%Y-%m-%d %H:%M:%S")
        diem22 = 2

        diem3 = "2020-12-15 10:00:00"
        diem31 = datetime.strptime(diem3, "%Y-%m-%d %H:%M:%S")
        diem32 = 1

        diem4 = "2020-12-15 13:00:00"
        diem41 = datetime.strptime(diem4, "%Y-%m-%d %H:%M:%S")
        diem42 = 3

        diem5 = "2020-12-15 17:00:00"
        diem51 = datetime.strptime(diem5, "%Y-%m-%d %H:%M:%S")
        diem52 = 1

        diem6 = "2020-12-15 20:00:00"
        diem61 = datetime.strptime(diem6, "%Y-%m-%d %H:%M:%S")
        diem62 = 4

        diem7 = "2020-12-15 22:00:00"
        diem71 = datetime.strptime(diem7, "%Y-%m-%d %H:%M:%S")
        diem72 = 2

        diem82 = 1

        API.objects.all().delete()

        for x in range(0, 40, 1):
            tg1 = json_data['list'][x]['dt_txt']
            h = tg1[11] + tg1[12]
            h = int(h)
            for i in range(0, 3, 1):
                tg = ''
                for j in range(0, 19, 1):
                    if h < 10:
                        if j == 12:
                            tg += str(h)
                        else:
                            tg += tg1[j]
                    else:
                        h1 = str(h)
                        if j == 11:
                            tg += h1[0]
                        else:
                            if j == 12:
                                tg += h1[1]
                            else:
                                tg += tg1[j]
                print(tg)
                h += 1
                api = API()
                api.thoigian = tg
                td1 = datetime.strptime(tg, "%Y-%m-%d %H:%M:%S")
                ktg = -1
                for qwe in range(1, 2, 1):
                    if td1.time() <= diem11.time():
                        ktg = diem12
                        api.khoangtg = diem12
                        break
                    if td1.time() <= diem21.time():
                        ktg = diem22
                        api.khoangtg = diem22
                        break
                    if td1.time() <= diem31.time():
                        ktg = diem32
                        api.khoangtg = diem32
                        break
                    if td1.time() <= diem41.time():
                        ktg = diem42
                        api.khoangtg = diem42
                        break
                    if td1.time() <= diem51.time():
                        ktg = diem52
                        api.khoangtg = diem52
                        break
                    if td1.time() <= diem61.time():
                        ktg = diem62
                        api.khoangtg = diem62
                        break
                    if td1.time() <= diem71.time():
                        ktg = diem72
                        api.khoangtg = diem72
                        break
                    if td1.time() > diem71.time():
                        ktg = diem82
                        api.khoangtg = diem82
                        break

                api.nhietdo = json_data['list'][x]['main']['temp']
                api.doam = json_data['list'][x]['main']['humidity']
                randoms = random.randrange(1, 9, 1)
                api.songuoi = int(randoms)
                a = json_data['list'][x]['main']['temp']
                b = json_data['list'][x]['main']['humidity']
                lndd = float(a) * wdd[1] + float(b) * wdd[2] + randoms * wdd[3] + float(ktg) * wdd[4]
                if lndd < 0:
                    lndd = 0
                api.luongnuocdudoan = lndd

                api.save()
        data = API.objects.all()

        cf = API.objects.all()
        n = len(cf)
        k = 0
        date = datetime.now()
        luongnuocdudoan = 0
        dudoanngay.objects.all().delete()
        for i in cf:
            k = k + 1
            if i.thoigian.date() == date.date():
                luongnuocdudoan += i.luongnuocdudoan
            if i.thoigian.date() != date.date():
                dudoanngay1 = dudoanngay()
                dudoanngay1.thoigian = date.date()
                dudoanngay1.luongnuocdudoan = luongnuocdudoan
                dudoanngay1.save()
                date = i.thoigian
                luongnuocdo = 0
                luongnuocdudoan = 0
            if k == n:
                dudoanngay1 = dudoanngay()
                dudoanngay1.thoigian = date.date()
                dudoanngay1.luongnuocdudoan = luongnuocdudoan
                dudoanngay1.save()
            data1 = dudoanngay.objects.all()
        cuoi = dudoanngay.objects.all()
        for ngu in cuoi:
            if ngu.luongnuocdudoan > 140:
                email = "long161711@gmail.com"
                pwd = "117161gnol"
                addreas = request.user.email
                msg = "Lượng nước sử dụng ngày " + str(ngu.thoigian) + " theo dự báo sẽ là " + str(
                    ngu.luongnuocdudoan) + "L đã đạt đến mức cao. Mong bạn sử dụng nước tiết kiệm hơn"
                # guoi email
                msa = "luong nuoc su dung ngay "+str(ngu.thoigian)+"theo du bao se la " +str(ngu.luongnuocdudoan)+"L. da dat muc cao mong ban su dung nuoc tiet kiem"
                print(msg)
                client = smtplib.SMTP("smtp.gmail.com", 587)
                client.starttls()
                try:
                    client.login(email, pwd)
                    client.sendmail(email, addreas, msa)
                    all = "guoi thanh cong toi :" + addreas
                    print(all)
                except:
                    print("khong guoi dc")
        return render(request, 'LOGIN/dudoanAPI.html',{ "data": data, "data1":data1 })
        # for x in range(0, 40, 1):
        #     dulieu1 = []
        #     api = API()
        #     tg =json_data['list'][x]['dt_txt']
        #     api.thoigian = tg
        #     td1 = datetime.strptime(tg, "%Y-%m-%d %H:%M:%S")
        #     ktg = -1
        #     for qwe in range(1, 2, 1):
        #         if td1.time() <= diem11.time():
        #             ktg = diem12
        #             api.khoangtg = diem12
        #             break
        #         if td1.time() <= diem21.time():
        #             ktg = diem22
        #             api.khoangtg = diem22
        #             break
        #         if td1.time() <= diem31.time():
        #             ktg = diem32
        #             api.khoangtg = diem32
        #             break
        #         if td1.time() <= diem41.time():
        #             ktg = diem42
        #             api.khoangtg = diem42
        #             break
        #         if td1.time() <= diem51.time():
        #             ktg = diem52
        #             api.khoangtg = diem52
        #             break
        #         if td1.time() <= diem61.time():
        #             ktg = diem62
        #             api.khoangtg = diem62
        #             break
        #         if td1.time() <= diem71.time():
        #             ktg = diem72
        #             api.khoangtg = diem72
        #             break
        #         if td1.time() > diem71.time():
        #             ktg = diem82
        #             api.khoangtg = diem82
        #             break
        #
        #     api.nhietdo = json_data['list'][x]['main']['temp']
        #     api.doam = json_data['list'][x]['main']['humidity']
        #     randoms = random.randrange(1, 9, 1)
        #     api.songuoi= randoms
        #     a = json_data['list'][x]['main']['temp']
        #     b = json_data['list'][x]['main']['humidity']
        #     lndd = float(a)*wdd[1]+float(b)*wdd[2]+randoms*wdd[3]+float(ktg)*wdd[4]
        #     if lndd < 0:
        #         lndd = 0
        #     api.luongnuocdudoan = lndd
        #
        #
        #     api.save()
        #
        #     dulieu1.append(json_data['list'][x]['dt_txt'])
        #     dulieu1.append(json_data['list'][x]['main']['temp'])
        #     dulieu1.append(json_data['list'][x]['main']['humidity'])
        #     dulieu.append(dulieu1)
        # # print(json_data)
        # # print(dulieu)
        # # data = API.objects.all()
        # # contect = {'data': data}
        # return  render(request, 'LOGIN/dudoanAPI.html')
class dudoan(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'LOGIN/dudoan.html')
    def post(self, request):
        if request.method == "POST":
            nhietdo = request.POST['nhietdo']
            doam = request.POST['doam']
            songuoi = request.POST['songuoi']
            wdudoan = Wdudoan.objects.all()
            luongnuoc = 0.1
            for w in wdudoan:
                if w.email == request.user.email:
                    luongnuocda = w.wnhietdo*float(nhietdo) + w.wdoam*float(doam) + w.wsonguoi*float(songuoi)+w.wkhoangtg*float(4)
                    luongnuocthieu =w.wnhietdo*float(nhietdo) + w.wdoam*float(doam) + w.wsonguoi*float(songuoi)
                    a=w.wnhietdo*float(nhietdo) + w.wdoam*float(doam) + w.wsonguoi*float(songuoi)+w.wkhoangtg*float(1)
                    b=w.wnhietdo*float(nhietdo) + w.wdoam*float(doam) + w.wsonguoi*float(songuoi)+w.wkhoangtg*float(2)
                    c=w.wnhietdo*float(nhietdo) + w.wdoam*float(doam) + w.wsonguoi*float(songuoi)+w.wkhoangtg*float(3)
                    luongnuocngay = luongnuocthieu*float(7)+luongnuocda*float(3)+a*float(7)+b*float(4)+c*float(3)
                    if luongnuocda < 0:
                        return render(request, 'LOGIN/luongnuocdudoan.html')
                    if luongnuocthieu < 0:
                        luongnuocthieu = 0
                    if luongnuocngay<0:
                        return render(request, 'LOGIN/luongnuocdudoan.html')
                    contex = {"luongnuocda": luongnuocda,"luongnuocthieu": luongnuocthieu,"luongnuocngay": luongnuocngay, "alo1":nhietdo, "alo2":doam, "alo3":songuoi}
                    return render(request, 'LOGIN/luongnuocdudoan.html', contex)
            print(luongnuoc)
            return render(request, 'LOGIN/chuacodulieu.html')
class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        trucx1 = []
        trucy1 = []
        trucy2 = []
        cf = dulieudauvao.objects.all()
        for item in cf:
            trucx1.append(item.thoigian)
            trucy1.append(item.luongnuoc)
            trucy2.append(item.luongnuocdudoan)
        data = {
            "trucx": trucx1,
            "trucy": trucy1,
            "trucy1": trucy2,
        }
        return Response(data)

class thingspeak1(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        trucx1 = []
        trucy1 = []
        trucy2 = []
        cf = thingspeaks.objects.all()
        for item in cf:
            trucx1.append(item.thoigian)
            trucy1.append(item.luongnuoc)
            trucy2.append(item.luongnuocdudoan)
        data = {
            "trucx": trucx1,
            "trucy": trucy1,
            "trucy1": trucy2,
        }
        return Response(data)

class dataAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        trucx1 = []
        trucy1 = []
        api = API.objects.all()
        for item in api:
            trucx1.append(item.thoigian)
            trucy1.append(item.luongnuocdudoan)
        data = {
            "trucx": trucx1,
            "trucy": trucy1,
        }
        return Response(data)
def logouts(request):
    logout(request)
    return render(request, 'LOGIN/login.html')