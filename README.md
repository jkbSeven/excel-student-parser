# excel-parser
Higher abstraction of operating on excel files, based on openpyxl.  
Ultimate goal is to allow simple implementation of "first come, first served" group assignments, with collision detection.

### json format
```json
{
  "subjects":{
    "SUBJECT_NAME":{
      "groups":{
        "GROUP_ID":{
          "limit": "LIMIT", # 0 = split evenly
          "day": "DAY",
          "timeStart": "TIME_START",
          "timeEnd": "TIME_END",
          "frequency": "FREQUENCY" # 1 = every week, 2 = every 2 weeks, 3 = other
        }
      }
    }
  }
}
```
