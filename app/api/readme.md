## Format

Timestamp format is in

`year-month-date-hour:minute:second`

eg.

`2022-09-21-14:49:40.811523`

## Calling the api

`127.0.0.1:5000` being your local host or url.

### Call all rows
`127.0.0.1:5000/api/airquality`

Shows 20 per page

eg.

`http://127.0.0.1:5000/api/airquality`

### Call specific row

`127.0.0.1:5000/api/airquality/<string:timestamp>`

eg.

`http://127.0.0.1:5000/api/airquality/2022-09-21-14:49:40.811523`

### Insert row

`127.0.0.1:5000/api/airqualitys <data>`

Timestamp if not supplied uses the default time

eg.

`http://127.0.0.1:5000/api/airqualitys temp=10 humidity=10 particles=10 eco2=10 tvoc=10`

### Editing row

`127.0.0.1:5000/api/airqualitys/<timestamp> <data>`

eg.

`http://127.0.0.1:5000/api/airqualitys/2022-09-27-15:06:08.284466 tvoc=20`