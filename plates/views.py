
# Create your views here.
#plates/views:

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import NewPlate, PlateContent
from .forms import PostForm, PostForm2

from django.db.models import Max
#import uuid
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse


# Create basic views:
def home_page(request):
    return render(request, 'homepage.html', {})

def longplay_page(request):
    return render(request, 'longplaypage.html', {})

def soloplay_page(request):
    return render(request, 'soloplaypage.html', {})

def liveplay_page(request):
    return render(request, 'liveplaypage.html', {})

def chat_page(request):
    return render(request, 'chatpage.html', {})

def help_page(request):
    return render(request, 'helppage.html', {})


#inserting in new row for fields: id, title, theme, subtheme
def create_plates(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            #pass_key = uuid.uuid4()
            #post.plate_uuid = pass_key

            #post.room = 1
            post.created_date= timezone.now()
            post.plate_complete = False
            post.owner = request.user

            post.save()
            #Post.id is 'NULL' until the instance is created? This is not elegant
            post.room = post.id
            post.save()
        #2nd Form - getting storytext
            form2 = PostForm2(request.POST)

            #This text is used to describe the room:
            if form2.is_valid():
                post2 = form2.save(commit=False)
                #assign the current id ('Newplate') to detail model('PlateContect')
                #Need to directly link it with 'objects.get' as direct assignment wont work
                pk = post.id
                b = NewPlate.objects.get(id=pk).id
                post2.plate_id= NewPlate.objects.get(id=b)

                post2.published_date= timezone.now()
                post2.Plate_position = 1
                post2.save()

            return redirect('plates:draft_plates_title_show')
  								#draft_plates_title_show
    else:
        form = PostForm()
        form2 = PostForm2()
        context = {'form': form,'form2': form2}
        return render(request, 'create_plates.html', context)


def draft_plates_title_show(request):
    newplate = NewPlate.objects.filter(created_date__lte=timezone.now(), plate_complete__in=[False]).order_by(
        'created_date')
    context = {'newplate': newplate}
    return render(request, 'draft_plates_title_show.html', context)


def draft_plates_content_show(request, pk):
    mod = NewPlate.objects.all()
    newplate = get_object_or_404(mod, pk=pk)
    platecontent = PlateContent.objects.filter(plate_id=pk)
    context = {'newplate': newplate, 'platecontent': platecontent}
    return render(request, 'draft_plates_content_show.html', context)


def draft_plates_add_text(request, pk):
    # print out the last plate - to help with editing:
    maxy = PlateContent.objects.filter(plate_id=pk).aggregate(Max('Plate_position'))

    if request.method == "POST":
        form2 = PostForm2(request.POST)

        if form2.is_valid():
            post2 = form2.save(commit=False)

            b = NewPlate.objects.get(id=pk)
            post2.plate_id = b
            post2.published_date = timezone.now()
            post2.Plate_position = maxy.get('Plate_position__max') + 1
            post2.save()

            return HttpResponseRedirect(reverse('plates:draft_plates_content_show', args=[pk]))

    else:
        lasttext = PlateContent.objects.filter(plate_id=pk, Plate_position=maxy.get('Plate_position__max'))
        form2 = PostForm2()
        return render(request, 'draft_plates_add_text.html', {'lasttext': lasttext, 'form2': form2})


def draft_plates_publish(request, pk):
    newplate = get_object_or_404(NewPlate, pk=pk)
    if request.method == "POST":
        newplate.plate_complete = True
        newplate.save()

        newplate = NewPlate.objects.filter(created_date__lte=timezone.now(), plate_complete__in=[True]).order_by(
            'created_date')
        context = {'newplate': newplate}
        return render(request, 'draft_plates_title_show.html', context)

    context = {}
    return render(request, 'draft_plates_publish.html', context)


def final_plates_title_show(request):
    newplate = NewPlate.objects.filter(created_date__lte=timezone.now(), plate_complete__in=[True]).order_by(
        'created_date')
    context = {'newplate': newplate}
    return render(request, 'final_plates_title_show.html', context)


def final_plates_content_show(request, pk):
    mod = NewPlate.objects.all()
    newplate = get_object_or_404(mod, pk=pk)
    platecontent = PlateContent.objects.filter(plate_id=pk)
    context = {'newplate': newplate, 'platecontent': platecontent}
    return render(request, 'final_plates_content_show.html', context)


