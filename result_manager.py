import time
import openpyxl as excel
from typing import List

from utils.consts import RESULTS_FILEPATH

class Result:
    """Class for temporarily saving results data"""
    def __init__(self, dimentions:int, count:int, time:float) -> None:
        self.dimentions:int = dimentions
        self.count:int = count
        self.time:float = time

    def __lt__(self, other):
         return self.dimentions < other.dimentions

def write_results(results:List[Result], sync:bool) -> None:
    """Writes results to excel file located in utils.consts.RESULTS_FILE

    Args:
        results (List[Result]): list of results
        type (str): type of results. Expected values are "consecutive" and "parallel"

    Returns:
        str: "Succsessfully written reults to the file"
    """
    wb = excel.load_workbook(RESULTS_FILEPATH)
    
    # test sheet
    current_time = time.strftime("%H-%M", time.localtime())
    type = "synchronous" if sync else "multiprocessed"
    ts_name = f"{current_time} {type}"
    ts =  wb.create_sheet(ts_name)
    
    # init cells
    # column names
    ts["A1"] = "dim"
    ts["B1"] = "count"
    ts["C1"] = "time, sec"
    ts["D1"] = "time, min"
    ts["E1"] = "avg matrix/min"
    # additional cells
    ts["G1"] = "total time spent, min"
    ts["G2"] = f"=SUM(C2:C{len(results)+1})/60"
    
    # iterate results
    for i in range(len(results)):
        result = results[i]
        ts_row = str(i+2)
        # write results to its sheet
        ts["A"+ts_row] = result.dimentions
        ts["B"+ts_row] = result.count
        ts["C"+ts_row] = result.time
        ts["D"+ts_row] = round(result.time/60, 2)
        ts["E"+ts_row] = f"=60*B{ts_row}/C{ts_row}"

    wb.save(RESULTS_FILEPATH)
    if sync:
        mode = "Sync"
    else:
        mode = "Mult"
    print(f"{mode} | Succsessfully written reults to the file")