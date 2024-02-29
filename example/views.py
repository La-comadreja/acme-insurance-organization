from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  html = f'''
     <html>
       <body>
         <h1>Hello World!</h1>
         <p>Congratulations on getting your first Vercel app to run.</p>
       </body>
     </html>
   '''
  return HttpResponse(html)
