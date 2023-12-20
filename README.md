# excel-parser
Higher abstraction of operating on excel files, based on openpyxl.  
Ultimate goal is to allow simple implementation of "first come, first served" group assignments, with collision detection.

### json format
```json
{
  "subjects":{
    "SUBJECT_NAME":{
      "groups":[
        {
          "limit": "LIMIT", # 0 if no limit
          "day": "DAY", # format: "mon", "tue", "wed", "thu", "fri", "sat", "sun"
          "timeStart": "TIME_START", # format: "hh:mm"
          "timeEnd": "TIME_END", # format: "hh:mm"
          "frequency": "FREQUENCY", # 0 = other, 1 = every week, 2 = every 2 weeks
          "collisions": ["SUBJECT_NAME:GROUP_NUMBER", "..."] # SUBJECT_NAME has to be a subject in this json file; empty list if no collisions
        }, # ... more groups
      ]
    }, # ... more subjects
  }
}
```
