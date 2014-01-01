import os, simplejson, settings, time



class ThermometerNotFound(ValueError):
    pass


class Thermometer():
    name = None
    path = None

    def __init__(self, name):
        self.name = name
        self._build_path()

    def _build_path(self, ):
        self.path = os.path.join(settings.BASE_PATH, self.name, settings.TAIL_PATH)
        if not os.path.isfile(self.path):
            raise ThermometerNotFound("Thermometer with name %s not found" % self.name)


    def _read_raw(self, ):
        f = open(self.path, 'r')
        lines = f.readlines()
	f.close()
	return lines

    def read(self):
	lines = self._read_raw()
	while lines[0].strip()[-3:] != 'YES':
	    time.sleep(0.2)
	    lines = self._read_raw()
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
	    temp_string = lines[1][equals_pos+2:]

	temp_c = float(temp_string) / 1000.0
	temp_f = temp_c * 9.0 / 5.0 + 32.0
	return {"celsius": float(temp_c), "fahrenheit": float(temp_f)}

    def to_json(self):
	return simplejson.dumps({"name": self.name, "temperature": self.read()})


def get_thermometers():
    therms = {}
    for dirname, dirnames, filenames in os.walk('/sys/bus/w1/devices/'):
	for subdirname in dirnames:
	    if not subdirname.startswith("28-"):
		continue

	    therms[subdirname] = Thermometer(subdirname)
    return therms


def read_temperatures(thermometer=None):
    therms = get_thermometers()
    if thermometer:
	return {thermometer: therms[thermometer].read()}

    temps = {}
    for thermometer in therms:
	temps[thermometer] = therms[thermometer].read()
    return temps




