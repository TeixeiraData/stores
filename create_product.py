import csv
with open('./m.product.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    writer.writerow(['product_id','price','product_category','product_name'])
    writer.writerow(['101','200','Sandwich','Egg Special'])
    writer.writerow(['102','130','Cookie','White Choco'])
    writer.writerow(['103','150','Fruit','Apple'])
    writer.writerow(['104','400','Sandwich','Teriyaki Special'])
    writer.writerow(['105','300','Cookie','Dark Choco'])
    writer.writerow(['106','450','Fruit','Peach'])
    writer.writerow(['107','340','Sandwich','Beans Special'])
    writer.writerow(['108','240','Ice Cream','Vanilla'])
    writer.writerow(['109','110','Fruit','Orange'])
    writer.writerow(['110','460','Sandwich','Strawberry Fruit'])
    writer.writerow(['111','320','Ice Cream','Fruit Mix'])
    writer.writerow(['112','90','Fruit','Banana'])
    writer.writerow(['113','390','Sandwich','BLT MIX'])
    writer.writerow(['114','180','Chocolte','Blueberry Mix'])
    writer.writerow(['115','140','Fruit','Lemon'])
    writer.writerow(['116','550','Sandwich','BBQ Mix'])
    writer.writerow(['117','1300','Cookie','Big Portion MIX'])
    writer.writerow(['118','490','Fruit','Strawberry'])
    writer.writerow(['119','330','Chocolate','Black Choco'])
    writer.writerow(['120','160','Chocolate','Plain Cookie'])