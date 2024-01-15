from pandas import read_excel

from .models import Region, Customer, Facility


def parseObjectsFromFile(file, id):
    try:
        customer = Customer.objects.get(id=id)
    except:
        return 1
    column_set = ['Территория', 'МВЗ', 'Название магазина', 'Адрес магазина']
    all_data = read_excel(file)
    column_names = all_data.columns.tolist()  # получаем список столбцов
    for item in column_set:
        if not (item in column_names):
            return 1
    # TODO тут надо будет сделать все объекты заказчика не активными

    for index, row_data in all_data.iterrows():
        region = row_data[column_set[0]]
        number = row_data[column_set[1]]
        title = row_data[column_set[2]]
        address = row_data[column_set[3]]
        region, _ = Region.objects.get_or_create(title=region)
        facility, _ = Facility.objects.get_or_create(
            title=title,
            customer=customer,
            region=region)
        facility.active = True
        facility.address = address
        facility.customer_number = number
        facility.save()

    return 0
