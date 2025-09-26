from array import array
# Compute the Total, average , minimum and maximum of warehouse pallet count
pallet_counts = (25, 30, 35, 40, 45, 50);
sum=sum(pallet_counts);
average=(sum/3);
print("The total of werahouse pallet quantity is =",sum);
print("The Average of werahouse pallet quantity is =",average);
print("The minimum of werahouse pallet quantity is =",min(pallet_counts));
print("The maximim of werahouse pallet quantity is =",max(pallet_counts));
# The warehouse report Using string
report=f"In warehouse pallet count summary to total the total is {sum} And average is {average}";
print(report);
# Use booleans
if average>30:
    print(average,"Is above standard");
else:
    print(average,"is below standard");
# list of item of warehouse pallet count
element=["Tables","Chair","Containers","Gas","Jerican"];
print(element);
element.append("Matelas");
print(element);
element.remove(element[2]);
print(element);
# Sort the list
element.sort()
print("Sorted list of pallet IDs:", element);
print("-" * 20)
# use array to make a sum
total=0;
arr=array('i',[25,30,35,40,45]);
for sum in arr:
    total=total+sum;
print(total);
#Use dictionary
pallet_records = [
    {'id': 101, 'name': 'Electronics', 'value': 50},
    {'id': 105, 'name': 'Furniture', 'value': 65},
    {'id': 102, 'name': 'Appliances', 'value': 48},
    {'id': 108, 'name': 'Books', 'value': 72}
]
print("Dictionary Items for warehouse pallet:", pallet_records)
# Update item
for record in pallet_records:
    if record['id'] == 105:
        record['value'] = 68
        print("\nUpdated record 105:", record)
        break
# Delete item
pallet_records = [record for record in pallet_records if record['id'] != 102]
print("\nAfter deleting record 102:", pallet_records)








