from flask import Flask
from flask_restful import Resource, Api, request

import RPi.GPIO as gpio

app = Flask(__name__)
api = Api(app)

# A dictionary containing the LEDs GPIO number by color name
PINS_BY_COLOR = {"red": 17, "blue": 18, "green": 27}


def generate_output(success, data=None, error=None):
    """
    :param success: Was the request successful? True or False
    :param data: Data to return if success was True
    :param error: Error to return if success was False
    """
    response = {"success": success}
    if data:
        response['data'] = data
    if error:
        response['error'] = error

    app.logger.debug('Returning: %s' % response)
    return response


class Root(Resource):
    """
    The root resource
    """

    def get(self):
        return generate_output(True, data={"LEDs": PINS_BY_COLOR.keys()})

    def post(self):
        return generate_output(True, data={"LEDs": PINS_BY_COLOR.keys()})


class LEDOff(Resource):
    """
    The off endpoint
    """

    def get(self):
        led_color = request.args.get("led")
        if led_color is not None:
            return self.handle_led(led_color)
        else:
            return generate_output(False, error="No LED color was specified")

    def post(self):
        led_color = request.form.get("led")
        if led_color is not None:
            return self.handle_led(led_color)
        else:
            return generate_output(False, error="No LED color was specified")

    def handle_led(self, led_color):
        if led_color in PINS_BY_COLOR:
            gpio.output(PINS_BY_COLOR[led_color], gpio.LOW)
            return generate_output(True, data=led_color + " LED is now off.")
        else:
            return generate_output(False, error="No LED named " + led_color)


class LEDOn(Resource):
    """
    The on endpoint
    """
    def get(self):
        led_color = request.args.get("led")
        if led_color is not None:
            return self.handle_led(led_color)
        else:
            return generate_output(False, error="No LED color was specified")

    def post(self):
        led_color = request.form.get("led")
        if led_color is not None:
            return self.handle_led(led_color)
        else:
            return generate_output(False, error="No LED color was specified")

    def handle_led(self, led_color):
        if led_color in PINS_BY_COLOR:
            gpio.output(PINS_BY_COLOR[led_color], gpio.HIGH)
            return generate_output(True, data=led_color + " LED is now on.")
        else:
            return generate_output(False, error="No LED named " + led_color)


class LEDStatus(Resource):
    """
    The status endpoint
    """
    def get(self):
        led_color = request.args.get("led")
        if led_color is not None:
            return self.handle_led(led_color)
        else:
            return generate_output(False, error="No LED color was specified")

    def post(self):
        led_color = request.form.get("led")
        if led_color is not None:
            return self.handle_led(led_color)
        else:
            return generate_output(False, error="No LED color was specified")

    def handle_led(self, led_color):
        states = {True: "on", False: "off"}
        if led_color in PINS_BY_COLOR:
            state = gpio.input(PINS_BY_COLOR[led_color])
            return generate_output(True, data=led_color + " LED is currently " + states[state] + ".")
        else:
            return generate_output(False, error="No LED named " + led_color)

api.add_resource(Root, "/")
api.add_resource(LEDOff, "/off")
api.add_resource(LEDOn, "/on")
api.add_resource(LEDStatus, "/status")

if __name__ == "__main__":
    print "[*] Configuring GPIO"
    gpio.setmode(gpio.BCM)
    for pin in PINS_BY_COLOR.iteritems():
        gpio.setup(pin[1], gpio.OUT)

    app.run(debug=True, host='')
