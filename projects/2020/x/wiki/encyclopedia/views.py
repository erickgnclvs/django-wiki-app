from django.shortcuts import render
from markdown import Markdown

from django.http import Http404

from . import util


def index(request):
    return render(request, 'encyclopedia/index.html', {
        "entries": util.list_entries()
    })

def wiki(request, entry):
    print(entry)
    if entry not in util.list_entries():
        return render(request, "encyclopedia/error.html", {
            "message" : "No such entry"
        })
    content = util.get_entry(entry)
    return render(request, "encyclopedia/wiki.html", {
        "title": entry,
        "content": Markdown().convert(content)
        })

def search(request):
    return render(request, 'encyclopedia/search.html')
    