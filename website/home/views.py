from django.shortcuts import render
from django.db import connection



def home(request):   
    context = {} 
    if request.method == "POST":
        data = request.POST.dict()
        product_name = data.get("product")    

        with connection.cursor() as cursor:
            query = "SELECT * FROM home_product WHERE name LIKE '%%%s%%'" % (product_name);            
            print(" \n\n\nQuery is ", query, "\n\n\n")
            cursor.execute(query)
            rows = cursor.fetchall()
            context['data'] = rows

    return render(request, 'home/index.html', context)


