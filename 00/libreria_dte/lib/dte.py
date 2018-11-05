# coding: utf-8
import json

def get_rut_emisor(data):
    data = json.loads(data)
    rut = data.get('Encabezado', {}).get('Emisor', {}).get('RUTEmisor')
    try:
        check_rut(rut)
        error = 0
    except ValueError as exc:
        error = exc
        
    return {
        'status': 0 if error == 0 else 1,
        'result': error or rut
    }

def get_sum_detail(data):
    data = json.loads(data)
    return sum(line.get('PrcItem') for line in data.get('Detalle', []))


def check_rut(rut):
    if rut != '55-5555555-5':
        raise ValueError('RUT invalido')
