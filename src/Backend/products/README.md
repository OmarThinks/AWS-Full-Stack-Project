# Products Application:


# Technologies Used:
1. Django
2. Django REST Framework


# How to run:


Creating Database environment Variables:

<b>

```bash
export DEFAULT_DB_ENGINE="django.db.backends.sqlite3"
export DEFAULT_DB_NAME=$PWD/"db.sqlite3"
```

<b>

These were the default values for database env variables.  
And this is how you can run the code.



<b>

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate products
python manage.py runserver
```
</b>





# Models:
There is only one model, the Product Model.
<table>
	<tr>
		<th>Field Name</th>
		<th>Field Type</th>
		<th>Unique</th>
		<th>Minimum</th>
		<th>Maximum</th>
		<th>Required</th>
		<th>Can be modified</th>
	</tr>
	<tr>
		<th>ID</th>
		<td>Integer</td>
		<td>True</td>
		<td>-</td>
		<td>-</td>
		<td>Auto Generated</td>
		<td>False</td>
	</tr>
	<tr>
		<th>name</th>
		<td>string</td>
		<td>false</td>
		<td>-</td>
		<td>150</td>
		<td>True</td>
		<td>True</td>
	</tr>
	<tr>
		<th>price</th>
		<td>float</td>
		<td>false</td>
		<td>0.1</td>
		<td>1000000</td>
		<td>True</td>
		<td>True</td>
	</tr>
	<tr>
		<th>in_stock</th>
		<td>boolean</td>
		<td>false</td>
		<td>-</td>
		<td>-</td>
		<td>True</td>
		<td>True</td>
	</tr>
</table>






# Endpoints:

## 1) http://127.0.0.1:8000/api/
Returns the api Resources

```json
{
    "products": "http://127.0.0.1:8000/api/products/"
}
```

<img src="images/api.gif">



## 2) Product Endpoints:


## 2-1) (GET) http://127.0.0.1:8000/api/products/

Displays a paginated list of products, each page contains 5 results.

<img src="images/products.gif">


## 2-2) (POST) http://127.0.0.1:8000/api/products/
Create new products

## 2-3) (GET) http://127.0.0.1:8000/api/products/<id>
Get details of a product


<img src="images/product_id.gif">


## 2-4) (PUT) http://127.0.0.1:8000/api/products/<id>
Modify a product

## 2-5) (DELETE) http://127.0.0.1:8000/api/products/<id>
Delete a product

