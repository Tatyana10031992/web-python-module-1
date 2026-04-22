"""
ЗАДАЧА: Учёт инвентаря на складе

Формат строки:
дата,товар,тип,количество

Операции:
2024-01-01,яблоко,IN,50
2024-01-02,банан,IN,30
2024-01-03,яблоко,OUT,10
2024-01-03,груша,OUT,5
2024-01-04,груша,IN,20
2024-01-05,банан,OUT,40
2024-01-06,яблоко,OUT,5

Типы операций:
- IN  : поступление товара
- OUT : отгрузка товара

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Создать файл inventory.txt с операциями склада

2. Прочитать файл и загрузить все операции.

3. Для каждого товара:
   - посчитать итоговое количество на складе
   - посчитать общее количество поступивших единиц
   - посчитать общее количество отгруженных единиц

4. Найти товары:
   - у которых итоговое количество < 0 (ошибка учёта)
   - которые ни разу не поступали, но отгружались

5. Найти товар с:
   - максимальным количеством поступлений
   - максимальным количеством отгрузок

6. Сформировать множество всех дат,
   когда происходили операции с товаром "яблоко".

7. Записать подробный отчёт в файл report.txt.

- ОТЧЁТ ПО СКЛАДУ
- Итоговые остатки
- Общее поступление
- Общая отгрузка
- Товары с отрицательным остатком:
- Товары без поступлений, но с отгрузкой:
- Товар с максимальным поступлением:
- Товар с максимальной отгрузкой:
- Даты операций с яблоком:
"""




with open("inventory.txt", "w", encoding="utf-8") as file:
   operations = [
      "2024-01-01,яблоко,IN,50",
      "2024-01-02,банан,IN,30",
      "2024-01-03,яблоко,OUT,10",
      "2024-01-03,груша,OUT,5",
      "2024-01-04,груша,OUT,20",
      "2024-01-05,банан,OUT,40",
      "2024-01-06,яблоко,OUT,5",
   ]
   file.write("\n".join(operations))
      

operations = []
with open("inventory.txt", "r", encoding="utf-8") as file:
   for line in file:
      date, product, operation_type, quantity = line.split(",")
      
      operations.append({
         "date": date,
         "product": product,
         "operation_type": operation_type,
         "quantity": int(quantity)
       })

for operation in operations:
   print(operation)


total_count = {}
total_in = {}
total_out = {}
for operation in operations:
   date, product, operation_type, quantity = operation["date"], operation["product"], operation["operation_type"], operation["quantity"]

   total_count.setdefault(product, 0)
   total_in.setdefault(product, 0)
   total_out.setdefault(product, 0)
   if operation_type == "IN":
      total_count[product] += quantity
      total_in[product] += quantity

   else:
      total_count[product] -= quantity
      total_out[product] += quantity

for key, value in total_count.items():
   print(f"На складе {key}: {value}")
print("-"*20)
for key, value in total_in.items():
   print(f"Приехало {key}: {value}")
print("-"*20)
for key, value in total_out.items():
   print(f"Отгружено {key}: {value}")



error_products = []
for product, count in total_count.items():
   if count < 0:
      error_products.append(product)
     

if error_products:
   print("\nОбнаружены товары с отрицательным остатком ")
   for product in error_products:
      print(f"{product}: {total_count[product]}")
else:
   print("\nВсе товары учтены корректно" )


shipped_without_receipt = []
for product in total_out:
   if total_in.get(product, 0) == 0 and total_out[product] > 0:
      shipped_without_receipt.append(product)
   
if shipped_without_receipt:
   print("\nТовары которые не поступали не отгружались:")
   for product in shipped_without_receipt:
      print(f"{product}: отгружено {total_out[product]}")
else:
   print("\nНет товаров которые отгружались без поступлений")
   


max_in_product = None
max_in_quantity = -1

for product, quantity in total_in.items():
   if quantity > max_in_quantity:
      max_in_product = product
      max_in_quantity = quantity

max_out_product = None
max_out_quantity = -1
for product, quantity in total_out.items():
    if quantity > max_out_quantity:
        max_out_product = product
        max_out_quantity = quantity
   
      
apple_dates = set()

for operation in operations:
   if operation["product"] == "яблоко":
      apple_dates.add(operation["date"])

print("\nДата операции с товаром 'яблоко': ")
for date in sorted(apple_dates):
   print(date)


with open("report.txt", "w", encoding="utf-8") as report_file:
   report_file.write("Отчет по складу") 
   report_file.write("=" * 40 + "\n\n")

   report_file.write("Итоговые остатки\n")   
   for product, count in sorted(total_count.items()):
        report_file.write(f"   {product}: {count}\n")
   report_file.write("\n")

   report_file.write("Общее поступление\n")   
   for product, qty in sorted(total_in.items()):
      report_file.write(f"   {product}: {qty}\n")
   report_file.write("\n")

   report_file.write("Общая отгрузка")   
   for product, count in sorted(total_count.items()):
        report_file.write(f"   {product}: {count}\n")
   report_file.write("\n")

   report_file.write("Товары с отрицательным остатком:\n")
   if error_products:
      for product in error_products:
         report_file.write(f" {product}: {total_count[product]}\n")
   else:
      report_file.write("\n")

   report_file.write("Товары без поступлений, но с отгрузкой:\n")   
   if shipped_without_receipt:
      for product in shipped_without_receipt:
         report_file.write(f" {product}: отгружено {total_count[product]}\n") 
   else:
      report_file.write("\n")

   report_file.write("Товары с максимальным поступлением:\n")
   if max_in_product:
      report_file.write(f" {max_in_product}: {max_in_quantity}\n")
   else:
      report_file.write("\n")
     
   report_file.write("Товары с максимальной отгрузкой\n")
   if max_out_product:
      report_file.write(f" {max_out_product}: {max_out_quantity}\n")
   else:
      report_file.write("\n")

   report_file.write("Даты операций с яблоком\n")
   if apple_dates:
      for date in sorted(apple_dates):
         report_file.write(f" {date}\n")
print("Отчет успешно записан в файл 'report.txt' ")


      
         

      
         
