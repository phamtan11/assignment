import numpy as np

from app.utils.quantile import Quantile

APPENDED = "appended"
INSERTED = "inserted"


class Assignment:
    def __init__(self):
        self.data_sets = {}

    def add_pool(self, data):
        pool_id = data.get("poolId", None)
        pool_values = data.get("poolValues", [])
        if pool_id in self.data_sets:
            self.data_sets[pool_id].extend(pool_values)
            return APPENDED
        else:
            self.data_sets[pool_id] = pool_values
            return INSERTED

    def query(self, data):
        pool_id = data.get("poolId", None)
        percentile = data.get("percentile", 50.0)
        if pool_id in self.data_sets:
            pool_values = self.data_sets[pool_id]
            count_elements = len(pool_values)
            if count_elements < 100:
                quantile = Quantile(pool_values, percentile)
                print(f'quantile R1: {quantile.r1()}')
            return np.percentile(pool_values, percentile), len(pool_values)
        return 0, 0







