from speed import Speed
import pyspeedtest
from alexa_skill.intents import BaseIntents
from alexa_skill.intents import BuildInIntents

buildin_intents = BuildInIntents(
    help_message='Say to Alexa: "test my internet"',
    not_handled_message="Sorry, I'm a very dumb, dumb, stupid idiot; I've already called the police on myself. Just kitten, haha. Could you repeat that?",
    stop_message='stop',
    cancel_message='cancel',
)


class SpeedIntents(BaseIntents):
    @property
    def mapper(self):
        return {'test_speed': self.test_speed}

    def test_speed(self):
        # fast_response = requests.get('https://www.fast.com')
        # if fast_response.status_code != 200:
        #     return self.response('Sorry, I could not connect to python speed test. Please try again'), False

        # soup = BeautifulSoup(fast_response)
        # speed_value = soup.find("div",attrs={"class":"speed-results-container","id":"speed-value"}).text
        # print(speed_value)
        # speed_unit = soup.find("div",attrs={"class":"speed-units-container","id":"speed-units"}).text
        # print(speed_unit)

        st = pyspeedtest.SpeedTest()

        ping = 'Your ping is: ' + str(st.ping()) + ' milliseconds'
        down = st.download() / 1000000
        if down < 1:
            down = 'Your download speed is: ' + str(down * 1000) + ' kilobytes per second'
        else:
            down = str(down) + ' megabytes per second'
        up = st.upload() / 1000000
        if up < 1:
            up = 'Your upload speed is: ' + str(up * 1000) + ' kilobytes per second'
        else:
            up = str(up) + ' megabytes per second'

        speed = Speed(ping, up, down)
        return self.response(speed), True
