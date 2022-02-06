"""
call all serializers for easy global calling
so we use : from .serializer import YourSerializer
better than using : from .serializer.YourFileName import YourSerializer
"""
from .todo import ToDoListSerializer
