from typing import Optional
# attribute
from resources.SchemaError import *

_value = "value"
_mutable = "mutable"
_type = "type"
_choice = "choice"
_date = "date"
_required = "required"


def validate_schema_value(schema_value: Optional[dict]):
    if schema_value is None:
        return False
    for k, v in schema_value.items():
        attr = attr_types.get(k)
        if attr is None:
            return False
        if type(attr) is tuple:
            if not (type(v) in attr):
                return False
        elif type(v) != attr:
            return False
    return True


def validate_schema(schema: dict):
    for value in schema.values():
        if type(value) is not dict:
            return False
        if not validate_schema_value(value):
            print(value)
            return False
    return True


def get_schema(schema_name: str):
    schema = schemas.get(schema_name)
    if schema is None:
        raise WrongSchemaName
    if not validate_schema(schema):
        raise SchemaError
    return schema


class Attr:
    value: str = _value
    mutable: str = _mutable
    type: str = _type
    choice: str = _choice
    date: str = _date
    required: str = _required


attr_types = {
    _value: (int, bool, str),
    _mutable: bool,
    _type: dict,
    _required: bool
}


class Type:
    choice: str = _choice
    date: str = _date


# snippet
_locale = {
    _value: "ko_KR",
    _mutable: False
}
_mktId = {
    _value: "ALL",
    _mutable: True,
    _required: True,
    _type: {
        _type: _choice,
        _value: ('ALL', 'SKT', 'KSQ', 'KNX')
    }
}
_share = {
    _value: 1,
    _mutable: True,
    _type: {
        _type: _choice,
        _value: (1, 2, 3)
    }
}
_money = {
    _value: 1,
    _mutable: True,
    _type: {
        _type: _choice,
        _value: (1, 2, 3, 4)
    }
}
_date_type = {
    _type: _date,
    _value: "%Y%m%d"
}

_str_type = {
    _type: "str"
}

# schema names
all_stock_prices = "all_stock_prices"
all_stock_fluctuations = "all_stock_fluctuations"
search_stock = "search_stock"
stock_price_info = "stock_price_info"

# schemas
schemas = {
    search_stock: {
        "bld": {
            _value: "dbms/comm/finder/finder_stkisu",
            _mutable: False
        },
        "locale": _locale,
        "mktsel": _mktId,
        "typeNo": {
            _value: 0,
            _mutable: False
        },
        "searchText": {
            _type: _str_type,
            _required: True
        }
    },
    all_stock_prices: {
        "bld": {
            _value: "dbms/MDC/STAT/standard/MDCSTAT01501",
            _mutable: False
        },
        "locale": _locale,
        "mktId": _mktId,
        "trdDd": {
            _type: _date_type,
            _required: True
        },
        "share": _share,
        "money": _money,
        "csvxls_isNo": {
            _value: False,
            _mutable: False
        }
    },
    all_stock_fluctuations: {
        "bld": {
            _value: "dbms/MDC/STAT/standard/MDCSTAT01602",
            _mutable: False
        },
        "locale": _locale,
        "mktId": _mktId,
        "strtDd": {
            _type: _date_type,
            _required: True
        },
        "endDd": {
            _type: _date_type,
            _required: True
        },
        "adjStkPrc_check": {
            _value: "Y",
            _mutable: False
        },
        "adjStkPrc": {
            _value: 2,
            _mutable: False
        },
        "share": _share,
        "money": _money,
        "csvxls_isNo": {
            _value: False,
            _mutable: False
        }
    },
    stock_price_info: {
        "bld": {
            _value: 'dbms/MDC/STAT/standard/MDCSTAT01701',
            _mutable: False
        },
        "locale": _locale,
        "isuCd": {
            _type: _str_type,
            _required: True
        },
        "strtDd": {
            _type: _date_type,
            _required: True
        },
        "endDd": {
            _type: _date_type,
            _required: True
        },
        "share": _share,
        "money": _money,
        "csvxls_isNo": {
            _value: False,
            _mutable: False
        }
    }
}
