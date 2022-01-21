"""Module for generating games by user report"""
import sqlite3
from django.shortcuts import render
from dubsapi.models import LineItem
from dubsapi.views import Connection
from django.http import JsonResponse
from django.db import connection

def totalSales(request):
    with connection.cursor() as cursor:
        query="""
        SELECT
            sum(p.price) AS total_sales
        FROM
            dubsapi_lineitem li
        JOIN
            dubsapi_order o ON o.id = li.order_id 
        JOIN
            dubsapi_product p ON p.id = li.product_id
        JOIN
            dubsapi_customer c ON c.id = o.customer_id
        """
        cursor.execute(query)
        row = dictfetchall(cursor)
        
        print(row)
        total_sales = {}
        total_sales["total_sales"] = row

    return JsonResponse(total_sales)

def productSales(request):
    with connection.cursor() as cursor:
        query="""
        SELECT 
            COUNT(li.product_id) as total_number_sold,
            li.product_id,
            p.name
        FROM
            dubsapi_lineitem li
        JOIN
            dubsapi_product p ON p.id = li.product_id
        GROUP BY 
            product_id, p.name
        """
        cursor.execute(query)
        row = dictfetchall(cursor)
        
        print(row)
        product_sales = {}
        product_sales["product_sales"] = row

    return JsonResponse(product_sales)

def singleProductSales(request, id):
    with connection.cursor() as cursor:
        query="""
        SELECT 
            COUNT(li.product_id),
            li.product_id,
            p.name
        FROM
            dubsapi_lineitem li
        JOIN
            dubsapi_product p ON p.id = li.product_id
        GROUP BY 
            product_id, p.name
        HAVING 
            product_id = %s
        """
        cursor.execute(query, [id])
        row = dictfetchall(cursor)
        
        print(row)
        product_sales = {}
        product_sales["product_sales"] = row

    return JsonResponse(product_sales)

def toppingSales(request):
    with connection.cursor() as cursor:
        query="""
        SELECT 
            COUNT(lit.topping_id) AS topping_count,
            lit.topping_id,
            t.name
        FROM
            dubsapi_lineitemtopping lit
        JOIN
            dubsapi_topping t ON t.id = lit.topping_id
        GROUP BY 
            topping_id, t.name
        """
        cursor.execute(query)
        row = dictfetchall(cursor)
        
        print(row)
        topping_sales = {}
        topping_sales["topping_sales"] = row

    return JsonResponse(topping_sales)

def dailySales(request):
    with connection.cursor() as cursor:
        query="""
        SELECT
            o.created_date,

            sum(p.price) AS total_sales
        FROM
            dubsapi_lineitem li
        JOIN
            dubsapi_order o ON o.id = li.order_id 
        JOIN
            dubsapi_product p ON p.id = li.product_id
        JOIN
            dubsapi_customer c ON c.id = o.customer_id
        GROUP BY o.created_date
        """
        cursor.execute(query)
        row = dictfetchall(cursor)

        daily_sales = {}
        daily_sales["daily_sales"] = row

    return JsonResponse(daily_sales)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]