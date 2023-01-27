from django.shortcuts import render, redirect
from markdown import Markdown
from django.http import HttpResponse
import random as mucholoco # It seems we cant use random as the name because of some conflicts

from . import util


def index(request):
    return render(request, 'encyclopedia/index.html', {
        "entries": util.list_entries()
    })




def wiki(request, entry):
    """
    This part is still wrong, I can access the CSS.md entry by /wiki/CSS but not /wiki/css
    """
    if entry not in util.list_entries(): # This part is case sensitive
        return render(request, "encyclopedia/error.html", {
            "message" : "No such entry"
        })

    content = util.get_entry(entry)

    return render(request, "encyclopedia/wiki.html", {
        "title": entry,
        "content": Markdown().convert(content)
        })


def search(request):
    entry = request.POST['q']
    entries = util.list_entries()
    if entry in entries:
        return redirect('wiki', entry=entry) # This part is case sensitive
    else:
        results = []
        for i in entries:
            if entry.lower() in i.lower():
                results.append(i)
        return render(request, 'encyclopedia/search.html', {
            "results": results
            })

def new(request):
    if request.method == 'GET':
        context = {
            'foo'   : ['b', 'a', 'r']
        }
        return render(request, 'encyclopedia/new_page.html', context)
    
    else:
        title = request.POST['title']
        content = request.POST['content']
        instance = util.get_entry(title)
        if instance is not None:
            return HttpResponse('error')
        else:
            util.save_entry(title, content)
            # return render(request, "encyclopedia/wiki.html", {
            #     "title": title,
            #     "content": Markdown().convert(content)
            # })
            return redirect('wiki', entry=title)

def edit(request):
    if request.method == 'GET':
        context = {
            'message' : 'No such entry to edit'
        }
        return render(request, 'encyclopedia/error.html', context)
    else:
        # Show form to edit entry (populated)
        title = request.POST['title']
        content = util.get_entry(title)
        context = {
            'title'  : title,
            'content': content
        }
        return render(request, 'encyclopedia/edit_page.html', context)


def save(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        # return render(request, "encyclopedia/wiki.html", {
        #     "title": title,
        #     "content": Markdown().convert(content)
        # })
        return redirect('wiki', entry=title)

    else: 
        context = {
            'message' : 'No such entry to save'
        }
        return render(request, 'encyclopedia/error.html', context)        

def random(request):
    entries = util.list_entries()
    randomized = mucholoco.choice(entries)
    return redirect('wiki', entry=randomized)