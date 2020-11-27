# sms-activate-api
 Implementation of the sms-activate.ru API of public requests

## Lists of countries, services, operators
   https://sms-activate.ru/ru/api2

## Methods

| Method        | Description           | 
| ------------- |:---------------------:|
| SmsActivate(api_key) | Returns the SmsActivate object for working with api_key |
| get_balance() | Returns the current balance for the api_key |
| get_balance_and_cashback() | Returns balance with cashback|
| get_numbers_status(country, operator) | Request for the number of available numbers. Returns json: {"[service]_[redirection]:[number_of_numbers]"}|
| get_number(service, country, forward, operator, ref, phone_exception)| Returns list = ['number_id', 'number']|
| get_m_services_number(m_service, country, m_forward, operator, ref, exception)| Returns json: {{'phone':phone,'activation':activation,'service':service},{'phone':phone,'activation':activation,'service':service}}|
| set_status(status, number_id, forward)| Changes the status of the ordered number. Returns the response status string |
| get_status| Return the activation status string|
| get_full_sms(phone_id)| Returns the full text of the message|
| get_prices(service, country)| Return {"Country":{"Service":{"cost":cost,"count":numbers}},"retry":Repeated SMS reception}|
| get_countries()|Return json: {{'Country':{'id':0,'rus':"Россия","eng:"Russia","chn":"俄罗斯","visible":1,"retry":1,"rent":1,"multiService":1}}|
| get_qiwi_requisites()| {"status":"status","wallet":"PAYMENT WALLET NUMBER","upToDate":"The validity period of the details.","comment":"COMMENT FOR PAYMENT"}|
| get_additional_service(service, parent_id)| Additional service for numbers with forwarding|
| get_rent_services_and_countries(time, operator, country)| Return json, example: { "countries": { "0": 0 }, "operators": { "0": "aiva", "1": "any", "2": "beeline", ... "16": "yota" }, "services": { "full": { "cost": 42.93, "quant": 20 }, "vk": { "cost": 21.95, "quant": 20 }, "ok": { "cost": 7.68, "quant": 55 }, "ot": { "cost": 5.2, "quant": 42 } } }|
| get_rent_number(service, time, operator, country, url)| Returns phone number for lease{ "status": "success", "phone": { "id": 1049, "endDate": "2020-01-31T12:01:52", "number": "79959707564" } }|
| get_rent_status(number_id)| Returns json: { "status": "error", "message": "*possible_answer*" }|
| set_rent_status(number_id, status)| Change rent status. Returns json: { "status": "success" }|
| get_rent_list()| Returns json, example: { "status": "success", "values": { "0": { "id": "123456", "phone": "79181234567" }, "1": { "id": "123457", "phone": "79181234568" } } }|

## Example
```python
if float(phone.get_balance()) > 5:
    response = phone.get_number('ds', country=0)
print(response)                                 # ['341965911', '79670146229']
response = phone.set_status('8', response[0])   # 8 - Cancel activation (if the number doesn't fit you)
print(response)                                 # ACCESS_CANCEL
```
