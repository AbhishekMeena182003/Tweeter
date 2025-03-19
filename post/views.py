from django.shortcuts import render,HttpResponse
from .models import Tweet
from .forms import Tweetforms,UserRegistrationForm
from django.shortcuts  import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


def Index(request):
    return render (request,"base.html")

def tweet_list(request):
    tweets=Tweet.objects.all()
    return render (request, "tweet_list.html", {"tweets": tweets})

@login_required
def tweet_create(request):
    if request.method=="POST":
        form=Tweetforms(request.POST, request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)

            tweet.user=request.user
            tweet.save()
        
            return redirect("tweet_list")    
    else:
        form=Tweetforms()
    return render(request, "tweetforms.html",{"forms":form})


@login_required
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id, user=request.user)
    if request.method=="POST":
        form=Tweetforms(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        
        form=Tweetforms(instance=tweet)
    return render(request, "tweetforms.html",{"form":form})

@login_required
def tweet_delete(request, tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id, user=request.user)

    if request.method=="POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, "tweetforms_delete.html",{"tweet":tweet})


def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password1'])
      user.save()
      login(request, user)
      return redirect('tweet_list')
  else:
    form = UserRegistrationForm()

  return render(request, 'registration/register.html', {'form': form})



