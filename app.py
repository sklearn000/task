from bottle import Bottle
from bottle import run,route,template,static_file,request,abort

import asyncio

import os

import pandas as pd
import sqlite3
import time
from sqlite3 import connect
from datetime import date,datetime,time

from pathlib import Path


app=Bottle()
UPLOAD_DIR="upload"
con = sqlite3.connect('data.db')

@app.route('/static/js/<filename>')
def server_js(filename):
   return static_file(filename, root='static/js')

@app.route('/static/css/<filename>')
def server_css(filename):
   return static_file(filename, root='static/css')


@app.route('/static/fonts/<filename>')
def server_jpg(filename):
   return static_file(filename, root='static/fonts')


@app.route('/static/images/<filename>')
def server_jpg(filename):
   return static_file(filename, root='static/images/', mimetype='image/jpg')

@app.route('/static/images/activities/<filename>')
def server_jpg(filename):
   return static_file(filename, root='static/images/activities', mimetype='image/jpg')

@app.route('/static/images/tabs/<filename>')
def server_jpg(filename):
   return static_file(filename, root='static/images/tabs', mimetype='image/jpg')

@app.route('/static/images/gallery/<filename>')
def server_jpg(filename):
   return static_file(filename, root='static/images/gallery', mimetype='image/jpg')

@app.route('/static/images/pattern/<filename>')
def server_jpg(filename):
   return static_file(filename, root='static/images/pattern', mimetype='image/jpg')



@app.route('/static/images/gallery/<filename>')
def server_jpg(filename):
   return static_file(filename, root='static/images/gallery', mimetype='image/jpg')


@app.route('/static/template/js/<filename>')
def server_jpg(filename):
   return static_file(filename, root='static/template/js')

@app.route('/static/template/css/<filename>')
def server_jpg(filename):
   return static_file(filename, root='static/template/css')

@app.route('/static/template/font/<filename>')
def server_jpg(filename):
   return static_file(filename, root='static/template/font')


@app.route('/static/template/images/<filename>')
def server_jpg(filename):
   return static_file(filename, root='static/template/images')




@app.route('/upload/<filename>')
def server_png(filename):
   return static_file(filename,  root=UPLOAD_DIR, mimetype='image/png')

@app.route('/upload/<filename>')
def upload_jpg(filename):
   return static_file(filename, root= UPLOAD_DIR, mimetype='image/jpg')





@app.route('/upload',method ='GET')
def upload_dir():
                                     
         return template('upload.html')



@app.route('/upload',method ='POST')
def upload_dir():
                    con = sqlite3.connect('profiles.db')
                    conn = sqlite3.connect('dates.db')
                    username = request.forms.get('username')
                    email = request.forms.get('email')
                    password =request.forms.get('password') 
                    address = request.forms.get('address')
                    phone =request.forms.get('phone') 
                    gender =request.forms.get('gender')
                    photo = request.files.get('upload')
                   
                    db =con.cursor()
                    pb=conn.cursor()
                    date = datetime.now()
                    today=date.now()
                    this_hour =today.hour
                    this_min =today.minute
                    this_sec=today.second
                    this_date= today.strftime("%A, %d. %B %Y %I:%M%p")
                    
                    
                    if photo:
                        
                         this_pic = photo.filename
                         photo_path =os.path.join( UPLOAD_DIR,photo.filename)
                         db.execute('''CREATE TABLE IF NOT Exists profile(this_pic,username,email,password, phone ,address,gender)''')  
                         db.execute("INSERT INTO profile VALUES (?,?,?,?,?,?,?)", (this_pic,username,email, password ,phone,address,gender)) 
                         con.commit()
                         con.close() 
                         photo.save(photo_path)
                        
                         
                         return template('register.html' , username=username,email=email,phone=phone,address=address,gender=gender,UPLOAD_DIR=UPLOAD_DIR, this_pic=this_pic,this_date=this_date,this_hour=this_hour,this_min=this_min,this_sec=this_sec)

                        


  
@app.route('/', method ='GET')
def index():
       username =request.forms.get('username')
       return template('home.html',username=username )

@app.route('/home', method ='GET')
def home():
       username =request.forms.get('username')
       return template('home.html',username=username )
@app.route('/service', method ='GET')
def service():
       username =request.forms.get('username')
       return template('upload.html',username=username )

@app.route('/history', method ='GET')
def history():
       username =request.forms.get('username')
       return template('test.html',username=username )

@app.route('/portfolio', method ='GET')
def portfolio():
       username =request.forms.get('username')
       return template('cbt.html',username=username )




                        



@app.route('/login',method ='GET')
def login():
       
       
       
       return template('login.html' )



      
        


@app.route('/login',method='POST')

def login():

      from sqlite3 import connect
      import urllib.request
      con = sqlite3.connect('profiles.db')
    
      db =con.cursor()
      db.execute('SELECT * FROM profile')
    
      res = db.fetchall()
    
      for row in res: 
            photo = request.files.get('upload') 
      
      
            username =request.forms.get('username')
            password =request.forms.get('password')
      
     
   
            db_string= pd.DataFrame(res,columns=['photo', 'username','email','password', 'phone', 'address','gender'])
            photos =pd.DataFrame({'photo':db_string["photo"]})
      
            con.commit()
            con.close() 
            print(db_string.to_string())
            print(row)
            print(res)
      
            return template('index.html',username=username)




            
  
         
     
if __name__ == '__main__':
     run( app,host='localhost', port=8080)