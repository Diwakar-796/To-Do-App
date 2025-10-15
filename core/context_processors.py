from .models import Category, Task, LEVEL

def default(request):
    tasks = []
    task_done = 0
    categories = Category.objects.all()

    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('-level')
        try:
            task_done = tasks.filter(is_done=True)
        except:
            task_done = 0

    return {
        'tasks': tasks,
        'categories': categories,
        'task_done': task_done,
        'levels': LEVEL,
    }
