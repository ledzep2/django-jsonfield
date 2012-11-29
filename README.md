**This is a patched version of `django-jsonfield` which makes use of `django-jsonformfieldex` to provide form features**

This patched jsonfield also supports ModelForm. So you can define fields INSIDE json field in your model, and have the form available everywhere including **django admin**!

How it works?
-------------

    class MyCustomer(Model):
        slug = SlugField()
        store = JSONField({
            "profile": {
                "name": forms.CharField(max_length=10),
    			"email": forms.EmailField,
            },
            "account1": {
    			"number": forms.IntegerField,
    			"balance": forms.DecimalField(max_digits=10, decimal_places=2),
            },
    		"date_joined": forms.DateTimeField,
        })

    class MyCustomerForm(forms.ModelForm):
    	model = MyCustomer

And `MyCustomerForm` renders like this:

![screenshot1](http://ledzep2.github.com/django-jsonformfieldex/screenshot1.jpg)

Usage
------

Patched version of `JSONField` constructor takes two arguments itself. The original JSONField arguments still work.

* `fields`: a dict of fields
You can provide either field type or field instance for each field.

* `allow_json_input`: True|False
If True, it will render an additional textarea allowing user to enter arbitary json string (just like jsonfield)

Note: when `fields` is empty, `allow_json_input` will be automatically set to True

***

below is the original version of django-jsonfield readme.

***

django-jsonfield is a reusable django field that allows you to store validated JSON in your model.

It silently takes care of serialization. To use, simply add the field to one of your models.

===

from django.db import models
from jsonfield import JSONField

class MyModel(models.Model):
	json = JSONField()
	
For some DB backends, if you need to use the field in indexes or uniqueness constraints, the default JSONField, (which is a subclass of TextField) may not be suitable. For those cases, JSONCharField (a subclass of CharField) is provided. You will of course need to specify max_length, and it is your responsibility to ensure that this length is sufficient to hold whatever you would like the field to contain.