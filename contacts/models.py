from django.db import models as mds
from slavanka.params import short_len,long_len
 
class Office(mds.Model):
    @staticmethod
    def get_hierarch_all():
        offices=[]         

        for office in Office.objects.all():
            office.phones=[
                phone
                for phone in Phone.objects.filter(office=office)
            ]                
            
            office.emails=[
                email
                for email in Email.objects.filter(office=office)
            ]               
            
            office.shedule_items=[
                shedule_item
                for shedule_item in SheduleItem.objects.filter(office=office)
            ]                                           
            
            if office.address=='' and len(office.shedule_items)==0:
                office.inline=True
            else:
                office.inline=False
            
            offices.append(office)
        
        return  offices

    title=mds.CharField(max_length=short_len,default='')
    address=mds.CharField(max_length=long_len,default='',blank=True)  

    def __str__(self):
        return self.title
    

class SheduleItem(mds.Model):
    days=mds.CharField(max_length=short_len,default='Ежедневно')
    times=mds.CharField(max_length=short_len,default='Круглосуточно')
    office=mds.ForeignKey(
        Office,
        on_delete=mds.CASCADE
    )

    def __str__(self):
        return 'f{self.days}:{self.times}'

class Contact(mds.Model):
    class Meta:
        abstract=True   
    
    value=mds.CharField(max_length=short_len,primary_key=True)
    owner=mds.CharField(max_length=short_len,blank=True,default='')
    office=mds.ForeignKey(
        Office,
        on_delete=mds.CASCADE
    )

    def __str__(self):
        if self.owner=='':
            return self.value
        else:
            return self.owner

class Phone(Contact):
    value=mds.CharField(max_length=20,primary_key=True) 
    
class Email(Contact):
     pass
    
