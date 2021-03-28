import configparser


class CreateConfigParse():

    def add_keys(self):
        config = configparser.ConfigParser()
        config['AWSEducateKeys'] = {'access_key_id': 'ASIAZE7J44S6VDG5XAYC',
                                    'secret_access_key': 'vzjYoHy3h+btbWnd54HjcCQYEhjUxrSvYrPJ5KNP',
                                    'session_token': 'FwoGZXIvYXdzEAMaDHwHYdLA4pIGQ9l1jSK/AdiNUrf4vm12LT233oBSYqYdhfTaYrzZaFCL1uwN5I9rOqLpk9qeTN6npRb7HkdgNZbzereeLsG2yjgBQdLBeeR6ARq+JhFe4QPWU2Ekha4kDCyzKDRQGdhfXOVG3ZB7Vr1gzUCKrhRsc7rV8gRDmnnQ0OEstYJxPTSE15Mhg3U1OPwNheqiUTQpAdU5+rvSAWr/f21z0jz//9EkYVLqAjV/fd1K4cDBb5QeQqCewxieK6KyNv8/YFq/Iuoz2bdfKLHF/4IGMi1+F1ukaSOYzH0sbU2/akm2P/8L1nONRy17EZpuhJ/PafE+/ZorX3SIBCdDmPk=',
                                    'region_name': 'us-east-1'
                                    }
        with open('.awskeys.ini', 'w') as configfile:
            config.write(configfile)
        return True
