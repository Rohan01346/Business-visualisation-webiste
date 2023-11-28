from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as Login
from django.contrib.auth import logout as Logout
from django.contrib.auth.decorators import login_required
from .models import User_Info

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import gspread
import pandas as pd
import csv
import openpyxl
from json import dumps

# Create your views here.

def home(request):
    return render(request , "index.html")

def login(request):
    if(request.method == "POST"):
        login_email=request.POST["login-email"]
        login_password=request.POST["login-password"]

        user = authenticate(username = login_email , password = login_password)

        if(user):
            Login(request, user)
            messages.success(request , "LOGGED IN SUCCESSFULLY!!!")
            return render(request, "dashboard.html" )
            

        else:
            messages.error(request , "WRONG CREDENTIALS!!!")
            return render(request , "login.html")

        
    return render(request , "login.html")

def signup(request):
    if(request.method == "POST"):
       name=request.POST["myName"]
       dob=request.POST["Dob"]
       email=request.POST["signup-email"]
       password=request.POST["signup-password"]
       re_password=request.POST["password"]
       phone=request.POST["phone"]
       company=request.POST["company"]
       designation=request.POST["desigination"]
       industry=request.POST["industry"]
       security_que=request.POST["security-que"]
       business_name=request.POST["business-name"]
       business_goal=request.POST["business-goal"]
       target=request.POST["target"]
       type=request.POST["type"]
       field=request.POST["field"]

       data  = User_Info.objects.all()
       for i in data:
           #print(i.username , email , str(i.username) == email)
           #print()
           if(str(i.name) == email ):
               messages.error(request , "Account Already Exists!!!")
               return render(request , "signup.html")

       myuser = User.objects.create_user(email ,"blank", password )

       user = User_Info(mail = email , password = password , name = name)
       
       user.save()
       myuser.save()
       
       messages.success(request , "ACCOUNT CREATED!!!")

       return redirect("login")
    

    return render(request , "signup.html")

def dashboard(request):
    value = 0

        
    if(request.method == "POST"):

        value = 1
        try:
            file = request.FILES["file"]

            current_user = request.user
            
            data1 = pd.read_excel(file , engine="openpyxl" , sheet_name="sales")
            data2 = pd.read_excel(file , engine="openpyxl" , sheet_name="stock")
            (User_Info.objects.filter(mail = str(current_user))).update(file = file)
            newdata = data1.drop("SKU",axis=1)
            newdata2 = data2.drop(["Alternate Name","SKU"],axis=1)
            # file = "data.csv"
            # data = pd.read_csv("C:\Users\bharg\OneDrive\Desktop\MINOR Local\home\"+file)
            rows1 = []
            rows2 = []
            for index,row in data1.iterrows():
                rows1.append(row)
            for index,row in data2.iterrows():
                rows2.append(row)

        except:
            messages("Upload Again!!!")
            return render(request,"dashboard.html")

        #SALES
        total_sales = list(newdata.sum(axis=0))
        high_sales = newdata.columns[[total_sales.index(max(total_sales))]][0]
        lowest_sales= newdata.columns[[total_sales.index(min(total_sales))]][0]

        newdata_json = newdata.to_json
        data1_json = data1.to_json



        sku_label = []
        month_value = []
        for i in newdata.columns:
            month_value.append(list(newdata[i]))


        month_value_april = list(newdata["April"])

        sku_label = list(data1["SKU"])

        #STOCKS
        col = []
        val = []
        a = []
        for i in newdata2:
            col.append(i)
            for j in range(len(newdata2[i])):
                a.append(newdata2[i][j])
            val.append(a)

        avg =[]
        cost_good_sold =[]
        inventory_turnover = []
        days_inventory =[]
    
        bad_goods = []
        good_goods = []
        for i in range(len(newdata2)):
            avg.append((newdata2.iloc[i][1]+newdata2.iloc[i][7])/2)
            cost_good_sold.append(newdata2.iloc[i][1]+newdata2.iloc[i][3]-newdata2.iloc[i][7])

        for i in range(len(avg)):
            try:
                inventory_turnover.append(cost_good_sold[i]/avg[i])
            except:
                inventory_turnover.append(0)
        
        for i in range(len(avg)):
            if(inventory_turnover[i]<1):
                days_inventory.append(365)
            else:
                days_inventory.append((avg[i]/cost_good_sold[i])*365)

        sku = list(data1["SKU"])
        for i in range(len(days_inventory)):
            avg = sum(days_inventory)/len(days_inventory)
            if(days_inventory[i]>avg):
                bad_goods.append(sku[i])
            else:
                good_goods.append(sku[i])




        #return HttpResponse("he")
        return render(request , "dashboard.html" , {"lowest_sales":lowest_sales, "good_goods":good_goods,"bad_goods":bad_goods ,"sku_label":sku_label ,"month_value_april":month_value_april, "month_value":month_value,"MyData_key2":list(data2.keys()) , "MyData_values2":rows2,"MyData_key1":list(data1.keys()) , "MyData_values1":rows1 , "value":value , "filename":file, "total_sales":total_sales,"data_json":data1_json ,"newdata_json":newdata_json ,"high_sales":high_sales} )
    return render(request , "dashboard.html" ,{"value":value})


