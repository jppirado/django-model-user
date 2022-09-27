from django.contrib import admin

# Register your models here.

from .models import Post

@admin.register(Post) 
class PostAdmin( admin.ModelAdmin ):
    list_display = ('titulo' , '_autor')
    exclude = ('autor' ,)


    def _autor(self , instance):
        return f'{instance.autor.get_full_name()}'
    #instance está relacionando ao objeto post, no entanto o objeto post
    #contém o atributo user que possui o metodo getfull name

    def get_queryset( self , request ):
        qs = super(PostAdmin , self ).get_queryset( request )
        return qs.filter(autor=request.user)
    
    def save_model( self , request , obj , form , change):
        # é o obj em questão que se trada de post
        obj.autor = request.user
        return super().save_model( request, obj, form, change)