# Route Analysis
Route Analysis is a tool that takes a list of flights and lists airport pairs.


## Inputs
### Example CSV:
|From    |To      |
|--------|--------|
|JFK/KJFK|LAX/KLAX|
|LAX/KLAX|JFK/KJFK|
|JFK/KJFK|LHR/EGLL|
|LHR/EGLL|LAX/KLAX|
|LAX/KLAX|JFK/KJFK|
|LAX/KLAX|LHR/EGLL|
|JFK/KJFK|NRT/RJAA|
|NRT/RJAA|JFK/KJFK|

### Optional:
Update `columns` to match the appopriate CSV headers.

Update the `directional` boolean to support directionality of routes (eg `JFK/LAX` is / is not the same as `LAX/JFK`)


## Outputs
### Search route:
LHR/JFK (Directionality Disabled):
```
Found LHR/JFK in list of routes (1)
```

LHR/JFK (Directionality Enabled):
```
Did not find LHR/JFK in list of routes
```

### Search airport:
LHR (Directionality Disabled):
```
Found LHR in list of airports
Found 2 routes from LHR to JFK (1), LAX (2)
```
LHR (Directionality Enabled):
```
Found LHR in list of airports
Found routes from LHR to LAX (1)
```



-----
[Route Analysis](https://github.com/henrygriffiths/route_analysis) is released under the [MIT License](LICENSE)
