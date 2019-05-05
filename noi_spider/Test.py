import csv
def write_dict():
    with open('phone.csv', 'w')as f:
        writer = csv.DictWriter(f, fieldnames=("id", 'name', 'phone'))
        writer.writeheader()  # 写入头
        writer.writerow({'id': 101, 'name': 'swt', 'phone': '123456789'})
        writer.writerow({'id': 102, 'name': 'zs', 'phone': '123451111'})
        writer.writerow({'id': 103, 'name': 'lt', 'phone': '123422229'})
        writer.writerow({'id': 104, 'name': 'bw', 'phone': '1234563333'})
    print('写入成功')

write_dict()