def logout(request):
    Logout(request)
    messages.success(request , "LOGOUT SUCCESSFULLY!!!")
    return render(request , "index.html")

def profile(request):
    return render(request , "profile.html")

##########################################################################################################################################
def example(request):

    # current_user = request.user
    # # data  = User_Info.objects.all()

    # # for i in data:
    # #     print(i.name)

    # #############################################  SPREADSHEEET CREATED  ###################################
    # creds = None
    # SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    # if os.path.exists('token.json'): # TOKEN CONTAINS REFRESH TOKEN AND ACCESS TOKEN
    #     creds = Credentials.from_authorized_user_file('token.json' , SCOPES)

    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow  = InstalledAppFlow.from_client_secrets_file('credentials.json' , SCOPES)
    #         creds = flow.run_local_server(port=0)
    #     with open('token.json' , 'w') as token:
    #         token.write(creds.to_json())
    
    # service = build('sheets' , 'v4' , credentials=creds)

    # s = {
    #     'properties':{
    #         'title': str(current_user) + "_SpreadSheeet"
    #     }
    # }
    # spreadsheet = service.spreadsheets().create(body = s , fields = 'spreadsheetId').execute()
    # sid = spreadsheet.get('spreadsheetId')
    # #####################################################################################################




    # ##################################### UPLOAD FILE TO SPREADSHEET ####################################

    # client = gspread.authorize(creds)
    # csv_file = pd.read_csv(User_Info.objects.filter(mail = str(current_user))[0].file)

    # spreadsheet = client.open_by_key(sid)
    # worksheet = spreadsheet.sheet1
    # f = (csv_file, "r")
    # values = [r for r in csv.reader(f)]
    # worksheet.update(values)

    # #####################################################################################################





    # #################################### ACCESS THE SPREADSHEET FROM ID #################################


    # #sheet = service.spreadsheets().get(spreadsheetId = "19rm9TZSw61BMI9fLUVYtcXIv2WwMFRAfjAR2jNcMThY").execute()
    # gc = gspread.authorize(creds)
    # sheet_key_get = gc.open_by_key(sid)
    # sheet = sheet_key_get.sheet1
    # data = sheet.get_all_records()
    # final_data = pd.DataFrame(data)
    # print(final_data)

    # ######################################################################################################

    # return HttpResponse(sid)
    current_user = request.user
    data = pd.read_csv(r"C:\Users\bharg\OneDrive\Desktop\MINOR Local\home\data.csv")
    MyData = {}
    rows = []
    for index,row in data.iterrows():
        rows.append(row)
    # for i in data.items():
    #     a.append(i[0])
    #     b.append(i[1])
    # count=0
    # for i in range(len(a)):
    #     MyData.update({a[i]:b[count]})
    #     count=count+1
    # print((MyData['Country']))
    #return render(request , "example.html" , {'MyData_key':list(data.columns) , 'MyData_value':list(data.values)})
    #return HttpResponse("h1")
    return render(request , "example.html" , {"MyData_key":data.keys() , "MyData_values":rows})
def trys(request):

    return render(request , "example.html")


def forgot(request):

    return render(request , "forgot.html")