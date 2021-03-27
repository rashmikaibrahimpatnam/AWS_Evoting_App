import configparser


class CreateConfigParse:
    
    def add_keys(self):
        config = configparser.ConfigParser()
        config['AWSEducateKeys'] = {'access_key_id': 'ASIAZE7J44S64BGJWCKN',
                                    'secret_access_key': 'R58tmmIDtEvAOWH1S5P7hPQjw7IlZ4jhlXJ4q2VE',
                                    'session_token': 'FwoGZXIvYXdzEMf//////////wEaDPA1r1b2yBH9IEUAUiK/AQDrA3n+K0w+rm7Wu3oxX26un+ylKHiJaM/dx/CvJ1jrgJMNRgy2GbDkXv14NFAGaOHDeC3Hs7T+5KALrQDgcT36hH4jvVbRq5yqV6ywGUxERtFGWz/epCMpoVoL8AoSVwIFGGbktoNeIGr+e2cDysuzS5sbWw2NukSTwVq18Y3FH81aPDl/ZmbJMd7lDbHuUBbW+0Tgk5kINuIXpvakLV0DQj+vDgK6CubLpPVsgoi/vFdchskGno+rvm7eTwIFKMyl8oIGMi05PsILrW9eAgn9PDnXJwIcyHcBZtPW6uyQsLFkysqkbdUVuh9nC39xNGI5AHY=',
                                    'region_name': 'us-east-1'
                                    }
        with open('.awskeys.ini', 'w') as configfile:
            config.write(configfile)
        return True
