import configparser


class CreateConfigParse:

    def add_keys(self):
        config = configparser.ConfigParser()
        config['AWSEducateKeys'] = {'access_key_id': 'ASIAZE7J44S6QGVGVGNY',
                                    'secret_access_key': '6YP/15UG6lIma/JuZg79ugYZF36OmPegjdW9ouoe',
                                    'session_token': 'FwoGZXIvYXdzECgaDIpTYHW134yZ69A0pSK/Acd8H282zDunrzPUZLSNgg+/dxgZFgAdksRYtaQSPZ3xwymgbqwW1k3UwVcS9aEruEvZ+mfGhaPYjTkd7bUCkATjJWvOhAuyF5j7+IQ9Gcr7hIQ9ObDKL9Km+nh3QAt5OkwVhNzd81O9QZNE2050eUGX7zFYy1rIJUE8afRwc0aG3igUny4zkmbZ9wblHiVzWNGkN0gaW3foe//GlUQdH5+FzQOQOwBcqUo81cam2Dku4mDL58O8h7XvqcsbIyY5KN/Lh4MGMi3qpbyJ6IiAm9qZqqhgnaenIWuRG6UDY3GYOQ6fX44uFLP7Yn1qh/JKvH0xN3s=',
                                    'region_name': 'us-east-1'
                                    }
        with open('.awskeys.ini', 'w') as configfile:
            config.write(configfile)
        return True
