from django.shortcuts import render, redirect
from .models import Poll
from .forms import CreatePollForm
from django.http import HttpResponse

# Create your views here.

def home(request):
    polls = Poll.objects.all()
    context = {'polls':polls}
    return render(request, 'pollapp/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid(): #To check if there is any information that has been fed into the form
            form.save() #To save the form to the database
            return redirect('home') #To return the user to the homepage
             
    else:
        form = CreatePollForm()
    context = {'form':form}
    return render(request, 'pollapp/create.html', context )

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id) #To query the database for the particular question
                                        #No need to loop over it. Just write poll.question in vote.html
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')
        
        poll.save()   #To save the results into the database

        return redirect('results', poll_id) # To return the user to the results page.
                                            # poll_id bcos the results are specific to a particular poll

    context = {'poll':poll}
    return render(request, 'pollapp/vote.html', context )

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {'poll':poll}
    return render(request, 'pollapp/results.html', context )


