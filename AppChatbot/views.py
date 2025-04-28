from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User_Details,Admin_Details,Hospital_Details,Doctor_Details,Training_Data
from django.contrib.sessions.models import Session
import datetime
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Avg, Max, Min, Sum, Count

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from django.db.models import Q



def home(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'home.html', {})


def Admin_login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        
        if Admin_Details.objects.filter(Username=Username, Password=password).exists():
                user = Admin_Details.objects.get(Username=Username, Password=password)
                request.session['type_id'] = 'Admin'
                request.session['login'] = 'Yes'
                return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/Admin_login/')
    else:
        return render(request, 'Admin_login.html', {})


def User_login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        
        if User_Details.objects.filter(Username=Username, Password=password).exists():
                user = User_Details.objects.get(Username=Username, Password=password)
                request.session['customer_id'] = str(user.id)
                request.session['type_id'] = 'User'
                request.session['login'] = 'Yes'
                return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/User_login/')

    else:
        return render(request, 'User_login.html', {})


def Register(request):
    if request.method == 'POST':           
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        Username = request.POST['Username']
        Dob = request.POST['Dob']
        Gender = request.POST['Gender']
        Phone = request.POST['Phone']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Address1 = request.POST['Address1']
        Address2 = request.POST['Address2']
        City = request.POST['City']
        State = request.POST['State']
        final_address = Address1+ " " + Address2
        register = User_Details( First_name=First_name, Last_name=Last_name, Dob=Dob, Gender=Gender ,Phone= Phone,Email= Email,Username= Username,Password=Password,Address=final_address,City=City,State=State)
        register.save()
        messages.info(request,'User Register Successfully')
        return redirect('/User_login/')
    else:
        return render(request, 'Register.html', {})



def logout(request):
    Session.objects.all().delete()
    messages.info(request,'Account logout')
    return redirect('/')



def ManageHospital(request):
    if request.method == 'POST':             
        AmbulanceService = request.POST['AmbulanceService']
        BloodBank = request.POST['BloodBank']
        EmergencyContact = request.POST['EmergencyContact']
        Contact = request.POST['Contact']
        Address = request.POST['Address']
        Name = request.POST['Name']
        MHospital = Hospital_Details( Name=Name, Address=Address, Contact=Contact, EmergencyContact=EmergencyContact ,BloodBank= BloodBank,AmbulanceService= AmbulanceService)
        MHospital.save()
        messages.info(request,'Hospital Details Added Successfully')
        return redirect('/ManageHospital/')
    else:
        Hospital = Hospital_Details.objects.all()
        return render(request, 'ManageHospital.html', {'Hospital':Hospital})


