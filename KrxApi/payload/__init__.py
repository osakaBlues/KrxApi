class Payload:
    def to_dict(self) -> dict:
        result = {}
        for k in dir(self):
            try:
                v = getattr(self, k)
            except AttributeError:
                continue
            if not callable(v) and not k.startswith("_") and v is not None:
                result[k] = v
        return result
