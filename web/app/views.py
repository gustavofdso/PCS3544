from django.shortcuts import redirect
from django.views.generic import TemplateView

from app.forms import CommentForm
from app.models import Comment


class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self):
        return {
            'queryset': Comment.objects.all(),
            'form': CommentForm()
        }

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid(): form.save()
        return redirect('index')