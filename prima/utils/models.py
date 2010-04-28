from datetime import datetime
from django.db import models
from django.contrib.contenttypes.models import ContentType

class ContentAwareModel(models.Model):
    
    '''
        An Abstract model: models which subclass the SelfAwareModel
        will have a series of methods that give quick access to that
        model's meta information:
        
        Content Type & it's ID
        App Label
        Model Name
        Class Name
        
        The aim is to make working with generic models easier from a
        template as generic relations offer a good deal of information
        about the related object, but accessing information about the 
        target object/model itself can be frustrating.
        
        Way to add Standarized functionality with out changing model strucure
    '''
        
    def get_ct(self):
        '''returns the ContentType Object for this model'''
        return ContentType.objects.get_for_model(self)

    def get_ct_id(self):
        '''returns the ID of the ContentType for this model'''
        return self.get_ct().id

    def get_app_label(self):
        '''returns the app lable for this model'''
        return self.get_ct().app_label

    def get_model_name(self):
        '''returns the model name of the contenttype object for this model'''
        return self.get_ct().model

    def get_class_name(self):
        '''returns the value of the verbose name in the models meta data'''
        return self._meta.verbose_name
    
    class Meta: 
        abstract = True
        
class SelfAwareModel(ContentAwareModel):
    '''
        a subclass of the ContentAwareModel with added fields
        created - date time field that defaults to the current time
        modified - date time field which is changed to the current date and time
        when the model is saved.
        
        this is effectivly a time stamp model that is content aware
        
        Abstract class to be subclassed 
    '''    
    created = models.DateTimeField(default=datetime.now(), editable=False)
    modified = models.DateTimeField(blank=True, null=True, editable=False, auto_now=True)
    
    class Meta:
        abstract = True
        