import csv
with open('./m.store.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    writer.writerow(['store_id','address','tel','zip_code'])
    writer.writerow(['1','AAAGGGCCC','5943251456','XXX'])
    writer.writerow(['2','DKKT:LDK:LB','5343251456','YYYY'])
    writer.writerow(['3','DJDEJTLKA','5453251456','ZZZZ'])
    writer.writerow(['4','SDF:KLTKA','5143251456','XXYY'])
    writer.writerow(['5','KL:DSKF:LTBA','4443251456','YYXX'])
    writer.writerow(['6','SLTKPOSNBS','343251456','YZYZ'])
    writer.writerow(['7','SDJFLKSJLBKA','4243251456','ZYZY'])
    writer.writerow(['8','DKJL:JKTSBS','4643251456','XYXY'])
    writer.writerow(['9','SD:LKTLNBS','6443251456','YXYX'])