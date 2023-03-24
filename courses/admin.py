from django.contrib import admin
from .models import Course, Module, Lesson, CourseCategory

admin.site.register(CourseCategory)
admin.site.register(Module)
admin.site.register(Lesson)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    '''Admin View for Course'''

    filter_horizontal = ["instructors"]
    list_display = ["title", "category", "_instructors",
                    "_number_of_lessons", "_number_of_enrolled_students", "price", "discounted_price", "updated_at", "created_at"]

    def _instructors(self, obj):
        instructors = obj.instructors.all()
        text = ""
        for instructor in instructors:
            text += instructor.user.get_full_name()
            text += ", "
        return text
    
    def _number_of_enrolled_students(self, obj):
        # Student.objects.filter(enrolled_courses=obj).count()
        return obj.enrolled_students.count()

    def _number_of_lessons(self, obj):
        return Lesson.objects.filter(module__course__id=obj.id).count()
    
