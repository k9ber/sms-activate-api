import requests


class SmsActivate:
    def __init__(self, api_key):
        self.api_key = api_key

    def __request(self, params):
        request_params = {'api_key': self.api_key}
        for _key, _value in params.items():
            if _value != '':
                request_params[_key] = _value
        try:
            return requests.get('https://sms-activate.ru/stubs/handler_api.php', request_params)
        except(ConnectionError, TimeoutError):
            return 'NO_CONNECTION'

    def get_balance(self):
        return self.request({'action': 'getBalance'}).text.split(':')[1]

    def get_balance_and_cashback(self):
        return self.request({'action': 'getBalanceAndCashBack'}).text.split(':')[1]

    def get_numbers_status(self, country='', operator=''):
        return self.request({'action': 'getNumbersStatus', 'country': country, 'operator': operator}).json()

    def get_number(self, service: str, country='', forward='', operator='', ref='', phone_exception=''):
        return self.request({'action': 'getNumber', 'service': service, 'forward': forward, 'operator': operator,
                             'ref': ref, 'country': country, 'phoneException': phone_exception}).text.split(':')[1:]

    def get_m_service_number(self, m_service: str, country='', m_forward='', operator='', ref='', exception=''):
        """m_service = "service1,service2,service3" """
        return self.request({'action': 'getMultiServiceNumber', 'multiService': m_service, 'multiForward': m_forward,
                             'operator': operator, 'ref': ref, 'country': country, 'phoneException': exception}).json()

    def set_status(self, status, number_id, forward=''):
        return self.request({'action': 'setStatus', 'status': status, 'id': number_id, 'forward': forward}).text

    def get_status(self, phone_id):
        return self.request({'action': 'getStatus', 'id': phone_id}).text

    def get_full_sms(self, phone_id):
        return self.request({'action': 'getFullSms', 'id': phone_id}).text

    def get_prices(self, service='', country=''):
        return self.request({'action': 'getPrices', 'service': service, 'country': country}).text

    def get_countries(self):
        return self.request({'action': 'getCountries'}).json()

    def get_qiwi_requisites(self):
        return self.request({'action': 'getQiwiRequisites'}).json()

    def get_additional_service(self, service, parent_id):
        return self.request({'action': 'getAdditionalService', 'service': service, 'id': parent_id}).text.split(':')

    def get_rent_services_and_countries(self, time='', operator='', country=''):
        return self.request({'action': 'getRentServicesAndCountries', 'time': time, 'operator': operator,
                             'country': country}).json()

    def get_rent_number(self, service, time='', operator='', country='', url=''):
        return self.request({'action': 'getRentNumber', 'service': service, 'time': time, 'operator': operator,
                             'country': country, 'url': url}).json()

    def get_rent_status(self, number_id):
        return self.request({'action': 'getRentStatus', 'id': number_id}).json()

    def set_rent_status(self, number_id, status):
        return self.request({'action': 'setRentStatus', 'id': number_id, 'status': status}).json()

    def get_rent_list(self):
        return self.request({'action': 'getRentList'}).json()
