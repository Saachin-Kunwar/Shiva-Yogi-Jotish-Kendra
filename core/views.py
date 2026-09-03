from django.shortcuts import render, redirect
from django.contrib import messages
from programs.models import Program
from blog.models import Post
from .models import GuruProfile
from .forms import BookingForm

def home(request):
    programs = Program.objects.all()[:6]
    recent_posts = Post.objects.all().order_by('-created_at')[:3]
    guru = GuruProfile.objects.first()
    return render(request, 'core/home.html', {
        'programs': programs,
        'recent_posts': recent_posts,
        'guru': guru
    })

def book_consultation(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your consultation has been booked successfully! We will contact you soon.')
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'core/booking.html', {'form': form})

def about(request):
    guru = GuruProfile.objects.first()
    return render(request, 'core/about.html', {'guru': guru})

def contact(request):
    guru = GuruProfile.objects.first()
    return render(request, 'core/contact.html', {'guru': guru})