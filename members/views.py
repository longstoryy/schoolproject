from django.shortcuts import render,redirect,get_object_or_404
from .models import Member,Entry,Pupil
from django.contrib.auth import authenticate, login,logout
from .forms import RegistrationForm
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .forms import MemberForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import TopicForm,EntryForm,ScoreForm







def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context,request))

@login_required
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymembers': mymember
  }
  return HttpResponse(template.render(context, request))

# Create your views here.
@login_required
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def testing(request):
    template=loader.get_template('template.html')
    context ={
        'fruit':['Orange','Pawpaw','Mango','Watermelon','Banana'],
    }
    return HttpResponse(template.render(context,request))

# this are the login and logout 

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')  # Replace 'home' with the URL name of your home page
            
        else:
            # Invalid login credentials, handle appropriately (e.g., show an error message)
            pass

    return render(request, 'registration/login.html')
    
def custom_logout(request):
    logout(request)
    return redirect('custom_login')  # Redirect to the desired page after logout

# registration view

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account was sucessfully created ")

            login(request, user)

            return redirect('main')  # Redirect to the desired page after registration
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class MemberListView(ListView):
    model = Member
    template_name = 'member_list.html'
    context_object_name = 'members'
    
    


class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm
    template_name = 'create_member.html'
    success_url = reverse_lazy('member_list')

class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'update_member.html'
    success_url = reverse_lazy('member_list')

class MemberDeleteView(DeleteView):
    model = Member
    template_name = 'delete_member.html'
    success_url = reverse_lazy('member_list')

def send_email_view(request):
    if request.method == 'POST':
        subject = 'Hello from My Website'
        message = 'Thank you for visiting our website!'
        from_email = 'longstory411@gmail.com'
        recipient_list = ['cephasadjetey1@gmail.com']

        x=send_mail(subject, message, from_email, recipient_list)
        print(x)
        return render(request, 'email_sent.html')  # Display a confirmation page

    return render(request, 'send_email.html')  # Display a form to send email

def topics(request):
    topics =Member.objects.order_by('date_added')
    context={'topics':topics}
    return render(request,'topics.html',context)

def topic(request,topic_id):
    topic = Member.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context={'topic':topic, 'entries': entries}
    return render(request,'topic.html',context)





def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            if form.is_valid():
                form.save()
                return redirect('topics')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'new_topic.html', context)


def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Member.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            if form.is_valid():
                new_entry = form.save(commit=False)
                new_entry.topic = topic
                new_entry.save()
                return redirect('topic', topic_id=topic_id)
    # Display a blank or invalid form.
    context = {'topic': topic,'form': form}
    return render(request, 'new_entry.html', context)

def edit_entry(request,entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form =  EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('topic', topic_id=topic.id)
    # Display a blank or invalid form.
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)






# scores/views.py
from django.shortcuts import render

def score_form(request):
    if request.method == 'POST':
        # Handle form submission
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the results page after submission
            return redirect('score_results')

    else:
        form = ScoreForm()

    return render(request, 'scores/score_form.html', {'form': form})


def score_results(request):
    # Retrieve all pupils from the database
    pupils = Pupil.objects.all()
    
    # Calculate total score and average for each pupil
    for pupil in pupils:
        total = pupil.score_1 + pupil.score_2 + pupil.score_3 + pupil.score_4
        average = total / 4
        pupil.total = total
        pupil.average = average

    # Sort pupils by total score (highest to lowest)
    pupils = sorted(pupils, key=lambda x: x.total, reverse=True)

    # Enumerate the pupils starting from 1
    enumerated_pupils = enumerate(pupils, start=1)

    # Render the template with the sorted and enumerated pupils
    return render(request, 'scores/score_results.html', {'pupils': pupils})

