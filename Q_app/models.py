from django.db import models
import os
from django.db.models.deletion import CASCADE
from django.db.models.base import Model
import MySQLdb as sql

# Create your models here.

class logindetails(models.Model):
    username=models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role=models.CharField(max_length=20)
    mail=models.EmailField(max_length=30)

def upload_path(instance, filename):
    # change the filename here is required
    return os.path.join("uploads", filename)


class clientdetails(models.Model):
    clientname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.BinaryField(max_length=100)
    def _enc(self, value):  #this function encrypt the password
       conn = sql.connect(user='root',passwd='root',db='marketing')
       cur = conn.cursor()
       cur.execute("SELECT AES_ENCRYPT('{}','pass')".format(value))
       return cur.fetchone()[0]
    
    email=models.CharField(max_length=100)
    date=models.CharField(max_length=50)
    image=models.ImageField(upload_to=upload_path)
    role = models.CharField(max_length=20)


class requirements(models.Model):
    deptid  = models.ForeignKey(clientdetails,on_delete=CASCADE)
    name = models.CharField(max_length=100)
    campaign_name = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    sel_options = models.CharField(max_length=100)
    selected_col = models.CharField(max_length=100)
    client_access = models.CharField(max_length=200)
    planned_impressions = models.CharField(max_length=100)
    planned_cpm = models.CharField(max_length=100)
    planned_clicks = models.CharField(max_length=100)
    planned_cpc = models.CharField(max_length=100)
    planned_session = models.CharField(max_length=100)
    planned_cps = models.CharField(max_length=100)
    planned_budget_impressions = models.CharField(max_length=100)
    planned_budget_clicks = models.CharField(max_length=100)
    planned_budget_sessions = models.CharField(max_length=100)
    ctr = models.CharField(max_length=10)

class user_report(models.Model):
    clientname = models.CharField(max_length=100)
    campaign_name = models.CharField(max_length=100)
    date=models.CharField(max_length=10)
    no_of_impressions=models.IntegerField()
    no_of_clicks=models.IntegerField()
    no_of_sessions=models.IntegerField()
    cpm=models.FloatField()
    cpc=models.FloatField()
    cost_per_session=models.FloatField()
    total_cpm=models.FloatField()
    total_cpc=models.FloatField()
    total_cps=models.FloatField()
    
    ctr=models.FloatField()
    clientid = models.ForeignKey(requirements,on_delete=CASCADE)
