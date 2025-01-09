from typing import List
def rango(xs: List) -> List[int]:
     return [min(xs), max(xs)]
 
print(rango([3, 2, 7, 5]))  