from django.db import models
from prima.utils.models import SelfAwareModel, ContentAwareModel

class Board(ContentAwareModel):
    
    class Meta:
        pass
class Topic(SelfAwareModel):
    class Meta:
        abstrac = True
class BasicTopic(Topic):
    
    class Meta:
        pass
    
class IssueTrackingTopic(Topic):
    
    class Meta:
        pass    
class Post(SelfAwareModel):
    
    class Meta:
        pass
    
class Attachment(ContentAwareModel):
    
    class Meta:
        pass
    