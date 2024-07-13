from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import * 
from news.models import News
from django.core.paginator import Paginator
from django.core.mail import send_mail, EmailMultiAlternatives


  
# Create your views here.
# return HttpResponse("world")


def home(request):

    Servicedata = ServiceModel.objects.all()
    Aboutdata = AboutModel.objects.all()
    Clientdata = ClientModel.objects.all()
    Countsdata = Counts.objects.all()
    Testimonialsdata = Testimonials.objects.all()
    Teamdata = Team.objects.all()
    Featuresdata = Features.objects.all()
    Newsdata = News.objects.all()
    portfoliodata = Portfolio.objects.all()
    headerdata = Header.objects.all()
    herodata = Hero.objects.all()
    footerdata = Footer.objects.all()
    socialdata = Social.objects.all()
    
    
    data = {
        'Servicedata': Servicedata,
        'Aboutdata': Aboutdata,
        'Clientdata':Clientdata,
        'Featuresdata':Featuresdata,
        'Testimonialsdata':Testimonialsdata,
        'Teamdata':Teamdata,
        'Countsdata':Countsdata,
        'Newsdata': Newsdata,
        'portfoliodata': portfoliodata,
        'headerdata': headerdata,
        'herodata': herodata,
        'footerdata': footerdata,
        'socialdata': socialdata
    }
    return render(request, "blog/index.html", data)

def innerpage(request):
    return render(request, "blog/inner-page.html")


def port_data(request, pk):
    Servicedata = ServiceModel.objects.all()
    headerdata = Header.objects.all()
    footerdata = Footer.objects.all()
    socialdata = Social.objects.all()
    port_data=Portfolio_details.objects.get(pk=pk)
    #port_data = get_object_or_404(Portfolio_details, pk=pk)
    data = {
        'Servicedata': Servicedata,
        'headerdata': headerdata,
        'port_data': port_data,
        'footerdata': footerdata,
        'socialdata': socialdata

    }
    return render(request, "blog/portfolio-details.html", data)



# def port_data(request):
    # port_data =  Portfolio_details.objects.all()
    # return render(request, "blog/portfolio-details.html", {'port_data': port_data})

# def port_data(request, pk):
    # port_data = Portfolio_details.objects.all()
    # port_data = get_object_or_404(Portfolio_details, pk=pk)
# 
    # data = {
        # 'port_data': port_data
    # }
    # return render(request, "blog/portfolio-details.html",data)

def port(request):
    portfoliodata = Portfolio.objects.all()
    Servicedata = ServiceModel.objects.all()
    headerdata = Header.objects.all()
    footerdata = Footer.objects.all()
    socialdata = Social.objects.all()
    data = {
        'Servicedata': Servicedata,
        'headerdata': headerdata,
        'portfoliodata': portfoliodata,
        'footerdata': footerdata,
        'socialdata': socialdata 
    }
    return render(request, "blog/portfolio.html",data)

def subscribe(request):
    if request.method == "POST":
        
        email = request.POST.get('email')
        if email:
            Subscribe.objects.create(
                email = email
            )
            
    return redirect('/')
    #return render(request, "blog/index.html")


def contact(request):
    Servicedata = ServiceModel.objects.all()
    headerdata = Header.objects.all()
    footerdata = Footer.objects.all()
    socialdata = Social.objects.all()
    
    if request.method == "POST":  # Check if the form is submitted via POST
        name = request.POST.get('name')  # Get the 'name' field from the form
        email = request.POST.get('email')  # Get the 'email' field from the form
        subject = request.POST.get('subject')  # Get the 'subject' field from the form
        msg = request.POST.get('message')  # Get the 'message' field from the form
        
        if name and email and subject and msg:  # Check if all fields are filled
            # Create a new entry in the ContactModel (you need to have this model defined in your models.py)
            ContactModel.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=msg,
            )
            
            # Email subject and message
            email_subject = 'Inquiry Mail'
            email_message = """<html>
                <head>
                <title>Contact</title>
                <style>
                    .mailer-main{
                        border:1px solid green;
                        width:80%;
                        margin: auto;
                        padding: 20px;
                        height:450px;
                    }
                    .hr{
                        width: 100%;
                    }
                </style>
            </head>
            <body>
                <div class="mailer-main">
                    <h1>Patel Tech</h1>
                    <hr class="hr">
                    <div>
                        <h3>Inquiry Confirmed!</h3>
                        <h4>Thank You</h4>
                        <p>
                            We are pleased to have you on our site your query will be looked after soon by us.
                        </p>
                    </div>
                </div>
            </body>
            </html>"""
            from_email = 'popti1617@gmail.com'
            to = [email]
            subject = email_subject
            message = email_message
            email_from = from_email
            recipient_list = to
            send_mail(subject, message, email_from, recipient_list)
        else:
            # Display an error message if any field is missing
            messages.error(request, 'All fields are required!')

    
    data = {
        'Servicedata': Servicedata,
        'headerdata': headerdata,
        'footerdata': footerdata,
        'socialdata': socialdata
    }
    
    # Render the contact.html template
    return render(request, "blog/contact.html", data)