def ManageDoctor(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Gender = request.POST['Gender']
        Address = request.POST['Address']
        Phone = request.POST['Phone']
        Email = request.POST['Email']
        City = request.POST['City']
        Speciality = request.POST['Speciality']
        MDoctor = Doctor_Details( Name=Name, Gender=Gender, Address=Address, Phone=Phone ,Email= Email,City= City,Speciality= Speciality)
        MDoctor.save()
        messages.info(request,'Doctor Details Added Successfully')         
        return redirect('/ManageDoctor/')
    else:
        Doctor = Doctor_Details.objects.all()
        return render(request, 'ManageDoctor.html', {'Doctor':Doctor})

def ViewUser(request):
    if request.method == 'POST':             
        return redirect('/ViewUser/')
    else:
        Users = User_Details.objects.all()
        return render(request, 'ViewUser.html', {'Users':Users})


def HospitalDetails(request):
    if request.method == 'POST':             
        return redirect('/HospitalDetails/')
    else:
        Hospital = Hospital_Details.objects.all()
        return render(request, 'HospitalDetails.html', {'Hospital':Hospital})



def DoctorDetails(request):
    if request.method == 'POST':             
        return redirect('/HospitalDetails/')
    else:
        Doctor = Doctor_Details.objects.all()
        return render(request, 'DoctorDetails.html', {'Doctor':Doctor})
                                                                                                   
                                                                                                                                                        
                                                                                                                                                                  

def Chatpage(request):
    if request.method == 'POST':        
        return redirect('/Chatpage/')
    else:
        return render(request, 'Chatpage.html', {})       
        '''
        print(len(Stopwords))
        chatbot = ChatBot("Hello")
        conversation = [
            "",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "That is good to hear",
            "Thank you.",
            "You're welcome."
        ]

        trainer = ListTrainer(chatbot)

        trainer.train(conversation)
        response = chatbot.get_response("what is 1 + 1")
        print(response)'''
        


def Chatreply(request):
    Training_Data.objects.all().update(Score=0)    
    inputtext = request.POST.get('text')
    print(inputtext)
    example_sent = inputtext 
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(example_sent) 
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    filtered_sentence = [] 
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
    print(word_tokens) 
    print(filtered_sentence) 
    score = 0
    for x in filtered_sentence:
        keyword = x
        keyword = str(keyword)
        print('keyword',keyword)
        if Training_Data.objects.filter(MainKeyword=keyword).exists():
            print("enter")
            score = 0;            
            Cnt = Training_Data.objects.filter(MainKeyword=keyword).count()
            print('count',Cnt)
            if Cnt > 1:
                doc = Training_Data.objects.all().filter(MainKeyword=keyword) 
                i = 0
                while i < int(Cnt):
                    print(doc[i].id)
                    TrainData = Training_Data.objects.all().filter(id=doc[i].id)
                    score += 2
                    for y in filtered_sentence:
                        
                        if y.lower() == TrainData[0].Helping1.lower():
                            score +=1
                            print("enter")

                        if y.lower() == TrainData[0].Helping2.lower():
                            score +=1
                            print("enter")

                        if y.lower() == TrainData[0].Helping3.lower():
                            score +=1
                            print("enter")

                        if y.lower() == TrainData[0].Helping4.lower():
                            score +=1
                            print("enter")
                            
                    print("Score",score)
                    Training_Data.objects.filter(id=TrainData[0].id).update(Score=score)
                    score = 0
                    i += 1
            else:
                TrainData = Training_Data.objects.all().filter(MainKeyword=keyword)
                score += 2
                for y in filtered_sentence:
                    
                    if y.lower() == TrainData[0].Helping1.lower():
                        score +=1
                        print("enter")

                    if y.lower() == TrainData[0].Helping2.lower():
                        score +=1
                        print("enter")

                    if y.lower() == TrainData[0].Helping3.lower():
                        score +=1
                        print("enter")

                    if y.lower() == TrainData[0].Helping4.lower():
                        score +=1
                        print("enter")
                        
                print("Score",score)
                Training_Data.objects.filter(id=TrainData[0].id).update(Score=score)

    maxscore = Training_Data.objects.aggregate(Max('Score'))
    print("Max Score:", maxscore)
    
    # Extract the correct value from the aggregation
    scr = maxscore.get('Score__max')
    
    if scr is not None and isinstance(scr, (int, float)):  # Ensure scr is numeric
        if scr > 0:
            data = Training_Data.objects.filter(Score=scr)
            answer = data[0].Output
            print("Answer : ", data[0].Output)
        else:
            answer = "not found"
    else:
        print("not found")
        answer = "not found"

    data = {
        'respond': answer
    }
    return JsonResponse(data)


def TrainingData(request):
    if request.method == 'POST':  
        MainKeyword = request.POST['MainKeyword']
        Helpingkeyword1 = request.POST['Helpingkeyword1']
        Helpingkeyword2 = request.POST['Helpingkeyword2']
        Helpingkeyword3 = request.POST['Helpingkeyword3']
        Helpingkeyword4 = request.POST['Helpingkeyword4']   
        Output = request.POST['Output']   

         
        register = Training_Data(MainKeyword=MainKeyword,Helping1=Helpingkeyword1,Helping2=Helpingkeyword2,Helping3=Helpingkeyword3,Helping4=Helpingkeyword4,Output=Output,Score="0")
        register.save()     
        messages.info(request,'Data Added Successfully') 
        return redirect('/TrainingData/')
    else:
        Doctor = Doctor_Details.objects.all()
        return render(request, 'TrainingData.html', {'Doctor':Doctor})