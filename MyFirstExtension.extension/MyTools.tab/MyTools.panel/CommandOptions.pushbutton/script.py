from pyrevit import forms

selected_schedules = forms.select_schedules()
if selected_schedules:
    do_stuff()