#def contact(request):
#    Servicedata = ServiceModel.objects.all()
#    headerdata = Header.objects.all()
#    footerdata = Footer.objects.all()
#    socialdata = Social.objects.all()
#    if request.method == "POST":  # Check if the form is submitted via POST
#        name = request.POST.get('name')  # Get the 'name' field from the form
#        email = request.POST.get('email')  # Get the 'email' field from the form
#        subject = request.POST.get('subject')  # Get the 'subject' field from the form
#        msg = request.POST.get('message')  # Get the 'message' field from the form
#
#
#        
#        if name and email and subject and msg:  # Check if all fields are filled
#            # Create a new entry in the ContactModel (you need to have this model defined in your models.py)
#            ContactModel.objects.create(
#                name=name,
#                email=email,
#                subject=subject,
#                message=msg,
#            )
#            # Display a success message
#            messages.success(request, "Your inquiry has been successfully submitted!")
#        else:
#            # Display an error message if any field is missing
#            messages.error(request, 'All fields are required!')
#            send_mail(
#            'Subject',
#            'Message',
#            'from@example.com',
#            ['to@example.com'],
#            fail_silently=False,
#        )
#    subject='Inquiry Mail'
#    message = """<html>
#                <head>
#                <title>Booking</title>
#                <style>
#                    .mailer-main{
#                        border:1px solid green;
#                        width:80%;
#                        margin: auto;
#                        padding: 20px;
#                        height:450px;
#                    }
#                    .hr{
#                        width: 100%;
#                    }
#                  
#                  
#                  
#                </style>
#            </head>
#            <body>
#                <div class="mailer-main">
#                    <h1>Sogo Hotel</h1>
#                    <hr class="hr">
#                    <div>
#                        <h3>Booking Confirmed!</h3>
#                        <h4>Thank You</h4>
#                        <p>
#                            We are pleased to inform you that your booking request has been received.
#                        </p>
#                    </div>
#                </div>
#            </body>
#            </html>""",
#    from_email = 'popti1617@gmailcom'
#    to = ['khushipatel161002@gmail.com']
#    msg = EmailMultiAlternatives(subject,message,from_email,to)
#    msg.content_subtype='html'
#    msg.send()
#
#    data = {
#        'Servicedata': Servicedata,
#        'headerdata': headerdata,
#        'footerdata': footerdata,
#        'socialdata': socialdata
#    }
#    # Render the contact.html template
#    return render(request, "blog/contact.html",data)
#


# def contact(request):
    # if request.method == "POST":
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')
        # msg = request.POST.get('message')
        # if name and email and subject and msg:
            # business.Model.objects.create(
                #  name = Name,
                #  email = Email,
                #  subject = Subject,
                #  msg = Message,
            # 
            # )
            # messages.success(request,message="Your inquiry has been successfully submitted!")
        # else:
            # messages.error(request,message='All fields are required!')
# 
    # return render(request,"blog/contact.html")

def calculator(request):
    result = ''
    if request.method == "POST":
        try:
            val1 = float(request.POST.get('val1'))
            operator = request.POST.get('operator')
            val2 = float(request.POST.get('val2'))

            if operator == '+':
                result = val1 + val2
            elif operator == '-':
                result = val1 - val2
            elif operator == '*':
                result = val1 * val2
            elif operator == '/':
                result = val1 / val2
            elif operator == '%':
                result = val1 % val2
            else:
                result = 'Invalid operator'
        except ValueError:
            result = 'Invalid input'

    return render(request, "blog/calculator.html", {'c': result})


