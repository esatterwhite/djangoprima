from django.db.models import permalink
from utils.models import ContentAwareModel, SelfAwareModel

class BaseBoard(ContentAwareModel):
    class Meta:
        abstract = True
        
class Board(BaseBoard):
    
    class Meta:
        permissions = ( 
           ('',''),
        )
        ordering = ()
        verbose_name = ''
    
    def __unicode__(self):
        pass
    
    @permalink
    def get_absolute_url(self):
        return ('',(),{})
    def save(self, *args, **kwargs):
        
        super(Board, self).save(args, kwargs)
    
    def delete(self):
        
        super(Board, self).delete()
        
class BaseTopic(SelfAwareModel):
    class Meta:
        abstract = True
        
class Topic(BaseTopic):
    
    class Meta:
        pass
    
class IssueTrackingTopic(BaseTopic):
    
    class Meta:
        pass    
class Post(SelfAwareModel):
    
    class Meta:
        pass
class Poll(SelfAwareModel):
    
    class Meta:
        pass
class PollOption(ContentAwareModel):
    
    class Meta:
        pass    
class Attachment(ContentAwareModel):
    
    class Meta:
        pass
    