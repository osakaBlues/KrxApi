# attribute
_value = "value"
_mutable = "mutable"
_type = "type"
_choice = "choice"
_date = "date"

# snippet
_locale = {
    _value: "ko_KR",
    _mutable: False
}
_mktId = {
    _value: "ALL",
    _mutable: True,
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

# schemas
schemas = {
    "all_stock_prices": {
        "bld": {
            _value: "dbms/MDC/STAT/standard/MDCSTAT01501",
            _mutable: False
        },
        "locale": _locale,
        "mktId": _mktId,
        "trdDd": {
            _type: {
                _type: _date,
                _value: "%Y%m%d"
            }
        },
        "share": _share,
        "money": _money,
        "csvxls_isNo": {
            _value: False,
            _mutable: False
        }
    },
    "all_stock_fluctuations": {
        "bld": {
            _value: "dbms/MDC/STAT/standard/MDCSTAT01602",
            _mutable: False
        },
        "locale": _locale,
        "mktId": _mktId,
        "strtDd": {
            _type: {
                _type: _date,
                _value: "%Y%m%d"
            }
        },
        "endDd": {
            _type: {
                _type: _date,
                _value: "%Y%m%d"
            }
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
    }
}
