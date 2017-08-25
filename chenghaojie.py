import xlrd
def process_doctor_data():
    file_path = '/Users/chenghaojie/Desktop/111.xlsx'
    file_obj = xlrd.open_workbook(file_path)
    table = file_obj.sheets()[0]
    rows = table.nrows
    doctor_info_list = []
    for row in range(0, rows):
        info = table.row_values(row)
        doctor_info_list.append({'username': str(int(info[1])), 'graph': int(info[3]), 'tele': int(info[4])})
    return doctor_info_list



from api.manager.doctor_manager import *
from clinic.models import *
def change_doctor_price(doctor_info_list):
    for doctor_info in doctor_info_list:
        doctor = get_doctor_by_username(doctor_info['username'])
        growth = DoctorGrowthSystem.objects.get(doctor_id=doctor.id)
        growth.grade = 50
        growth.save()
        doctor.pro_price = doctor_info['graph']
        doctor.tel_price = doctor_info['tele']*10
        doctor.save()
        print doctor.id