def even(request):
    c = ''
    if request.method== "POST":
        num = eval(request.POST.get('num'))
        if num % 2 == 0:
            c = "Even Number"
        else:
            c = "Odd Number"
    return render(request,"blog/even.html", {'c' : c})


def mark(request):
    # t=''
    # p=''
    # c=''
    data={}
    if request.method == "POST":
        s1 = eval(request.POST.get('s1'))
        s2 = eval(request.POST.get('s2'))
        s3 = eval(request.POST.get('s3'))
        s4 = eval(request.POST.get('s4'))
        s5 = eval(request.POST.get('s5'))

        t = s1+s2+s3+s4+s5
        p = t*100/500
        if p >= 90:
            c = "Distinction"
        elif p <90 and p >= 80 :
            c = "Fist Class"
        elif p< 80 and p <=70 :
            c = "Second Class"
        elif p< 70 and p <=45 :
            c = "Third Class"
        elif p< 45 and p <=33 :
            c = "Pass"
        else:
            c = "Fail"
        data = {
            't': t,
            'p': p,
            'c': c
        }

        
    return render(request, "blog/marksheet.html",data)

def services(request):
     Servicedata = ServiceModel.objects.all()
     headerdata = Header.objects.all()
     footerdata = Footer.objects.all()
     socialdata = Social.objects.all()

     paginator = Paginator(Servicedata,2)
     page_num = request.GET.get('page')
     Servicedatafinal = paginator.get_page(page_num)
     last_page = Servicedatafinal.paginator.num_pages
     data = {
         'Servicedata': Servicedatafinal,
         'last_page': last_page,
         'total_page': [n+1 for n in range(last_page)],
         'headerdata': headerdata,
         'footerdata': footerdata,
         'socialdata': socialdata 
     }
     return render(request, "blog/services.html",data)

def news(request,slug):
    Newsdata = News.objects.get(slug = slug)
    Servicedata = ServiceModel.objects.all()
    headerdata = Header.objects.all()
    footerdata = Footer.objects.all()
    socialdata = Social.objects.all()
    data = {
        'Servicedata': Servicedata,
        'headerdata': headerdata,
        'footerdata': footerdata,
        'socialdata': socialdata,
        'Newsdata': Newsdata,
    }


    return render(request, "blog/news.html",data)


def about(request):
     Aboutdata = AboutModel.objects.all()
     Servicedata = ServiceModel.objects.all()
     headerdata = Header.objects.all()
     footerdata = Footer.objects.all()
     socialdata = Social.objects.all()
     data = {
        'Aboutdata': Aboutdata,
        'Servicedata': Servicedata,
        'headerdata': headerdata,
        'footerdata': footerdata,
        'socialdata': socialdata
     }
     return render(request, "blog/about.html",data)

def team(request):
    Teamdata = Team.objects.all()
    Servicedata = ServiceModel.objects.all()
    headerdata = Header.objects.all()
    footerdata = Footer.objects.all()
    socialdata = Social.objects.all()
    data = {
        'Teamdata': Teamdata,
        'Servicedata': Servicedata,
        'headerdata': headerdata,
        'footerdata': footerdata,
        'socialdata': socialdata
    }
    return render(request, "blog/team.html",data)

def footer(request):
    Servicedata = ServiceModel.objects.all()
    headerdata = Header.objects.all()
    footerdata = Footer.objects.all()
    socialdata = Social.objects.all()

    data = {
        'Servicedata': Servicedata,
        'headerdata': headerdata,
        'footerdata': footerdata,
        'socialdata': socialdata
    }

    return render(request, "blog/footer.html",data)

def service_detail(request, slug):
    service = ServiceModel.objects.get(slug = slug)
    Servicedata = ServiceModel.objects.all()
    headerdata = Header.objects.all()
    footerdata = Footer.objects.all()
    socialdata = Social.objects.all()

    data = {
        'service': service,
        'Servicedata': Servicedata,
        'headerdata': headerdata,
        'footerdata': footerdata,
        'socialdata': socialdata

    }
    return render(request, 'blog/service_detail.html', data)
