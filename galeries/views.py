from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from galeries.forms import GalleryForm, PhotoForm
from galeries.models import Gallery


def gallery_details(request, gallery_id):
    gallery = Gallery.objects.get(pk=gallery_id)

    return render(
        request,
        'galleries/details.html',
        {'gallery': gallery}
    )


def galleries_list(request):
    galleries = Gallery.objects.all()
    galleries = [g for g in galleries if g.photos.count() > 0]
    #
    # per_page = request.GET.get('per_page', 3)
    # page_number = request.GET.get('page')
    #
    # paginator = Paginator(galleries, per_page)
    #
    # page_obj = paginator.get_page(page_number)

    return render(
        request,
        'galleries/list.html',
        {'galleries': galleries}
    )


def add_gallery_view(request, gallery_id):
    # if request.method == "GET":
    #     gallery_form = GalleryForm
    # elif request.method == "POST":
    #     gallery_form = GalleryForm(request.POST)
    #     if gallery_form.is_valid():
    #         gallery = gallery_form.save()
    #         return HttpResponseRedirect(reverse("galleries:add_photo", args=[gallery.id]))
    gallery = Gallery.objects.get(pk=gallery_id)
    return render(
        request,
        'galleries/details.html',
        {'gallery': gallery}
    )


def add_photos_view(request, gallery_id):
    gallery = Gallery.objects.get(pk=gallery_id)
    form = PhotoForm()
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.gallery = gallery
            instance.save()
        return HttpResponseRedirect(reverse("galleries:add_photo", args=[gallery_id]))

    return render(
        request,
        'galleries/list.html',
        {'photo_form': form, 'gallery': gallery}
    )
