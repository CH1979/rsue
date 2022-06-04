from django import forms
from .models import Group, Students, Lecture, List_Of_Control_Activities, \
    List_Of_Control_Activities_Value, Grade


class AddGroupStudent(forms.ModelForm):
    """ Форма создания группы учеников """

    class Meta:
        model = Group
        fields = "__all__"


class AddStudent(forms.ModelForm):
    """ Форма создания cтудентов """

    class Meta:
        model = Students
        fields = "__all__"


class AddLecture(forms.ModelForm):
    """ Форма создания Занятий """

    class Meta:
        model = Lecture
        fields = "__all__"


class AddGrade(forms.ModelForm):
    """ Форма создания оценок студентам """

    class Meta:
        model = Grade
        fields = "__all__"


class AddList(forms.ModelForm):
    """ Форма создания листа контрольных мероприятий """

    class Meta:
        model = List_Of_Control_Activities
        fields = "__all__"

        widgets = {
            'date_of_approval': forms.DateInput(
                format=('%Y/%m/%d'),
                attrs={
                    'class': 'form-control', 
                    'type': 'date',
                    'value': '2022-06-03'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(AddList, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == 'group':
                visible.field.widget.attrs['class'] = "form-select"
            else:
                visible.field.widget.attrs['class'] = "form-control"


class AddValue(forms.ModelForm):
    """ Форма создания содержимого в листе контрольных мероприятий """

    class Meta:
        model = List_Of_Control_Activities_Value
        fields = "__all__"
