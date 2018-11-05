#!/usr/bin/env python
# coding: utf-8
from lib.dte import get_rut_emisor, get_sum_detail

if __name__ == '__main__':
    data = """
    {
        "Encabezado": {
            "Emisor": {
                "RUTEmisor": "55-5555555-5"
            }
        },
        "Detalle": [
            {
                "NmbItem": "Conectores RJ45",
                "QtyItem": 450,
                "PrcItem": 70
            },
            {
                "NmbItem": "Conectores RJ45",
                "QtyItem": 450,
                "PrcItem": 80
            },
            {
                "NmbItem": "Conectores RJ45",
                "QtyItem": 450,
                "PrcItem": 150
            }
        ]
    }
    """
    try:
        res = get_rut_emisor(data)
    except ValueError as exc:
        res = False
        print 'Hubo un error: %s' % exc
    if res:
        print res['result']
    print get_sum_detail(data)
