import logging
import alexa_skill
import falcon
from app import buildin_intents, SpeedIntents

class Fulfiller(object):
    def on_post(self, req, resp):
        get_response = alexa_skill.Processor(
            req.media,
            buildin_intents,
            'Would you like to test your internet connection?',
            'Good bye',
            SpeedIntents(),  # Add implemented intent
        )
        json_response, handled = get_response()
        logging.info('Response was handled by system: {}'.format(handled))
        resp.media = json_response


app = falcon.API(media_type=falcon.MEDIA_JSON)
app.add_route('/v1/alexa/fulfiller', Fulfiller())