# Utilities
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Views
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Model
from .models import Task


class ListTasks(LoginRequiredMixin, ListView):
    """ A view that displays the list of tasks."""
    model = Task
    context_object_name = 'task_list' # overrides the default context object name (object_list)

    def get_context_data(self, **kwargs):
        """ Overrides the method inherited from the FormMixin to add various filters to the QuerySet """
        context_data = super().get_context_data(**kwargs)

        # Display only the tasks created by the user
        context_data['task_list'] = context_data['task_list'].filter(user=self.request.user)

        # Count the number of tasks that have yet to be completed
        context_data['count'] = context_data['task_list'].filter(is_completed=False).count()

        # Search for tasks based on their prefix (case-insensitive)
        search_text = self.request.GET.get("search-text") or ""

        if search_text:
            context_data['task_list'] = context_data['task_list'].filter(title__icontains=search_text)
        
        context_data['search_text'] = search_text # Outputs the search content to display it on the page

        return context_data

class AddTask(LoginRequiredMixin, CreateView):
    """A view that displays a form for creating a task."""
    model = Task
    context_object_name = 'task' # overrides the default context object name (object)
    fields = ['title', 'description', 'is_important', 'is_completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form): 
        """ Overrides the method to ensure the user is set when a task is created. """
        form.instance.user = self.request.user

        return super(AddTask, self).form_valid(form)

class EditTask(LoginRequiredMixin, UpdateView):
    """A view that displays a form for editing a task."""
    model = Task
    context_object_name = 'task'
    fields = ['title', 'description', 'is_important', 'is_completed']
    success_url = reverse_lazy('tasks')

class DeleteTask(DeleteView):
    """ A view that displays a confirmation page and deletes an existing list item."""
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')





