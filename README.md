# RESTFUL LEDs
A RESTful API for controlling LEDs on a Raspberry Pi.

## End Points

| Request Type  | End Point     | Description       | Parameters    | Possible Values   |
|---------------|---------------|-------------------|---------------|-------------------|
| GET/POST      | /             | Lists LED colors  |               |                   |
| GET/POST      | /on           | Turn on LED       | led           | red, blue, green  |
| GET/POST      | /off          | Turn off LED      | led           | red, blue, green  |
| GET/POST      | /status       | On/Off LED status | led           | red, blue, green  |


## Example

The following example would turn on the red LED
```
http://<server_ip>/on?led=red
```
